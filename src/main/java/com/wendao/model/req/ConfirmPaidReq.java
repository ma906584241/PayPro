package com.wendao.model.req;

import lombok.Data;
import javax.validation.constraints.NotBlank;

@Data
public class ConfirmPaidReq {
    @NotBlank(message = "订单号不能为空")
    private String orderId;

    @NotBlank(message = "请使用完整支付链接")
    private String paymentConfirmToken;
}
