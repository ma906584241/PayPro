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

`getOrderById` 将 createTime 转成展示 time，没有处理查不到订单时的 null。`updateOrder` 设置 updateTime；`changeOrderState` 同样设置 updateTime；批准路径直接 `updateById`，没有同步设置 updateTime。

`Product` 字段：`Integer id`、`String productName`、`BigDecimal money`、`String description / extend / type / downloadUrl`。公开商品接口清除 downloadUrl，服务内部可读取完整商品；付款成功分支尚未将它交给邮件模板。

## Mapper 查询

| 方法 | 条件与结果 |
| --- | --- |
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
| `{订单id}` | UUID 形式管理员 Token | `paypro.token.expire` 天 | 普通和 OpenAPI 下单写；读详情、编辑、删除、批准和驳回校验 |
| `{客户端IP}` | `added` | `paypro.rateLimit.ipExpire` 分钟 | 普通下单只写；没有先读后拒绝请求的逻辑 |
| `pay:decrement_lock:{payType}:{baseAmount}` | `1` | 5 秒 | SET NX 减额临时锁；持有者 finally 删除 |
| `pay:*` | 非独立缓存模型 | 无统一 TTL | 打开 openAlipay 时 KEYS 获取并删除全部匹配键，会包含其他请求的锁 |
| `order` 缓存命名空间 | 声明性名称 | 未配置 | 控制器有 CacheConfig / CacheEvict，但没有 Cacheable 读缓存 |

普通 IP / 订单键没有项目命名空间，在共用 Redis DB 时存在命名冲突可能。当前业务直接注入 `StringRedisTemplate`；`RedisConfig` 另行创建 Object 类型 RedisTemplate，设置字符串 key 和 Jackson value，启用了 default typing，但当前订单路径未直接使用这个 Bean。

## 一致性与迁移

事务只覆盖数据库参与的操作；Redis、异步邮件、HTTP 回调不随 MySQL 事务回滚。下单事务完成前就可能发出异步邮件。批准外部订单先 HTTP 回调再更新本地状态：对方完成而本地更新失败会产生状态分歧；没有 Outbox、通知记录、重试队列或幂等状态机。

Compose 仅在 MySQL 数据卷首次初始化时执行挂载目录中的 SQL。已有数据卷不会因更新脚本而自动加字段。该 SQL 含 `DROP TABLE IF EXISTS`，是初始化文件，不能作为保留数据的升级迁移直接重放。增量升级应单独备份并按实际库结构执行所需 ALTER / CREATE INDEX；本次未对数据库执行任何操作。

MyBatis-Plus 配置声明 `logic-delete-field=delFlag`，实体和表都没有该字段，所以不能当作软删除机制；当前删除是 `deleteById`。
