package com.wendao.service;

import com.wendao.common.utils.EmailUtils;
import com.wendao.config.PayProConfig;
import com.wendao.entity.Order;
import com.wendao.mapper.OrderMapper;
import com.wendao.model.ResponseVO;
import com.wendao.model.req.OpenApiOrderReq;
import com.wendao.model.req.OrderReq;
import com.wendao.model.resp.AddOrderResp;
import com.wendao.model.resp.OpenApiOrderResp;
import com.wendao.service.impl.OrderServiceImpl;
import com.wendao.utils.OpenApiSignUtil;
import com.wendao.utils.PaymentConfirmTokens;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.mock.web.MockHttpServletRequest;
import org.springframework.test.util.ReflectionTestUtils;

import java.math.BigDecimal;
import java.util.Date;
import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

class OrderCreationNotificationTest {
    private OrderServiceImpl service;
    private OrderMapper orders;
    private EmailUtils mail;
    private OpenApiSignUtil signs;
    private AtomicReference<Order> inserted;

    @BeforeEach
    @SuppressWarnings("unchecked")
    void setup() {
        service = new OrderServiceImpl();
        orders = mock(OrderMapper.class);
        mail = mock(EmailUtils.class);
        signs = mock(OpenApiSignUtil.class);
        StringRedisTemplate redis = mock(StringRedisTemplate.class);
        ValueOperations<String, String> values = mock(ValueOperations.class);
        when(redis.opsForValue()).thenReturn(values);
        PayProConfig config = new PayProConfig();
        config.setQrCodeNum(2);
        config.setSite("https://pay.example.com");
        config.getRateLimit().setIpExpire(2L);
        config.getDecrement().setEnabled(false);
        ReflectionTestUtils.setField(service, "orderMapper", orders);
        ReflectionTestUtils.setField(service, "redisTemplate", redis);
        ReflectionTestUtils.setField(service, "payProConfig", config);
        ReflectionTestUtils.setField(service, "emailUtils", mail);
        ReflectionTestUtils.setField(service, "openApiSignUtil", signs);
        ReflectionTestUtils.setField(service, "thisService", service);
        inserted = new AtomicReference<>();
        when(orders.insert(any(Order.class))).thenAnswer(invocation -> { inserted.set(invocation.getArgument(0)); return 1; });
    }

    private OrderReq normalRequest() {
        OrderReq request = new OrderReq();
        request.setMoney(new BigDecimal("9.90"));
        request.setPayType("wechat");
        request.setEmail("buyer@example.com");
        return request;
    }

    private MockHttpServletRequest browser() {
        MockHttpServletRequest request = new MockHttpServletRequest();
        request.setRemoteAddr("192.0.2.1");
        return request;
    }

    @Test
    void ordinaryOrderDoesNotSendMailAndOnlyStoresCredentialHash() {
        ResponseVO<AddOrderResp> response = service.addOrder(normalRequest(), browser());
        assertEquals(200, response.getCode());
        assertTrue(PaymentConfirmTokens.matches(response.getData().getPaymentConfirmToken(), inserted.get().getPaymentConfirmTokenHash()));
        assertEquals("NOT_REQUESTED", inserted.get().getAdminNoticeStatus());
        assertEquals("OTHER", inserted.get().getOrderSource());
        assertNull(inserted.get().getPaymentConfirmedAt());
        verifyNoInteractions(mail);
    }

    @Test
    void customAmountDoesNotAccidentallyKeepPreviouslySelectedProduct() {
        OrderReq request = normalRequest();
        request.setCustom(true);
        request.setProductId(1L);
        service.addOrder(request, browser());
        assertNull(inserted.get().getProductId());
        assertEquals("OTHER", inserted.get().getOrderSource());
        verifyNoInteractions(mail);
    }

    @Test
    void productOrderKeepsItsSourceWithoutSendingMail() {
        OrderReq request = normalRequest();
        request.setProductId(1L);
        service.addOrder(request, browser());
        assertEquals("PRODUCT", inserted.get().getOrderSource());
        verifyNoInteractions(mail);
    }

    @Test
    void openApiReturnsCompleteConfirmationLinkWithoutNotifyingAdmin() {
        OpenApiOrderReq request = new OpenApiOrderReq();
        request.setOrderNo("EXT+1 & 订单#1");
        request.setAmount(new BigDecimal("9.90"));
        request.setPayType("wechat");
        request.setTimestamp(System.currentTimeMillis());
        when(signs.verifyTimestamp(anyLong())).thenReturn(true);
        when(signs.verifySign(request)).thenReturn(true);
        OpenApiOrderResp response = service.createOpenApiOrder(request);
        assertTrue(PaymentConfirmTokens.matches(response.getPaymentConfirmToken(), inserted.get().getPaymentConfirmTokenHash()));
        assertTrue(response.getReturnUrl().contains("paymentConfirmToken=" + response.getPaymentConfirmToken()));
        assertTrue(response.getReturnUrl().contains("orderId=EXT%2B1%20%26%20%E8%AE%A2%E5%8D%95%231"));
        assertEquals("OPENAPI", inserted.get().getOrderSource());
        assertEquals(0, inserted.get().getState());
        verifyNoInteractions(mail);
    }

    @Test
    void customAndNullSourceLegacyOrdersCanBeApprovedOnlyOnce() {
        Order order = new Order();
        order.setId("CUSTOM-1");
        order.setState(0);
        order.setCreateTime(new Date());
        order.setEmail("buyer@example.com");
        when(orders.selectById("CUSTOM-1")).thenReturn(order);
        when(orders.approveOrder("CUSTOM-1")).thenReturn(1);
        assertEquals(1, service.pass("CUSTOM-1"));
        assertEquals(1, order.getState());
        assertEquals(1, service.pass("CUSTOM-1"));
        verify(orders, times(1)).approveOrder("CUSTOM-1");
        verify(mail, times(1)).sendTemplateMail(any(), eq("buyer@example.com"), anyString(), eq("order-success"), same(order));
    }
}
