package com.wendao.service;

import com.wendao.controller.OrderController;
import com.wendao.exception.ApiException;
import com.wendao.exception.GlobalExceptionHandler;
import com.wendao.model.req.ConfirmPaidReq;
import com.wendao.model.resp.PaymentConfirmationResp;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.test.util.ReflectionTestUtils;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

class PaymentConfirmationControllerTest {
    private PaymentConfirmationService service;
    private MockMvc mvc;

    @BeforeEach
    void setup() {
        service = mock(PaymentConfirmationService.class);
        OrderController controller = new OrderController();
        ReflectionTestUtils.setField(controller, "paymentConfirmationService", service);
        mvc = MockMvcBuilders.standaloneSetup(controller)
                .setControllerAdvice(new GlobalExceptionHandler()).build();
    }

    @Test
    void confirmationUsesPostAndReturnsPendingPaymentState() throws Exception {
        PaymentConfirmationResp result = new PaymentConfirmationResp();
        result.setOrderState(0);
        result.setNoticeStatus("SENDING");
        when(service.confirm(any(ConfirmPaidReq.class))).thenReturn(result);
        mvc.perform(post("/order/confirm-paid").contentType("application/json")
                        .content("{\"orderId\":\"order-1\",\"paymentConfirmToken\":\"test-token\"}"))
                .andExpect(jsonPath("$.code").value(200))
                .andExpect(jsonPath("$.data.orderState").value(0))
                .andExpect(jsonPath("$.data.noticeStatus").value("SENDING"));
    }

    @Test
    void missingConfirmationCredentialIsAValidationError() throws Exception {
        mvc.perform(post("/order/confirm-paid").contentType("application/json")
                        .content("{\"orderId\":\"order-1\"}"))
                .andExpect(jsonPath("$.code").value(400));
        verifyNoInteractions(service);
    }

    @Test
    void statusUsesScopedCredentialHeaderAndNeverConfirmsAnOrder() throws Exception {
        PaymentConfirmationResp result = new PaymentConfirmationResp();
        result.setNoticeStatus("NOT_REQUESTED");
        when(service.status("order-1", "payer-only-token")).thenReturn(result);
        mvc.perform(get("/order/payment-confirmation").param("orderId", "order-1")
                        .header("X-Payment-Confirm-Token", "payer-only-token"))
                .andExpect(jsonPath("$.code").value(200));
        verify(service).status("order-1", "payer-only-token");
        verify(service, never()).confirm(any());
    }

    @Test
    void invalidScopedTokenIsRejectedWithoutReturningAdminLinks() throws Exception {
        when(service.status("order-1", null)).thenThrow(new ApiException(403, "Invalid credential"));
        mvc.perform(get("/order/payment-confirmation").param("orderId", "order-1"))
                .andExpect(jsonPath("$.code").value(403))
                .andExpect(jsonPath("$.data").doesNotExist());
    }
}
