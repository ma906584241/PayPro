# Java 源码符号目录

由本项目 CodeGraph 静态索引生成。列出所有 Java 文件中的类型、显式方法、字段和枚举；不包括 Lombok 运行注解处理后生成的 getter/setter。

签名使用索引原始类型 / 参数，方法名单独列出；省略可能包含配置值的 docstring。行号对应当前工作区源码，不代表运行覆盖率。

## PayApplication.java

[src/main/java/com/wendao/PayApplication.java](../src/main/java/com/wendao/PayApplication.java) — Spring Boot 入口，开启缓存、异步、调度与 Mapper 扫描

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PayApplication` | `com.wendao::PayApplication` | 12–25 |
| method | `main` | `void (String[] args)` | 22–24 |

## DateUtils.java

[src/main/java/com/wendao/common/utils/DateUtils.java](../src/main/java/com/wendao/common/utils/DateUtils.java) — 日期起止、统计窗口、日期差和日期集合工具

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `DateUtils` | `com.wendao.common.utils::DateUtils` | 12–342 |
| method | `getDayBegin` | `Date ()` | 15–22 |
| method | `getDayEnd` | `Date ()` | 25–31 |
| method | `getBeginDayOfYesterday` | `Date ()` | 34–39 |
| method | `getEndDayOfYesterDay` | `Date ()` | 42–47 |
| method | `getBeginDayOfTomorrow` | `Date ()` | 50–55 |
| method | `getEndDayOfTomorrow` | `Date ()` | 58–63 |
| method | `getBeginDayOfWeek` | `Date ()` | 66–80 |
| method | `getEndDayOfWeek` | `Date ()` | 83–89 |
| method | `getBeginDayOfLastWeek` | `Date ()` | 92–106 |
| method | `getEndDayOfLastWeek` | `Date ()` | 109–115 |
| method | `getBeginDayOfMonth` | `Date ()` | 118–122 |
| method | `getEndDayOfMonth` | `Date ()` | 125–131 |
| method | `getBeginDayOfLastMonth` | `Date ()` | 134–138 |
| method | `getEndDayOfLastMonth` | `Date ()` | 141–147 |
| method | `getBeginDayOfYear` | `Date ()` | 150–156 |
| method | `getEndDayOfYear` | `java.util.Date ()` | 159–165 |
| method | `getDayStartTime` | `Timestamp (Date d)` | 168–176 |
| method | `getDayEndTime` | `Timestamp (Date d)` | 179–187 |
| method | `getNowYear` | `Integer ()` | 190–195 |
| method | `getNowMonth` | `int ()` | 198–203 |
| method | `getDiffDays` | `int (Date beginDate, Date endDate)` | 206–214 |
| method | `dateDiff` | `long (Date beginDate, Date endDate)` | 217–221 |
| method | `max` | `Date (Date beginDate, Date endDate)` | 224–235 |
| method | `min` | `Date (Date beginDate, Date endDate)` | 238–249 |
| method | `getFirstSeasonDate` | `Date (Date date)` | 252–259 |
| method | `getNextDay` | `Date (Date date, int i)` | 262–267 |
| method | `getFrontDay` | `Date (Date date, int i)` | 270–275 |
| method | `getTimeList` | `List (int beginYear, int beginMonth, int endYear,                                    int endMonth, int k)` | 278–302 |
| method | `getTimeList` | `List (int beginYear, int beginMonth, int k)` | 305–317 |
| method | `parseStartDate` | `Date (String str)` | 319–329 |
| method | `parseEndDate` | `Date (String str)` | 331–341 |

## EmailUtils.java

[src/main/java/com/wendao/common/utils/EmailUtils.java](../src/main/java/com/wendao/common/utils/EmailUtils.java) — 异步 Thymeleaf HTML 邮件与邮箱格式校验

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `EmailUtils` | `com.wendao.common.utils::EmailUtils` | 20–92 |
| field | `log` | `Logger log` | 23–23 |
| field | `mailSender` | `JavaMailSender mailSender` | 26–26 |
| field | `templateEngine` | `TemplateEngine templateEngine` | 29–29 |
| field | `payProConfig` | `PayProConfig payProConfig` | 32–32 |
| method | `sendTemplateMail` | `void (String sender, String sendto,String title, String templateName,Object o)` | 41–48 |
| method | `sendTemplateMailOrThrow` | `void (String sender, String sendto, String title,                                        String templateName, Object o)` | 51–73 |
| method | `checkEmail` | `boolean (String email)` | 80–91 |

## IpInfoUtils.java

[src/main/java/com/wendao/common/utils/IpInfoUtils.java](../src/main/java/com/wendao/common/utils/IpInfoUtils.java) — 从代理头和请求读取客户端 IP

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `IpInfoUtils` | `com.wendao.common.utils::IpInfoUtils` | 13–56 |
| field | `log` | `Logger log` | 15–15 |
| method | `getIpAddr` | `String (HttpServletRequest request)` | 22–55 |

## StringUtils.java

[src/main/java/com/wendao/common/utils/StringUtils.java](../src/main/java/com/wendao/common/utils/StringUtils.java) — 空白检查、日期转换、Bean 转 Map、四位备注码

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `StringUtils` | `com.wendao.common.utils::StringUtils` | 14–108 |
| field | `dateFormat` | `SimpleDateFormat dateFormat` | 16–16 |
| method | `getTimeStamp` | `String (Date date)` | 23–29 |
| method | `getDate` | `Date (String time)` | 36–44 |
| method | `isBlank` | `boolean (String str)` | 51–64 |
| method | `isNotBlank` | `boolean (String str)` | 71–73 |
| method | `beanToMap` | `Map<String, Object> (T bean)` | 81–90 |
| method | `getRandomNum` | `String ()` | 95–102 |
| method | `main` | `void (String[] args)` | 104–106 |

## Config.java

[src/main/java/com/wendao/config/Config.java](../src/main/java/com/wendao/config/Config.java) — CORS、Thymeleaf 全局变量、分页插件与 Snowflake Bean

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `Config` | `com.wendao.config::Config` | 15–61 |
| field | `payConfig` | `PayProConfig payConfig` | 19–19 |
| method | `configureThymeleafStaticVars` | `void (ThymeleafViewResolver viewResolver)` | 25–37 |
| method | `addCorsMappings` | `void (CorsRegistry registry)` | 39–47 |
| method | `mybatisPlusInterceptor` | `MybatisPlusInterceptor ()` | 49–54 |
| method | `snowflake` | `Snowflake ()` | 56–59 |

## PayProConfig.java

[src/main/java/com/wendao/config/PayProConfig.java](../src/main/java/com/wendao/config/PayProConfig.java) — paypro 配置绑定、配置商品检索、外置二维码映射

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PayProConfig` | `com.wendao.config::PayProConfig` | 15–271 |
| field | `title` | `String title` | 23–23 |
| field | `indexTitle` | `String indexTitle` | 28–28 |
| field | `alipayUserId` | `String alipayUserId` | 33–33 |
| field | `alipayCustomQrUrl` | `String alipayCustomQrUrl` | 38–38 |
| field | `mobile` | `String mobile` | 43–43 |
| field | `name` | `String name` | 48–48 |
| field | `alipayDmfAppId` | `String alipayDmfAppId` | 53–53 |
| field | `alipayDmfAppPrivateKey` | `String alipayDmfAppPrivateKey` | 58–58 |
| field | `alipayDmfPublicKey` | `String alipayDmfPublicKey` | 63–63 |
| field | `alipayDmfSubject` | `String alipayDmfSubject` | 68–68 |
| field | `supportMail` | `String supportMail` | 73–73 |
| field | `site` | `String site` | 78–78 |
| field | `email` | `Email email` | 83–83 |
| field | `rateLimit` | `RateLimit rateLimit` | 88–88 |
| field | `token` | `Token token` | 93–93 |
| field | `order` | `Order order` | 98–98 |
| field | `qrCodeNum` | `Integer qrCodeNum` | 103–103 |
| field | `downloadUrl` | `String downloadUrl` | 106–106 |
| field | `payMethods` | `List<PayMethod> payMethods` | 108–108 |
| field | `qrDir` | `String qrDir` | 114–114 |
| class | `Email` | `com.wendao.config::PayProConfig::Email` | 119–130 |
| field | `receiver` | `String receiver` | 124–124 |
| field | `sender` | `String sender` | 129–129 |
| class | `RateLimit` | `com.wendao.config::PayProConfig::RateLimit` | 135–142 |
| field | `ipExpire` | `Long ipExpire` | 140–140 |
| class | `Token` | `com.wendao.config::PayProConfig::Token` | 144–156 |
| field | `expire` | `Long expire` | 149–149 |
| field | `value` | `String value` | 154–154 |
| class | `Order` | `com.wendao.config::PayProConfig::Order` | 158–164 |
| field | `timeoutMinutes` | `Long timeoutMinutes` | 163–163 |
| class | `PayMethod` | `com.wendao.config::PayProConfig::PayMethod` | 166–175 |
| field | `id` | `String id` | 168–168 |
| field | `name` | `String name` | 169–169 |
| field | `description` | `String description` | 170–170 |
| field | `icon` | `String icon` | 171–171 |
| field | `status` | `boolean status` | 172–172 |
| field | `allowNight` | `boolean allowNight` | 173–173 |
| field | `useLocalQrCode` | `boolean useLocalQrCode` | 174–174 |
| method | `getUseLocalQrCode` | `Boolean (String payType)` | 178–187 |
| method | `getPayTypeMap` | `Map<String, Boolean> ()` | 190–196 |
| field | `products` | `List<ProductConfig> products` | 201–201 |
| field | `decrement` | `Decrement decrement` | 206–206 |
| class | `Decrement` | `com.wendao.config::PayProConfig::Decrement` | 208–224 |
| field | `enabled` | `boolean enabled` | 213–213 |
| field | `maxCount` | `int maxCount` | 218–218 |
| field | `step` | `BigDecimal step` | 223–223 |
| class | `ProductConfig` | `com.wendao.config::PayProConfig::ProductConfig` | 229–238 |
| field | `id` | `Integer id` | 231–231 |
| field | `productName` | `String productName` | 232–232 |
| field | `money` | `BigDecimal money` | 233–233 |
| field | `description` | `String description` | 234–234 |
| field | `extend` | `String extend` | 235–235 |
| field | `type` | `String type` | 236–236 |
| field | `downloadUrl` | `String downloadUrl` | 237–237 |
| method | `getProductConfigById` | `ProductConfig (Integer id)` | 244–250 |
| method | `getProductConfigsByTypes` | `List<ProductConfig> (List<String> types)` | 256–261 |
| method | `addResourceHandlers` | `void (org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry registry)` | 263–270 |

## RedisConfig.java

[src/main/java/com/wendao/config/RedisConfig.java](../src/main/java/com/wendao/config/RedisConfig.java) — Object RedisTemplate 与 Jackson 序列化配置

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `RedisConfig` | `com.wendao.config::RedisConfig` | 13–36 |
| method | `redisTemplate` | `RedisTemplate<Object, Object> (RedisConnectionFactory redisConnectionFactory)` | 16–35 |

## OrderController.java

[src/main/java/com/wendao/controller/OrderController.java](../src/main/java/com/wendao/controller/OrderController.java) — 订单、审核、统计、OpenAPI 和支付方式路由

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `OrderController` | `com.wendao.controller::OrderController` | 40–302 |
| field | `log` | `Logger log` | 45–45 |
| field | `orderService` | `OrderService orderService` | 48–48 |
| field | `paymentConfirmationService` | `PaymentConfirmationService paymentConfirmationService` | 51–51 |
| method | `confirmPaid` | `ResponseVO<PaymentConfirmationResp> (@RequestBody @Validated ConfirmPaidReq request)` | 53–57 |
| method | `paymentConfirmation` | `ResponseVO<PaymentConfirmationResp> (@RequestParam String orderId,             @RequestHeader(value = "X-Payment-Confirm-Token", required = false) String token)` | 59–64 |
| field | `redisTemplate` | `StringRedisTemplate redisTemplate` | 67–67 |
| field | `emailUtils` | `EmailUtils emailUtils` | 70–70 |
| field | `payProConfig` | `PayProConfig payProConfig` | 73–73 |
| method | `getOrderList` | `ResponseVO<IPage<Order>> (@RequestBody GetOrderListReq req)` | 75–81 |
| method | `getOrderState` | `ResponseVO (@PathVariable String id)` | 83–107 |
| method | `getPayData` | `ResponseVO<Object> (@PathVariable String id,                                      @RequestParam String token)` | 109–128 |
| method | `addOrder` | `ResponseVO<AddOrderResp> (@RequestBody @Validated OrderReq orderReq, HttpServletRequest request)` | 130–137 |
| method | `editOrder` | `ResponseVO (@ModelAttribute Order order,                                   @RequestParam String id,                                   @RequestParam String token)` | 139–162 |
| method | `pass` | `String (@RequestParam String id,                          @RequestParam String token,                          @RequestParam String myToken,                          Model model)` | 169–195 |
| method | `backPay` | `String (@RequestParam String id,                           @RequestParam String token,                           @RequestParam String myToken,                           Model model)` | 197–226 |
| method | `dePay` | `ResponseVO<Object> (@RequestParam String id,                                  @RequestParam String token)` | 228–251 |
| method | `statistic` | `ResponseVO<Object> (@RequestParam Integer type,                                     @RequestParam(required = false) String start,                                     @RequestParam(required = false) String end,                                     @RequestParam String myToken)` | 257–268 |
| method | `getOrderId` | `String (String id)` | 270–272 |
| method | `createOpenApiOrder` | `ResponseVO<OpenApiOrderResp> (@RequestBody @Validated OpenApiOrderReq req)` | 274–294 |
| method | `getPayMethods` | `ResponseVO<PayProConfig.PayMethod> ()` | 296–301 |

## PageController.java

[src/main/java/com/wendao/controller/PageController.java](../src/main/java/com/wendao/controller/PageController.java) — 根页与通用模板路由，支付宝页状态副作用

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PageController` | `com.wendao.controller::PageController` | 23–67 |
| field | `log` | `Logger log` | 26–26 |
| field | `orderService` | `OrderService orderService` | 29–29 |
| field | `redisTemplate` | `StringRedisTemplate redisTemplate` | 32–32 |
| method | `index` | `String (Model model)` | 34–37 |
| method | `showPage` | `String (@PathVariable String page,                            HttpServletRequest request)` | 39–58 |
| method | `favicon` | `void ()` | 63–66 |

## ProductController.java

[src/main/java/com/wendao/controller/ProductController.java](../src/main/java/com/wendao/controller/ProductController.java) — 按 ID / 类型公开读取配置商品

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `ProductController` | `com.wendao.controller::ProductController` | 19–41 |
| field | `productService` | `ProductService productService` | 26–26 |
| method | `get` | `ResponseVO<Product> (Integer productId)` | 28–33 |
| method | `getListByType` | `ResponseVO<List<Product>> (@RequestBody GetProductListReq req)` | 35–40 |

## MsgContentsDTO.java

[src/main/java/com/wendao/dto/MsgContentsDTO.java](../src/main/java/com/wendao/dto/MsgContentsDTO.java) — 消息内容与付款方备注正则提取

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `MsgContentsDTO` | `com.wendao.dto::MsgContentsDTO` | 13–33 |
| field | `desc` | `String desc` | 15–15 |
| field | `title` | `String title` | 16–16 |
| field | `url` | `String url` | 17–17 |
| method | `extractRemark` | `String ()` | 23–32 |

## WeChatMsgDTO.java

[src/main/java/com/wendao/dto/WeChatMsgDTO.java](../src/main/java/com/wendao/dto/WeChatMsgDTO.java) — 微信消息结构，当前未接入到账业务入口

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `WeChatMsgDTO` | `com.wendao.dto::WeChatMsgDTO` | 11–26 |
| field | `seq` | `long seq` | 13–13 |
| field | `id` | `long id` | 14–14 |
| field | `time` | `Date time` | 15–15 |
| field | `talker` | `String talker` | 16–16 |
| field | `talkerName` | `String talkerName` | 17–17 |
| field | `isChatRoom` | `boolean isChatRoom` | 18–18 |
| field | `sender` | `String sender` | 19–19 |
| field | `senderName` | `String senderName` | 20–20 |
| field | `isSelf` | `boolean isSelf` | 21–21 |
| field | `type` | `int type` | 22–22 |
| field | `subType` | `int subType` | 23–23 |
| field | `content` | `String content` | 24–24 |
| field | `contents` | `MsgContentsDTO contents` | 25–25 |

## Order.java

[src/main/java/com/wendao/entity/Order.java](../src/main/java/com/wendao/entity/Order.java) — 订单持久化实体及邮件管理 URL 临时属性

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `Order` | `com.wendao.entity::Order` | 18–151 |
| field | `id` | `String id` | 26–26 |
| field | `nickName` | `String nickName` | 28–28 |
| field | `money` | `BigDecimal money` | 30–30 |
| field | `userId` | `String userId` | 32–32 |
| field | `description` | `String description` | 37–37 |
| field | `createTime` | `Date createTime` | 39–39 |
| field | `updateTime` | `Date updateTime` | 41–41 |
| field | `email` | `String email` | 46–46 |
| field | `state` | `Integer state` | 51–51 |
| field | `payType` | `String payType` | 53–53 |
| field | `payNum` | `String payNum` | 58–58 |
| field | `payQrNum` | `Integer payQrNum` | 63–63 |
| field | `matchMode` | `String matchMode` | 68–68 |
| field | `actualAmount` | `BigDecimal actualAmount` | 73–73 |
| field | `decrementIndex` | `Integer decrementIndex` | 78–78 |
| field | `custom` | `Boolean custom` | 83–83 |
| field | `mobile` | `Boolean mobile` | 88–88 |
| field | `device` | `String device` | 93–93 |
| field | `productId` | `Long productId` | 98–98 |
| field | `orderSource` | `String orderSource` | 101–101 |
| field | `notifyUrl` | `String notifyUrl` | 104–104 |
| field | `expireTime` | `Date expireTime` | 107–107 |
| field | `paymentConfirmTokenHash` | `String paymentConfirmTokenHash` | 112–112 |
| field | `paymentConfirmedAt` | `Date paymentConfirmedAt` | 116–116 |
| field | `adminNoticeStatus` | `String adminNoticeStatus` | 120–120 |
| field | `time` | `String time` | 123–123 |
| field | `passUrl` | `String passUrl` | 127–127 |
| field | `backUrl` | `String backUrl` | 131–131 |
| field | `editUrl` | `String editUrl` | 135–135 |
| field | `delUrl` | `String delUrl` | 139–139 |
| field | `closeUrl` | `String closeUrl` | 143–143 |
| field | `statistic` | `String statistic` | 147–147 |
| field | `downloadUrl` | `String downloadUrl` | 150–150 |

## Product.java

[src/main/java/com/wendao/entity/Product.java](../src/main/java/com/wendao/entity/Product.java) — 配置商品实体，非数据库表

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `Product` | `com.wendao.entity::Product` | 11–36 |
| field | `id` | `Integer id` | 17–17 |
| field | `productName` | `String productName` | 19–19 |
| field | `money` | `BigDecimal money` | 21–21 |
| field | `description` | `String description` | 26–26 |
| field | `extend` | `String extend` | 28–28 |
| field | `type` | `String type` | 31–31 |
| field | `downloadUrl` | `String downloadUrl` | 34–34 |

## AdminNoticeStatus.java

[src/main/java/com/wendao/enums/AdminNoticeStatus.java](../src/main/java/com/wendao/enums/AdminNoticeStatus.java) — 管理员通知状态，与订单付款状态分离

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| enum | `AdminNoticeStatus` | `com.wendao.enums::AdminNoticeStatus` | 4–6 |
| enum_member | `FAILED` | `com.wendao.enums::AdminNoticeStatus::FAILED` | 5–5 |
| enum_member | `NOT_REQUESTED` | `com.wendao.enums::AdminNoticeStatus::NOT_REQUESTED` | 5–5 |
| enum_member | `SENDING` | `com.wendao.enums::AdminNoticeStatus::SENDING` | 5–5 |
| enum_member | `SENT` | `com.wendao.enums::AdminNoticeStatus::SENT` | 5–5 |

## OrderStatesEnum.java

[src/main/java/com/wendao/enums/OrderStatesEnum.java](../src/main/java/com/wendao/enums/OrderStatesEnum.java) — 订单状态 0 / 1 / 2 / 4 / 5

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| enum | `OrderStatesEnum` | `com.wendao.enums::OrderStatesEnum` | 4–38 |
| enum_member | `WAIT_PAY` | `com.wendao.enums::OrderStatesEnum::WAIT_PAY` | 7–7 |
| enum_member | `SUCCESS_PAY` | `com.wendao.enums::OrderStatesEnum::SUCCESS_PAY` | 9–9 |
| enum_member | `FAIL_PAY` | `com.wendao.enums::OrderStatesEnum::FAIL_PAY` | 11–11 |
| enum_member | `SCANE_QR` | `com.wendao.enums::OrderStatesEnum::SCANE_QR` | 13–13 |
| enum_member | `EXPIRED` | `com.wendao.enums::OrderStatesEnum::EXPIRED` | 15–15 |
| field | `state` | `Integer state` | 20–20 |
| field | `desc` | `String desc` | 21–21 |
| method | `getState` | `Integer ()` | 23–25 |
| method | `getDesc` | `String ()` | 27–29 |
| method | `OrderStatesEnum` | `(int state, String desc)` | 31–34 |

## ApiException.java

[src/main/java/com/wendao/exception/ApiException.java](../src/main/java/com/wendao/exception/ApiException.java) — 业务异常与错误码常量

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `ApiException` | `com.wendao.exception::ApiException` | 5–30 |
| field | `code` | `int code` | 8–8 |
| field | `message` | `String message` | 9–9 |
| method | `ApiException` | `(int code, String message)` | 11–15 |
| method | `ApiException` | `(String message)` | 17–19 |
| class | `ErrorCode` | `com.wendao.exception::ApiException::ErrorCode` | 21–29 |
| field | `SUCCESS` | `int SUCCESS` | 22–22 |
| field | `INVALID_PARAM` | `int INVALID_PARAM` | 23–23 |
| field | `SIGN_ERROR` | `int SIGN_ERROR` | 24–24 |
| field | `TIMESTAMP_ERROR` | `int TIMESTAMP_ERROR` | 25–25 |
| field | `DUPLICATE_ORDER` | `int DUPLICATE_ORDER` | 26–26 |
| field | `AMOUNT_ERROR` | `int AMOUNT_ERROR` | 27–27 |
| field | `SYSTEM_ERROR` | `int SYSTEM_ERROR` | 28–28 |

## GlobalExceptionHandler.java

[src/main/java/com/wendao/exception/GlobalExceptionHandler.java](../src/main/java/com/wendao/exception/GlobalExceptionHandler.java) — 业务、参数与通用异常转换为 ResponseVO

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `GlobalExceptionHandler` | `com.wendao.exception::GlobalExceptionHandler` | 12–55 |
| field | `log` | `Logger log` | 15–15 |
| method | `handleValidation` | `ResponseVO<?> (MethodArgumentNotValidException e)` | 17–22 |
| method | `handleMissingInput` | `ResponseVO<?> (Exception e)` | 24–27 |
| method | `handleApiException` | `ResponseVO<?> (ApiException e)` | 29–36 |
| method | `handleIllegalArgumentException` | `ResponseVO<?> (IllegalArgumentException e)` | 38–45 |
| method | `handleException` | `ResponseVO<?> (Exception e)` | 47–54 |

## OrderMapper.java

[src/main/java/com/wendao/mapper/OrderMapper.java](../src/main/java/com/wendao/mapper/OrderMapper.java) — 订单 BaseMapper、聚合统计、过期与实际金额查询

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| interface | `OrderMapper` | `com.wendao.mapper::OrderMapper` | 16–59 |
| method | `claimPaymentNotice` | `int (@Param("id") String id, @Param("hash") String hash, @Param("now") Date now)` | 18–24 |
| method | `finishPaymentNotice` | `int (@Param("id") String id, @Param("status") String status)` | 26–28 |
| method | `approveOrder` | `int (@Param("id") String id)` | 30–31 |
| method | `getExpiredOrders` | `List<Order> (Integer state, Date expireTime)` | 33–36 |
| method | `countAllMoney` | `BigDecimal ()` | 38–39 |
| method | `countAllMoneyByType` | `BigDecimal (String payType)` | 41–42 |
| method | `countMoney` | `BigDecimal (Date date1, Date date2)` | 44–45 |
| method | `countMoneyByType` | `BigDecimal (String payType, Date date1, Date date2)` | 47–48 |
| method | `getDecrementOrderByAmount` | `Order (BigDecimal actualAmount, Date startTime, Date endTime)` | 53–58 |

## ResponseVO.java

[src/main/java/com/wendao/model/ResponseVO.java](../src/main/java/com/wendao/model/ResponseVO.java) — 通用 code / msg / data 响应封装

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `ResponseVO` | `com.wendao.model::ResponseVO` | 10–68 |
| field | `serialVersionUID` | `long serialVersionUID` | 16–16 |
| field | `code` | `int code` | 18–18 |
| field | `msg` | `String msg` | 20–20 |
| field | `data` | `T data` | 22–22 |
| method | `successResponse` | `ResponseVO (Object data)` | 24–26 |
| method | `successResponse` | `ResponseVO ()` | 28–30 |
| method | `errorResponse` | `ResponseVO ()` | 32–34 |
| method | `errorResponse` | `ResponseVO (int code, String msg)` | 36–38 |
| method | `errorResponse` | `ResponseVO (String msg)` | 40–42 |
| method | `isOk` | `boolean ()` | 44–46 |
| method | `ResponseVO` | `(int code, String msg)` | 49–53 |
| method | `success` | `ResponseVO ()` | 55–59 |
| method | `success` | `ResponseVO (T data)` | 61–66 |

## ConfirmPaidReq.java

[src/main/java/com/wendao/model/req/ConfirmPaidReq.java](../src/main/java/com/wendao/model/req/ConfirmPaidReq.java) — 客户主动声明付款请求，订单号和客户凭证非空

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `ConfirmPaidReq` | `com.wendao.model.req::ConfirmPaidReq` | 6–13 |
| field | `orderId` | `String orderId` | 9–9 |
| field | `paymentConfirmToken` | `String paymentConfirmToken` | 12–12 |

## GetOrderListReq.java

[src/main/java/com/wendao/model/req/GetOrderListReq.java](../src/main/java/com/wendao/model/req/GetOrderListReq.java) — 订单分页、状态、关键词与排序请求

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `GetOrderListReq` | `com.wendao.model.req::GetOrderListReq` | 10–35 |
| field | `pageIndex` | `Integer pageIndex` | 15–15 |
| field | `pageSize` | `Integer pageSize` | 20–20 |
| field | `orderBy` | `String orderBy` | 25–25 |
| field | `order` | `String order` | 30–30 |
| field | `keyword` | `String keyword` | 32–32 |
| field | `states` | `List<Integer> states` | 34–34 |

## GetProductListReq.java

[src/main/java/com/wendao/model/req/GetProductListReq.java](../src/main/java/com/wendao/model/req/GetProductListReq.java) — 商品类型列表请求

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `GetProductListReq` | `com.wendao.model.req::GetProductListReq` | 11–17 |
| field | `types` | `List<String> types` | 14–14 |

## OpenApiOrderReq.java

[src/main/java/com/wendao/model/req/OpenApiOrderReq.java](../src/main/java/com/wendao/model/req/OpenApiOrderReq.java) — 外部下单与签名参数模型

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `OpenApiOrderReq` | `com.wendao.model.req::OpenApiOrderReq` | 10–45 |
| field | `orderNo` | `String orderNo` | 14–14 |
| field | `amount` | `BigDecimal amount` | 17–17 |
| field | `payType` | `String payType` | 20–20 |
| field | `nickName` | `String nickName` | 22–22 |
| field | `description` | `String description` | 24–24 |
| field | `email` | `String email` | 26–26 |
| field | `notifyUrl` | `String notifyUrl` | 28–28 |
| field | `userId` | `String userId` | 30–30 |
| field | `productId` | `Long productId` | 32–32 |
| field | `sign` | `String sign` | 35–35 |
| field | `timestamp` | `Long timestamp` | 37–37 |
| field | `custom` | `Boolean custom` | 41–41 |
| field | `expireSeconds` | `Integer expireSeconds` | 44–44 |

## OrderReq.java

[src/main/java/com/wendao/model/req/OrderReq.java](../src/main/java/com/wendao/model/req/OrderReq.java) — 普通下单请求模型

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `OrderReq` | `com.wendao.model.req::OrderReq` | 11–65 |
| field | `nickName` | `String nickName` | 14–14 |
| field | `productId` | `Long productId` | 16–16 |
| field | `money` | `BigDecimal money` | 19–19 |
| field | `description` | `String description` | 24–24 |
| field | `createTime` | `Date createTime` | 26–26 |
| field | `updateTime` | `Date updateTime` | 28–28 |
| field | `email` | `String email` | 33–33 |
| field | `state` | `Integer state` | 38–38 |
| field | `payType` | `String payType` | 40–40 |
| field | `payNum` | `String payNum` | 45–45 |
| field | `custom` | `Boolean custom` | 50–50 |
| field | `userId` | `String userId` | 52–52 |
| field | `mobile` | `Boolean mobile` | 57–57 |
| field | `device` | `String device` | 62–62 |
| field | `time` | `String time` | 64–64 |

## AddOrderResp.java

[src/main/java/com/wendao/model/resp/AddOrderResp.java](../src/main/java/com/wendao/model/resp/AddOrderResp.java) — 普通下单支付信息响应

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `AddOrderResp` | `com.wendao.model.resp::AddOrderResp` | 13–62 |
| field | `paymentConfirmToken` | `String paymentConfirmToken` | 17–17 |
| field | `id` | `String id` | 23–23 |
| field | `money` | `BigDecimal money` | 26–26 |
| field | `payType` | `String payType` | 29–29 |
| field | `payNum` | `String payNum` | 32–32 |
| field | `custom` | `Boolean custom` | 38–38 |
| field | `payQrNum` | `Integer payQrNum` | 43–43 |
| field | `matchMode` | `String matchMode` | 49–49 |
| field | `actualAmount` | `BigDecimal actualAmount` | 55–55 |
| field | `fallbackToRemark` | `Boolean fallbackToRemark` | 61–61 |

## CountResp.java

[src/main/java/com/wendao/model/resp/CountResp.java](../src/main/java/com/wendao/model/resp/CountResp.java) — 成功订单原价统计响应

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `CountResp` | `com.wendao.model.resp::CountResp` | 7–17 |
| field | `amount` | `BigDecimal amount` | 10–10 |
| field | `weixin` | `BigDecimal weixin` | 12–12 |
| field | `alipay` | `BigDecimal alipay` | 14–14 |

## OpenApiOrderResp.java

[src/main/java/com/wendao/model/resp/OpenApiOrderResp.java](../src/main/java/com/wendao/model/resp/OpenApiOrderResp.java) — 外部下单、二维码与支付页响应

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `OpenApiOrderResp` | `com.wendao.model.resp::OpenApiOrderResp` | 11–44 |
| field | `paymentConfirmToken` | `String paymentConfirmToken` | 17–17 |
| field | `orderId` | `String orderId` | 19–19 |
| field | `orderNo` | `String orderNo` | 21–21 |
| field | `amount` | `BigDecimal amount` | 23–23 |
| field | `payType` | `String payType` | 25–25 |
| field | `payNum` | `String payNum` | 27–27 |
| field | `state` | `Integer state` | 29–29 |
| field | `message` | `String message` | 31–31 |
| field | `timestamp` | `Long timestamp` | 33–33 |
| field | `qrCodeUrl` | `String qrCodeUrl` | 35–35 |
| field | `returnUrl` | `String returnUrl` | 37–37 |
| field | `matchMode` | `String matchMode` | 39–39 |
| field | `actualAmount` | `BigDecimal actualAmount` | 41–41 |
| field | `fallbackToRemark` | `Boolean fallbackToRemark` | 43–43 |

## PaymentConfirmationResp.java

[src/main/java/com/wendao/model/resp/PaymentConfirmationResp.java](../src/main/java/com/wendao/model/resp/PaymentConfirmationResp.java) — 鉴权付款声明查询响应、通知状态和重试资格

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PaymentConfirmationResp` | `com.wendao.model.resp::PaymentConfirmationResp` | 7–18 |
| field | `orderState` | `Integer orderState` | 9–9 |
| field | `amount` | `BigDecimal amount` | 10–10 |
| field | `payType` | `String payType` | 11–11 |
| field | `payNum` | `String payNum` | 12–12 |
| field | `expireTime` | `Date expireTime` | 13–13 |
| field | `confirmedAt` | `Date confirmedAt` | 14–14 |
| field | `noticeStatus` | `String noticeStatus` | 15–15 |
| field | `canConfirm` | `boolean canConfirm` | 16–16 |
| field | `retryable` | `boolean retryable` | 17–17 |

## OrderService.java

[src/main/java/com/wendao/service/OrderService.java](../src/main/java/com/wendao/service/OrderService.java) — 订单业务接口

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| interface | `OrderService` | `com.wendao.service::OrderService` | 21–86 |
| method | `getOrderById` | `Order (String id)` | 28–28 |
| method | `addOrder` | `int (Order order)` | 35–35 |
| method | `updateOrder` | `int (Order order)` | 42–42 |
| method | `changeOrderState` | `int (String id,Integer state)` | 50–50 |
| method | `delOrder` | `int (String id)` | 57–57 |
| method | `statistic` | `CountResp (Integer type, String start, String end)` | 66–66 |
| method | `addOrder` | `ResponseVO<AddOrderResp> (OrderReq order, HttpServletRequest request)` | 68–68 |
| method | `pass` | `int (String id)` | 70–70 |
| method | `list` | `IPage<Order> (GetOrderListReq req)` | 72–72 |
| method | `createOpenApiOrder` | `OpenApiOrderResp (OpenApiOrderReq req)` | 74–74 |
| method | `getByActualAmount` | `Order (BigDecimal actualAmount, Date startTime, Date endTime)` | 79–79 |
| method | `getOccupiedDecrementSlots` | `Set<Integer> (String payType, BigDecimal baseAmount)` | 84–84 |

## PaymentConfirmationService.java

[src/main/java/com/wendao/service/PaymentConfirmationService.java](../src/main/java/com/wendao/service/PaymentConfirmationService.java) — 鉴权声明、发送锁、事务提交后调度及状态恢复

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PaymentConfirmationService` | `com.wendao.service::PaymentConfirmationService` | 20–158 |
| field | `log` | `Logger log` | 22–22 |
| field | `orders` | `OrderMapper orders` | 23–23 |
| field | `locks` | `PaymentNoticeLock locks` | 24–24 |
| field | `sender` | `PaymentNoticeSender sender` | 25–25 |
| method | `PaymentConfirmationService` | `(OrderMapper orders, PaymentNoticeLock locks, PaymentNoticeSender sender)` | 27–31 |
| method | `status` | `PaymentConfirmationResp (String id, String token)` | 33–35 |
| method | `confirm` | `PaymentConfirmationResp (ConfirmPaidReq request)` | 37–84 |
| class | `<TransactionSynchronizationAdapter$anon@61>` | `com.wendao.service::PaymentConfirmationService::confirm::<TransactionSynchronizationAdapter$anon@61>` | 61–73 |
| method | `afterCommit` | `void ()` | 62–65 |
| method | `afterCompletion` | `void (int completionStatus)` | 67–72 |
| method | `authorize` | `Order (String id, String token)` | 86–101 |
| method | `ensureConfirmable` | `void (Order order)` | 103–107 |
| method | `pending` | `boolean (Order order)` | 109–111 |
| method | `expiredBeforeConfirmation` | `boolean (Order order)` | 113–116 |
| method | `response` | `PaymentConfirmationResp (Order order)` | 118–139 |
| method | `dispatch` | `void (String id, String attempt)` | 141–149 |
| method | `release` | `void (String id, String attempt)` | 151–157 |

## PaymentNoticeLock.java

[src/main/java/com/wendao/service/PaymentNoticeLock.java](../src/main/java/com/wendao/service/PaymentNoticeLock.java) — Redis SET NX发送租约与Lua归属校验释放

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PaymentNoticeLock` | `com.wendao.service::PaymentNoticeLock` | 11–40 |
| field | `PREFIX` | `String PREFIX` | 13–13 |
| field | `RELEASE` | `DefaultRedisScript<Long> RELEASE` | 14–16 |
| field | `redis` | `StringRedisTemplate redis` | 17–17 |
| method | `PaymentNoticeLock` | `(StringRedisTemplate redis)` | 19–21 |
| method | `acquire` | `String (String id)` | 23–27 |
| method | `isOwned` | `boolean (String id, String attempt)` | 29–31 |
| method | `isLocked` | `boolean (String id)` | 33–35 |
| method | `release` | `void (String id, String attempt)` | 37–39 |

## PaymentNoticeSender.java

[src/main/java/com/wendao/service/PaymentNoticeSender.java](../src/main/java/com/wendao/service/PaymentNoticeSender.java) — 提交后异步邮件、独立审核链接、SMTP结果持久化

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PaymentNoticeSender` | `com.wendao.service::PaymentNoticeSender` | 22–108 |
| field | `log` | `Logger log` | 24–24 |
| field | `orders` | `OrderMapper orders` | 25–25 |
| field | `locks` | `PaymentNoticeLock locks` | 26–26 |
| field | `redis` | `StringRedisTemplate redis` | 27–27 |
| field | `mail` | `EmailUtils mail` | 28–28 |
| field | `config` | `PayProConfig config` | 29–29 |
| method | `PaymentNoticeSender` | `(OrderMapper orders, PaymentNoticeLock locks,                                StringRedisTemplate redis, EmailUtils mail, PayProConfig config)` | 31–38 |
| method | `send` | `void (String id, String attempt)` | 40–94 |
| method | `reviewUrl` | `String (String path, String id, String token, boolean secondFactor)` | 96–107 |

## ProductService.java

[src/main/java/com/wendao/service/ProductService.java](../src/main/java/com/wendao/service/ProductService.java) — 商品业务接口

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| interface | `ProductService` | `com.wendao.service::ProductService` | 13–24 |
| method | `get` | `ResponseVO<Product> (Integer productId)` | 14–14 |
| method | `getListByType` | `ResponseVO<List<Product>> (GetProductListReq req)` | 16–16 |
| method | `getProductById` | `Product (Integer productId)` | 23–23 |

## OrderServiceImpl.java

[src/main/java/com/wendao/service/impl/OrderServiceImpl.java](../src/main/java/com/wendao/service/impl/OrderServiceImpl.java) — 普通 / 外部下单、减额、审核、分页、统计与回调

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `OrderServiceImpl` | `com.wendao.service.impl::OrderServiceImpl` | 47–747 |
| field | `log` | `Logger log` | 50–50 |
| field | `orderMapper` | `OrderMapper orderMapper` | 53–53 |
| field | `redisTemplate` | `StringRedisTemplate redisTemplate` | 56–56 |
| field | `thisService` | `OrderService thisService` | 59–59 |
| field | `payProConfig` | `PayProConfig payProConfig` | 62–62 |
| field | `emailUtils` | `EmailUtils emailUtils` | 65–65 |
| field | `snowflake` | `Snowflake snowflake` | 68–68 |
| field | `openApiSignUtil` | `OpenApiSignUtil openApiSignUtil` | 71–71 |
| field | `resourceLoader` | `ResourceLoader resourceLoader` | 74–74 |
| method | `getOrderById` | `Order (String id)` | 76–81 |
| method | `addOrder` | `int (Order pay)` | 83–97 |
| method | `updateOrder` | `int (Order pay)` | 99–104 |
| method | `changeOrderState` | `int (String id, Integer state)` | 106–114 |
| method | `delOrder` | `int (String id)` | 116–120 |
| method | `statistic` | `CountResp (Integer type, String start, String end)` | 122–172 |
| method | `addOrder` | `ResponseVO<AddOrderResp> (OrderReq req, HttpServletRequest request)` | 174–282 |
| method | `pass` | `int (String id)` | 287–323 |
| class | `<TransactionSynchronizationAdapter$anon@312>` | `com.wendao.service.impl::OrderServiceImpl::pass::<TransactionSynchronizationAdapter$anon@312>` | 312–317 |
| method | `afterCommit` | `void ()` | 313–316 |
| method | `list` | `IPage<Order> (GetOrderListReq req)` | 325–367 |
| method | `createOpenApiOrder` | `OpenApiOrderResp (OpenApiOrderReq req)` | 369–555 |
| method | `checkQrFileExists` | `boolean (String payType, BigDecimal amount, int qrNum)` | 565–591 |
| method | `callbackFaka` | `void (String notifyUrl, String orderNo, BigDecimal amount, String payNum)` | 594–604 |
| class | `DecrementSlotResult` | `com.wendao.service.impl::OrderServiceImpl::DecrementSlotResult` | 610–616 |
| field | `success` | `boolean success` | 612–612 |
| field | `fallbackToRemark` | `boolean fallbackToRemark` | 613–613 |
| field | `slotIndex` | `int slotIndex` | 614–614 |
| field | `actualAmount` | `BigDecimal actualAmount` | 615–615 |
| method | `tryAllocateDecrementSlot` | `DecrementSlotResult (             String payType, BigDecimal baseAmount, PayProConfig.Decrement config)` | 628–680 |
| method | `checkAnyQrFileExists` | `boolean (String payType, BigDecimal baseAmount, BigDecimal amount)` | 687–711 |
| method | `getByActualAmount` | `Order (BigDecimal actualAmount, Date startTime, Date endTime)` | 713–716 |
| method | `getOccupiedDecrementSlots` | `Set<Integer> (String payType, BigDecimal baseAmount)` | 718–741 |
| method | `getDecrementLockKey` | `String (String payType, String baseAmount)` | 743–745 |

## ProductServiceImpl.java

[src/main/java/com/wendao/service/impl/ProductServiceImpl.java](../src/main/java/com/wendao/service/impl/ProductServiceImpl.java) — YAML 商品转实体，公开接口清除下载链接

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `ProductServiceImpl` | `com.wendao.service.impl::ProductServiceImpl` | 17–65 |
| field | `payProConfig` | `PayProConfig payProConfig` | 21–21 |
| method | `getProductById` | `Product (Integer productId)` | 23–27 |
| method | `get` | `ResponseVO<Product> (Integer productId)` | 29–38 |
| method | `getListByType` | `ResponseVO<List<Product>> (GetProductListReq req)` | 40–49 |
| method | `toProductEntity` | `Product (PayProConfig.ProductConfig config)` | 54–64 |

## OpenApiSignUtil.java

[src/main/java/com/wendao/utils/OpenApiSignUtil.java](../src/main/java/com/wendao/utils/OpenApiSignUtil.java) — OpenAPI MD5 签名、验签及五分钟时间戳验证

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `OpenApiSignUtil` | `com.wendao.utils::OpenApiSignUtil` | 14–113 |
| field | `log` | `Logger log` | 17–17 |
| field | `secretKey` | `String secretKey` | 20–20 |
| method | `generateSign` | `String (Map<String, Object> params)` | 22–54 |
| method | `verifySign` | `boolean (OpenApiOrderReq req)` | 56–92 |
| method | `verifyTimestamp` | `boolean (Long timestamp)` | 94–107 |
| method | `main` | `void (String[] args)` | 109–112 |

## PaymentConfirmTokens.java

[src/main/java/com/wendao/utils/PaymentConfirmTokens.java](../src/main/java/com/wendao/utils/PaymentConfirmTokens.java) — 生成客户随机凭证、保存哈希并恒定时间校验

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PaymentConfirmTokens` | `com.wendao.utils::PaymentConfirmTokens` | 12–47 |
| field | `RANDOM` | `SecureRandom RANDOM` | 13–13 |
| method | `PaymentConfirmTokens` | `()` | 15–15 |
| method | `initialize` | `String (Order order)` | 17–24 |
| method | `matches` | `boolean (String token, String expectedHash)` | 26–32 |
| method | `hash` | `String (String token)` | 34–46 |

## EmailUtilsOutcomeTest.java

[src/test/java/com/wendao/service/EmailUtilsOutcomeTest.java](../src/test/java/com/wendao/service/EmailUtilsOutcomeTest.java) — 真实Thymeleaf渲染和Mock JavaMailSender结果测试

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `EmailUtilsOutcomeTest` | `com.wendao.service::EmailUtilsOutcomeTest` | 27–77 |
| method | `engine` | `SpringTemplateEngine ()` | 28–37 |
| method | `reviewTemplateRendersAndSmtpErrorsReachNotificationWorker` | `void ()` | 39–61 |
| method | `actualThymeleafJavaScriptInliningPreservesAlipayUrlParameters` | `void ()` | 63–76 |

## OrderCreationNotificationTest.java

[src/test/java/com/wendao/service/OrderCreationNotificationTest.java](../src/test/java/com/wendao/service/OrderCreationNotificationTest.java) — 下单不发信、来源、自定义金额、编码链接和批准幂等测试

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `OrderCreationNotificationTest` | `com.wendao.service::OrderCreationNotificationTest` | 30–140 |
| field | `service` | `OrderServiceImpl service` | 31–31 |
| field | `orders` | `OrderMapper orders` | 32–32 |
| field | `mail` | `EmailUtils mail` | 33–33 |
| field | `signs` | `OpenApiSignUtil signs` | 34–34 |
| field | `inserted` | `AtomicReference<Order> inserted` | 35–35 |
| method | `setup` | `void ()` | 37–60 |
| method | `normalRequest` | `OrderReq ()` | 62–68 |
| method | `browser` | `MockHttpServletRequest ()` | 70–74 |
| method | `ordinaryOrderDoesNotSendMailAndOnlyStoresCredentialHash` | `void ()` | 76–85 |
| method | `customAmountDoesNotAccidentallyKeepPreviouslySelectedProduct` | `void ()` | 87–96 |
| method | `productOrderKeepsItsSourceWithoutSendingMail` | `void ()` | 98–105 |
| method | `openApiReturnsCompleteConfirmationLinkWithoutNotifyingAdmin` | `void ()` | 107–123 |
| method | `customAndNullSourceLegacyOrdersCanBeApprovedOnlyOnce` | `void ()` | 125–139 |

## PaymentConfirmationControllerTest.java

[src/test/java/com/wendao/service/PaymentConfirmationControllerTest.java](../src/test/java/com/wendao/service/PaymentConfirmationControllerTest.java) — MockMvc请求体、请求头和参数错误测试

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PaymentConfirmationControllerTest` | `com.wendao.service::PaymentConfirmationControllerTest` | 19–72 |
| field | `service` | `PaymentConfirmationService service` | 20–20 |
| field | `mvc` | `MockMvc mvc` | 21–21 |
| method | `setup` | `void ()` | 23–30 |
| method | `confirmationUsesPostAndReturnsPendingPaymentState` | `void ()` | 32–43 |
| method | `missingConfirmationCredentialIsAValidationError` | `void ()` | 45–51 |
| method | `statusUsesScopedCredentialHeaderAndNeverConfirmsAnOrder` | `void ()` | 53–63 |
| method | `invalidScopedTokenIsRejectedWithoutReturningAdminLinks` | `void ()` | 65–71 |

## PaymentConfirmationDatabaseIT.java

[src/test/java/com/wendao/service/PaymentConfirmationDatabaseIT.java](../src/test/java/com/wendao/service/PaymentConfirmationDatabaseIT.java) — 可选隔离MySQL/Redis增量迁移、12请求并发和元数据保护测试

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PaymentConfirmationDatabaseIT` | `com.wendao.service::PaymentConfirmationDatabaseIT` | 34–161 |
| field | `dataSource` | `DriverManagerDataSource dataSource` | 36–36 |
| field | `sessions` | `SqlSessionFactory sessions` | 37–37 |
| field | `redisFactory` | `JedisConnectionFactory redisFactory` | 38–38 |
| field | `redis` | `StringRedisTemplate redis` | 39–39 |
| method | `setup` | `void ()` | 41–62 |
| method | `cleanup` | `void ()` | 64–67 |
| method | `additiveMigrationPreservesLegacyRowsAndLeavesThemUnenrolled` | `void ()` | 69–84 |
| method | `realRedisLockAndSqlClaimDeduplicateConcurrentRequestsAndPersistSent` | `void ()` | 86–137 |
| method | `ordinaryEntityUpdatesCannotOverwritePrivateNotificationMetadata` | `void ()` | 139–160 |

## PaymentConfirmationServiceTest.java

[src/test/java/com/wendao/service/PaymentConfirmationServiceTest.java](../src/test/java/com/wendao/service/PaymentConfirmationServiceTest.java) — 声明鉴权、事务回滚、去重、失败重试及JSON隐私测试

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PaymentConfirmationServiceTest` | `com.wendao.service::PaymentConfirmationServiceTest` | 24–207 |
| field | `orders` | `OrderMapper orders` | 25–25 |
| field | `locks` | `PaymentNoticeLock locks` | 26–26 |
| field | `sender` | `PaymentNoticeSender sender` | 27–27 |
| field | `service` | `PaymentConfirmationService service` | 28–28 |
| field | `order` | `Order order` | 29–29 |
| field | `token` | `String token` | 30–30 |
| method | `setup` | `void ()` | 32–45 |
| method | `cleanup` | `void ()` | 47–52 |
| method | `request` | `ConfirmPaidReq ()` | 54–59 |
| method | `allowClaim` | `void ()` | 61–74 |
| method | `statusNeverClaimsOrSends` | `void ()` | 76–84 |
| method | `confirmationRecordsDeclarationButNeverPaymentSuccess` | `void ()` | 86–96 |
| method | `actualTransactionDefersMailUntilCommit` | `void ()` | 98–109 |
| method | `rollbackNeverDispatchesAndReleasesLock` | `void ()` | 111–121 |
| method | `previouslySentNoticeRemainsDeduplicatedEvenWithoutRedisLock` | `void ()` | 123–129 |
| method | `concurrentRequestDoesNotStartAnotherMail` | `void ()` | 131–139 |
| method | `staleSendingLeaseIsReadOnlyAndRetryable` | `void ()` | 141–149 |
| method | `failedNoticeRetryPreservesOriginalDeclarationTime` | `void ()` | 151–160 |
| method | `rejectedAsyncExecutionCanBeRetried` | `void ()` | 162–168 |
| method | `legacyAndInvalidCredentialsNeverSendMail` | `void ()` | 170–176 |
| method | `missingAndTerminalOrdersAreRejected` | `void ()` | 178–186 |
| method | `expiredUnreportedOrderCannotNotify` | `void ()` | 188–194 |
| method | `payerSecretsAndMetadataDoNotLeakThroughPublicOrderJson` | `void ()` | 196–206 |

## PaymentNoticeSenderTest.java

[src/test/java/com/wendao/service/PaymentNoticeSenderTest.java](../src/test/java/com/wendao/service/PaymentNoticeSenderTest.java) — SMTP结果、锁归属、旧任务和旧订单隔离测试

| 类别 | 名称 | 签名 / 类型 | 行号 |
| --- | --- | --- | --- |
| class | `PaymentNoticeSenderTest` | `com.wendao.service::PaymentNoticeSenderTest` | 21–123 |
| field | `orders` | `OrderMapper orders` | 22–22 |
| field | `locks` | `PaymentNoticeLock locks` | 23–23 |
| field | `mail` | `EmailUtils mail` | 24–24 |
| field | `sender` | `PaymentNoticeSender sender` | 25–25 |
| field | `order` | `Order order` | 26–26 |
| field | `payerToken` | `String payerToken` | 27–27 |
| field | `values` | `ValueOperations<String, String> values` | 28–28 |
| method | `setup` | `void ()` | 30–58 |
| method | `smtpAcceptancePersistsSentAndBuildsSeparateAdminLinks` | `void ()` | 60–70 |
| method | `smtpFailureIsRecordedForRetry` | `void ()` | 72–80 |
| method | `reviewLinksPreserveSpecialCharactersInExternalOrderNumbers` | `void ()` | 82–96 |
| method | `lostOwnershipDoesNotDeliverOrOverwriteAnotherAttempt` | `void ()` | 98–104 |
| method | `oldAttemptDoesNotSaveAnOutcomeAfterLosingItsLease` | `void ()` | 106–111 |
| method | `legacyOrAlreadyReviewedOrdersAreNeverBackfilled` | `void ()` | 113–122 |
