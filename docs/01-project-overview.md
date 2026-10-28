# 项目概览

## 定位与实际功能

PayPro 面向个人开发者，当前通过微信和支付宝个人收款二维码提供收款页面。订单写入 MySQL，管理员通过邮件携带的链接审核，Redis 保存审核 Token。当前仓库的主要完成路径是人工核验到账后批准订单。

| 能力 | 当前源码情况 |
| --- | --- |
| 商品展示 | 从 `paypro.products` 加载；公开接口清除 `downloadUrl` |
| 普通下单 | `POST /order/add`，UUID 订单号，返回金额、备注和匹配模式 |
| 外部订单 | `POST /api/openapi/add`，外部订单号直接作为主键，MD5 签名与五分钟时间窗口 |
| 支付页 | 展示静态二维码，或生成跳转支付宝页面的二维码；每两秒查订单状态 |
| 减额匹配 | 分配不同实际金额并查找对应二维码；有按金额查询的方法，但没有自动到账消息入口 |
| 管理审核 | 邮件链接批准、驳回、编辑、删除；Token 和部分操作的二次口令 |
| 通知 | 新订单客户主动确认付款后异步通知管理员；审核通过后通知客户或回调 OpenAPI |
| 记录与统计 | 公开分页查询成功记录，管理员按时间统计成功订单原始金额 |
| 商品交付 | 存在 CODE 商品批准分支，但普通下单的订单来源、下载链接传递和模板显示存在缺口 |
| 微信自动确认 | 有消息 DTO 和减额查单辅助方法，没有消息接收与自动批准实现 |
| 支付宝当面付 | 有 SDK、配置字段和界面选项，没有预下单、验签通知或回调控制器 |
| 自动过期 | 有状态 5、过期字段和 Mapper；未见 `@Scheduled` 任务，下单未设置过期时间 |
| 防刷和幂等 | 记录 IP 缓存，没有入口拦截；批准缺少状态条件与幂等控制 |

事实来源：[OrderServiceImpl](../src/main/java/com/wendao/service/impl/OrderServiceImpl.java)、[OrderController](../src/main/java/com/wendao/controller/OrderController.java)、[PayProConfig](../src/main/java/com/wendao/config/PayProConfig.java)。

## 技术与版本

| 层次 | 仓库实际使用 |
| --- | --- |
| 工程 | Maven 单模块，`com.codewendao:paypro:1.0-SNAPSHOT` |
| Java | `java.version=1.8`；编译插件 source / target 均为 1.8 |
| 后端 | Spring Boot `2.3.2.RELEASE`，Spring MVC、Cache、Async、Scheduling |
| 持久化 | MyBatis-Plus `3.5.1`，Druid `1.1.4`，MySQL Connector 版本由父 POM 管理 |
| 缓存 | `spring-boot-starter-redis:1.4.7.RELEASE` 与 Boot 2.3.2 混用；需构建验证兼容性 |
| 模板与邮件 | Thymeleaf、NekoHTML `1.9.22`、Spring Mail |
| 工具 | Hutool `5.4.6`、Fastjson `2.0.23`、Lombok、Hibernate Validator `6.1.5.Final` |
| 接口注解 | Springfox Swagger UI / Swagger2 `2.7.0`；仓库没有 Docket / EnableSwagger2 配置 |
| 支付依赖 | Alipay SDK `3.7.26.ALL`；依赖存在不代表当面付已实现 |
| 前端 | 独立 HTML 页面、CDN Vue `3.3.4`、Remix Icon `3.5.0`、少数 jQuery `1.11.2` 页面 |
| 二维码 | 内置 `qcode.min.js` 文件头标明 `qrcode@1.5.1` |
| 容器 | 构建镜像 Maven `3.6.3-jdk-8`，运行镜像 OpenJDK `8u312-jdk-bullseye`，MySQL `5.7`，Redis `7-alpine` |

完整依赖见 [依赖与配置目录](10-dependencies-and-config.md)。这是仓库声明版本的记录，未进行在线版本或漏洞审计。

README 标注产品版本 `1.0.9`，SQL 的减额迁移注释写 `v2.0`，Maven 产物为 `1.0-SNAPSHOT`；这些标记分别属于说明、迁移和构建，不能视为统一发行号。

## 目录职责

```text
PayPro/
├── pom.xml / settings.xml       Maven 与中央仓库镜像配置
├── Dockerfile                   从源码构建并打包运行镜像
├── docker-compose.yml           MySQL、Redis、pay 三服务编排
├── docker-compose               Linux x86-64 ELF 二进制，不是 YAML
├── install.sh                   Linux 一键部署入口
├── config/application-prod.yml  外置生产配置
├── qr/                          外置收款二维码
├── images/                      README 功能截图
├── src/main/java/com/wendao/
│   ├── PayApplication.java       启动与扫描
│   ├── config/                  MVC、配置绑定、Redis 序列化
│   ├── controller/              页面、订单、商品入口
│   ├── service/impl/            下单、审核、减额、配置商品业务
│   ├── mapper/                  OrderMapper，订单 CRUD 和统计 SQL
│   ├── entity/                  Order / Product
│   ├── model/                   ResponseVO、请求和响应
│   ├── dto/                     微信消息结构，当前没有接收入口
│   ├── enums/                   订单状态
│   ├── exception/               业务异常与统一处理
│   ├── common/utils/            日期、字符串、IP、邮件
│   └── utils/                   OpenAPI 签名
├── src/main/resources/
│   ├── application.yml          基础配置，默认 local profile
│   ├── sql/pay.sql              建表与减额字段、索引
│   ├── templates/               15 个页面与邮件模板
│   ├── static/                  CSS、JS、图片、内置二维码
│   ├── start.sh                 容器 JVM 启动
│   └── Dockerfile               从预构建 JAR 打镜像的另一入口
└── docs/                        本轮生成的完整说明与图谱
```

原始文件逐项说明见 [全量文件清单](09-file-inventory.md)。仓库新增 `src/test/java` 后端测试和 `src/test/frontend` 页面组件测试；没有 Maven Wrapper、前端 `package.json`、CI 配置、独立 Mapper XML、登录模块或根目录 LICENSE 文件。

## 模块分工

`PageController` 选择模板；`ProductController → ProductServiceImpl → PayProConfig` 读取配置商品；`OrderController → OrderServiceImpl → OrderMapper` 处理订单。订单服务依赖 `StringRedisTemplate`、`OpenApiSignUtil`、`EmailUtils` 和资源加载器。`EmailUtils` 将对象转 Map 后渲染 Thymeleaf，再调用 SMTP。

`DateUtils` 提供统计日期窗口；`StringUtils` 提供日期、空白检查、Bean 转 Map、四位备注号；`IpInfoUtils` 读取代理头与远程地址。`WeChatMsgDTO`、`MsgContentsDTO` 没有被现有支付业务接入。
