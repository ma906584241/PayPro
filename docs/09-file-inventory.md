# 全量文件清单

项目原始文件共 **153** 个；不包含本轮 docs 与 .codegraph 产物。

从工作区实际内容计算 SHA-256。文本行数按 UTF-8 读取；图片 / 二进制不按文本计行。此清单不复制配置值或收款二维码内容。

## 文件类型统计

| 扩展名 | 数量 |
| --- | ---: |
| .css | 1 |
| .example | 1 |
| .html | 15 |
| .ico | 1 |
| .java | 32 |
| .jpg | 2 |
| .js | 3 |
| .md | 3 |
| .png | 81 |
| .sh | 2 |
| .sql | 1 |
| .xml | 2 |
| .yml | 3 |
| 无扩展名 | 6 |

## 文件与用途

| 文件 | 字节 | 行数 | 格式 / 用途 |
| --- | ---: | ---: | --- |
| [.dockerignore](../.dockerignore) | 149 | 9 |  排除私密环境、Git、图谱、文档与本地构建产物的 Docker 上下文规则 |
| [.env.example](../.env.example) | 159 | 3 |  QQ SMTP 授权码环境变量示例，不含真实凭据 |
| [.gitattributes](../.gitattributes) | 154 | 7 |  文本 LF 规则和 Compose 二进制标记 |
| [.gitignore](../.gitignore) | 66 | 4 |  IDE、构建产物和本地配置排除规则 |
| [Dockerfile](../Dockerfile) | 695 | 28 |  Maven 构建 + JDK8 运行的多阶段镜像 |
| [OPEN_API.md](../OPEN_API.md) | 6686 | 222 |  原 OpenAPI 说明，与当前实现存在差异 |
| [README.md](../README.md) | 11440 | 328 |  原项目介绍、开源 / 高级版说明和截图 |
| [config/application-prod.yml](../config/application-prod.yml) | 3313 | 122 |  外置生产配置，含部署账号与业务参数 |
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
| [pom.xml](../pom.xml) | 5445 | 153 |  Maven 坐标、父 POM、依赖、编译与打包插件 |
| [qr/alipay/custom.png](../qr/alipay/custom.png) | 140820 | — | PNG 591×576 运行时外置支付二维码：alipay/custom.png |
| [qr/wechat/0.01/1.png](../qr/wechat/0.01/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/0.01/1.png |
| [qr/wechat/0.01/2.png](../qr/wechat/0.01/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/0.01/2.png |
| [qr/wechat/1.00/1.png](../qr/wechat/1.00/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/1.00/1.png |
| [qr/wechat/1.00/2.png](../qr/wechat/1.00/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/1.00/2.png |
| [qr/wechat/10.00/1.png](../qr/wechat/10.00/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/10.00/1.png |
| [qr/wechat/10.00/2.png](../qr/wechat/10.00/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/10.00/2.png |
| [qr/wechat/29.00/1.png](../qr/wechat/29.00/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/29.00/1.png |
| [qr/wechat/29.00/2.png](../qr/wechat/29.00/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/29.00/2.png |
| [qr/wechat/29.00/28.98/1.png](../qr/wechat/29.00/28.98/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/29.00/28.98/1.png |
| [qr/wechat/29.00/28.98/2.png](../qr/wechat/29.00/28.98/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/29.00/28.98/2.png |
| [qr/wechat/29.00/28.99/1.png](../qr/wechat/29.00/28.99/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/29.00/28.99/1.png |
| [qr/wechat/29.00/28.99/2.png](../qr/wechat/29.00/28.99/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/29.00/28.99/2.png |
| [qr/wechat/49.00/1.png](../qr/wechat/49.00/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/49.00/1.png |
| [qr/wechat/49.00/2.png](../qr/wechat/49.00/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/49.00/2.png |
| [qr/wechat/5.00/1.png](../qr/wechat/5.00/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/5.00/1.png |
| [qr/wechat/5.00/2.png](../qr/wechat/5.00/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/5.00/2.png |
| [qr/wechat/5.00/4.98/1.png](../qr/wechat/5.00/4.98/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/5.00/4.98/1.png |
| [qr/wechat/5.00/4.98/2.png](../qr/wechat/5.00/4.98/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/5.00/4.98/2.png |
| [qr/wechat/5.00/4.99/1.png](../qr/wechat/5.00/4.99/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/5.00/4.99/1.png |
| [qr/wechat/5.00/4.99/2.png](../qr/wechat/5.00/4.99/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/5.00/4.99/2.png |
| [qr/wechat/5.00/5.01/1.png](../qr/wechat/5.00/5.01/1.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/5.00/5.01/1.png |
| [qr/wechat/5.00/5.01/2.png](../qr/wechat/5.00/5.01/2.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/5.00/5.01/2.png |
| [qr/wechat/custom.png](../qr/wechat/custom.png) | 133294 | — | PNG 717×618 运行时外置支付二维码：wechat/custom.png |
| [qr/wechat_zs/custom.png](../qr/wechat_zs/custom.png) | 63239 | — | JPEG 运行时外置支付二维码：wechat_zs/custom.png |
| [settings.xml](../settings.xml) | 234 | 10 |  Maven central 镜像配置 |
| [src/main/java/com/wendao/PayApplication.java](../src/main/java/com/wendao/PayApplication.java) | 719 | 25 |  Spring Boot 入口，开启缓存、异步、调度与 Mapper 扫描 |
| [src/main/java/com/wendao/common/utils/DateUtils.java](../src/main/java/com/wendao/common/utils/DateUtils.java) | 11724 | 342 |  日期起止、统计窗口、日期差和日期集合工具 |
| [src/main/java/com/wendao/common/utils/EmailUtils.java](../src/main/java/com/wendao/common/utils/EmailUtils.java) | 2805 | 88 |  异步 Thymeleaf HTML 邮件与邮箱格式校验 |
| [src/main/java/com/wendao/common/utils/IpInfoUtils.java](../src/main/java/com/wendao/common/utils/IpInfoUtils.java) | 1780 | 56 |  从代理头和请求读取客户端 IP |
| [src/main/java/com/wendao/common/utils/StringUtils.java](../src/main/java/com/wendao/common/utils/StringUtils.java) | 2522 | 108 |  空白检查、日期转换、Bean 转 Map、四位备注码 |
| [src/main/java/com/wendao/config/Config.java](../src/main/java/com/wendao/config/Config.java) | 2367 | 61 |  CORS、Thymeleaf 全局变量、分页插件与 Snowflake Bean |
| [src/main/java/com/wendao/config/PayProConfig.java](../src/main/java/com/wendao/config/PayProConfig.java) | 6487 | 271 |  paypro 配置绑定、配置商品检索、外置二维码映射 |
| [src/main/java/com/wendao/config/RedisConfig.java](../src/main/java/com/wendao/config/RedisConfig.java) | 1690 | 36 |  Object RedisTemplate 与 Jackson 序列化配置 |
| [src/main/java/com/wendao/controller/OrderController.java](../src/main/java/com/wendao/controller/OrderController.java) | 11293 | 281 |  订单、审核、统计、OpenAPI 和支付方式路由 |
| [src/main/java/com/wendao/controller/PageController.java](../src/main/java/com/wendao/controller/PageController.java) | 1956 | 67 |  根页与通用模板路由，支付宝页状态副作用 |
| [src/main/java/com/wendao/controller/ProductController.java](../src/main/java/com/wendao/controller/ProductController.java) | 1329 | 41 |  按 ID / 类型公开读取配置商品 |
| [src/main/java/com/wendao/dto/MsgContentsDTO.java](../src/main/java/com/wendao/dto/MsgContentsDTO.java) | 895 | 33 |  消息内容与付款方备注正则提取 |
| [src/main/java/com/wendao/dto/WeChatMsgDTO.java](../src/main/java/com/wendao/dto/WeChatMsgDTO.java) | 528 | 26 |  微信消息结构，当前未接入到账业务入口 |
| [src/main/java/com/wendao/entity/Order.java](../src/main/java/com/wendao/entity/Order.java) | 2775 | 137 |  订单持久化实体及邮件管理 URL 临时属性 |
| [src/main/java/com/wendao/entity/Product.java](../src/main/java/com/wendao/entity/Product.java) | 686 | 36 |  配置商品实体，非数据库表 |
| [src/main/java/com/wendao/enums/OrderStatesEnum.java](../src/main/java/com/wendao/enums/OrderStatesEnum.java) | 570 | 38 |  订单状态 0 / 1 / 2 / 4 / 5 |
| [src/main/java/com/wendao/exception/ApiException.java](../src/main/java/com/wendao/exception/ApiException.java) | 835 | 30 |  业务异常与错误码常量 |
| [src/main/java/com/wendao/exception/GlobalExceptionHandler.java](../src/main/java/com/wendao/exception/GlobalExceptionHandler.java) | 1458 | 40 |  业务、参数与通用异常转换为 ResponseVO |
| [src/main/java/com/wendao/mapper/OrderMapper.java](../src/main/java/com/wendao/mapper/OrderMapper.java) | 1743 | 42 |  订单 BaseMapper、聚合统计、过期与实际金额查询 |
| [src/main/java/com/wendao/model/ResponseVO.java](../src/main/java/com/wendao/model/ResponseVO.java) | 1482 | 68 |  通用 code / msg / data 响应封装 |
| [src/main/java/com/wendao/model/req/GetOrderListReq.java](../src/main/java/com/wendao/model/req/GetOrderListReq.java) | 533 | 35 |  订单分页、状态、关键词与排序请求 |
| [src/main/java/com/wendao/model/req/GetProductListReq.java](../src/main/java/com/wendao/model/req/GetProductListReq.java) | 224 | 17 |  商品类型列表请求 |
| [src/main/java/com/wendao/model/req/OpenApiOrderReq.java](../src/main/java/com/wendao/model/req/OpenApiOrderReq.java) | 960 | 45 |  外部下单与签名参数模型 |
| [src/main/java/com/wendao/model/req/OrderReq.java](../src/main/java/com/wendao/model/req/OrderReq.java) | 1186 | 65 |  普通下单请求模型 |
| [src/main/java/com/wendao/model/resp/AddOrderResp.java](../src/main/java/com/wendao/model/resp/AddOrderResp.java) | 1418 | 59 |  普通下单支付信息响应 |
| [src/main/java/com/wendao/model/resp/CountResp.java](../src/main/java/com/wendao/model/resp/CountResp.java) | 306 | 17 |  成功订单原价统计响应 |
| [src/main/java/com/wendao/model/resp/OpenApiOrderResp.java](../src/main/java/com/wendao/model/resp/OpenApiOrderResp.java) | 759 | 42 |  外部下单、二维码与支付页响应 |
| [src/main/java/com/wendao/service/OrderService.java](../src/main/java/com/wendao/service/OrderService.java) | 1996 | 86 |  订单业务接口 |
| [src/main/java/com/wendao/service/ProductService.java](../src/main/java/com/wendao/service/ProductService.java) | 629 | 24 |  商品业务接口 |
| [src/main/java/com/wendao/service/impl/OrderServiceImpl.java](../src/main/java/com/wendao/service/impl/OrderServiceImpl.java) | 31364 | 755 |  普通 / 外部下单、减额、审核、分页、统计与回调 |
| [src/main/java/com/wendao/service/impl/ProductServiceImpl.java](../src/main/java/com/wendao/service/impl/ProductServiceImpl.java) | 2350 | 65 |  YAML 商品转实体，公开接口清除下载链接 |
| [src/main/java/com/wendao/utils/OpenApiSignUtil.java](../src/main/java/com/wendao/utils/OpenApiSignUtil.java) | 4767 | 113 |  OpenAPI MD5 签名、验签及五分钟时间戳验证 |
| [src/main/resources/Dockerfile](../src/main/resources/Dockerfile) | 421 | 20 |  从预构建 JAR 构建运行镜像的旧入口 |
| [src/main/resources/application.yml](../src/main/resources/application.yml) | 3146 | 127 |  包内基础 Spring 与 paypro 配置 |
| [src/main/resources/favicon.ico](../src/main/resources/favicon.ico) | 12181 | — | PNG 256×256 站点图标资源 |
| [src/main/resources/sql/pay.sql](../src/main/resources/sql/pay.sql) | 2690 | 57 |  订单表初始化、减额迁移和索引 |
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
| [src/main/resources/static/assets/js/api-config.js](../src/main/resources/static/assets/js/api-config.js) | 1882 | 62 |  API 基址、端点和超时配置 |
| [src/main/resources/static/assets/js/http-util.js](../src/main/resources/static/assets/js/http-util.js) | 5580 | 194 |  fetch 请求类和全局单例封装 |
| [src/main/resources/static/assets/js/qcode.min.js](../src/main/resources/static/assets/js/qcode.min.js) | 23743 | 7 |  第三方 qrcode@1.5.1 浏览器二维码库 |
| [src/main/resources/static/assets/qr/alipay/0.01/1.png](../src/main/resources/static/assets/qr/alipay/0.01/1.png) | 140820 | — | PNG 591×576 随 JAR 打包的支付二维码：alipay/0.01/1.png |
| [src/main/resources/static/assets/qr/alipay/0.01/2.png](../src/main/resources/static/assets/qr/alipay/0.01/2.png) | 140820 | — | PNG 591×576 随 JAR 打包的支付二维码：alipay/0.01/2.png |
| [src/main/resources/static/assets/qr/alipay/custom.png](../src/main/resources/static/assets/qr/alipay/custom.png) | 140820 | — | PNG 591×576 随 JAR 打包的支付二维码：alipay/custom.png |
| [src/main/resources/static/assets/qr/wechat/0.01/1.png](../src/main/resources/static/assets/qr/wechat/0.01/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/0.01/1.png |
| [src/main/resources/static/assets/qr/wechat/0.01/2.png](../src/main/resources/static/assets/qr/wechat/0.01/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/0.01/2.png |
| [src/main/resources/static/assets/qr/wechat/10.00/1.png](../src/main/resources/static/assets/qr/wechat/10.00/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/10.00/1.png |
| [src/main/resources/static/assets/qr/wechat/10.00/2.png](../src/main/resources/static/assets/qr/wechat/10.00/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/10.00/2.png |
| [src/main/resources/static/assets/qr/wechat/100.00/1.png](../src/main/resources/static/assets/qr/wechat/100.00/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/100.00/1.png |
| [src/main/resources/static/assets/qr/wechat/100.00/2.png](../src/main/resources/static/assets/qr/wechat/100.00/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/100.00/2.png |
| [src/main/resources/static/assets/qr/wechat/20.00/1.png](../src/main/resources/static/assets/qr/wechat/20.00/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/20.00/1.png |
| [src/main/resources/static/assets/qr/wechat/20.00/2.png](../src/main/resources/static/assets/qr/wechat/20.00/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/20.00/2.png |
| [src/main/resources/static/assets/qr/wechat/200.00/1.png](../src/main/resources/static/assets/qr/wechat/200.00/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/200.00/1.png |
| [src/main/resources/static/assets/qr/wechat/200.00/2.png](../src/main/resources/static/assets/qr/wechat/200.00/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/200.00/2.png |
| [src/main/resources/static/assets/qr/wechat/5.00/1.png](../src/main/resources/static/assets/qr/wechat/5.00/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/5.00/1.png |
| [src/main/resources/static/assets/qr/wechat/5.00/2.png](../src/main/resources/static/assets/qr/wechat/5.00/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/5.00/2.png |
| [src/main/resources/static/assets/qr/wechat/5.00/4.98/1.png](../src/main/resources/static/assets/qr/wechat/5.00/4.98/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/5.00/4.98/1.png |
| [src/main/resources/static/assets/qr/wechat/5.00/4.98/2.png](../src/main/resources/static/assets/qr/wechat/5.00/4.98/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/5.00/4.98/2.png |
| [src/main/resources/static/assets/qr/wechat/5.00/4.99/1.png](../src/main/resources/static/assets/qr/wechat/5.00/4.99/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/5.00/4.99/1.png |
| [src/main/resources/static/assets/qr/wechat/5.00/4.99/2.png](../src/main/resources/static/assets/qr/wechat/5.00/4.99/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/5.00/4.99/2.png |
| [src/main/resources/static/assets/qr/wechat/5.00/5.01/1.png](../src/main/resources/static/assets/qr/wechat/5.00/5.01/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/5.00/5.01/1.png |
| [src/main/resources/static/assets/qr/wechat/5.00/5.01/2.png](../src/main/resources/static/assets/qr/wechat/5.00/5.01/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/5.00/5.01/2.png |
| [src/main/resources/static/assets/qr/wechat/50.00/1.png](../src/main/resources/static/assets/qr/wechat/50.00/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/50.00/1.png |
| [src/main/resources/static/assets/qr/wechat/50.00/2.png](../src/main/resources/static/assets/qr/wechat/50.00/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/50.00/2.png |
| [src/main/resources/static/assets/qr/wechat/500.00/1.png](../src/main/resources/static/assets/qr/wechat/500.00/1.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/500.00/1.png |
| [src/main/resources/static/assets/qr/wechat/500.00/2.png](../src/main/resources/static/assets/qr/wechat/500.00/2.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/500.00/2.png |
| [src/main/resources/static/assets/qr/wechat/custom.png](../src/main/resources/static/assets/qr/wechat/custom.png) | 133294 | — | PNG 717×618 随 JAR 打包的支付二维码：wechat/custom.png |
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
| [src/main/resources/templates/payment-review.html](../src/main/resources/templates/payment-review.html) | 7406 | 203 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/payment.html](../src/main/resources/templates/payment.html) | 18756 | 848 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/recharge.html](../src/main/resources/templates/recharge.html) | 21294 | 664 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/statistic.html](../src/main/resources/templates/statistic.html) | 5382 | 156 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [src/main/resources/templates/success.html](../src/main/resources/templates/success.html) | 669 | 24 |  HTML / Thymeleaf 页面或邮件模板，详见前端说明 |
| [一键启动说明.md](../一键启动说明.md) | 4868 | 172 |  原 Linux 部署与二维码使用说明 |
| [获取支付宝userId.jpg](../获取支付宝userId.jpg) | 25132 | — | JPEG 支付宝收款用户 ID 配置辅助图片 |

## 文件哈希

| 文件 | SHA-256 |
| --- | --- |
| `.dockerignore` | `a16862698e3805dd674d9be88f8743ab6b143bea55a507ae4893036018b358fc` |
| `.env.example` | `b2666e8628f7f9fb9bc3c3bdfa7515a3807a2cc1f320ead00677f4efb4f3d90b` |
| `.gitattributes` | `70690cd5f403076a5a6a09b5172ed427841d80a4297df1ccdac6472b540abc3c` |
| `.gitignore` | `b54697b7acd41356ffb7e6fefb20d4e99d19d3d50d6350e5d4d1472165b5ee38` |
| `Dockerfile` | `40f927b0a3ca11e8534bb79d037f8647ce2628bc8f68fc428e60b5ac22f66516` |
| `OPEN_API.md` | `31acfd5be9d5130d11cdc3ac62a220b8afc322eae7d6b34f375d691467e8332c` |
| `README.md` | `18373a348ea36d81b8659bd16d6e3524ef92555b1956dadd822a14bb95c9cb61` |
| `config/application-prod.yml` | `6aa3b86688d7c47fc894570c76afb378ecb9f741626ae24255a8ad104e177c39` |
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
| `pom.xml` | `a8c7ca771b5874eaf42ef120e449fb916a50cc117572e2c846a7de08b7c832f8` |
| `qr/alipay/custom.png` | `3332c58e4053d84a1b3e1da720fcda251db0dc29c2adc0c6bbc1bd1298e7ec48` |
| `qr/wechat/0.01/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/0.01/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/1.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/1.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/10.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/10.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/29.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/29.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/29.00/28.98/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/29.00/28.98/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/29.00/28.99/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/29.00/28.99/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/49.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/49.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/5.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/5.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/5.00/4.98/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/5.00/4.98/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/5.00/4.99/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/5.00/4.99/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/5.00/5.01/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/5.00/5.01/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat/custom.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `qr/wechat_zs/custom.png` | `5222b62afc32b5a70f89db3f8c48c84bb7a4df22bc539ad1fbf444d6cdd13334` |
| `settings.xml` | `7609701f327048ca05325a0e23c659053255b8a92c6176983e2b12626385787a` |
| `src/main/java/com/wendao/PayApplication.java` | `8c457e980e7ef305a3d90fd048f4d971e2ac4a66c2a24d777f2e7fb33bc43824` |
| `src/main/java/com/wendao/common/utils/DateUtils.java` | `469849df931908ad032c90b572da61d35e6348150083804bdd5757bdc08b971d` |
| `src/main/java/com/wendao/common/utils/EmailUtils.java` | `07884127923b84e4befcca62f847880fcfa6fa84f266dc0871bf641f504f948b` |
| `src/main/java/com/wendao/common/utils/IpInfoUtils.java` | `2a284e216a97065de98ffc90feb3b10a6a6f26b6017aed7f972e53fc6f8827ba` |
| `src/main/java/com/wendao/common/utils/StringUtils.java` | `951ecbc84b202c7864a83545785b7fe8b7d74c96a570653a2724c35104ff471b` |
| `src/main/java/com/wendao/config/Config.java` | `3ab32e0fe0d59caef5f78639c19e7c9c95f5b2cb0c24253a63d9f9647082e736` |
| `src/main/java/com/wendao/config/PayProConfig.java` | `347ebcce697062e4c118be026acd22e14693e24fbae3ede00104cd220d0e6df2` |
| `src/main/java/com/wendao/config/RedisConfig.java` | `8e70587a300e902cd43c22404ddca723a1b51e2af7cbfb7bec157b184d24feb6` |
| `src/main/java/com/wendao/controller/OrderController.java` | `d6ec8d9b582e136d71d19589230f407a7501bfab4b52b5fa513236fb3d2b0c1d` |
| `src/main/java/com/wendao/controller/PageController.java` | `5fbb6497d147fd6efe34ebb9c61ee5d8e6cc5ecd06a5bb16667bff78a0b5569f` |
| `src/main/java/com/wendao/controller/ProductController.java` | `cfd5fbd21d437afb9723695478b77c6dd4ad55febff5c0eec5ec4492b60a9acc` |
| `src/main/java/com/wendao/dto/MsgContentsDTO.java` | `238cfb23b61364253ffcd7d97c4632044e8ea5a12b1d262712931eb2b9c32c6a` |
| `src/main/java/com/wendao/dto/WeChatMsgDTO.java` | `d0dcdbff296e3183e94213e247954b1fa588069797ddb3e4eb5eea396db6075a` |
| `src/main/java/com/wendao/entity/Order.java` | `9e80fd19437ceefb56d0d2ba5767e698d612b83dacea3b6ef0c2b33b389908a9` |
| `src/main/java/com/wendao/entity/Product.java` | `cf666dd581ac159cc767ca01b349250685c3a7adfdc279e98ac503c9ab912703` |
| `src/main/java/com/wendao/enums/OrderStatesEnum.java` | `478cef8269922429015d2d69a6018e0a70813caa34a4411090207c137d8f5c8d` |
| `src/main/java/com/wendao/exception/ApiException.java` | `7e394aead2bda9f5895b53983bd723a1b40ee4f3efb160610db746eb82ba84dc` |
| `src/main/java/com/wendao/exception/GlobalExceptionHandler.java` | `d5d9ac15a050de3aa9c03abb7b5b70801509437ce096cac2796532764da425e1` |
| `src/main/java/com/wendao/mapper/OrderMapper.java` | `9cacf0e36996005604a4f0339164b55f055a3531a7eece5c49c8dab980b63348` |
| `src/main/java/com/wendao/model/ResponseVO.java` | `6ec52e7e7f190dcd68d01136a7fb075ff0089575dca55263e7b9fec24a75dbb8` |
| `src/main/java/com/wendao/model/req/GetOrderListReq.java` | `28abcf694d8012b6422f9a69244c1a3c37ece87952a1f2bac593fe85191935f5` |
| `src/main/java/com/wendao/model/req/GetProductListReq.java` | `44e058e5b62354c8654ff5dda7f309534d8c7a21481a9285070018f39abf1a03` |
| `src/main/java/com/wendao/model/req/OpenApiOrderReq.java` | `8ba90f21b686661725542c8e738f4dda868668eaeb1b6c4a96491d7642fb7105` |
| `src/main/java/com/wendao/model/req/OrderReq.java` | `52eec650ab8a4b69c98acfe73c641e4d98bafe342b1728a7f2ff3321efdf4579` |
| `src/main/java/com/wendao/model/resp/AddOrderResp.java` | `c34e8b12eca4ba943de6120cd864efbbb6e863109f56a86395a9d55c16915b78` |
| `src/main/java/com/wendao/model/resp/CountResp.java` | `d628a611529a7fd7256f0dc8b45e38156413151c84bdf0fe689f3481dadd1abb` |
| `src/main/java/com/wendao/model/resp/OpenApiOrderResp.java` | `f84529ccd8c64f179215ff3f64c8b86370cf57d23b4455832768e66611ebee8e` |
| `src/main/java/com/wendao/service/OrderService.java` | `1c96edeed6edc10d4b3f737268c20831602c16df4720f5e8dd1d9c1b06fe1969` |
| `src/main/java/com/wendao/service/ProductService.java` | `bda889122eb71304b3d0b70b2bbb25366cb372a3375946134d8956dd227a0282` |
| `src/main/java/com/wendao/service/impl/OrderServiceImpl.java` | `13f4be83eff78fe868e5c27b5d64daadd38e52cfa7b2a8710dc0aa570bd2086f` |
| `src/main/java/com/wendao/service/impl/ProductServiceImpl.java` | `3227257a7d5eb3409f2dc6e76df31202d3ea92729861ce60ce9dc828ab8f07e3` |
| `src/main/java/com/wendao/utils/OpenApiSignUtil.java` | `3c034f739dac48f08f2ffef7027c4fe011058242ca8ffb8dbe36df6d53d44867` |
| `src/main/resources/Dockerfile` | `be685213c61f9b1cb6923dbd7d4f31fd69568474af3acd116c623ee72f6c8e7f` |
| `src/main/resources/application.yml` | `a3e81c2a7913fcc27581c76ecafcdc29a54877ccc0df6c5dcea1cacc568a2700` |
| `src/main/resources/favicon.ico` | `0af6688af0cdbb443f6607af6c5a8f23bc61ba34f1fbe0f3ff8553466823cf95` |
| `src/main/resources/sql/pay.sql` | `ef7cf076fb95d0327856086063110895b14693bf756f96592a12ad1fa7222c9d` |
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
| `src/main/resources/static/assets/js/api-config.js` | `ce83027ec7d4b5a906b475189064c6a56ba6b8ac118413e4324debd04b8803eb` |
| `src/main/resources/static/assets/js/http-util.js` | `073311b2b9cd4b0ecada7e0c37d010cfc9d910bc1c82e9a8b2e05dd0cb715222` |
| `src/main/resources/static/assets/js/qcode.min.js` | `083e3ea2f36e97de4ae8b2b8ac6da0298289bbd7bc111f54589d991c642baff2` |
| `src/main/resources/static/assets/qr/alipay/0.01/1.png` | `3332c58e4053d84a1b3e1da720fcda251db0dc29c2adc0c6bbc1bd1298e7ec48` |
| `src/main/resources/static/assets/qr/alipay/0.01/2.png` | `3332c58e4053d84a1b3e1da720fcda251db0dc29c2adc0c6bbc1bd1298e7ec48` |
| `src/main/resources/static/assets/qr/alipay/custom.png` | `3332c58e4053d84a1b3e1da720fcda251db0dc29c2adc0c6bbc1bd1298e7ec48` |
| `src/main/resources/static/assets/qr/wechat/0.01/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/0.01/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/10.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/10.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/100.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/100.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/20.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/20.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/200.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/200.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/5.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/5.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/5.00/4.98/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/5.00/4.98/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/5.00/4.99/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/5.00/4.99/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/5.00/5.01/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/5.00/5.01/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/50.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/50.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/500.00/1.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/500.00/2.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
| `src/main/resources/static/assets/qr/wechat/custom.png` | `a3feb84e0c7dba3ba0ea09f08ba10d47d5b0e49768af627d5c61faf15b983ee6` |
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
| `src/main/resources/templates/payment-review.html` | `2c91d0d7b73de4232538629933536bd4f4e8fb07d5ac312051bffe25ad662d6f` |
| `src/main/resources/templates/payment.html` | `a075d383d4508ef61431c362b808bf55b41224c927e9e5cd127c5c6c239d9c2f` |
| `src/main/resources/templates/recharge.html` | `1e81d9bc0ce4e4c76c0663e43410441c75d56b65971211748321a553443dfae0` |
| `src/main/resources/templates/statistic.html` | `11790591acbc5a173ce7acb5e890d58691d72132a0413ccd8ff3e11b98362463` |
| `src/main/resources/templates/success.html` | `4bc87da7d10fc38844d81cbe08d418d79efd864277a87f60c7f5b949c67165ab` |
| `一键启动说明.md` | `984f3577f2d05f9002e487c6ca8f0a0478c7bc79a2ece12b212cf8b3b98130a5` |
| `获取支付宝userId.jpg` | `ec12bd3bbf1bc7bd91e97e9846177dd1f6bc51e85444580a9fff6346fe3f25fd` |
