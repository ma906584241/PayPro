# 全量文件清单

项目原始文件共 **168** 个；不包含本轮 docs 与 .codegraph 产物。

从工作区实际内容计算 SHA-256。文本行数按 UTF-8 读取；图片 / 二进制不按文本计行。此清单不复制配置值或收款二维码内容。

## 文件类型统计

| 扩展名 | 数量 |
| --- | ---: |
| .cjs | 1 |
| .css | 1 |
| .example | 1 |
| .html | 15 |
| .ico | 1 |
| .java | 45 |
| .jpg | 2 |
| .js | 3 |
| .md | 3 |
| .png | 81 |
| .sh | 2 |
| .sql | 2 |
| .xml | 2 |
| .yml | 3 |
| 无扩展名 | 6 |

## 文件与用途

| 文件 | 字节 | 行数 | 格式 / 用途 |
| --- | ---: | ---: | --- |
| [.dockerignore](../.dockerignore) | 158 | 9 |  排除私密环境、Git、图谱、文档与本地构建产物的 Docker 上下文规则 |
| [.env.example](../.env.example) | 162 | 3 |  QQ SMTP 授权码环境变量示例，不含真实凭据 |
| [.gitattributes](../.gitattributes) | 154 | 7 |  文本 LF 规则和 Compose 二进制标记 |
| [.gitignore](../.gitignore) | 66 | 4 |  IDE、构建产物和本地配置排除规则 |
| [Dockerfile](../Dockerfile) | 695 | 28 |  Maven 构建 + JDK8 运行的多阶段镜像 |
| [OPEN_API.md](../OPEN_API.md) | 7181 | 226 |  原 OpenAPI 说明，与当前实现存在差异 |
| [README.md](../README.md) | 11440 | 328 |  原项目介绍、开源 / 高级版说明和截图 |
| [config/application-prod.yml](../config/application-prod.yml) | 3340 | 122 |  外置生产配置，含部署账号与业务参数 |
| [docker-compose](../docker-compose) | 12212176 | — | ELF 64-bit x86-64 Linux x86-64 ELF Compose 可执行文件（非文本） |
| [docker-compose.yml](../docker-compose.yml) | 2257 | 88 |  MySQL / Redis / pay 三服务与卷、健康检查 |
| [images/alipay_confirm.png](../images/alipay_confirm.png) | 200293 | — | PNG 1915×899 原 README 功能截图 |
| [images/home.png](../images/home.png) | 1074574 | — | PNG 3322×1634 原 README 功能截图 |
| [images/payment-help.png](../images/payment-help.png) | 378393 | — | PNG 2434×1506 原 README 功能截图 |
| [images/payment-review.png](../images/payment-review.png) | 51312 | — | PNG 704×792 原 README 功能截图 |
| [images/payment.png](../images/payment.png) | 1042242 | — | PNG 2328×1530 原 README 功能截图 |
| [images/recharge.png](../images/recharge.png) | 1193066 | — | PNG 2358×1682 原 README 功能截图 |
| [images/wechat_confirm.png](../images/wechat_confirm.png) | 389500 | — | JPEG 原 README 功能截图 |
| [install.sh](../install.sh) | 4247 | 128 |  Linux 一键部署与 Compose 安装 |
| [pom.xml](../pom.xml) | 5647 | 159 |  Maven 坐标、父 POM、依赖、编译与打包插件 |
| [qr/alipay/custom.png](../qr/alipay/custom.png) | 166855 | — | PNG 432×428 运行时外置支付二维码：alipay/custom.png |
| [qr/wechat/0.01/1.png](../qr/wechat/0.01/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/0.01/1.png |
| [qr/wechat/0.01/2.png](../qr/wechat/0.01/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/0.01/2.png |
| [qr/wechat/1.00/1.png](../qr/wechat/1.00/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/1.00/1.png |
| [qr/wechat/1.00/2.png](../qr/wechat/1.00/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/1.00/2.png |
| [qr/wechat/10.00/1.png](../qr/wechat/10.00/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/10.00/1.png |
| [qr/wechat/10.00/2.png](../qr/wechat/10.00/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/10.00/2.png |
| [qr/wechat/29.00/1.png](../qr/wechat/29.00/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/29.00/1.png |
| [qr/wechat/29.00/2.png](../qr/wechat/29.00/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/29.00/2.png |
| [qr/wechat/29.00/28.98/1.png](../qr/wechat/29.00/28.98/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/29.00/28.98/1.png |
| [qr/wechat/29.00/28.98/2.png](../qr/wechat/29.00/28.98/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/29.00/28.98/2.png |
| [qr/wechat/29.00/28.99/1.png](../qr/wechat/29.00/28.99/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/29.00/28.99/1.png |
| [qr/wechat/29.00/28.99/2.png](../qr/wechat/29.00/28.99/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/29.00/28.99/2.png |
| [qr/wechat/49.00/1.png](../qr/wechat/49.00/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/49.00/1.png |
| [qr/wechat/49.00/2.png](../qr/wechat/49.00/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/49.00/2.png |
| [qr/wechat/5.00/1.png](../qr/wechat/5.00/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/5.00/1.png |
| [qr/wechat/5.00/2.png](../qr/wechat/5.00/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/5.00/2.png |
| [qr/wechat/5.00/4.98/1.png](../qr/wechat/5.00/4.98/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/5.00/4.98/1.png |
| [qr/wechat/5.00/4.98/2.png](../qr/wechat/5.00/4.98/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/5.00/4.98/2.png |
| [qr/wechat/5.00/4.99/1.png](../qr/wechat/5.00/4.99/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/5.00/4.99/1.png |
| [qr/wechat/5.00/4.99/2.png](../qr/wechat/5.00/4.99/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/5.00/4.99/2.png |
| [qr/wechat/5.00/5.01/1.png](../qr/wechat/5.00/5.01/1.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/5.00/5.01/1.png |
| [qr/wechat/5.00/5.01/2.png](../qr/wechat/5.00/5.01/2.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/5.00/5.01/2.png |
| [qr/wechat/custom.png](../qr/wechat/custom.png) | 50953 | — | PNG 444×447 运行时外置支付二维码：wechat/custom.png |
| [qr/wechat_zs/custom.png](../qr/wechat_zs/custom.png) | 63239 | — | JPEG 运行时外置支付二维码：wechat_zs/custom.png |
| [settings.xml](../settings.xml) | 234 | 10 |  Maven central 镜像配置 |
| [src/main/java/com/wendao/PayApplication.java](../src/main/java/com/wendao/PayApplication.java) | 719 | 25 |  Spring Boot 入口，开启缓存、异步、调度与 Mapper 扫描 |
| [src/main/java/com/wendao/common/utils/DateUtils.java](../src/main/java/com/wendao/common/utils/DateUtils.java) | 11724 | 342 |  日期起止、统计窗口、日期差和日期集合工具 |
| [src/main/java/com/wendao/common/utils/EmailUtils.java](../src/main/java/com/wendao/common/utils/EmailUtils.java) | 3088 | 92 |  异步 Thymeleaf HTML 邮件与邮箱格式校验 |
| [src/main/java/com/wendao/common/utils/IpInfoUtils.java](../src/main/java/com/wendao/common/utils/IpInfoUtils.java) | 1780 | 56 |  从代理头和请求读取客户端 IP |
| [src/main/java/com/wendao/common/utils/StringUtils.java](../src/main/java/com/wendao/common/utils/StringUtils.java) | 2522 | 108 |  空白检查、日期转换、Bean 转 Map、四位备注码 |
| [src/main/java/com/wendao/config/Config.java](../src/main/java/com/wendao/config/Config.java) | 2367 | 61 |  CORS、Thymeleaf 全局变量、分页插件与 Snowflake Bean |
| [src/main/java/com/wendao/config/PayProConfig.java](../src/main/java/com/wendao/config/PayProConfig.java) | 6487 | 271 |  paypro 配置绑定、配置商品检索、外置二维码映射 |
| [src/main/java/com/wendao/config/RedisConfig.java](../src/main/java/com/wendao/config/RedisConfig.java) | 1690 | 36 |  Object RedisTemplate 与 Jackson 序列化配置 |
| [src/main/java/com/wendao/controller/OrderController.java](../src/main/java/com/wendao/controller/OrderController.java) | 12339 | 302 |  订单、审核、统计、OpenAPI 和支付方式路由 |
| [src/main/java/com/wendao/controller/PageController.java](../src/main/java/com/wendao/controller/PageController.java) | 1956 | 67 |  根页与通用模板路由，支付宝页状态副作用 |
| [src/main/java/com/wendao/controller/ProductController.java](../src/main/java/com/wendao/controller/ProductController.java) | 1329 | 41 |  按 ID / 类型公开读取配置商品 |
| [src/main/java/com/wendao/dto/MsgContentsDTO.java](../src/main/java/com/wendao/dto/MsgContentsDTO.java) | 895 | 33 |  消息内容与付款方备注正则提取 |
| [src/main/java/com/wendao/dto/WeChatMsgDTO.java](../src/main/java/com/wendao/dto/WeChatMsgDTO.java) | 528 | 26 |  微信消息结构，当前未接入到账业务入口 |
| [src/main/java/com/wendao/entity/Order.java](../src/main/java/com/wendao/entity/Order.java) | 3269 | 151 |  订单持久化实体及邮件管理 URL 临时属性 |
| [src/main/java/com/wendao/entity/Product.java](../src/main/java/com/wendao/entity/Product.java) | 686 | 36 |  配置商品实体，非数据库表 |
| [src/main/java/com/wendao/enums/AdminNoticeStatus.java](../src/main/java/com/wendao/enums/AdminNoticeStatus.java) | 179 | 6 |  管理员通知状态，与订单付款状态分离 |
| [src/main/java/com/wendao/enums/OrderStatesEnum.java](../src/main/java/com/wendao/enums/OrderStatesEnum.java) | 570 | 38 |  订单状态 0 / 1 / 2 / 4 / 5 |
| [src/main/java/com/wendao/exception/ApiException.java](../src/main/java/com/wendao/exception/ApiException.java) | 835 | 30 |  业务异常与错误码常量 |
| [src/main/java/com/wendao/exception/GlobalExceptionHandler.java](../src/main/java/com/wendao/exception/GlobalExceptionHandler.java) | 2305 | 55 |  业务、参数与通用异常转换为 ResponseVO |
| [src/main/java/com/wendao/mapper/OrderMapper.java](../src/main/java/com/wendao/mapper/OrderMapper.java) | 2814 | 59 |  订单 BaseMapper、聚合统计、过期与实际金额查询 |
| [src/main/java/com/wendao/model/ResponseVO.java](../src/main/java/com/wendao/model/ResponseVO.java) | 1482 | 68 |  通用 code / msg / data 响应封装 |
| [src/main/java/com/wendao/model/req/ConfirmPaidReq.java](../src/main/java/com/wendao/model/req/ConfirmPaidReq.java) | 309 | 13 |  客户主动声明付款请求，订单号和客户凭证非空 |
| [src/main/java/com/wendao/model/req/GetOrderListReq.java](../src/main/java/com/wendao/model/req/GetOrderListReq.java) | 533 | 35 |  订单分页、状态、关键词与排序请求 |
| [src/main/java/com/wendao/model/req/GetProductListReq.java](../src/main/java/com/wendao/model/req/GetProductListReq.java) | 224 | 17 |  商品类型列表请求 |
| [src/main/java/com/wendao/model/req/OpenApiOrderReq.java](../src/main/java/com/wendao/model/req/OpenApiOrderReq.java) | 960 | 45 |  外部下单与签名参数模型 |
| [src/main/java/com/wendao/model/req/OrderReq.java](../src/main/java/com/wendao/model/req/OrderReq.java) | 1186 | 65 |  普通下单请求模型 |
| [src/main/java/com/wendao/model/resp/AddOrderResp.java](../src/main/java/com/wendao/model/resp/AddOrderResp.java) | 1543 | 62 |  普通下单支付信息响应 |
| [src/main/java/com/wendao/model/resp/CountResp.java](../src/main/java/com/wendao/model/resp/CountResp.java) | 306 | 17 |  成功订单原价统计响应 |
| [src/main/java/com/wendao/model/resp/OpenApiOrderResp.java](../src/main/java/com/wendao/model/resp/OpenApiOrderResp.java) | 802 | 44 |  外部下单、二维码与支付页响应 |
| [src/main/java/com/wendao/model/resp/PaymentConfirmationResp.java](../src/main/java/com/wendao/model/resp/PaymentConfirmationResp.java) | 425 | 18 |  鉴权付款声明查询响应、通知状态和重试资格 |
| [src/main/java/com/wendao/service/OrderService.java](../src/main/java/com/wendao/service/OrderService.java) | 1996 | 86 |  订单业务接口 |
| [src/main/java/com/wendao/service/PaymentConfirmationService.java](../src/main/java/com/wendao/service/PaymentConfirmationService.java) | 6574 | 158 |  鉴权声明、发送锁、事务提交后调度及状态恢复 |
| [src/main/java/com/wendao/service/PaymentNoticeLock.java](../src/main/java/com/wendao/service/PaymentNoticeLock.java) | 1441 | 40 |  Redis SET NX发送租约与Lua归属校验释放 |
| [src/main/java/com/wendao/service/PaymentNoticeSender.java](../src/main/java/com/wendao/service/PaymentNoticeSender.java) | 4980 | 108 |  提交后异步邮件、独立审核链接、SMTP结果持久化 |
| [src/main/java/com/wendao/service/ProductService.java](../src/main/java/com/wendao/service/ProductService.java) | 629 | 24 |  商品业务接口 |
| [src/main/java/com/wendao/service/impl/OrderServiceImpl.java](../src/main/java/com/wendao/service/impl/OrderServiceImpl.java) | 31070 | 747 |  普通 / 外部下单、减额、审核、分页、统计与回调 |
| [src/main/java/com/wendao/service/impl/ProductServiceImpl.java](../src/main/java/com/wendao/service/impl/ProductServiceImpl.java) | 2350 | 65 |  YAML 商品转实体，公开接口清除下载链接 |
| [src/main/java/com/wendao/utils/OpenApiSignUtil.java](../src/main/java/com/wendao/utils/OpenApiSignUtil.java) | 4767 | 113 |  OpenAPI MD5 签名、验签及五分钟时间戳验证 |
| [src/main/java/com/wendao/utils/PaymentConfirmTokens.java](../src/main/java/com/wendao/utils/PaymentConfirmTokens.java) | 1701 | 47 |  生成客户随机凭证、保存哈希并恒定时间校验 |
| [src/main/resources/Dockerfile](../src/main/resources/Dockerfile) | 421 | 20 |  从预构建 JAR 构建运行镜像的旧入口 |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 3173 | 127 |  包内基础 Spring 与 paypro 配置 |
| [src/main/resources/favicon.ico](../src/main/resources/favicon.ico) | 12181 | — | PNG 256×256 站点图标资源 |
| [src/main/resources/sql/migrations/20261028_payment_confirmation.sql](../src/main/resources/sql/migrations/20261028_payment_confirmation.sql) | 450 | 7 |  已有数据库增量升级，仅新增三个付款声明字段 |
| [src/main/resources/sql/pay.sql](../src/main/resources/sql/pay.sql) | 2860 | 60 |  订单表初始化、减额迁移和索引 |
| [src/main/resources/start.sh](../src/main/resources/start.sh) | 2075 | 51 |  容器 JVM、profile、日志与 JMX 启动参数 |
| [src/main/resources/static/assets/images/500_icon.png](../src/main/resources/static/assets/images/500_icon.png) | 61612 | — | PNG 289×274 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/alipay.png](../src/main/resources/static/assets/images/alipay.png) | 11351 | — | PNG 288×68 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/alipay@2x.png](../src/main/resources/static/assets/images/alipay@2x.png) | 9646 | — | PNG 288×68 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/alipaydmf.png](../src/main/resources/static/assets/images/alipaydmf.png) | 10879 | — | PNG 288×68 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/aliremark.png](../src/main/resources/static/assets/images/aliremark.png) | 26147 | — | PNG 747×485 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/confirm.png](../src/main/resources/static/assets/images/confirm.png) | 9683 | — | PNG 200×200 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/fail.png](../src/main/resources/static/assets/images/fail.png) | 7274 | — | PNG 200×200 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/order.png](../src/main/resources/static/assets/images/order.png) | 4470 | — | PNG 200×200 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/pay.png](../src/main/resources/static/assets/images/pay.png) | 4633 | — | PNG 200×200 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/qr.png](../src/main/resources/static/assets/images/qr.png) | 3948 | — | PNG 200×200 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/red.png](../src/main/resources/static/assets/images/red.png) | 6370 | — | PNG 200×200 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/sort_desc_disabled.png](../src/main/resources/static/assets/images/sort_desc_disabled.png) | 1045 | — | PNG 19×19 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/success.png](../src/main/resources/static/assets/images/success.png) | 6909 | — | PNG 200×200 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/wechat-explain.png](../src/main/resources/static/assets/images/wechat-explain.png) | 7171 | — | PNG 260×86 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/wechat.png](../src/main/resources/static/assets/images/wechat.png) | 8930 | — | PNG 288×68 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/weixin.png](../src/main/resources/static/assets/images/weixin.png) | 7949 | — | PNG 288×68 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/weixinTip.png](../src/main/resources/static/assets/images/weixinTip.png) | 12526 | — | PNG 1146×529 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/weixinpay@2x.png](../src/main/resources/static/assets/images/weixinpay@2x.png) | 4359 | — | PNG 288×68 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/wxremark.png](../src/main/resources/static/assets/images/wxremark.png) | 19729 | — | PNG 650×465 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/wxzsremark.png](../src/main/resources/static/assets/images/wxzsremark.png) | 56701 | — | JPEG 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/zfb.png](../src/main/resources/static/assets/images/zfb.png) | 18919 | — | PNG 200×200 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/zfb_open.jpg](../src/main/resources/static/assets/images/zfb_open.jpg) | 292312 | — | JPEG 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/images/优惠.png](../src/main/resources/static/assets/images/优惠.png) | 4276 | — | PNG 200×200 页面支付图标、备注说明或状态图片 |
| [src/main/resources/static/assets/js/api-config.js](../src/main/resources/static/assets/js/api-config.js) | 1992 | 64 |  API 基址、端点和超时配置 |
| [src/main/resources/static/assets/js/http-util.js](../src/main/resources/static/assets/js/http-util.js) | 5580 | 194 |  fetch 请求类和全局单例封装 |
| [src/main/resources/static/assets/js/qcode.min.js](../src/main/resources/static/assets/js/qcode.min.js) | 23743 | 7 |  第三方 qrcode@1.5.1 浏览器二维码库 |
| [src/main/resources/static/assets/qr/alipay/0.01/1.png](../src/main/resources/static/assets/qr/alipay/0.01/1.png) | 166855 | — | PNG 432×428 随 JAR 打包的支付二维码：alipay/0.01/1.png |
| [src/main/resources/static/assets/qr/alipay/0.01/2.png](../src/main/resources/static/assets/qr/alipay/0.01/2.png) | 166855 | — | PNG 432×428 随 JAR 打包的支付二维码：alipay/0.01/2.png |
| [src/main/resources/static/assets/qr/alipay/custom.png](../src/main/resources/static/assets/qr/alipay/custom.png) | 166855 | — | PNG 432×428 随 JAR 打包的支付二维码：alipay/custom.png |
| [src/main/resources/static/assets/qr/wechat/0.01/1.png](../src/main/resources/static/assets/qr/wechat/0.01/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/0.01/1.png |
| [src/main/resources/static/assets/qr/wechat/0.01/2.png](../src/main/resources/static/assets/qr/wechat/0.01/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/0.01/2.png |
| [src/main/resources/static/assets/qr/wechat/10.00/1.png](../src/main/resources/static/assets/qr/wechat/10.00/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/10.00/1.png |
| [src/main/resources/static/assets/qr/wechat/10.00/2.png](../src/main/resources/static/assets/qr/wechat/10.00/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/10.00/2.png |
| [src/main/resources/static/assets/qr/wechat/100.00/1.png](../src/main/resources/static/assets/qr/wechat/100.00/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/100.00/1.png |
| [src/main/resources/static/assets/qr/wechat/100.00/2.png](../src/main/resources/static/assets/qr/wechat/100.00/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/100.00/2.png |
| [src/main/resources/static/assets/qr/wechat/20.00/1.png](../src/main/resources/static/assets/qr/wechat/20.00/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/20.00/1.png |
| [src/main/resources/static/assets/qr/wechat/20.00/2.png](../src/main/resources/static/assets/qr/wechat/20.00/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/20.00/2.png |
| [src/main/resources/static/assets/qr/wechat/200.00/1.png](../src/main/resources/static/assets/qr/wechat/200.00/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/200.00/1.png |
| [src/main/resources/static/assets/qr/wechat/200.00/2.png](../src/main/resources/static/assets/qr/wechat/200.00/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/200.00/2.png |
| [src/main/resources/static/assets/qr/wechat/5.00/1.png](../src/main/resources/static/assets/qr/wechat/5.00/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/5.00/1.png |
| [src/main/resources/static/assets/qr/wechat/5.00/2.png](../src/main/resources/static/assets/qr/wechat/5.00/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/5.00/2.png |
| [src/main/resources/static/assets/qr/wechat/5.00/4.98/1.png](../src/main/resources/static/assets/qr/wechat/5.00/4.98/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/5.00/4.98/1.png |
| [src/main/resources/static/assets/qr/wechat/5.00/4.98/2.png](../src/main/resources/static/assets/qr/wechat/5.00/4.98/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/5.00/4.98/2.png |
| [src/main/resources/static/assets/qr/wechat/5.00/4.99/1.png](../src/main/resources/static/assets/qr/wechat/5.00/4.99/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/5.00/4.99/1.png |
| [src/main/resources/static/assets/qr/wechat/5.00/4.99/2.png](../src/main/resources/static/assets/qr/wechat/5.00/4.99/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/5.00/4.99/2.png |
| [src/main/resources/static/assets/qr/wechat/5.00/5.01/1.png](../src/main/resources/static/assets/qr/wechat/5.00/5.01/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/5.00/5.01/1.png |
| [src/main/resources/static/assets/qr/wechat/5.00/5.01/2.png](../src/main/resources/static/assets/qr/wechat/5.00/5.01/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/5.00/5.01/2.png |
| [src/main/resources/static/assets/qr/wechat/50.00/1.png](../src/main/resources/static/assets/qr/wechat/50.00/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/50.00/1.png |
| [src/main/resources/static/assets/qr/wechat/50.00/2.png](../src/main/resources/static/assets/qr/wechat/50.00/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/50.00/2.png |
| [src/main/resources/static/assets/qr/wechat/500.00/1.png](../src/main/resources/static/assets/qr/wechat/500.00/1.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/500.00/1.png |
| [src/main/resources/static/assets/qr/wechat/500.00/2.png](../src/main/resources/static/assets/qr/wechat/500.00/2.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/500.00/2.png |
| [src/main/resources/static/assets/qr/wechat/custom.png](../src/main/resources/static/assets/qr/wechat/custom.png) | 50953 | — | PNG 444×447 随 JAR 打包的支付二维码：wechat/custom.png |
| [src/main/resources/static/assets/qr/wechat_zs/custom.png](../src/main/resources/static/assets/qr/wechat_zs/custom.png) | 63239 | — | JPEG 随 JAR 打包的支付二维码：wechat_zs/custom.png |
| [src/main/resources/static/css/common.css](../src/main/resources/static/css/common.css) | 3962 | 151 |  全站主题、布局、按钮与动画 |
| [src/main/resources/templates/error.html](../src/main/resources/templates/error.html) | 932 | 27 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/help.html](../src/main/resources/templates/help.html) | 11690 | 296 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/history.html](../src/main/resources/templates/history.html) | 17648 | 440 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/home.html](../src/main/resources/templates/home.html) | 11950 | 398 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/index.html](../src/main/resources/templates/index.html) | 10262 | 314 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/openAlipay.html](../src/main/resources/templates/openAlipay.html) | 18684 | 466 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/order-del.html](../src/main/resources/templates/order-del.html) | 5069 | 170 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/order-edit.html](../src/main/resources/templates/order-edit.html) | 6868 | 221 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/order-fail.html](../src/main/resources/templates/order-fail.html) | 6570 | 215 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/order-success.html](../src/main/resources/templates/order-success.html) | 2683 | 54 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/payment-review.html](../src/main/resources/templates/payment-review.html) | 8019 | 212 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/payment.html](../src/main/resources/templates/payment.html) | 25800 | 953 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/recharge.html](../src/main/resources/templates/recharge.html) | 21398 | 664 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/statistic.html](../src/main/resources/templates/statistic.html) | 5382 | 156 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/success.html](../src/main/resources/templates/success.html) | 669 | 24 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/test/frontend/payment-confirmation.test.cjs](../src/test/frontend/payment-confirmation.test.cjs) | 6123 | 97 |  Node原生测试运行真实支付页组件，Mock网络和计时器 |
| [src/test/java/com/wendao/service/EmailUtilsOutcomeTest.java](../src/test/java/com/wendao/service/EmailUtilsOutcomeTest.java) | 3531 | 77 |  真实Thymeleaf渲染和Mock JavaMailSender结果测试 |
| [src/test/java/com/wendao/service/OrderCreationNotificationTest.java](../src/test/java/com/wendao/service/OrderCreationNotificationTest.java) | 6075 | 140 |  下单不发信、来源、自定义金额、编码链接和批准幂等测试 |
| [src/test/java/com/wendao/service/PaymentConfirmationControllerTest.java](../src/test/java/com/wendao/service/PaymentConfirmationControllerTest.java) | 3364 | 72 |  MockMvc请求体、请求头和参数错误测试 |
| [src/test/java/com/wendao/service/PaymentConfirmationDatabaseIT.java](../src/test/java/com/wendao/service/PaymentConfirmationDatabaseIT.java) | 8295 | 161 |  可选隔离MySQL/Redis增量迁移、12请求并发和元数据保护测试 |
| [src/test/java/com/wendao/service/PaymentConfirmationServiceTest.java](../src/test/java/com/wendao/service/PaymentConfirmationServiceTest.java) | 8491 | 207 |  声明鉴权、事务回滚、去重、失败重试及JSON隐私测试 |
| [src/test/java/com/wendao/service/PaymentNoticeSenderTest.java](../src/test/java/com/wendao/service/PaymentNoticeSenderTest.java) | 5095 | 123 |  SMTP结果、锁归属、旧任务和旧订单隔离测试 |
| [一键启动说明.md](../一键启动说明.md) | 4868 | 172 |  原 Linux 部署与二维码使用说明 |
| [获取支付宝userId.jpg](../获取支付宝userId.jpg) | 25132 | — | JPEG 支付宝收款用户 ID 配置辅助图片 |

## 文件哈希

| 文件 | SHA-256 |
| --- | --- |
| `.dockerignore` | `d03e99b7deb238e5ae585912060dd6cdc730f30dbbb228ebbfd7d931dab032b7` |
| `.env.example` | `9c2a01f4e39b59e6221594c28b8bbe6139b6772dc63b94fb6004277e6f9614c0` |
| `.gitattributes` | `70690cd5f403076a5a6a09b5172ed427841d80a4297df1ccdac6472b540abc3c` |
| `.gitignore` | `b54697b7acd41356ffb7e6fefb20d4e99d19d3d50d6350e5d4d1472165b5ee38` |
| `Dockerfile` | `40f927b0a3ca11e8534bb79d037f8647ce2628bc8f68fc428e60b5ac22f66516` |
| `OPEN_API.md` | `2d301fd410f97417a2b8cc88f766268d8f3ac717db668382a7cf86f1dcc63a72` |
| `README.md` | `18373a348ea36d81b8659bd16d6e3524ef92555b1956dadd822a14bb95c9cb61` |
| `config/application-prod.yml` | `b23614e67efee97b8ce094714ba5c7a062da82a93cc741d1c339c8485d09108b` |
| `docker-compose` | `f5f7d605fa17d35a29b217557db4cbe70c1824f3061c522d3cb712bf33db3a67` |
| `docker-compose.yml` | `41edb3d8cdb9a1fd4d6838dd686e8fb674686c013db9202e3510e60c90ca5784` |
| `images/alipay_confirm.png` | `2464a3782dd56fc2a193471fff102b604497c0c25c470a1c798be034e852c652` |
| `images/home.png` | `ce6f5be3c1f0813727f3c32462dd4e5971c4d2642a2b037a75bb464167260691` |
| `images/payment-help.png` | `8408d44e338da0f4bc5c1c057ba15fc614cdf6721d64e702ab9138b19e8d4f20` |
| `images/payment-review.png` | `57fe57b12d021e0c9fbfea1f196ea3b0b3fb2861655dd4a70ee8a2d7492f5e76` |
| `images/payment.png` | `9420875321a7fa3267321a5c340a1dfda71e82133f29b5e77cb77d32e074bda0` |
| `images/recharge.png` | `764eb5c779f3a9496192695cdec03f266661daa5343e64898814873f38027f0f` |
| `images/wechat_confirm.png` | `3b31f62279db8ce4b4f3b484ede6fb944ef891d6ef3338c4cbfa6ddfd1958e0a` |
| `install.sh` | `2af21f3b55b535bb4a9f9dc05438e29e5cc0d236833f10ac44db1b9494d70aa6` |
| `pom.xml` | `3c44aeea6f5822d67c9d0af6103a752b597df662536288282338d6782fd13426` |
| `qr/alipay/custom.png` | `cf4e53fa94d3ed1d810bcc377c0a8e03a578763f93014a6f6738ea35fd6c91bf` |
| `qr/wechat/0.01/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/0.01/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/1.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/1.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/10.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/10.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/29.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/29.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/29.00/28.98/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/29.00/28.98/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/29.00/28.99/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/29.00/28.99/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/49.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/49.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/5.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/5.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/5.00/4.98/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/5.00/4.98/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/5.00/4.99/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/5.00/4.99/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/5.00/5.01/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/5.00/5.01/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat/custom.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `qr/wechat_zs/custom.png` | `5222b62afc32b5a70f89db3f8c48c84bb7a4df22bc539ad1fbf444d6cdd13334` |
| `settings.xml` | `7609701f327048ca05325a0e23c659053255b8a92c6176983e2b12626385787a` |
| `src/main/java/com/wendao/PayApplication.java` | `8c457e980e7ef305a3d90fd048f4d971e2ac4a66c2a24d777f2e7fb33bc43824` |
| `src/main/java/com/wendao/common/utils/DateUtils.java` | `469849df931908ad032c90b572da61d35e6348150083804bdd5757bdc08b971d` |
| `src/main/java/com/wendao/common/utils/EmailUtils.java` | `ce0acb5f3c45fc10a09201d7bfac6d9cbd56e40ef64e8130e34fb614a15b0cd6` |
| `src/main/java/com/wendao/common/utils/IpInfoUtils.java` | `2a284e216a97065de98ffc90feb3b10a6a6f26b6017aed7f972e53fc6f8827ba` |
| `src/main/java/com/wendao/common/utils/StringUtils.java` | `951ecbc84b202c7864a83545785b7fe8b7d74c96a570653a2724c35104ff471b` |
| `src/main/java/com/wendao/config/Config.java` | `3ab32e0fe0d59caef5f78639c19e7c9c95f5b2cb0c24253a63d9f9647082e736` |
| `src/main/java/com/wendao/config/PayProConfig.java` | `347ebcce697062e4c118be026acd22e14693e24fbae3ede00104cd220d0e6df2` |
| `src/main/java/com/wendao/config/RedisConfig.java` | `8e70587a300e902cd43c22404ddca723a1b51e2af7cbfb7bec157b184d24feb6` |
| `src/main/java/com/wendao/controller/OrderController.java` | `04bf4a30f4cf3b3e7f1a3e1045bc16cf454a64f80d8fe999d9d39361615f8ee7` |
| `src/main/java/com/wendao/controller/PageController.java` | `5fbb6497d147fd6efe34ebb9c61ee5d8e6cc5ecd06a5bb16667bff78a0b5569f` |
| `src/main/java/com/wendao/controller/ProductController.java` | `cfd5fbd21d437afb9723695478b77c6dd4ad55febff5c0eec5ec4492b60a9acc` |
| `src/main/java/com/wendao/dto/MsgContentsDTO.java` | `238cfb23b61364253ffcd7d97c4632044e8ea5a12b1d262712931eb2b9c32c6a` |
| `src/main/java/com/wendao/dto/WeChatMsgDTO.java` | `d0dcdbff296e3183e94213e247954b1fa588069797ddb3e4eb5eea396db6075a` |
| `src/main/java/com/wendao/entity/Order.java` | `8516711ff652e5c77f55d8999b27628646efc66608691de451925dcdb5362dc8` |
| `src/main/java/com/wendao/entity/Product.java` | `cf666dd581ac159cc767ca01b349250685c3a7adfdc279e98ac503c9ab912703` |
| `src/main/java/com/wendao/enums/AdminNoticeStatus.java` | `823ef681f5cf457f0b63c9080c68755852b0b3d471633b8b9a7d53523f6574da` |
| `src/main/java/com/wendao/enums/OrderStatesEnum.java` | `478cef8269922429015d2d69a6018e0a70813caa34a4411090207c137d8f5c8d` |
| `src/main/java/com/wendao/exception/ApiException.java` | `7e394aead2bda9f5895b53983bd723a1b40ee4f3efb160610db746eb82ba84dc` |
| `src/main/java/com/wendao/exception/GlobalExceptionHandler.java` | `06a4ada7450b252cea6fa32330b8423cdca4c9cde1e8041cbb7008a2fda671af` |
| `src/main/java/com/wendao/mapper/OrderMapper.java` | `79d815326b072701146a77530930048d897274e19ed9bf3e8c5fdb26987d020b` |
| `src/main/java/com/wendao/model/ResponseVO.java` | `6ec52e7e7f190dcd68d01136a7fb075ff0089575dca55263e7b9fec24a75dbb8` |
| `src/main/java/com/wendao/model/req/ConfirmPaidReq.java` | `b8a7a38737fe7b58bcbc942e317c102ee4c347e73600a90531949a35088c19f3` |
| `src/main/java/com/wendao/model/req/GetOrderListReq.java` | `28abcf694d8012b6422f9a69244c1a3c37ece87952a1f2bac593fe85191935f5` |
| `src/main/java/com/wendao/model/req/GetProductListReq.java` | `44e058e5b62354c8654ff5dda7f309534d8c7a21481a9285070018f39abf1a03` |
| `src/main/java/com/wendao/model/req/OpenApiOrderReq.java` | `8ba90f21b686661725542c8e738f4dda868668eaeb1b6c4a96491d7642fb7105` |
| `src/main/java/com/wendao/model/req/OrderReq.java` | `52eec650ab8a4b69c98acfe73c641e4d98bafe342b1728a7f2ff3321efdf4579` |
| `src/main/java/com/wendao/model/resp/AddOrderResp.java` | `41f9212f6f7bbb2f5d5a1aade1d296993a83beed8eb2a1be6ede4fe28a8898b6` |
| `src/main/java/com/wendao/model/resp/CountResp.java` | `d628a611529a7fd7256f0dc8b45e38156413151c84bdf0fe689f3481dadd1abb` |
| `src/main/java/com/wendao/model/resp/OpenApiOrderResp.java` | `5e8717b31359b4c23f76a962a59ca8767241bc8f4ac34f99d40f691b320e73a6` |
| `src/main/java/com/wendao/model/resp/PaymentConfirmationResp.java` | `d3ea48bcfb58a0fb149867cc3341835a940c70d10a056abf9980d6be90183072` |
| `src/main/java/com/wendao/service/OrderService.java` | `1c96edeed6edc10d4b3f737268c20831602c16df4720f5e8dd1d9c1b06fe1969` |
| `src/main/java/com/wendao/service/PaymentConfirmationService.java` | `8b6d0a9cf633f0a0f90f74b2eeb6f1e44006a25e656da79faba5a1c87e5627cf` |
| `src/main/java/com/wendao/service/PaymentNoticeLock.java` | `5592d9fbad9817780f2bfdc5b7e2d5e2d799798f1328e6ddbedd263b402d4ec5` |
| `src/main/java/com/wendao/service/PaymentNoticeSender.java` | `74a80f0f4296f752355de3f174364488215fcb39d04846919a9377ed431ab482` |
| `src/main/java/com/wendao/service/ProductService.java` | `bda889122eb71304b3d0b70b2bbb25366cb372a3375946134d8956dd227a0282` |
| `src/main/java/com/wendao/service/impl/OrderServiceImpl.java` | `85bd7856bc1e568e21ce6fdaa4feade0d51de348c3cd16003b78f1aedaf6de4b` |
| `src/main/java/com/wendao/service/impl/ProductServiceImpl.java` | `3227257a7d5eb3409f2dc6e76df31202d3ea92729861ce60ce9dc828ab8f07e3` |
| `src/main/java/com/wendao/utils/OpenApiSignUtil.java` | `3c034f739dac48f08f2ffef7027c4fe011058242ca8ffb8dbe36df6d53d44867` |
| `src/main/java/com/wendao/utils/PaymentConfirmTokens.java` | `c18be8813a0526c5335c30774322e558d7c2d1a48831aa2a5c63125bfbfe70a2` |
| `src/main/resources/Dockerfile` | `be685213c61f9b1cb6923dbd7d4f31fd69568474af3acd116c623ee72f6c8e7f` |
| `src/main/resources/application.yml` | `58d74eedc5e581f09ee2e0ecbb21e0f8aa75b8c821238c8072301577b2c6026f` |
| `src/main/resources/favicon.ico` | `0af6688af0cdbb443f6607af6c5a8f23bc61ba34f1fbe0f3ff8553466823cf95` |
| `src/main/resources/sql/migrations/20261028_payment_confirmation.sql` | `f349bba7e501b5be814d7e8a4ebd3fdfc10e611d5ef1646601f84986e0af5782` |
| `src/main/resources/sql/pay.sql` | `4ff7ba6597cfd3e2606fd6e9dfef1833097df345eaacd6f8f80a8face676db8f` |
| `src/main/resources/start.sh` | `a9e498c0e6b08cd4be7902bbac3bd714e12de0cdee800d58fdf7bf4b6b9734a5` |
| `src/main/resources/static/assets/images/500_icon.png` | `9eaa46406803eaf732486458667dd5009d07fbdf7febd9b2e7cac6dc434d3768` |
| `src/main/resources/static/assets/images/alipay.png` | `369727eb6961772ecd9db1fe5505f9115002e301c2901c852fd99a6a5b5885d1` |
| `src/main/resources/static/assets/images/alipay@2x.png` | `16881970f2c76ee3e7b31ea6b0286c1ee0bae397affa17266c6559e828e730bc` |
| `src/main/resources/static/assets/images/alipaydmf.png` | `7bf33a8ed4db449dfd22c5d475f74eb48710313c26708d3e8aabbc7f809743d6` |
| `src/main/resources/static/assets/images/aliremark.png` | `24b9a301ce795762c9fa123db4f90973aa6c8b5aeaccb86baf06c6a9fbd4d0e8` |
| `src/main/resources/static/assets/images/confirm.png` | `7cd1ea7906a0b56ca47aab7e65a2a82551d3489f86ada397c232b79ca48137f5` |
| `src/main/resources/static/assets/images/fail.png` | `74c333ab13a45e4392ad5a2ae4dc8b26ce1bb71c3061d721d6c189fb562d4b5f` |
| `src/main/resources/static/assets/images/order.png` | `8d5e3870a77a5ffab2dd282ecb760be5f5daf31645dd13b8a4ff5aef75a726ab` |
| `src/main/resources/static/assets/images/pay.png` | `9c76c4fbd05507a436f959eb0f3a3617ec9b272411c7f34a7cd1a2dfb92cb11f` |
| `src/main/resources/static/assets/images/qr.png` | `78fb7a4443a19cd804ea3e3a22ab6bf29dbd1e08479abc60fa34a49bacc470c8` |
| `src/main/resources/static/assets/images/red.png` | `c8b497a8d53ca404ba608a7df080ac3a82eb9716cf5e8bd2ace0cb0e76bfc450` |
| `src/main/resources/static/assets/images/sort_desc_disabled.png` | `3450cc1e5a1585690226a713a726753b3fa2d177e41338a36e0a3188e3f02663` |
| `src/main/resources/static/assets/images/success.png` | `813308f9f0ae30f6b597ebd7c3edb096bd0a6fd06911bd62d5aa3808730203a9` |
| `src/main/resources/static/assets/images/wechat-explain.png` | `065210ec1605af8a5656cdce8bbe55ed5a7e931b0e7df7e0765b7ee46dc585fe` |
| `src/main/resources/static/assets/images/wechat.png` | `3da26fa06168fa7181fc38b9eef6e87afd5fef2d7c12c70cbabe6f32be4bc8fd` |
| `src/main/resources/static/assets/images/weixin.png` | `cf63d2e754b31359e2a16e1566e1a6109de275a05a5d8980f35a72270f3a68a3` |
| `src/main/resources/static/assets/images/weixinTip.png` | `05daa4d1591c490552227c4b7e26669099a4c5844535303cddd53104d1624bd5` |
| `src/main/resources/static/assets/images/weixinpay@2x.png` | `e72e53b7efc4728c6f7d09192992ef1db3a7eca8a22b6a3f3213388822e478ee` |
| `src/main/resources/static/assets/images/wxremark.png` | `b91323be9fd76c87cf9a2d02dad34f693d51175b34e3fb8bdb696d4175dbcaee` |
| `src/main/resources/static/assets/images/wxzsremark.png` | `185d1a13bb32a9fd869f339915565a8d3db1b8d0885fddb36e39004338c17ecf` |
| `src/main/resources/static/assets/images/zfb.png` | `2c1e62aad011e245998e46f0164e539a43bba392fefcc486d919acb95d03fb14` |
| `src/main/resources/static/assets/images/zfb_open.jpg` | `e5dd3183734eb6ce8950567779bca932ecca8e6881cbfacc920316603557198a` |
| `src/main/resources/static/assets/images/优惠.png` | `63f10cc03f8a0f6dbed745b5ddde5224f95eb59f08f7f534855bf74fe7072b33` |
| `src/main/resources/static/assets/js/api-config.js` | `a740e322302833ed60078a6cb0f303c041c4b06bbed258da7698b532c250cab3` |
| `src/main/resources/static/assets/js/http-util.js` | `073311b2b9cd4b0ecada7e0c37d010cfc9d910bc1c82e9a8b2e05dd0cb715222` |
| `src/main/resources/static/assets/js/qcode.min.js` | `083e3ea2f36e97de4ae8b2b8ac6da0298289bbd7bc111f54589d991c642baff2` |
| `src/main/resources/static/assets/qr/alipay/0.01/1.png` | `cf4e53fa94d3ed1d810bcc377c0a8e03a578763f93014a6f6738ea35fd6c91bf` |
| `src/main/resources/static/assets/qr/alipay/0.01/2.png` | `cf4e53fa94d3ed1d810bcc377c0a8e03a578763f93014a6f6738ea35fd6c91bf` |
| `src/main/resources/static/assets/qr/alipay/custom.png` | `cf4e53fa94d3ed1d810bcc377c0a8e03a578763f93014a6f6738ea35fd6c91bf` |
| `src/main/resources/static/assets/qr/wechat/0.01/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/0.01/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/10.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/10.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/100.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/100.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/20.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/20.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/200.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/200.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/5.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/5.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/5.00/4.98/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/5.00/4.98/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/5.00/4.99/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/5.00/4.99/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/5.00/5.01/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/5.00/5.01/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/50.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/50.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/500.00/1.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/500.00/2.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat/custom.png` | `ef5b69721ea9bbf8f2372dd6062f6f8c65bfa6023ebeb83ed7ecea6c03cf2d53` |
| `src/main/resources/static/assets/qr/wechat_zs/custom.png` | `5222b62afc32b5a70f89db3f8c48c84bb7a4df22bc539ad1fbf444d6cdd13334` |
| `src/main/resources/static/css/common.css` | `438bf7fa887467a061ac45ff1c1890ca5d182065052c7f064f2ec503c3416599` |
| `src/main/resources/templates/error.html` | `c0e0d87e327ba9cec3e997bf6e67ef0b398fa13f796bf3eac7e322dcb9db5150` |
| `src/main/resources/templates/help.html` | `d6407a171524598c1aec9846999741084b6f05a4fee1bbce47dc7abe061a6b78` |
| `src/main/resources/templates/history.html` | `669d878095ba2e28ebda9149a1803cf857f6d777d159573a8dd8b62caa863fd0` |
| `src/main/resources/templates/home.html` | `f07b5e8e09b9e6c3f796b3b85e24a5a4625b95fd0ab3f5cebc3a45cfdafb452b` |
| `src/main/resources/templates/index.html` | `42350ef758852a2adaee417760f095b08c996197bb982fd9b9fa72fb34af13d1` |
| `src/main/resources/templates/openAlipay.html` | `e4b36bec8970602312a037fdfb3482352c8ceaf85528655e13ad1f89b5e6c26c` |
| `src/main/resources/templates/order-del.html` | `3f9db80562c957aa14aa81f85abca506b284db6b83c4cfd6dd8454bf42eb0025` |
| `src/main/resources/templates/order-edit.html` | `57a9bebf4d8da4a248edf8356704ccfe65024b6ec74fcce644f274432c344f20` |
| `src/main/resources/templates/order-fail.html` | `307c348da85ea121445e7d845624ee2cb0ba845fb99ebec3b1e8180130baed87` |
| `src/main/resources/templates/order-success.html` | `24f14ebaae7bfd4a53e2ee632d0bd5f1f0ac6b9429aa9efe1fce36584841996b` |
| `src/main/resources/templates/payment-review.html` | `47666c750442838199b61cd1eab3f21c8f4f7b9981675616d266f57f98c955a0` |
| `src/main/resources/templates/payment.html` | `0856bde841566189f2a25e2660235c65ec3d0888ae55b7d6516ddd36256bc248` |
| `src/main/resources/templates/recharge.html` | `e6a4da8461e64c45449be91e5063b95102c6f207b13c10a8373144d3aba9a9b2` |
| `src/main/resources/templates/statistic.html` | `11790591acbc5a173ce7acb5e890d58691d72132a0413ccd8ff3e11b98362463` |
| `src/main/resources/templates/success.html` | `4bc87da7d10fc38844d81cbe08d418d79efd864277a87f60c7f5b949c67165ab` |
| `src/test/frontend/payment-confirmation.test.cjs` | `6bcf7088960393fc6ebcaa190151f30a1953d4ed1d75eda1fe52bb083a7038bd` |
| `src/test/java/com/wendao/service/EmailUtilsOutcomeTest.java` | `e2252827e1f395b20554a4af0644812fcc73f612220db732f129ef8236e26c53` |
| `src/test/java/com/wendao/service/OrderCreationNotificationTest.java` | `0084c4cd0830b33b774f790d67825236256d3a9ac453be588c1c7a7e3f664b8a` |
| `src/test/java/com/wendao/service/PaymentConfirmationControllerTest.java` | `4bd315d73cd4d8ef49c01b87c1a3ef9403ee446e7a45d393781da2702dd9b3cf` |
| `src/test/java/com/wendao/service/PaymentConfirmationDatabaseIT.java` | `021ff66b1ccd8fb94aac29f143529c3ebf58fc93d385e52f07bad4fb6d261193` |
| `src/test/java/com/wendao/service/PaymentConfirmationServiceTest.java` | `4fbf3764a262ef01a1ffade1189c568d6e720fb374bf1a8e67cfeefb571d2eaf` |
| `src/test/java/com/wendao/service/PaymentNoticeSenderTest.java` | `315eabc0f0d044ea980404a4c7e9fe2e6acc9ef13139f237db903a0596f846cb` |
| `一键启动说明.md` | `984f3577f2d05f9002e487c6ca8f0a0478c7bc79a2ece12b212cf8b3b98130a5` |
| `获取支付宝userId.jpg` | `ec12bd3bbf1bc7bd91e97e9846177dd1f6bc51e85444580a9fff6346fe3f25fd` |
