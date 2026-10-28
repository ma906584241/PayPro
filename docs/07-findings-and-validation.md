# 已知问题、文档差异与验证范围

下表保留首次静态阅读的问题编号；其后已经修改支付展示、二维码、品牌及管理员邮件机制。当前修复状态和运行验证见文末及 [管理员邮件触发机制：实施与上线说明](01-管理员邮件触发机制/实施与上线说明.md)；未关闭的问题仍需单独处理。

## 优先核对的问题

| 编号 | 发现与影响 | 代码依据 | 建议方向 |
| --- | --- | --- | --- |
| F01 | OpenAPI 签名工具在 INFO 打印原始签名串和密钥，日志包含实际密钥 | OpenApiSignUtil.generateSign，约 47–48 行 | 删除密钥和完整原串日志，按需脱敏请求字段 |
| F02 | 普通下单已拒绝空值及非正金额，仍未复核商品价格、精度、支付方式或邮箱 | OrderReq、OrderServiceImpl.addOrder(req)，约 177 行 | 服务端依据商品算价，校验类型和允许的金额范围 |
| F03（已修复） | 来源明确为PRODUCT/OTHER；空来源旧数据及自定义金额可正常批准；商品交付仍未扩展 | OrderServiceImpl.addOrder、pass，约 185 / 288 行 | 明确订单来源和每种来源的终态处理 |
| F04 | 商品下载链接未转入订单，成功模板的下载地址还被注释，交付邮件缺失链接 | OrderServiceImpl.pass、order-success.html:48 | 用内部商品数据组装专用交付模型并恢复链接展示 |
| F05（批准已修复） | 批准以状态0/4原子更新并幂等返回；驳回、编辑和旧页面修改仍缺少完整状态约束 | OrderController.pass、OrderServiceImpl.pass | 原子状态更新、业务幂等、记录通知结果 |
| F06 | OpenAPI notifyUrl 可由调用者提供，批准时服务端直接 POST，没有地址限制、结果检查或重试 | callbackFaka，约 592 行 | 校验回调地址，定义确认协议与重试 / 幂等 |
| F07 | 减额锁失败仍继续、分配后 INSERT 前释放、无数据库唯一约束 | 两个下单方法、tryAllocateDecrementSlot | 锁覆盖查槽与提交，正确处理未获锁和锁归属，补数据库约束 |
| F08 | 活跃金额查询未按渠道、原价或过期时间隔离；两个渠道相同金额可能互相占槽 | tryAllocateDecrementSlot、getOccupiedDecrementSlots、OrderMapper | 依据完整业务维度查询，并释放终态 / 过期槽位 |
| F09 | 减额二维码检查仅查 classpath，外置新增金额不生效；只要任一编号存在就可能随机到缺失编号 | checkAnyQrFileExists、随机 payQrNum | 统一资源查找并从可用编号集合选取 |
| F10 | OpenAPI 普通备注二维码存在判断反向：不存在返回固定路径，存在反而返回 custom | createOpenApiOrder，约 475–482 行 | 修正判断，分别验证固定、自定义、缺失场景 |
| F11 | payment 自定义二维码字符串不插值；回退状态 custom=true 又抢先进入该分支 | payment.html:212–219 | 使用模板字符串并明确回退分支优先级 |
| F12 | payment 图片错误处理未设置 retried，兜底丢失可能重复触发 | payment.html:272–279 | 设置重试标记并提供终止错误状态 |
| F13 | expireSeconds / timeoutMinutes 未用于创建 expireTime，也没有定时过期任务 | createOpenApiOrder、PayProConfig.Order | 创建时设到期时间，并实现终态受限的过期任务 |
| F14（已修复） | 查询仅过期未声明的状态0/4，已成功和已声明待审核订单保留原状态 | OrderController.getOrderState:75–83 | 仅待处理状态过期，返回实际终态 |
| F15 | 无 Token 的 openAlipay 页面入口可改任意订单为 4，并删除全部 pay:*，可能干扰终态和其他锁 | PageController.showPage:47–52 | 授权并约束状态迁移，缩小清理键范围 |
| F16 | order/list 无鉴权，脱敏只覆盖部分字段；关键词 OR 未分组，可能越过状态条件 | OrderController.getOrderList、OrderServiceImpl.list | 用公开响应模型、限制状态、分组关键词条件 |
| F17 | 排序逻辑比较错字段，默认方向大写也与 desc 比较不同 | OrderServiceImpl.list:312–327 | 分开处理 orderBy 与 order，做允许列表映射 |
| F18 | Token 和二次口令出现在 GET URL 中，管理操作使用 GET；缺少统一登录授权层 | getAdminUrl、Controller pass/back/del | 收拢管理会话与写操作接口，减少 URL 凭证传播 |
| F19 | IP 缓存只写不读；配置 ipExpire 不构成限流 | addOrder:262 | 实现入口原子检查或移除误导配置 |
| F20 | OpenAPI custom 不签名却改变金额匹配路径；description/expireSeconds 签名后未落实实体行为 | verifySign、createOpenApiOrder | 对实际业务参数统一签名、验证和落库 |
| F21（部分修复） | 下单已移除发信；客户声明提交后异步通知并记录结果；SMTP跨系统恰好一次、OpenAPI可靠回调仍未实现 | addOrder、createOpenApiOrder、pass | 提交后通知或事务消息 / Outbox |
| F22 | 编辑页 info/testEmail、部分页面 data.message、支付宝查询 response.success 不匹配后端模型 | order-edit、order-del、recharge、openAlipay | 统一 description、msg、code 约定 |
| F23 | 前端支付方式硬编码，后端也未执行 status/allowNight 限制 | recharge.html、getPayMethods、下单服务 | 前端加载配置，后端强制校验 |
| F24 | CORS 任意来源并允许 credentials；Redis ObjectMapper 启用 default typing | Config.addCorsMappings、RedisConfig | 按实际部署收紧来源和反序列化类型；Object RedisTemplate 当前非订单主路径 |
| F25 | 基础 YAML / Compose 有固定账号与口令；JMX 关闭认证/SSL；构建依赖跨 Boot 版本 | application.yml、docker-compose.yml、start.sh、pom.xml | 统一外部配置并验证依赖与监听面；本文未做在线漏洞审计 |

上述文件均可在 [源码符号目录](08-source-catalog.md) 找到准确起止行。优先级建议：F01–F06 与 F14–F18 先核对对账、授权和交付；接着处理 F07–F13 的并发、二维码和过期；再完善接口一致性、配置与可维护性。

## 与原有说明的差异

| 原说明 | 当前仓库事实 |
| --- | --- |
| 包含微信自动确认和支付宝当面付 | README 功能对比将这些列为高级版；本仓库未见完整实现 |
| Vue 单页应用、组件化前端 | 多独立 HTML + 页面内 Vue，无构建和路由器 |
| Tailwind、Font Awesome | 实际 common.css、自定义 CSS、Remix Icon |
| 产品表 / 数据库商品 | 商品来自 paypro.products，只有订单表 |
| 项目结构中的 db.sql、src/test、home1.html | 实际 sql/pay.sql，当前已新增src/test；仍无db.sql或home1.html |
| OpenAPI 支持 expireSeconds 自动过期 | 参数参与签名但未设置 expireTime |
| 状态包含 3、未写 5 | 实际枚举没有 3，包含 5 |
| returnUrl 为支付完成返回地址 | 实际返回本系统 payment.html 地址 |
| open-api-test.html 测试页 | 仓库没有该页面 |
| 任意外置二维码都能覆盖内置并参与业务 | 展示层有回退，减额存在检测只查内置 |
| 所有服务应为 healthy | pay 没有 healthcheck，只有 mysql/redis 有 |
| 原 README 示例数据库 paypro、8080、mail.* | 实际 Compose 库 pay，端口 8889，邮件为 spring.mail.* 与 paypro.email.* |

## 首次项目阅读验证（支付选项精简前）

- 原始 Git 工作区开始时无未提交变更；原始项目文件为 151 个。
- 阅读 32 个 Java 文件、15 个 HTML 模板及配置、SQL、脚本、样式、原有说明；二进制和图片按清单、格式和哈希登记。
- 执行本机 `codegraph 0.9.9 init .`，建立项目专属 SQLite 索引，40 文件、914 节点、1381 关系；初始索引无文件解析错误。
- 初次无 projectPath 的 MCP 状态查询指向另一项目，未使用该数据；显式查询确认本项目未初始化后，在当前目录创建。随后 MCP transport 关闭，后续使用本地 CLI 和 SQLite 只读导出。
- 自动化检查通过：151 个原始文件哈希、32 个 Java 文件覆盖、40 个原生索引文件哈希、914 个节点与 1381 条边的导出一致性、16 个控制器方法路由、386 个 Markdown 本地文件链接、Markdown 围栏、3 个 Mermaid 源文件结构和 SQLite 完整性。脚本退出码 0，错误列表为空；图谱统计见 [CodeGraph](codegraph.md)。
- 本机 PATH 未发现 java/mvn，没有 Maven 编译、单元测试、服务启动、数据库连接、支付、邮件、回调或第三方协议联调；没有把这些静态检查称为运行通过。

首次阅读时仓库没有自动化测试和 CI；当前已新增测试，仍无 CI。后续修复应继续覆盖金额与签名、三种二维码模式、并发槽位、重复审核、过期终态、商品交付和回调失败等业务断言，而非只验证方法存在。

## 支付选项精简验证（2026-10-28）

充值页与基础、生产配置仅保留支付宝和微信支付。Playwright 本地预览验证两项均可点击和键盘切换、aria-pressed 与订单摘要一致；自定义金额 12 元选择微信后，提交参数为 money=12、payType=wechat、custom=true。1440、768、390、320px 宽度均无横向溢出，桌面和手机截图已目视核对。预览商品及下单接口为本地模拟，不会创建真实订单；线上代码未部署。原生 CodeGraph 和自动化文档已同步，当前统计以 codegraph.md 为准。

## 管理员邮件机制变更验证（2026-10-28）

当前已经完成30项JUnit测试、3项隔离MySQL8/Redis7集成测试、7项页面组件测试及JDK8/Maven可执行JAR打包。真实浏览器1440px桌面、390px微信手机页验证：打开/刷新/取消零提交；主动确认一次；刷新恢复等待审核；发送失败可重试；旧链接无按钮，无效凭证禁用按钮并隐藏二维码；无横向溢出。截图已目视核对。预览接口为本地模拟，未连接真实邮箱或支付渠道。

界面静态检测因缺少HTML解析依赖降级为正则，不能据此声称已完整验证对比度或所有可访问性规则。数据库迁移、并发锁与持久去重由独立集成测试验证；生产MySQL5.7未实际联调。详细上线步骤见 [管理员邮件触发机制：实施与上线说明](01-管理员邮件触发机制/实施与上线说明.md)。
