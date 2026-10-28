# 数据模型、SQL 与 Redis

## 数据来源

数据库只有一张业务表 `t_order`，由 [pay.sql](../src/main/resources/sql/pay.sql) 初始化。商品没有数据库表或 ProductMapper，来自 YAML。MyBatis-Plus 为 `OrderMapper extends BaseMapper<Order>` 提供常规 CRUD。

## t_order 完整字段

除主键和 `match_mode` 外，DDL 字段均可为 null；`order_source` 默认 PRODUCT。

| SQL 列 | 类型 | Java 属性 / 用途 |
| --- | --- | --- |
| id | varchar(255)，主键 | String id，普通 UUID 或外部订单号 |
| create_time | datetime | Date createTime |
| custom | bit(1) | Boolean custom |
| device | varchar(1000) | String device，User-Agent |
| email | varchar(255) | String email，通知邮箱 |
| description | varchar(255) | String description，留言 |
| mobile | bit(1) | Boolean mobile |
| money | decimal(19,2) | BigDecimal money，原始金额 |
| nick_name | varchar(255) | String nickName |
| pay_num | varchar(255) | String payNum，随机备注；减额模式可空 |
| pay_type | varchar(255) | String payType |
| state | int(11) | Integer state，实际枚举 0/1/2/4/5 |
| update_time | datetime | Date updateTime |
| user_id | varchar(10) | String userId，注意长度限制 |
| product_id | bigint(10) | Long productId，未声明外键 |
| pay_qr_num | int(10) | Integer payQrNum，1..qrCodeNum |
| order_source | varchar(20)，默认 PRODUCT | String orderSource |
| notify_url | varchar(100) | String notifyUrl，较长 URL 可能超限 |
| expire_time | datetime | Date expireTime，当前下单未写入 |
| payment_confirm_token_hash | char(64)，可空 | 客户确认凭证 SHA-256，仅新订单写入 |
| payment_confirmed_at | datetime，可空 | 首次客户付款声明时间，重试不覆盖 |
| admin_notice_status | varchar(16)，可空 | NOT_REQUESTED / SENDING / SENT / FAILED |
| match_mode | varchar(20)，非空，默认 REMARK | String matchMode，REMARK / DECREMENT |
| actual_amount | decimal(19,2) | BigDecimal actualAmount，实际待付金额 |
| decrement_index | int | Integer decrementIndex，0 起槽位 |

引擎 InnoDB，字符集 utf8mb4，排序规则 utf8mb4_general_ci。脚本先 DROP/CREATE，再通过 ALTER 增加最后三个减额字段，最后创建索引：

- `PRIMARY KEY(id)`：唯一订单号。
- `idx_actual_amount_state(actual_amount,state)`：减额活跃订单和按金额查找。
- `idx_pay_num_create_time(pay_num,create_time)`：备注匹配的索引准备；当前仓库未见按备注自动确认的业务入口。

不存在减额槽位唯一索引、外键、逻辑删除列或数据库级状态约束。`Order.id` 虽标 `IdType.AUTO`，实际是字符串且表并不自增，当前创建路径主动赋值；注解与模型语义不一致。

## 非数据库属性

`Order` 的 `time`、`passUrl / backUrl / editUrl / delUrl / closeUrl / statistic`、`downloadUrl` 均为 `@TableField(exist=false)`。其中六类管理地址标了 `@JsonIgnore`，time 与 downloadUrl 没有忽略。

`getOrderById` 将 createTime 转成展示 time，没有处理查不到订单时的 null。`updateOrder` 设置 updateTime；`changeOrderState` 同样设置 updateTime；批准使用专用条件 SQL 更新状态及 update_time。新增确认元数据均为 `@JsonIgnore`，普通 `updateById` 不更新它们，由专用 SQL 维护。

`Product` 字段：`Integer id`、`String productName`、`BigDecimal money`、`String description / extend / type / downloadUrl`。公开商品接口清除 downloadUrl，服务内部可读取完整商品；付款成功分支尚未将它交给邮件模板。

## Mapper 查询

| 方法 | 条件与结果 |
| --- | --- |
| claimPaymentNotice | 客户哈希匹配、状态0/4、未过期或曾确认、尚未SENT，记录首次时间及SENDING |
| finishPaymentNotice | 仅SENDING时保存发送结果及更新时间 |
| approveOrder | 仅状态0/4原子设为1及更新时间 |
| getExpiredOrders | 指定 state；有 expire_time 且早于 now，或未指定 expire_time 且 create_time 早于传入阈值 |
| countAllMoney | 状态 1 的 sum(money) |
| countAllMoneyByType | 状态 1 + pay_type 的 sum(money) |
| countMoney | 状态 1 + create_time between 起止时间 |
| countMoneyByType | 状态 1 + pay_type + create_time between |
| getDecrementOrderByAmount | actual_amount、DECREMENT、状态 0/4、创建时间窗口，最早一条 |

`getExpiredOrders` 当前没有业务调用方；减额按金额查询未过滤 pay_type 或 expire_time。SUM 没有行时 SQL 可返回 null，不能仅凭 CountResp 字段初始值认为一定返回 0。统计口径是创建时间和原价，不是实际到账时间或实际金额。

## Redis 键

| 键 | 值 | TTL | 写入 / 使用 |
| --- | --- | --- | --- |
| `{订单id}` | UUID 形式管理员 Token | `paypro.token.expire` 天 | 新订单在客户声明后的发送任务中创建，重试复用；旧订单保留已有值；读详情、编辑、删除、批准和驳回校验 |
| `order:paid-notice:{订单id}` | 发送尝试 UUID | 120秒 | SET NX 发送锁，Lua校验归属释放；避开旧pay:*清理 |
| `{客户端IP}` | `added` | `paypro.rateLimit.ipExpire` 分钟 | 普通下单只写；没有先读后拒绝请求的逻辑 |
| `pay:decrement_lock:{payType}:{baseAmount}` | `1` | 5 秒 | SET NX 减额临时锁；持有者 finally 删除 |
| `pay:*` | 非独立缓存模型 | 无统一 TTL | 打开 openAlipay 时 KEYS 获取并删除全部匹配键，会包含其他请求的锁 |
| `order` 缓存命名空间 | 声明性名称 | 未配置 | 控制器有 CacheConfig / CacheEvict，但没有 Cacheable 读缓存 |

普通 IP / 订单键没有项目命名空间，在共用 Redis DB 时存在命名冲突可能。当前业务直接注入 `StringRedisTemplate`；`RedisConfig` 另行创建 Object 类型 RedisTemplate，设置字符串 key 和 Jackson value，启用了 default typing，但当前订单路径未直接使用这个 Bean。

## 一致性与迁移

事务只覆盖数据库参与的操作；Redis、SMTP、HTTP 回调不随 MySQL 回滚。新流程在客户声明事务提交后发邮件，数据库记录通知状态，发送失败可由客户重试；不保证SMTP与数据库跨系统恰好一次。批准使用原子状态更新，外部回调仍在事务内；对方处理成功后本地回滚仍可能产生状态分歧，没有Outbox或可靠回调重试。

Compose 仅在 MySQL 数据卷首次初始化时执行挂载目录中的 SQL。已有数据卷不会因更新脚本而自动加字段。该 SQL 含 `DROP TABLE IF EXISTS`，是初始化文件，不能作为保留数据的升级迁移直接重放。新通知流程使用独立增量脚本 [20261028_payment_confirmation.sql](../src/main/resources/sql/migrations/20261028_payment_confirmation.sql)，仅增加三个可空列、保留旧数据，先迁移再发布。已在隔离临时数据库验证，未对线上数据库执行操作。

MyBatis-Plus 配置声明 `logic-delete-field=delFlag`，实体和表都没有该字段，所以不能当作软删除机制；当前删除是 `deleteById`。
