package com.wendao.utils;

import com.wendao.entity.Order;
import com.wendao.enums.AdminNoticeStatus;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Base64;

public final class PaymentConfirmTokens {
    private static final SecureRandom RANDOM = new SecureRandom();

    private PaymentConfirmTokens() { }

    public static String initialize(Order order) {
        byte[] bytes = new byte[32];
        RANDOM.nextBytes(bytes);
        String token = Base64.getUrlEncoder().withoutPadding().encodeToString(bytes);
        order.setPaymentConfirmTokenHash(hash(token));
        order.setAdminNoticeStatus(AdminNoticeStatus.NOT_REQUESTED.name());
        return token;
    }

    public static boolean matches(String token, String expectedHash) {
        if (token == null || !token.matches("[A-Za-z0-9_-]{43}") || expectedHash == null) {
            return false;
        }
        return MessageDigest.isEqual(hash(token).getBytes(StandardCharsets.US_ASCII),
                expectedHash.getBytes(StandardCharsets.US_ASCII));
    }

    private static String hash(String token) {
        try {
            byte[] bytes = MessageDigest.getInstance("SHA-256")
                    .digest(token.getBytes(StandardCharsets.UTF_8));
            StringBuilder value = new StringBuilder(64);
            for (byte b : bytes) {
                value.append(String.format("%02x", b & 0xff));
            }
            return value.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException("SHA-256 unavailable", e);
        }
    }
}
