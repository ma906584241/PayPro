# 前端页面与静态资源

## 组织方式

前端是 15 个独立 HTML / Thymeleaf 模板，多数页面各自挂载一个 Vue 应用，不是带构建工具和客户端路由器的统一 SPA。没有 package.json、npm 构建或 Vue SFC。实际图标是 Remix Icon，样式以 common.css 和页面内 CSS 为主，未见 README 所称的 Tailwind / Font Awesome 引入。

## 全部模板

| 文件 | 用途 | 关键交互 |
| --- | --- | --- |
| index.html | 根入口跳转页 | meta refresh 到 home.html，JS 再于 100ms 后跳转 |
| home.html | 收款系统介绍与入口 | Vue 仅挂载空状态，导航到捐赠、记录、帮助 |
| recharge.html | 商品 / 自定义金额下单 | CODE 商品列表、支付方式硬编码、邮箱输入、下单后拼接支付页 URL |
| payment.html | 扫码与支付结果 | 收款码、数据库可信金额、付款声明二次确认、失败重试、2秒审核状态轮询 |
| openAlipay.html | 支付宝内收款跳转 | 解析 money/payNum/id，调用 AlipayJSBridge，生成扫码、红包和好友 URL |
| history.html | 公开成功记录 | 请求 states=[1]，分页展示；统计卡仅累计当前页 |
| help.html | 帮助 FAQ | Vue 展开 / 收起静态问答，无业务请求 |
| statistic.html | 口令保护统计 | URL 中取 myToken，jQuery POST 统计，支持自定义日期 |
| order-edit.html | 管理员编辑订单 | id/token 获取详情，jQuery 表单保存 |
| order-del.html | 管理员确认删除 | id/token 调用 GET /order/del，成功跳 /success |
| payment-review.html | 管理审核邮件 | 展示订单、通过 / 驳回 / 编辑 / 统计 / 删除链接 |
| order-success.html | 成功通知邮件 | 展示金额、方式、留言、时间；下载链接内容已注释 |
| order-fail.html | 失败通知邮件 | 展示订单和返回首页；使用不存在的 info 字段 |
| error.html | 管理错误页 | 展示控制器 errorMsg |
| success.html | 管理成功页 | 操作完成提示 |

目录：[templates](../src/main/resources/templates)。`order-success` 被 PageController 特殊拦截为 index，邮件由 TemplateEngine 直接渲染不经过页面路由。

## 共享脚本

### api-config.js

BASE_URL 选择顺序：`window.API_CUSTOM_CONFIG.BASE_URL` → URL 的 `apiBase` → localStorage 的 `API_BASE_URL` → 当前 origin → 最后写死的开发隧道地址。浏览器普通环境通常到当前 origin 就返回。TIMEOUT 为 10000ms，默认 JSON 请求头。

新增 CONFIRM_PAID `/order/confirm-paid`、PAYMENT_CONFIRMATION `/order/payment-confirmation`；其他端点为 RECHARGE `/order/add`、STATUS `/order/state`、PRODUCT_DETAIL `/product/get`、PRODUCT_LIST `/product/getListByType`、PAY_LIST `/order/list`。`/getPayMethods` 不在这些端点中，recharge 没有动态读取支付方式。

### http-util.js

`HttpUtil.request` 合并选项，对非 FormData body 做 JSON.stringify，拼接 baseURL，以 fetch 和 AbortController 实现超时；非 2xx 抛异常，按 Content-Type 返回 JSON 或文本。封装 get/post/put/delete/upload，以及全局单例和 getRequest/postRequest。

实现差异：`httpRequest` 的 DELETE 分支实际调用 get；upload 传空 headers 不一定移除构造时的 JSON Content-Type；fetch 抛错时未在 finally 清理 timeout。当前页面主要调用 GET/POST，这些辅助分支不等于经过验证的上传 / 删除能力。

### qcode.min.js

已压缩的第三方 QRCode 浏览器代码，文件头标识 qrcode@1.5.1，payment 页面使用 `QRCode.toCanvas`；不属于自研到账识别模块。

## 支付页数据与问题

2026-10-28 充值页展示更新：支付方式仅显示支付宝转账、微信支付，两份 YAML 同步移除微信赞赏码和支付宝当面付。支付卡改为原生 button，支持键盘选择、aria-pressed 与可见焦点，并使用 Remix 品牌图标。修正充值页窄屏网格、输入框和自定义金额按钮的横向溢出；1440、768、390、320px 预览检查通过。后续支付页面中的历史类型兼容逻辑不属于本次移除范围。

URL 参数：`orderId / money / payType / payNum / customerQr / picName / qrCode / payQrNum / useLocalQrCode / matchMode / actualAmount / fallbackToRemark / paymentConfirmToken`。新链接通过凭证鉴权从服务端恢复金额、渠道及付款标识；旧链接保留URL展示，但不提供付款确认按钮。

本地二维码分支顺序是 customerQr → fallbackToRemark → DECREMENT → 普通固定金额。因此回退时后端同时给 custom=true，会优先落入 custom 分支；该分支又用单引号书写 `'assets/qr/${this.orderInfo.payType}/custom.png'`，变量不会插值。正常固定价路径使用 picName，但减额路径使用 money / actualAmount 字符串，金额小数位格式不同可能导致路径错误。

当前支付宝、微信使用上传的通用收款码；带有效确认凭证的新订单在加载确认信息前不显示二维码。客户声明后停止付款倒计时并继续等待审核；未设置expireTime的新订单不创建虚构五分钟倒计时。完整交互见 [管理员邮件触发机制：实施与上线说明](01-管理员邮件触发机制/实施与上线说明.md)。

历史兼容分支的图片加载失败时回退到 custom.png，却没有设置 `dataset.retried` 标记；兜底图片也失败时可能重复触发。倒计时只改变前端状态，不发送关单请求；服务端当前也未设置 expireTime，因此前端五分钟超时不代表数据库订单结束或金额槽位释放。

非本地二维码仅对 alipay 构建跳转 URL。alipay_dmf 的 qrCode 参数虽然读取，却没有实现消费和二维码生成逻辑，不能据此完成当面付。

## 支付宝页面

AlipayJSBridge 的扫码 URL 包含收款人 ID、金额和备注；另有收款码支付、加好友后红包支付入口。这里只记录代码中的 URL 组织方式，没有验证这些第三方客户端协议当前是否仍有效。

自动状态查询默认被注释；即便手动启用，查询用 `/order/state?orderId=...`，与后端 `/{id}` 不匹配；检查 response.success 也与 ResponseVO 不一致；成功时尝试跳往不存在的 payment-success.html。

打开 `/openAlipay?id=...` 的服务端副作用是设置状态 4 并清除 `pay:*`；`/openAlipay.html` 是否走相同副作用，需结合 Spring 路径后缀处理实际验证。

## 样式与外部资源

common.css 定义深色 Slate 背景、Indigo/Violet 主色、Sky 强调色、玻璃卡片、最大宽 1200px 容器、按钮悬浮、文字渐变、6 秒浮动动画和 footer。字体从 Google Fonts 加载 Plus Jakarta Sans。部分管理页采用独立浅色样式。

Vue / Remix Icon 由 BootCDN 提供；编辑、删除、统计页从 cdnjs 引入 jQuery；支付宝页引入 alipayobjects 的 JSAPI / AntUI；成功邮件引用外链图片。完整外部引用见 [依赖与配置目录](10-dependencies-and-config.md)，该列表仅描述源码引用，没有在线访问这些站点。

静态资源分为：

- `static/assets/images`：支付类型、备注说明、成功 / 失败、站内示意图片。
- `static/assets/qr`：随 JAR 打包的二维码。
- 根 `qr`：容器挂载、运行时外置二维码。
- 根 `images`：README 中七张功能截图。
- 根 `获取支付宝userId.jpg`：收款账号配置辅助图片。
- `resources/favicon.ico`：图标资源；同时存在空 favicon 控制器方法，实际返回需运行确认。

帮助页包含费用、额度和秒到账等静态说明；这些文字不由支付渠道实时提供，本次文档没有将其作为实际渠道规则或到账保证。
