# 依赖、配置键与外部资源目录

本页自动读取 POM 与 CodeGraph 配置键，不解析在线依赖树，不重复账号、口令和配置值。未显式写版本的依赖由父 POM 管理。

## Maven 直接依赖

| groupId | artifactId | 声明版本 | optional / scope |
| --- | --- | --- | --- |
| org.hibernate | hibernate-validator | 6.1.5.Final |  |
| org.springframework.boot | spring-boot-starter-web | 父 POM 管理 |  |
| org.springframework.boot | spring-boot-devtools | 父 POM 管理 | true |
| com.alibaba | druid | 1.1.4 |  |
| mysql | mysql-connector-java | 父 POM 管理 |  |
| org.springframework.boot | spring-boot-starter-redis | 1.4.7.RELEASE |  |
| org.springframework.boot | spring-boot-starter-thymeleaf | 父 POM 管理 |  |
| net.sourceforge.nekohtml | nekohtml | 1.9.22 |  |
| org.springframework.boot | spring-boot-starter-cache | 父 POM 管理 |  |
| org.springframework.boot | spring-boot-starter-mail | 父 POM 管理 |  |
| io.springfox | springfox-swagger-ui | 2.7.0 |  |
| io.springfox | springfox-swagger2 | 2.7.0 |  |
| com.alibaba | fastjson | 2.0.23 |  |
| com.alipay.sdk | alipay-sdk-java | 3.7.26.ALL |  |
| org.projectlombok | lombok | ${lombok.version} |  |
| com.baomidou | mybatis-plus-boot-starter | 3.5.1 |  |
| cn.hutool | hutool-all | 5.4.6 |  |

## 构建插件

| 插件 | 配置 |
| --- | --- |
| maven-compiler-plugin | source=1.8, target=1.8, encoding=UTF-8 |
| spring-boot-maven-plugin | fork=true |

## YAML 配置键

按索引中的 YAML 常量节点列出；列表项目的同名键会在不同源码行重复出现。Compose YAML 在当前索引没有标量节点，其服务 / 环境变量已在部署文档完整列出。Java 默认属性和 YAML 未声明字段见源码符号目录。

| 文件 | 行号 | 配置路径 |
| --- | ---: | --- |
| [config/application-prod.yml](../config/application-prod.yml) | 9 | `spring.mail.host` |
| [config/application-prod.yml](../config/application-prod.yml) | 10 | `spring.mail.port` |
| [config/application-prod.yml](../config/application-prod.yml) | 11 | `spring.mail.username` |
| [config/application-prod.yml](../config/application-prod.yml) | 12 | `spring.mail.password` |
| [config/application-prod.yml](../config/application-prod.yml) | 16 | `spring.mail.properties.mail.smtp.auth` |
| [config/application-prod.yml](../config/application-prod.yml) | 18 | `spring.mail.properties.mail.smtp.starttls.enable` |
| [config/application-prod.yml](../config/application-prod.yml) | 19 | `spring.mail.properties.mail.smtp.starttls.required` |
| [config/application-prod.yml](../config/application-prod.yml) | 21 | `spring.mail.properties.mail.smtp.ssl.trust` |
| [config/application-prod.yml](../config/application-prod.yml) | 26 | `paypro.site` |
| [config/application-prod.yml](../config/application-prod.yml) | 30 | `paypro.alipayUserId` |
| [config/application-prod.yml](../config/application-prod.yml) | 32 | `paypro.alipayCustomQrUrl` |
| [config/application-prod.yml](../config/application-prod.yml) | 36 | `paypro.title` |
| [config/application-prod.yml](../config/application-prod.yml) | 38 | `paypro.indexTitle` |
| [config/application-prod.yml](../config/application-prod.yml) | 40 | `paypro.name` |
| [config/application-prod.yml](../config/application-prod.yml) | 42 | `paypro.mobile` |
| [config/application-prod.yml](../config/application-prod.yml) | 47 | `paypro.email.receiver` |
| [config/application-prod.yml](../config/application-prod.yml) | 49 | `paypro.email.sender` |
| [config/application-prod.yml](../config/application-prod.yml) | 51 | `paypro.supportMail` |
| [config/application-prod.yml](../config/application-prod.yml) | 56 | `paypro.rateLimit.ipExpire` |
| [config/application-prod.yml](../config/application-prod.yml) | 61 | `paypro.token.value` |
| [config/application-prod.yml](../config/application-prod.yml) | 63 | `paypro.token.expire` |
| [config/application-prod.yml](../config/application-prod.yml) | 68 | `paypro.openapi.secret` |
| [config/application-prod.yml](../config/application-prod.yml) | 72 | `paypro.qrCodeNum` |
| [config/application-prod.yml](../config/application-prod.yml) | 77 | `paypro.decrement.enabled` |
| [config/application-prod.yml](../config/application-prod.yml) | 79 | `paypro.decrement.maxCount` |
| [config/application-prod.yml](../config/application-prod.yml) | 81 | `paypro.decrement.step` |
| [config/application-prod.yml](../config/application-prod.yml) | 87 | `paypro.products.product-name` |
| [config/application-prod.yml](../config/application-prod.yml) | 88 | `paypro.products.money` |
| [config/application-prod.yml](../config/application-prod.yml) | 89 | `paypro.products.description` |
| [config/application-prod.yml](../config/application-prod.yml) | 90 | `paypro.products.type` |
| [config/application-prod.yml](../config/application-prod.yml) | 91 | `paypro.products.extend` |
| [config/application-prod.yml](../config/application-prod.yml) | 92 | `paypro.products.download-url` |
| [config/application-prod.yml](../config/application-prod.yml) | 105 | `paypro.payMethods.name` |
| [config/application-prod.yml](../config/application-prod.yml) | 106 | `paypro.payMethods.description` |
| [config/application-prod.yml](../config/application-prod.yml) | 107 | `paypro.payMethods.icon` |
| [config/application-prod.yml](../config/application-prod.yml) | 108 | `paypro.payMethods.status` |
| [config/application-prod.yml](../config/application-prod.yml) | 109 | `paypro.payMethods.allow-night` |
| [config/application-prod.yml](../config/application-prod.yml) | 110 | `paypro.payMethods.use-local-qr-code` |
| [config/application-prod.yml](../config/application-prod.yml) | 112 | `paypro.payMethods.name` |
| [config/application-prod.yml](../config/application-prod.yml) | 113 | `paypro.payMethods.description` |
| [config/application-prod.yml](../config/application-prod.yml) | 114 | `paypro.payMethods.icon` |
| [config/application-prod.yml](../config/application-prod.yml) | 115 | `paypro.payMethods.status` |
| [config/application-prod.yml](../config/application-prod.yml) | 116 | `paypro.payMethods.allow-night` |
| [config/application-prod.yml](../config/application-prod.yml) | 117 | `paypro.payMethods.use-local-qr-code` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 2 | `server.port` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 6 | `spring.profiles.active` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 8 | `spring.mail.host` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 9 | `spring.mail.password` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 10 | `spring.mail.port` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 14 | `spring.mail.properties.mail.smtp.auth` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 16 | `spring.mail.properties.mail.smtp.starttls.enable` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 17 | `spring.mail.properties.mail.smtp.starttls.required` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 19 | `spring.mail.properties.mail.smtp.ssl.trust` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 20 | `spring.mail.username` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 24 | `spring.output.ansi.enabled` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 26 | `spring.thymeleaf.cache` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 27 | `spring.thymeleaf.enabled` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 28 | `spring.thymeleaf.mode` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 30 | `spring.datasource.driverClassName` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 31 | `spring.datasource.filters` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 32 | `spring.datasource.initialSize` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 33 | `spring.datasource.maxActive` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 34 | `spring.datasource.maxPoolPreparedStatementPerConnectionSize` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 35 | `spring.datasource.maxWait` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 36 | `spring.datasource.minEvictableIdleTimeMillis` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 37 | `spring.datasource.minIdle` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 38 | `spring.datasource.password` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 39 | `spring.datasource.poolPreparedStatements` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 40 | `spring.datasource.testOnBorrow` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 41 | `spring.datasource.testOnReturn` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 42 | `spring.datasource.testWhileIdle` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 43 | `spring.datasource.timeBetweenEvictionRunsMillis` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 44 | `spring.datasource.type` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 45 | `spring.datasource.url` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 46 | `spring.datasource.username` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 47 | `spring.datasource.validationQuery` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 49 | `spring.redis.database` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 50 | `spring.redis.host` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 51 | `spring.redis.port` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 53 | `spring.redis.pool.max-active` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 54 | `spring.redis.pool.max-idle` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 55 | `spring.redis.pool.max-wait` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 56 | `spring.redis.pool.min-idle` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 57 | `spring.redis.timeout` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 61 | `mybatis-plus.configuration.log-impl` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 62 | `mybatis-plus.mapper-locations` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 65 | `mybatis-plus.global-config.db-config.update-strategy` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 67 | `mybatis-plus.global-config.db-config.logic-delete-field` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 69 | `mybatis-plus.global-config.db-config.logic-delete-value` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 71 | `mybatis-plus.global-config.db-config.logic-not-delete-value` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 74 | `paypro.alipayCustomQrUrl` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 75 | `paypro.alipayUserId` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 76 | `paypro.indexTitle` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 77 | `paypro.name` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 78 | `paypro.title` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 79 | `paypro.site` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 80 | `paypro.qr-dir` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 81 | `paypro.mobile` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 83 | `paypro.email.receiver` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 84 | `paypro.email.sender` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 87 | `paypro.rateLimit.ipExpire` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 89 | `paypro.token.value` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 90 | `paypro.token.expire` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 91 | `paypro.qrCodeNum` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 93 | `paypro.decrement.enabled` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 94 | `paypro.decrement.maxCount` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 95 | `paypro.decrement.step` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 97 | `paypro.openapi.secret` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 100 | `paypro.products.product-name` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 101 | `paypro.products.money` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 102 | `paypro.products.description` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 103 | `paypro.products.type` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 104 | `paypro.products.extend` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 105 | `paypro.products.download-url` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 109 | `paypro.payMethods.name` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 110 | `paypro.payMethods.description` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 111 | `paypro.payMethods.icon` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 112 | `paypro.payMethods.status` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 113 | `paypro.payMethods.allow-night` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 114 | `paypro.payMethods.use-local-qr-code` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 116 | `paypro.payMethods.name` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 117 | `paypro.payMethods.description` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 118 | `paypro.payMethods.icon` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 119 | `paypro.payMethods.status` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 120 | `paypro.payMethods.allow-night` |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 121 | `paypro.payMethods.use-local-qr-code` |

## 页面外部引用

只记录 HTML 标签和 CSS 中实际声明的外链，不表示已验证可用或认可站点说明。

| 文件 | 标签 | URL |
| --- | --- | --- |
| help.html | link | `https://cdn.bootcdn.net/ajax/libs/remixicon/3.5.0/remixicon.css` |
| help.html | script | `https://cdn.bootcdn.net/ajax/libs/vue/3.3.4/vue.global.min.js` |
| history.html | link | `https://cdn.bootcdn.net/ajax/libs/remixicon/3.5.0/remixicon.css` |
| history.html | script | `https://cdn.bootcdn.net/ajax/libs/vue/3.3.4/vue.global.min.js` |
| home.html | link | `https://cdn.bootcdn.net/ajax/libs/remixicon/3.5.0/remixicon.css` |
| home.html | script | `https://cdn.bootcdn.net/ajax/libs/vue/3.3.4/vue.global.min.js` |
| index.html | link | `https://cdn.bootcdn.net/ajax/libs/remixicon/3.5.0/remixicon.css` |
| index.html | script | `https://cdn.bootcdn.net/ajax/libs/vue/3.3.4/vue.global.min.js` |
| openAlipay.html | link | `https://gw.alipayobjects.com/as/g/antui/antui/10.1.32/??dpl/widget/message.css,dpl/icon/message.css,dpl/widget/search.css` |
| openAlipay.html | link | `https://gw.alipayobjects.com/as/g/antui/antui/10.1.32/dpl/antui.css` |
| openAlipay.html | link | `https://gw.alipayobjects.com/as/g/antui/antui/10.1.32/dpl/widget/dialog.css` |
| openAlipay.html | link | `https://gw.alipayobjects.com/as/g/antui/antui/10.1.32/dpl/widget/notice.css` |
| openAlipay.html | link | `https://gw.alipayobjects.com/as/g/antui/antui/10.1.32/dpl/widget/tips.css` |
| openAlipay.html | script | `https://cdn.bootcdn.net/ajax/libs/vue/3.3.4/vue.global.min.js` |
| openAlipay.html | script | `https://gw.alipayobjects.com/as/g/antui/antui/10.1.32/antui.js` |
| openAlipay.html | script | `https://gw.alipayobjects.com/as/g/h5-lib/alipayjsapi/3.1.1/alipayjsapi.min.js` |
| order-del.html | script | `https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.min.js` |
| order-edit.html | script | `https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.min.js` |
| order-success.html | img | `https://i.loli.net/2018/07/18/5b4f12fb00713.png` |
| payment.html | link | `https://cdn.bootcdn.net/ajax/libs/remixicon/3.5.0/remixicon.css` |
| payment.html | script | `https://cdn.bootcdn.net/ajax/libs/vue/3.3.4/vue.global.min.js` |
| recharge.html | link | `https://cdn.bootcdn.net/ajax/libs/remixicon/3.5.0/remixicon.css` |
| recharge.html | script | `https://cdn.bootcdn.net/ajax/libs/vue/3.3.4/vue.global.min.js` |
| statistic.html | script | `https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.min.js` |
| common.css | @import | `https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap` |
