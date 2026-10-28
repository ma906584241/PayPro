package com.wendao.common.utils;

import com.wendao.config.PayProConfig;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;
import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.Context;

import javax.mail.internet.MimeMessage;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 */
@Component
public class EmailUtils {

    private static final Logger log = LoggerFactory.getLogger(EmailUtils.class);

    @Autowired
    private JavaMailSender mailSender;

    @Autowired
    private TemplateEngine templateEngine;

    @Autowired
    private PayProConfig payProConfig;

    /**
     * 发送模版邮件
     * @param sender
     * @param sendto
     * @param templateName
     * @param o
     */
    @Async
    public void sendTemplateMail(String sender, String sendto,String title, String templateName,Object o) {
        try {
            sendTemplateMailOrThrow(sender, sendto, title, templateName, o);
        } catch (Exception e) {
            log.error("邮件发送失败，模板 {}", templateName, e);
        }
    }

    /** Synchronous delivery for callers that persist the actual SMTP outcome. */
    public void sendTemplateMailOrThrow(String sender, String sendto, String title,
                                       String templateName, Object o) throws Exception {
        MimeMessage message = mailSender.createMimeMessage();
        //true表示需要创建一个multipart message html内容
        MimeMessageHelper helper = new MimeMessageHelper(message, true);
        helper.setFrom(sender);
        helper.setTo(sendto);
        helper.setSubject(title);

        Context context = new Context();
        context.setVariable("title",title);
        context.setVariables(StringUtils.beanToMap(o));
        context.setVariable("indexTitle", payProConfig.getIndexTitle());
        context.setVariable("name", payProConfig.getName());
        context.setVariable("supportMail", payProConfig.getSupportMail());
        //获取模板html代码
        String content = templateEngine.process(templateName, context);

        helper.setText(content, true);

        mailSender.send(message);
        log.info("邮件已交给 SMTP，模板 {}", templateName);
    }

    /**
     * 验证邮箱
     * @param email
     * @return
     */
    public static boolean checkEmail(String email) {
        boolean flag = false;
        try {
            String check = "^\\w+@[a-zA-Z0-9]{2,10}(?:\\.[a-z]{2,4}){1,3}$";
            Pattern regex = Pattern.compile(check);
            Matcher matcher = regex.matcher(email);
            flag = matcher.matches();
        } catch (Exception e) {
            flag = false;
        }
        return flag;
    }
}
