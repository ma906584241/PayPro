package com.wendao.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.wendao.entity.Order;
import com.wendao.exception.ApiException;
import com.wendao.mapper.OrderMapper;
import com.wendao.model.req.ConfirmPaidReq;
import com.wendao.model.resp.PaymentConfirmationResp;
import com.wendao.utils.PaymentConfirmTokens;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.transaction.support.TransactionSynchronization;
import org.springframework.transaction.support.TransactionSynchronizationManager;

import java.math.BigDecimal;
import java.util.Date;
import java.util.concurrent.atomic.AtomicBoolean;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

class PaymentConfirmationServiceTest {
    private OrderMapper orders;
    private PaymentNoticeLock locks;
    private PaymentNoticeSender sender;
    private PaymentConfirmationService service;
    private Order order;
    private String token;

    @BeforeEach
    void setup() {
        orders = mock(OrderMapper.class);
        locks = mock(PaymentNoticeLock.class);
        sender = mock(PaymentNoticeSender.class);
        service = new PaymentConfirmationService(orders, locks, sender);
        order = new Order();
        order.setId("order-1");
        order.setState(0);
        order.setMoney(new BigDecimal("9.90"));
        order.setPayType("wechat");
        token = PaymentConfirmTokens.initialize(order);
        when(orders.selectById("order-1")).thenReturn(order);
    }

    @AfterEach
    void cleanup() {
        if (TransactionSynchronizationManager.isSynchronizationActive()) {
            TransactionSynchronizationManager.clearSynchronization();
        }
    }

    private ConfirmPaidReq request() {
        ConfirmPaidReq request = new ConfirmPaidReq();
        request.setOrderId("order-1");
        request.setPaymentConfirmToken(token);
        return request;
    }

    private void allowClaim() {
        AtomicBoolean locked = new AtomicBoolean(true);
        when(locks.acquire("order-1")).thenReturn("attempt-1");
        when(locks.isLocked("order-1")).thenAnswer(invocation -> locked.get());
        doAnswer(invocation -> { locked.set(false); return null; }).when(locks).release("order-1", "attempt-1");
        when(orders.claimPaymentNotice(eq("order-1"), eq(order.getPaymentConfirmTokenHash()), any(Date.class)))
                .thenAnswer(invocation -> {
                    if (order.getPaymentConfirmedAt() == null) {
                        order.setPaymentConfirmedAt(invocation.getArgument(2));
                    }
                    order.setAdminNoticeStatus("SENDING");
                    return 1;
                });
    }

    @Test
    void statusNeverClaimsOrSends() {
        PaymentConfirmationResp result = service.status("order-1", token);
        assertTrue(result.isCanConfirm());
        assertNull(result.getConfirmedAt());
        assertEquals("NOT_REQUESTED", result.getNoticeStatus());
        verifyNoInteractions(sender, locks);
        verify(orders, never()).claimPaymentNotice(anyString(), anyString(), any());
    }

    @Test
    void confirmationRecordsDeclarationButNeverPaymentSuccess() {
        allowClaim();
        PaymentConfirmationResp result = service.confirm(request());
        assertNotNull(result.getConfirmedAt());
        assertEquals("SENDING", result.getNoticeStatus());
        assertEquals(0, result.getOrderState());
        assertEquals(0, order.getState());
        verify(sender).send("order-1", "attempt-1");
        verify(orders, never()).approveOrder(anyString());
    }

    @Test
    void actualTransactionDefersMailUntilCommit() {
        allowClaim();
        TransactionSynchronizationManager.initSynchronization();
        service.confirm(request());
        verifyNoInteractions(sender);
        for (TransactionSynchronization synchronization : TransactionSynchronizationManager.getSynchronizations()) {
            synchronization.afterCommit();
            synchronization.afterCompletion(TransactionSynchronization.STATUS_COMMITTED);
        }
        verify(sender).send("order-1", "attempt-1");
    }

    @Test
    void rollbackNeverDispatchesAndReleasesLock() {
        allowClaim();
        TransactionSynchronizationManager.initSynchronization();
        service.confirm(request());
        for (TransactionSynchronization synchronization : TransactionSynchronizationManager.getSynchronizations()) {
            synchronization.afterCompletion(TransactionSynchronization.STATUS_ROLLED_BACK);
        }
        verifyNoInteractions(sender);
        verify(locks).release("order-1", "attempt-1");
    }

    @Test
    void previouslySentNoticeRemainsDeduplicatedEvenWithoutRedisLock() {
        order.setPaymentConfirmedAt(new Date());
        order.setAdminNoticeStatus("SENT");
        assertEquals("SENT", service.confirm(request()).getNoticeStatus());
        verifyNoInteractions(sender, locks);
    }

    @Test
    void concurrentRequestDoesNotStartAnotherMail() {
        order.setPaymentConfirmedAt(new Date());
        order.setAdminNoticeStatus("SENDING");
        when(locks.acquire("order-1")).thenReturn(null);
        when(locks.isLocked("order-1")).thenReturn(true);
        assertFalse(service.confirm(request()).isCanConfirm());
        verifyNoInteractions(sender);
    }

    @Test
    void staleSendingLeaseIsReadOnlyAndRetryable() {
        order.setPaymentConfirmedAt(new Date());
        order.setAdminNoticeStatus("SENDING");
        assertEquals("FAILED", service.status("order-1", token).getNoticeStatus());
        assertTrue(service.status("order-1", token).isRetryable());
        verify(orders, never()).finishPaymentNotice(anyString(), anyString());
        verifyNoInteractions(sender);
    }

    @Test
    void failedNoticeRetryPreservesOriginalDeclarationTime() {
        Date firstConfirmation = new Date(System.currentTimeMillis() - 3000);
        order.setPaymentConfirmedAt(firstConfirmation);
        order.setAdminNoticeStatus("FAILED");
        order.setExpireTime(new Date(System.currentTimeMillis() - 1000));
        allowClaim();
        assertEquals(firstConfirmation, service.confirm(request()).getConfirmedAt());
        verify(sender).send("order-1", "attempt-1");
    }

    @Test
    void rejectedAsyncExecutionCanBeRetried() {
        allowClaim();
        doThrow(new IllegalStateException("executor unavailable")).when(sender).send(anyString(), anyString());
        assertEquals("FAILED", service.confirm(request()).getNoticeStatus());
        verify(locks).release("order-1", "attempt-1");
    }

    @Test
    void legacyAndInvalidCredentialsNeverSendMail() {
        assertEquals(403, assertThrows(ApiException.class, () -> service.status("order-1", "wrong")).getCode());
        order.setPaymentConfirmTokenHash(null);
        assertEquals(409, assertThrows(ApiException.class, () -> service.confirm(request())).getCode());
        verifyNoInteractions(sender, locks);
    }

    @Test
    void missingAndTerminalOrdersAreRejected() {
        assertEquals(404, assertThrows(ApiException.class, () -> service.status("missing", token)).getCode());
        for (int state : new int[]{1, 2, 5}) {
            order.setState(state);
            assertEquals(409, assertThrows(ApiException.class, () -> service.confirm(request())).getCode());
        }
        verifyNoInteractions(sender, locks);
    }

    @Test
    void expiredUnreportedOrderCannotNotify() {
        order.setExpireTime(new Date(System.currentTimeMillis() - 1000));
        assertEquals(5, service.status("order-1", token).getOrderState());
        assertEquals(409, assertThrows(ApiException.class, () -> service.confirm(request())).getCode());
        verifyNoInteractions(sender, locks);
    }

    @Test
    void payerSecretsAndMetadataDoNotLeakThroughPublicOrderJson() throws Exception {
        String json = new ObjectMapper().writeValueAsString(order);
        assertFalse(json.contains("paymentConfirmTokenHash"));
        assertFalse(json.contains("paymentConfirmedAt"));
        assertFalse(json.contains("adminNoticeStatus"));
        assertFalse(json.contains(token));
        Order second = new Order();
        assertNotEquals(token, PaymentConfirmTokens.initialize(second));
        assertTrue(PaymentConfirmTokens.matches(token, order.getPaymentConfirmTokenHash()));
    }
}
