package com.wendao.service;

import com.baomidou.mybatisplus.core.MybatisConfiguration;
import com.baomidou.mybatisplus.extension.spring.MybatisSqlSessionFactoryBean;
import com.wendao.entity.Order;
import com.wendao.mapper.OrderMapper;
import com.wendao.utils.PaymentConfirmTokens;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.condition.EnabledIfSystemProperty;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.support.EncodedResource;
import org.springframework.data.redis.connection.RedisStandaloneConfiguration;
import org.springframework.data.redis.connection.jedis.JedisConnectionFactory;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.jdbc.datasource.init.ScriptUtils;
import org.springframework.util.StreamUtils;

import java.math.BigDecimal;
import java.nio.charset.StandardCharsets;
import java.sql.Connection;
import java.sql.ResultSet;
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

/** Opt-in integration checks. Only a disposable loopback test database is allowed. */
@EnabledIfSystemProperty(named = "paypro.it.jdbcUrl", matches = ".+")
class PaymentConfirmationDatabaseIT {
    private DriverManagerDataSource dataSource;
    private SqlSessionFactory sessions;
    private JedisConnectionFactory redisFactory;
    private StringRedisTemplate redis;

    @BeforeEach
    void setup() throws Exception {
        String url = System.getProperty("paypro.it.jdbcUrl");
        assertTrue(url.startsWith("jdbc:mysql://127.0.0.1:") && url.contains("/paypro_confirmation_it?"),
                "Refusing to run against any database other than the isolated test database");
        dataSource = new DriverManagerDataSource(url, "root", "paypro-it-only");
        try (Connection connection = dataSource.getConnection()) {
            ScriptUtils.executeSqlScript(connection, new EncodedResource(new ClassPathResource("sql/pay.sql"), "UTF-8"));
        }
        MybatisSqlSessionFactoryBean factory = new MybatisSqlSessionFactoryBean();
        factory.setDataSource(dataSource);
        MybatisConfiguration config = new MybatisConfiguration();
        config.setMapUnderscoreToCamelCase(true);
        factory.setConfiguration(config);
        sessions = factory.getObject();
        sessions.getConfiguration().addMapper(OrderMapper.class);
        redisFactory = new JedisConnectionFactory(new RedisStandaloneConfiguration("127.0.0.1",
                Integer.parseInt(System.getProperty("paypro.it.redisPort"))));
        redisFactory.afterPropertiesSet();
        redis = new StringRedisTemplate(redisFactory);
        redis.afterPropertiesSet();
    }

    @AfterEach
    void cleanup() {
        if (redisFactory != null) { redisFactory.destroy(); }
    }

    @Test
    void additiveMigrationPreservesLegacyRowsAndLeavesThemUnenrolled() throws Exception {
        String sql = StreamUtils.copyToString(new ClassPathResource("sql/pay.sql").getInputStream(), StandardCharsets.UTF_8);
        sql = sql.replaceAll("(?m)^.*`(?:payment_confirm_token_hash|payment_confirmed_at|admin_notice_status)`.*\\R", "");
        try (Connection connection = dataSource.getConnection()) {
            ScriptUtils.executeSqlScript(connection, new EncodedResource(new ByteArrayResource(sql.getBytes(StandardCharsets.UTF_8)), "UTF-8"));
            connection.createStatement().executeUpdate("INSERT INTO t_order(id,state,money) VALUES('LEGACY',0,9.90)");
            ScriptUtils.executeSqlScript(connection, new ClassPathResource("sql/migrations/20261028_payment_confirmation.sql"));
            ResultSet row = connection.createStatement().executeQuery("SELECT * FROM t_order WHERE id='LEGACY'");
            assertTrue(row.next());
            assertEquals(new BigDecimal("9.90"), row.getBigDecimal("money"));
            assertNull(row.getString("payment_confirm_token_hash"));
            assertNull(row.getTimestamp("payment_confirmed_at"));
            assertNull(row.getString("admin_notice_status"));
        }
    }

    @Test
    void realRedisLockAndSqlClaimDeduplicateConcurrentRequestsAndPersistSent() throws Exception {
        Order order = new Order();
        String id = "CONCURRENT-" + UUID.randomUUID();
        order.setId(id); order.setState(0); order.setMoney(new BigDecimal("9.90"));
        String token = PaymentConfirmTokens.initialize(order);
        try (SqlSession session = sessions.openSession(true)) {
            session.getMapper(OrderMapper.class).insert(order);
        }
        PaymentNoticeLock locks = new PaymentNoticeLock(redis);
        AtomicReference<String> owner = new AtomicReference<>();
        CountDownLatch start = new CountDownLatch(1);
        ExecutorService pool = Executors.newFixedThreadPool(12);
        List<Future<Integer>> tasks = new ArrayList<>();
        try {
            for (int i = 0; i < 12; i++) {
                tasks.add(pool.submit(() -> {
                    start.await();
                    String attempt = locks.acquire(id);
                    if (attempt == null) { return 0; }
                    owner.set(attempt);
                    try (SqlSession session = sessions.openSession(true)) {
                        return session.getMapper(OrderMapper.class).claimPaymentNotice(id, order.getPaymentConfirmTokenHash(), new Date());
                    }
                }));
            }
            start.countDown();
            int claimed = 0;
            for (Future<Integer> task : tasks) { claimed += task.get(20, TimeUnit.SECONDS); }
            assertEquals(1, claimed);
            assertTrue(locks.isOwned(id, owner.get()));
            locks.release(id, "wrong-owner");
            assertTrue(locks.isOwned(id, owner.get()));
            try (SqlSession session = sessions.openSession(true)) {
                OrderMapper mapper = session.getMapper(OrderMapper.class);
                Order persisted = mapper.selectById(id);
                assertNotNull(persisted.getPaymentConfirmedAt());
                assertEquals(0, persisted.getState());
                mapper.finishPaymentNotice(id, "SENT");
                locks.release(id, owner.get());
                PaymentNoticeSender sender = mock(PaymentNoticeSender.class);
                PaymentConfirmationService service = new PaymentConfirmationService(mapper, locks, sender);
                com.wendao.model.req.ConfirmPaidReq request = new com.wendao.model.req.ConfirmPaidReq();
                request.setOrderId(id); request.setPaymentConfirmToken(token);
                assertEquals("SENT", service.confirm(request).getNoticeStatus());
                verifyNoInteractions(sender);
            }
        } finally {
            pool.shutdownNow();
            if (owner.get() != null) { locks.release(id, owner.get()); }
        }
    }

    @Test
    void ordinaryEntityUpdatesCannotOverwritePrivateNotificationMetadata() throws Exception {
        Order order = new Order();
        order.setId("METADATA"); order.setState(0);
        PaymentConfirmTokens.initialize(order);
        String hash = order.getPaymentConfirmTokenHash();
        try (SqlSession session = sessions.openSession(true)) {
            OrderMapper mapper = session.getMapper(OrderMapper.class);
            mapper.insert(order);
            mapper.claimPaymentNotice(order.getId(), hash, new Date());
            mapper.finishPaymentNotice(order.getId(), "SENT");
            Order form = new Order();
            form.setId(order.getId()); form.setNickName("Edited");
            form.setPaymentConfirmTokenHash("should-not-be-saved");
            form.setAdminNoticeStatus("FAILED");
            mapper.updateById(form);
            Order saved = mapper.selectById(order.getId());
            assertEquals(hash, saved.getPaymentConfirmTokenHash());
            assertEquals("SENT", saved.getAdminNoticeStatus());
            assertNotNull(saved.getPaymentConfirmedAt());
        }
    }
}
