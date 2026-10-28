package com.wendao.service;

import com.wendao.common.utils.EmailUtils;
import com.wendao.config.PayProConfig;
import com.wendao.entity.Order;
import com.wendao.mapper.OrderMapper;
import com.wendao.utils.PaymentConfirmTokens;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.mail.MailSendException;

import java.math.BigDecimal;
import java.util.Date;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

class PaymentNoticeSenderTest {
    private OrderMapper orders;
    private PaymentNoticeLock locks;
    private EmailUtils mail;
    private PaymentNoticeSender sender;
    private Order order;
    private String payerToken;
    private ValueOperations<String, String> values;

    @BeforeEach
    @SuppressWarnings("unchecked")
    void setup() {
        orders = mock(OrderMapper.class);
        locks = mock(PaymentNoticeLock.class);
        mail = mock(EmailUtils.class);
        StringRedisTemplate redis = mock(StringRedisTemplate.class);
        values = mock(ValueOperations.class);
        when(redis.opsForValue()).thenReturn(values);
        when(values.get("order-1")).thenReturn("admin-review-token");
        PayProConfig config = new PayProConfig();
        config.setSite("https://pay.example.com");
        config.setTitle("Test Site");
        config.getToken().setExpire(14L);
        config.getToken().setValue("test-admin-password");
        config.getEmail().setSender("sender@example.com");
        config.getEmail().setReceiver("admin@example.com");
        sender = new PaymentNoticeSender(orders, locks, redis, mail, config);
        order = new Order();
        order.setId("order-1");
        order.setState(0);
        order.setMoney(new BigDecimal("9.90"));
        order.setCreateTime(new Date());
        payerToken = PaymentConfirmTokens.initialize(order);
        order.setPaymentConfirmedAt(new Date());
        order.setAdminNoticeStatus("SENDING");
        when(orders.selectById("order-1")).thenReturn(order);
        when(locks.isOwned("order-1", "attempt-1")).thenReturn(true);
    }

    @Test
    void smtpAcceptancePersistsSentAndBuildsSeparateAdminLinks() throws Exception {
        sender.send("order-1", "attempt-1");
        verify(mail).sendTemplateMailOrThrow(eq("sender@example.com"), eq("admin@example.com"),
                contains("客户声明已付款"), eq("payment-review"), same(order));
        verify(orders).finishPaymentNotice("order-1", "SENT");
        assertTrue(order.getPassUrl().contains("admin-review-token"));
        assertFalse(order.getPassUrl().contains(payerToken));
        assertEquals(0, order.getState());
        verify(locks).release("order-1", "attempt-1");
    }

    @Test
    void smtpFailureIsRecordedForRetry() throws Exception {
        doThrow(new MailSendException("mock failure")).when(mail)
                .sendTemplateMailOrThrow(anyString(), anyString(), anyString(), anyString(), any());
        sender.send("order-1", "attempt-1");
        verify(orders).finishPaymentNotice("order-1", "FAILED");
        verify(orders, never()).finishPaymentNotice("order-1", "SENT");
        verify(locks).release("order-1", "attempt-1");
    }

    @Test
    void reviewLinksPreserveSpecialCharactersInExternalOrderNumbers() {
        String id = "EXT+1 & 订单#1";
        order.setId(id);
        when(orders.selectById(id)).thenReturn(order);
        when(locks.isOwned(id, "attempt-1")).thenReturn(true);
        when(values.get(id)).thenReturn("admin-review-token");
        sender.send(id, "attempt-1");
        String encoded = "id=EXT%2B1%20%26%20%E8%AE%A2%E5%8D%95%231";
        assertTrue(order.getPassUrl().contains(encoded));
        assertTrue(order.getBackUrl().contains(encoded));
        assertTrue(order.getEditUrl().contains(encoded));
        assertTrue(order.getDelUrl().contains(encoded));
        verify(orders).finishPaymentNotice(id, "SENT");
    }

    @Test
    void lostOwnershipDoesNotDeliverOrOverwriteAnotherAttempt() {
        when(locks.isOwned("order-1", "attempt-1")).thenReturn(false);
        sender.send("order-1", "attempt-1");
        verifyNoInteractions(mail);
        verify(orders, never()).finishPaymentNotice(anyString(), anyString());
    }

    @Test
    void oldAttemptDoesNotSaveAnOutcomeAfterLosingItsLease() {
        when(locks.isOwned("order-1", "attempt-1")).thenReturn(true, false);
        sender.send("order-1", "attempt-1");
        verify(orders, never()).finishPaymentNotice(anyString(), anyString());
    }

    @Test
    void legacyOrAlreadyReviewedOrdersAreNeverBackfilled() {
        order.setPaymentConfirmTokenHash(null);
        sender.send("order-1", "attempt-1");
        verifyNoInteractions(mail);
        order.setPaymentConfirmTokenHash("legacy-guard");
        order.setState(1);
        sender.send("order-1", "attempt-1");
        verifyNoInteractions(mail);
    }
}
