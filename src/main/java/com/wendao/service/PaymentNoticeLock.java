package com.wendao.service;

import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.core.script.DefaultRedisScript;
import org.springframework.stereotype.Component;

import java.util.Collections;
import java.util.UUID;
import java.util.concurrent.TimeUnit;

@Component
public class PaymentNoticeLock {
    private static final String PREFIX = "order:paid-notice:";
    private static final DefaultRedisScript<Long> RELEASE = new DefaultRedisScript<>(
            "if redis.call('get', KEYS[1]) == ARGV[1] then " +
                    "return redis.call('del', KEYS[1]) else return 0 end", Long.class);
    private final StringRedisTemplate redis;

    public PaymentNoticeLock(StringRedisTemplate redis) {
        this.redis = redis;
    }

    public String acquire(String id) {
        String attempt = UUID.randomUUID().toString();
        return Boolean.TRUE.equals(redis.opsForValue().setIfAbsent(
                PREFIX + id, attempt, 120, TimeUnit.SECONDS)) ? attempt : null;
    }

    public boolean isOwned(String id, String attempt) {
        return attempt != null && attempt.equals(redis.opsForValue().get(PREFIX + id));
    }

    public boolean isLocked(String id) {
        return Boolean.TRUE.equals(redis.hasKey(PREFIX + id));
    }

    public void release(String id, String attempt) {
        redis.execute(RELEASE, Collections.singletonList(PREFIX + id), attempt);
    }
}
