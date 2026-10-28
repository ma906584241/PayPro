# 接口参考

本文以控制器和模型为准，修正根目录 OPEN_API.md 中与实现不一致的内容。默认开发访问端口为 `8889`，路径均相对服务根地址。

## 返回约定

JSON 接口通常返回 `ResponseVO<T>`：

```json
{"code": 200, "msg": "success", "data": {}}
```

业务结果看 `code` 和 `msg`，不是 `success` 或 `message`。没有 `@ResponseStatus` 或显式 `ResponseEntity` 设置业务异常的 HTTP 状态，业务错误不能直接等同于 HTTP 4xx/5xx。`ResponseVO.isOk()` 是计算属性，实际 JSON 是否附带 `ok` 以 Jackson 序列化为准。

## 全部控制器路由

| HTTP | 路径 | 输入 | 输出 / 行为 | 校验 |
| --- | --- | --- | --- | --- |
| ANY | `/` | 无 | `index` 模板，随后跳 `home.html` | 无 |
| ANY | `/{page}` | 页面名；可带 `id` | 返回同名模板；`openAlipay` 会修改订单状态 | 无 |
| GET | `/favicon.ico`、`/favicon` | 无 | 空的 void 响应方法 | 无 |
| ANY，前端用 POST | `/order/list` | JSON `GetOrderListReq` | 分页订单，部分字段清空 | 无 Token 校验 |
| GET | `/order/state/{id}` | 路径 `id` | 状态整数，含按需过期判断 | 无 |
| GET | `/order/{id}` | `token` 查询参数 | 完整订单实体 | Redis Token |
| POST | `/order/add` | JSON `OrderReq` | `AddOrderResp` | `@Validated`，仅金额非 null 约束 |
| POST | `/order/edit` | 表单实体字段、`id`、`token` | 成功 / 失败 | Redis Token |
| GET | `/order/pass` | `id`、`token`、`myToken` | 成功重定向 `/success`，失败返回 `error` 模板 | Redis Token + 配置口令 |
| GET | `/order/back` | `id`、`token`、`myToken` | 设失败并可发邮件，重定向 `/success` | Redis Token + 配置口令 |
| GET | `/order/del` | `id`、`token` | 删除订单并返回 JSON | Redis Token |
| POST | `/order/statistic` | 表单 `type`、`myToken`，可选 `start/end` | `CountResp` | 配置口令 |
| POST | `/api/openapi/add` | JSON `OpenApiOrderReq` | `OpenApiOrderResp` | 必填、时间戳、MD5、金额与重复订单检查 |
| POST | `/getPayMethods` | 无 | `paypro.payMethods` 列表 | 无 |
| GET | `/product/get` | 查询 `productId`，Integer | 商品，下载地址设为 null | 无 |
| POST | `/product/getListByType` | JSON `{"types":["CODE"]}` | 商品列表，下载地址设为 null | 无 |

`ANY` 表示注解未限定 HTTP method，并不表示所有方法都能在有请求体等约束下成功调用。CodeGraph 记录 16 个 route 节点，`/favicon` 与 `/favicon.ico` 共用一个方法，但索引只建了首个别名节点。

来源：[OrderController](../src/main/java/com/wendao/controller/OrderController.java)、[ProductController](../src/main/java/com/wendao/controller/ProductController.java)、[PageController](../src/main/java/com/wendao/controller/PageController.java)。

## 普通下单

`POST /order/add`，`Content-Type: application/json`。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| money | BigDecimal | 唯一有非空校验的字段；服务没有正数、上限或商品价格复核 |
| productId | Long | 配置商品 ID |
| payType | String | 支付方式 ID；没有服务端允许列表检查 |
| nickName、description、email、userId | String | 昵称、留言、通知邮箱、外部用户标识 |
| custom、mobile | Boolean | 自定义金额、移动设备标记 |
| state | Integer | 模型默认 0，持久化方法会重设为 0 |
| payNum | String | 服务会重建或清空，不应由调用方决定 |
| createTime、updateTime | Date | 模型接受这些属性，创建时间会在持久化时重设 |
| device | String | 控制器覆盖为 User-Agent |
| time | String | 展示时间，非持久化实体字段 |

```json
{
  "money": 5.00,
  "productId": 1,
  "payType": "wechat",
  "email": "buyer@example.com",
  "nickName": "示例用户",
  "description": "示例订单",
  "custom": false
}
```

成功 data 字段：`id / money / payType / payNum / custom / payQrNum / matchMode / actualAmount / fallbackToRemark`。`payNum` 在 DECREMENT 下为 null；`custom` 在普通自定义或减额回退时为 true。必须用 `actualAmount` 展示真实待付金额，`money` 表示原始金额。

## 列表、编辑与统计

列表输入：`pageIndex=1`、`pageSize=10`、`orderBy`、`order="DESC"`、`keyword`、`states`。页面使用 `{"pageIndex":1,"pageSize":10,"states":[1]}`，响应 data 是 MyBatis-Plus 分页对象，含 `records / total / current / size / pages` 等。

列表将 `id/email` 置空，`payNum/mobile/custom/device` 置 null，其他实体字段仍可能返回。排序分支把 `order` 同时当字段名和方向使用，不能依赖其排序效果；关键词 email 与 nickName 的 OR 没有分组，可能绕过之前的状态过滤。

编辑接口是表单提交，不是 JSON。它加载当前状态并保留，用 `time` 字符串转换 `createTime`，调用 `updateById`。页面提交 `info / testEmail`，实体并没有这两个字段；有效留言字段是 `description`。

统计 `type`：

| 值 | 范围 |
| --- | --- |
| -1 | 全部成功订单 |
| 0 | 今天 |
| 6 | 昨天 |
| 1 | 本周 |
| 2 | 本月 |
| 3 | 本年 |
| 4 | 上周 |
| 5 | 上个月 |
| -2 | `start/end` 指定日期，格式 `yyyy-MM-dd`，扩展到当天开始和结束 |

结果：`amount / weixin / alipay`，均来自状态 1 的 `sum(money)`；没有 `alipayDmf` 字段。分渠道查询传入 `Wechat/Alipay`，下单一般写 `wechat/alipay`，是否匹配受数据库排序规则影响，当前初始化为大小写不敏感的 `utf8mb4_general_ci`。

## OpenAPI 下单参数

| 字段 | 类型 | 必填 / 实际行为 |
| --- | --- | --- |
| orderNo | String | 非空；直接作为订单主键 |
| amount | BigDecimal | 非 null；`0 < amount <= 100000`；未校验最多两位小数 |
| payType | String | 非空；未校验枚举、启用状态或夜间限制 |
| sign | String | 非空；与服务端大写 MD5 逐字比较 |
| timestamp | Long | 毫秒；模型未加非空注解，业务验证要求存在且在正负五分钟内 |
| nickName、description、email | String | 可选；description 参与签名但没有写入实体 |
| notifyUrl | String | 可选，但批准时直接调用此地址；未检查 URL 安全和回调响应 |
| userId | String | 可选；数据库长度 10 |
| productId | Long | 可选 |
| custom | Boolean | 可选；决定是否进入减额；**不参与签名** |
| expireSeconds | Integer | 可选；参与签名，但没有生成过期时间 |

### 签名的精确规则

[OpenApiSignUtil](../src/main/java/com/wendao/utils/OpenApiSignUtil.java) 仅取以下字段：

```text
orderNo, amount, payType, nickName, description, email,
notifyUrl, userId, productId, timestamp, expireSeconds
```

按字段名字母升序排列，跳过值为 null 和空字符串的字段；空格字符串不跳过。BigDecimal 四舍五入为两位小数并使用十进制普通字符串；其他值 `toString()`。逐项连接 `key=value&`，末尾追加 `key={secret}`，对整串做 MD5 并转大写。不执行 URL 编码、空白裁剪或路径规范化，`custom` 和 `sign` 不加入原串。

```text
amount=5.00&orderNo=EXT-DEMO-001&payType=wechat&timestamp={当前毫秒时间}&key={配置密钥}
```

请使用实时毫秒时间，而不是复制原说明中的过时时间。下面的 Python 示例显式按两位金额签名，实际调用前将占位密钥替换为本地配置：

```python
from decimal import Decimal, ROUND_HALF_UP
import hashlib, time

params = {
    "orderNo": "EXT-DEMO-001",
    "amount": "5.00",
    "payType": "wechat",
    "timestamp": int(time.time() * 1000),
}
signed = {**params, "amount": format(Decimal(params["amount"]).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP), "f")}
plain = "&".join(f"{k}={signed[k]}" for k in sorted(signed)
                 if signed[k] is not None and signed[k] != "")
params["sign"] = hashlib.md5((plain + "&key={配置密钥}").encode("utf-8")).hexdigest().upper()
```

### 成功响应字段

`orderId / orderNo / amount / payType / payNum / state / message / timestamp / qrCodeUrl / returnUrl / matchMode / actualAmount / fallbackToRemark`。

`orderId` 与 `orderNo` 当前相同。`amount` 为原价，`actualAmount` 为实际待付金额；`returnUrl` 实际指向本系统支付页，并不是商家支付成功后的跳转地址。`message` 是 OpenAPI data 内字段；外层错误说明仍是 `msg`。

### 错误码

| code | 含义 |
| --- | --- |
| 200 | 成功 |
| 400 | 参数错误或 IllegalArgumentException |
| 401 | 签名失败 |
| 402 | 时间戳无效或超窗 |
| 403 | 查询阶段发现重复订单号 |
| 404 | 业务金额错误 |
| 500 | 系统异常或字符串错误响应 |

`@Validated` 参数绑定异常没有专用异常处理，可能进入通用 500；并发重复订单在 INSERT 阶段也可能返回 500，不能保证所有重复都返回 403。

## OpenAPI 成功回调

批准来源为 OPENAPI 的订单时，`callbackFaka` 通过 `HttpUtil.post(notifyUrl, JSON字符串)` 发送以下字段：

```json
{"orderNo":"EXT-DEMO-001","amount":5.00,"payNum":"1234","sign":"{签名}"}
```

签名同一工具与密钥，只对这次回调的 `orderNo / amount / payNum` 计算；DECREMENT 下 payNum 可为 null，签名跳过 null。amount 是原价。代码没有显式设置 Content-Type，接收端需联调确认 Hutool 实际请求头；没有响应约定、确认重试、超时配置或回调幂等标识。

## 静态资源与页面入口

`/assets/**`、`/css/**` 属于静态资源；`/assets/qr/**` 有外置优先及内置回退。页面通过 `/{page}` 返回 Thymeleaf 模板；Spring 的后缀处理涉及 `.html`，部署时要验证扩展名路径。不存在原文档所述 `open-api-test.html`、`home1.html`、`payment-success.html`、`order-close.html`，不能依靠动态模板路由自动生成这些页面。
