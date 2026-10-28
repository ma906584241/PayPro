package com.wendao.model.resp;

import lombok.Data;
import java.math.BigDecimal;
import java.util.Date;

@Data
public class PaymentConfirmationResp {
    private Integer orderState;
    private BigDecimal amount;
    private String payType;
    private String payNum;
    private Date expireTime;
    private Date confirmedAt;
    private String noticeStatus;
    private boolean canConfirm;
    private boolean retryable;
}
