package com.wendao.service;

import cn.hutool.core.date.DateUtil;
import com.wendao.common.utils.EmailUtils;
import com.wendao.config.PayProConfig;
import com.wendao.entity.Order;
import com.wendao.enums.AdminNoticeStatus;
import com.wendao.mapper.OrderMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import org.springframework.web.util.UriComponentsBuilder;

import java.util.UUID;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

/** Runs in another thread only after the customer's confirmation transaction commits. */
@Service
public class PaymentNoticeSender {
    private static final Logger log = LoggerFactory.getLogger(PaymentNoticeSender.class);
    private final OrderMapper orders;
    private final PaymentNoticeLock locks;
    private final StringRedisTemplate redis;
    private final EmailUtils mail;
    private final PayProConfig config;

    public PaymentNoticeSender(OrderMapper orders, PaymentNoticeLock locks,
                               StringRedisTemplate redis, EmailUtils mail, PayProConfig config) {
        this.orders = orders;
        this.locks = locks;
        this.redis = redis;
        this.mail = mail;
        this.config = config;
    }

    @Async
    public void send(String id, String attempt) {
        try {
            if (!locks.isOwned(id, attempt)) {
                return;
            }
            Order order = orders.selectById(id);
            if (order == null || order.getPaymentConfirmTokenHash() == null
                    || order.getPaymentConfirmedAt() == null
                    || !AdminNoticeStatus.SENDING.name().equals(order.getAdminNoticeStatus())) {
                return;
            }
            if (!Integer.valueOf(0).equals(order.getState()) && !Integer.valueOf(4).equals(order.getState())) {
                orders.finishPaymentNotice(id, AdminNoticeStatus.FAILED.name());
                return;
            }
            // Keep a previously issued admin token valid if a mail attempt must be retried.
            redis.opsForValue().setIfAbsent(id, UUID.randomUUID().toString(),
                    config.getToken().getExpire(), TimeUnit.DAYS);
            String adminToken = redis.opsForValue().get(id);
            if (adminToken == null) {
                throw new IllegalStateException("Cannot issue review link");
            }
            order.setTime(DateUtil.formatDateTime(order.getCreateTime()));
            order.setPassUrl(reviewUrl("/order/pass", id, adminToken, true));
            order.setBackUrl(reviewUrl("/order/back", id, adminToken, true));
            order.setEditUrl(reviewUrl("/order-edit", id, adminToken, false));
            order.setDelUrl(reviewUrl("/order-del", id, adminToken, false));
            order.setStatistic(UriComponentsBuilder.fromHttpUrl(config.getSite() + "/statistic")
                    .queryParam("myToken", "{myToken}").encode()
                    .buildAndExpand(config.getToken().getValue()).toUriString());

            // This method returns only after SMTP accepts the message, or throws on failure.
            mail.sendTemplateMailOrThrow(config.getEmail().getSender(), config.getEmail().getReceiver(),
                    "【" + config.getTitle() + "】客户声明已付款，待核实", "payment-review", order);
            if (locks.isOwned(id, attempt)) {
                orders.finishPaymentNotice(id, AdminNoticeStatus.SENT.name());
            }
        } catch (Exception error) {
            log.error("订单 {} 的付款确认通知发送失败", id, error);
            try {
                if (locks.isOwned(id, attempt)) {
                    orders.finishPaymentNotice(id, AdminNoticeStatus.FAILED.name());
                }
            } catch (Exception persistenceError) {
                log.error("订单 {} 的通知状态保存失败，可在发送锁过期后重试", id, persistenceError);
            }
        } finally {
            try {
                locks.release(id, attempt);
            } catch (Exception error) {
                log.error("订单 {} 的通知锁释放失败，将自动过期", id, error);
            }
        }
    }

    private String reviewUrl(String path, String id, String token, boolean secondFactor) {
        UriComponentsBuilder builder = UriComponentsBuilder.fromHttpUrl(config.getSite() + path)
                .queryParam("id", "{id}").queryParam("token", "{token}");
        Map<String, Object> params = new LinkedHashMap<>();
        params.put("id", id);
        params.put("token", token);
        if (secondFactor) {
            builder.queryParam("myToken", "{myToken}");
            params.put("myToken", config.getToken().getValue());
        }
        return builder.encode().buildAndExpand(params).toUriString();
    }
}
