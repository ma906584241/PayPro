# 配置、构建与部署

## 配置文件与生效路径

| 文件 | 用途 |
| --- | --- |
| `src/main/resources/application.yml` | 包内基础配置；默认激活 local；端口 8889 |
| `src/main/resources/application-local.yml` | .gitignore 声明排除，但仓库没有此文件 |
| `config/application-prod.yml` | 外置生产配置；Compose 激活 prod 后加载 |
| `docker-compose.yml` | 容器环境变量、端口、目录与服务依赖 |
| `src/main/resources/start.sh` | 将 SERVER_PORT / SPRING_PROFILES 转为 JVM 启动参数 |

在本项目常规启动方式下，命令行参数和 Spring 直接环境属性能够覆盖 YAML；外置 profile 配置覆盖包内基础配置。`start.sh` 把 `/app/appsystems/config/` 放入 classpath，并在非空时传 `--spring.profiles.active=${SPRING_PROFILES}`。直接 Java 启动时，`SPRING_PROFILES` 并非标准激活属性；需用 `--spring.profiles.active` 或 `SPRING_PROFILES_ACTIVE`。

基础和生产 YAML 的 `paypro.site` 均读取 SITE_URL，默认 https://pay.aioperis.com；Compose 使用相同默认值。邮件配置从项目根目录 Git 忽略的 `.env` 读取 MAIL_PASSWORD 后传入容器，详见 [网站与邮件配置](13-site-and-mail-configuration.md)。

完整配置键清单见 [依赖与配置目录](10-dependencies-and-config.md)。以下解释关键业务配置，不重复实际账号、IP 和口令。

## paypro 配置

| 属性 | 用途 / 当前状态 |
| --- | --- |
| title、indexTitle | 邮件 / 页面标题，注入模板全局变量 |
| site | 支付页和管理邮件链接的服务根地址；应与真实可访问地址一致 |
| alipayUserId、alipayCustomQrUrl、mobile | 支付宝跳转收款参数；传入模板 |
| name | 收款人名称，当前为马宵冉；页面和邮件均注入此变量 |
| email.sender、email.receiver | 管理审核邮件发件人与收件人，需与 SMTP 账户匹配 |
| supportMail | 客服邮箱，当前为 contact@aioperis.com；帮助页与页脚显示邮件链接 |
| token.value | 管理操作的二次口令，不是 Redis 每单随机 Token |
| token.expire | 每单随机管理员 Token 有效天数，YAML 为 14 |
| rateLimit.ipExpire | IP 写缓存时长，实际单位分钟；基础 YAML 2，生产 YAML 1；没有限流读取 |
| qr-dir | 外置二维码目录；容器内默认 `/app/appsystems/qr` |
| qrCodeNum | 1 起随机二维码编号上限，YAML 为 2；需要完整提供编号 |
| decrement.enabled | Java 默认 false，当前两个 YAML 均为 false；支付宝、微信使用通用码与备注核对 |
| decrement.maxCount | Java 默认 5，YAML 为 2；包含槽位 0 后总候选数为 N+1 |
| decrement.step | Java / YAML 为 0.01，递减和回退金额步长 |
| order.timeoutMinutes | Java 默认 30；YAML 未提供，当前没有周期任务消费 |
| openapi.secret | 外部下单与成功回调签名共享密钥，OpenApiSignUtil 用 @Value 读取 |
| products | 商品列表，含 id/product-name/money/description/type/extend/download-url |
| payMethods | 支付方式列表，含 id/name/description/icon/status/allow-night/use-local-qr-code |
| downloadUrl | 全局 Java 属性存在，当前未消费；商品专属 download-url 在 products 中 |
| alipayDmfAppId / AppPrivateKey / PublicKey / Subject | Java 字段存在，未形成实际当面付集成 |

当前基础和生产配置、充值页面均只保留 `alipay`、`wechat`。微信赞赏码和支付宝当面付已移出展示及配置列表，历史订单的类型标记仍保留。支付方式的 `status / allow-night` 当前没有在下单服务强制执行；`use-local-qr-code` 实际影响减额分支。前端仍硬编码支付方式，修改 YAML 不等于修改用户看到的可选方式。

示例配置使用占位符，不能直接视为可用生产配置：

```yaml
paypro:
  site: https://pay.example.com
  qr-dir: /app/appsystems/qr
  token:
    value: ${PAYPRO_ADMIN_SECRET}
    expire: 14
  openapi:
    secret: ${PAYPRO_OPENAPI_SECRET}
  products:
    - id: 1
      product-name: 示例产品
      money: "5.00"
      type: CODE
      description: 示例说明
      extend: ""
      download-url: https://downloads.example.com/example.zip
```

## 环境变量

| 名称 | 读取位置 / 行为 |
| --- | --- |
| SERVER_PORT | application.yml 默认 8889；start.sh 转启动参数 |
| SPRING_PROFILES | 仅 start.sh 读取，Compose 设 prod |
| DB_URL、DB_USERNAME、DB_PASSWORD | datasource 占位符；Compose 指向 mysql 服务的 pay 库 |
| REDIS_HOST、REDIS_PORT、REDIS_DB | Redis 占位符；默认 loopback/6379/1 |
| REDIS_PASSWORD | Compose 设置，但 application.yml 没有引用这个名称 |
| SPRING_REDIS_PASSWORD | Compose 同时设置，通过 Spring 属性绑定提供实际 Redis 密码 |
| SITE_URL | 基础与生产 paypro.site 均读取此变量，默认站点实际 HTTPS 地址 |
| MAIL_PASSWORD | 从本地私密 .env 传入容器的 QQ SMTP 授权码；Compose 要求非空 |
| JVM_HEAP_SIZE | start.sh JVM 内存参数替换，默认 Xms/Xmx 1024M、Xmn 256M |
| SERVICE_NAME | start.sh 写入 SkyWalking agent name 属性，Compose 未设置 |
| HOSTNAME、JAVA_HOME | 容器或系统环境，由 start.sh 读取 |

`PAYPRO_SITE`、`SPRING_DATASOURCE_URL` 等标准 Spring 属性环境变量也可用于直接覆盖对应属性。包内基础数据库地址是远程地址且含默认口令，直接本地启动前要明确配置本地数据库；本文不复制这些值。

## 源码构建与本地运行

仓库指定 Java 8；start.sh 使用 CMS 与 Java 8 参数，不能认为所有更高 JDK 均可直接运行。项目没有 Maven Wrapper。

```powershell
# 在项目根目录，先准备可用 JDK 8、Maven、MySQL 与 Redis
mvn -s settings.xml clean package -DskipTests

# 明确指定自己的数据库和 Redis，不使用包内远程默认配置
$env:DB_URL = 'jdbc:mysql://127.0.0.1:3306/pay?useSSL=false&characterEncoding=utf-8&serverTimezone=GMT%2B8'
$env:DB_USERNAME = 'pay_user'
$env:DB_PASSWORD = '{本地数据库口令}'
$env:REDIS_HOST = '127.0.0.1'
$env:REDIS_PORT = '6379'
$env:SPRING_REDIS_PASSWORD = '{本地Redis口令}'
$env:PAYPRO_SITE = 'http://localhost:8889'
java -jar target/paypro-1.0-SNAPSHOT.jar --spring.profiles.active=prod --paypro.qr-dir=./qr
```

MySQL 必须已创建库并按实际情况初始化表。`settings.xml` 把 central 镜像指向阿里云仓库；根 Dockerfile 会自动复制它，本地构建只有加 `-s settings.xml` 才显式使用项目设置。

## Docker 部署

根 Dockerfile 有两个阶段：先拷贝 pom/src 并运行 `mvn package -DskipTests -B -q`，再将 JAR 和 start.sh 放入 Java 8 镜像。资源目录下的另一份 Dockerfile 直接 `COPY *.jar`，需要预构建产物和不同的构建上下文，不是 Compose 的默认入口。

| 服务 | 镜像 / 构建 | 发布端口 | 持久化 | 启动条件 |
| --- | --- | --- | --- | --- |
| mysql / pay-mysql | mysql:5.7 | 3306:3306 | mysql-data；SQL 初始化目录 | mysqladmin ping 健康检查 |
| redis / pay-redis | redis:7-alpine | 6379:6379 | redis-data:/data | 带密码 redis-cli ping |
| pay | build: .，pay:latest | 8889:8889 | config、qr、applogs、dump 绑定 | mysql/redis healthy |

网络为 `pay-network` bridge，所有容器 `restart: always`。pay 服务没有 healthcheck，所以不能要求三个服务都显示 healthy；应用就绪还需查看日志及 HTTP 响应。MySQL / Redis 密码出现在 Compose 环境、命令或健康检查中，更换时须同步修改所有引用。

目录映射：`./config → /app/appsystems/config`；`./qr → /app/appsystems/qr`；`./applogs → /app/applogs`；`./dump → /app/applogs/dump`。Redis 只显式挂载数据目录，没有额外配置 AOF 或快照策略。

Linux 部署命令：

```bash
bash install.sh
# 或已有 Compose 时
docker compose up -d --build
docker compose ps
docker compose logs --tail 100 pay
```

`install.sh` 检查 Docker 和访问权限，优先使用现有 Compose；否则把仓库的 Linux ELF 二进制安装到 Docker CLI 插件目录，必要时降级为 `/usr/local/bin/docker-compose`。它创建 config/qr/applogs/dump；缺失生产配置时生成最小模板并退出，已有模板不会检查其中账号是否可用。脚本成功只表示 Compose 启动命令成功，不代表真实支付和邮件正常。

## 二维码目录

```text
qr/
├── alipay/custom.png
├── wechat_zs/custom.png
└── wechat/
    ├── custom.png
    └── 5.00/
        ├── 1.png
        ├── 2.png
        ├── 4.99/1.png、2.png
        ├── 4.98/1.png、2.png
        └── 5.01/1.png、2.png
```

HTTP 资源映射外置优先、classpath 回退；但减额槽位的二维码存在检测仍只查 classpath。因此“外部覆盖内置”在文件展示层成立，不能直接推广到所有业务检查。根 qr 与内置二维码集合不完全相同，全量路径和哈希见文件清单。

## 日常维护与诊断

```bash
docker compose logs -f pay
docker compose restart pay              # 修改外置 YAML 后
docker compose up -d --build             # 修改源码后
docker compose down                     # 停服务，保留命名数据卷
```

仓库没有实现数据备份命令，应备份 MySQL 数据、生产配置与收款二维码。原说明中的 `docker compose down -v` 会删除命名数据卷，不属于保留数据的重启方式。

启动脚本输出 GC 日志到 `/app/applogs/gc.log`，OOM dump 到 `/app/applogs/dump/start-{时间}.hprof`。脚本配置了 JMX 30005 且关闭认证/SSL，Compose 未发布此端口；扩展部署时需核对实际网络暴露。SkyWalking 仅设置系统属性，没有加载 `-javaagent`，不能据此认定监控已接通。

排查顺序：构建日志 → mysql/redis 健康 → pay 启动日志与配置 → 站点 HTTP → 商品接口 → 二维码路径 → SMTP → 审核与回调。当前环境缺少 java/mvn，以上命令为部署说明，未在本轮实际执行。
