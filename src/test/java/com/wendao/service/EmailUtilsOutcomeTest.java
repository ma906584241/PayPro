package com.wendao.service;

import com.wendao.common.utils.EmailUtils;
import com.wendao.config.PayProConfig;
import com.wendao.entity.Order;
import org.junit.jupiter.api.Test;
import org.springframework.mail.MailSendException;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.test.util.ReflectionTestUtils;
import org.thymeleaf.spring5.SpringTemplateEngine;
import org.thymeleaf.templateresolver.ClassLoaderTemplateResolver;
import org.thymeleaf.context.Context;

import javax.mail.Session;
import javax.mail.internet.MimeMessage;
import java.math.BigDecimal;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Date;
import java.util.Properties;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

class EmailUtilsOutcomeTest {
    private SpringTemplateEngine engine() {
        ClassLoaderTemplateResolver resolver = new ClassLoaderTemplateResolver();
        resolver.setPrefix("templates/");
        resolver.setSuffix(".html");
        resolver.setCharacterEncoding("UTF-8");
        resolver.setTemplateMode("HTML");
        SpringTemplateEngine engine = new SpringTemplateEngine();
        engine.setTemplateResolver(resolver);
        return engine;
    }

    @Test
    void reviewTemplateRendersAndSmtpErrorsReachNotificationWorker() throws Exception {
        JavaMailSender smtp = mock(JavaMailSender.class);
        MimeMessage message = new MimeMessage(Session.getInstance(new Properties()));
        when(smtp.createMimeMessage()).thenReturn(message);
        EmailUtils mail = new EmailUtils();
        PayProConfig config = new PayProConfig();
        config.setIndexTitle("Test Site");
        config.setName("Test Recipient");
        config.setSupportMail("support@example.com");
        ReflectionTestUtils.setField(mail, "mailSender", smtp);
        ReflectionTestUtils.setField(mail, "templateEngine", engine());
        ReflectionTestUtils.setField(mail, "payProConfig", config);
        Order order = new Order();
        order.setId("ORDER-TEST");
        order.setMoney(new BigDecimal("9.90"));
        order.setPaymentConfirmedAt(new Date());
        mail.sendTemplateMailOrThrow("sender@example.com", "admin@example.com", "Review", "payment-review", order);
        verify(smtp).send(message);
        doThrow(new MailSendException("simulated SMTP failure")).when(smtp).send(any(MimeMessage.class));
        assertThrows(MailSendException.class, () -> mail.sendTemplateMailOrThrow(
                "sender@example.com", "admin@example.com", "Review", "payment-review", order));
    }

    @Test
    void actualThymeleafJavaScriptInliningPreservesAlipayUrlParameters() throws Exception {
        Context context = new Context();
        context.setVariable("indexTitle", "Test Site");
        context.setVariable("name", "Test Recipient");
        context.setVariable("supportMail", "support@example.com");
        context.setVariable("alipayCustomQrUrl", "https://qr.alipay.com/test?0&T=value with spaces");
        String html = engine().process("payment", context);
        assertFalse(html.contains("/*[[${alipayCustomQrUrl}]]*/"));
        assertFalse(html.contains("[[${indexTitle}]]"));
        assertTrue(html.contains("paymentConfirmToken"));
        assertTrue(html.contains("value with spaces"));
        Files.write(Paths.get("target/rendered-payment.html"), html.getBytes(StandardCharsets.UTF_8));
    }
}
