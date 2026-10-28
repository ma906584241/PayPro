package com.wendao.service;

import com.wendao.entity.Order;
import com.wendao.enums.AdminNoticeStatus;
import com.wendao.exception.ApiException;
import com.wendao.mapper.OrderMapper;
import com.wendao.model.req.ConfirmPaidReq;
import com.wendao.model.resp.PaymentConfirmationResp;
import com.wendao.utils.PaymentConfirmTokens;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.support.TransactionSynchronizationAdapter;
import org.springframework.transaction.support.TransactionSynchronizationManager;
import org.springframework.util.StringUtils;

import java.util.Date;

@Service
public class PaymentConfirmationService {
    private static final Logger log = LoggerFactory.getLogger(PaymentConfirmationService.class);
    private final OrderMapper orders;
    private final PaymentNoticeLock locks;
    private final PaymentNoticeSender sender;

    public PaymentConfirmationService(OrderMapper orders, PaymentNoticeLock locks, PaymentNoticeSender sender) {
        this.orders = orders;
        this.locks = locks;
        this.sender = sender;
    }

    public PaymentConfirmationResp status(String id, String token) {
        return response(authorize(id, token));
    }

    @Transactional(rollbackFor = Exception.class)
    public PaymentConfirmationResp confirm(ConfirmPaidReq request) {
        Order order = authorize(request.getOrderId(), request.getPaymentConfirmToken());
        if (AdminNoticeStatus.SENT.name().equals(order.getAdminNoticeStatus())) {
            return response(order);
        }
        ensureConfirmable(order);
        String attempt = locks.acquire(order.getId());
        if (attempt == null) {
            return response(order);
        }
        boolean dispatched = false;
        try {
            Date now = new Date();
            int changed = orders.claimPaymentNotice(order.getId(), order.getPaymentConfirmTokenHash(), now);
            if (changed == 0) {
                Order current = authorize(request.getOrderId(), request.getPaymentConfirmToken());
                if (!AdminNoticeStatus.SENT.name().equals(current.getAdminNoticeStatus())) {
                    ensureConfirmable(current);
                }
                return response(current);
            }
            final String id = order.getId();
            if (TransactionSynchronizationManager.isSynchronizationActive()) {
                TransactionSynchronizationManager.registerSynchronization(new TransactionSynchronizationAdapter() {
                    @Override
                    public void afterCommit() {
                        dispatch(id, attempt);
                    }

                    @Override
                    public void afterCompletion(int completionStatus) {
                        if (completionStatus != STATUS_COMMITTED) {
                            release(id, attempt);
                        }
                    }
                });
            } else {
                dispatch(id, attempt);
            }
            dispatched = true;
            return response(authorize(request.getOrderId(), request.getPaymentConfirmToken()));
        } finally {
            if (!dispatched) {
                release(order.getId(), attempt);
            }
        }
    }

    private Order authorize(String id, String token) {
        if (!StringUtils.hasText(id)) {
            throw new ApiException(400, "订单号不能为空");
        }
        Order order = orders.selectById(id);
        if (order == null) {
            throw new ApiException(404, "订单不存在");
        }
        if (!StringUtils.hasText(order.getPaymentConfirmTokenHash())) {
            throw new ApiException(409, "旧订单沿用原审核流程，请联系客服");
        }
        if (!PaymentConfirmTokens.matches(token, order.getPaymentConfirmTokenHash())) {
            throw new ApiException(403, "付款确认凭证无效，请使用完整支付链接");
        }
        return order;
    }

    private void ensureConfirmable(Order order) {
        if (!pending(order) || expiredBeforeConfirmation(order)) {
            throw new ApiException(409, "订单已结束或已过期，不能再通知管理员");
        }
    }

    private boolean pending(Order order) {
        return Integer.valueOf(0).equals(order.getState()) || Integer.valueOf(4).equals(order.getState());
    }

    private boolean expiredBeforeConfirmation(Order order) {
        return order.getPaymentConfirmedAt() == null && order.getExpireTime() != null
                && order.getExpireTime().before(new Date());
    }

    private PaymentConfirmationResp response(Order order) {
        PaymentConfirmationResp result = new PaymentConfirmationResp();
        boolean expired = pending(order) && expiredBeforeConfirmation(order);
        String status = order.getAdminNoticeStatus();
        if (status == null) {
            status = AdminNoticeStatus.NOT_REQUESTED.name();
        }
        if (AdminNoticeStatus.SENDING.name().equals(status) && !locks.isLocked(order.getId())) {
            status = AdminNoticeStatus.FAILED.name();
        }
        result.setOrderState(expired ? 5 : order.getState());
        result.setAmount(order.getActualAmount() != null ? order.getActualAmount() : order.getMoney());
        result.setPayType(order.getPayType());
        result.setPayNum(order.getPayNum());
        result.setExpireTime(order.getExpireTime());
        result.setConfirmedAt(order.getPaymentConfirmedAt());
        result.setNoticeStatus(status);
        result.setCanConfirm(pending(order) && !expired &&
                (AdminNoticeStatus.NOT_REQUESTED.name().equals(status) || AdminNoticeStatus.FAILED.name().equals(status)));
        result.setRetryable(order.getPaymentConfirmedAt() != null && result.isCanConfirm());
        return result;
    }

    private void dispatch(String id, String attempt) {
        try {
            sender.send(id, attempt);
        } catch (RuntimeException error) {
            // The committed claim remains retryable if the async executor cannot start work.
            log.error("订单 {} 的通知任务未能启动", id, error);
            release(id, attempt);
        }
    }

    private void release(String id, String attempt) {
        try {
            locks.release(id, attempt);
        } catch (RuntimeException error) {
            log.error("订单 {} 的通知锁将等待超时释放", id, error);
        }
    }
}
