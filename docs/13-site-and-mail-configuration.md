# 网站与邮件配置

2026-10-28，按用户提供的信息配置：

| 项目 | 当前值 |
| --- | --- |
| 网站名称 | AI智为工坊 |
| 收款人 / 品牌 | AI智为工作室 |
| 站点地址 | https://pay.aioperis.com |
| 客服邮箱 | contact@aioperis.com |
| SMTP 服务 | smtp.qq.com:465，隐式 SSL |
| 发件邮箱 | 906584241@qq.com |
| 管理员收件邮箱 | 906584241@qq.com |

基础与生产 YAML 同步更新，Compose 的站点默认值也改为真实 HTTPS 域名。网页标题、首页品牌、页脚联系邮箱、支付页收款人和邮件标题同步使用配置；页面与邮件渲染均提供 indexTitle、name、supportMail。

2026-10-29：收款人改为“AI智为工作室”。Compose 通过 `PAYPRO_NAME` 显式传入，默认使用该名称并覆盖旧 YAML；外置支付模板的升级脚本同时修复收款人配置绑定，防止恢复的旧模板继续写死个人姓名。服务器修复步骤见[线上支付页覆盖层排查](01-管理员邮件触发机制/线上支付页停留问题排查.md#2026-10-29收款人仍显示旧名称)。

## 授权码的保存方式

授权码仅保存在项目根目录 `.env` 的 MAIL_PASSWORD 中，不写入源码、本文或图谱导出。`.env` 已加入 Git 忽略，且通过 `.dockerignore` 排除在 Docker 构建上下文之外。[.env.example](../.env.example) 是不含实际授权码的示例文件。

Compose 自动读取根目录 `.env`，将 MAIL_PASSWORD 传入 pay 容器。Java 直接启动时则需要自行设置同名环境变量；Spring Boot 不会自动读取 `.env`。SMTP 使用 SSL，关闭 STARTTLS，并设置连接、读取与写入超时各 10 秒。

## 验证结果

- 到 smtp.qq.com:465 的 SSL 连接与 SMTP 登录成功，服务端认证返回 235；未执行邮件发送测试。
- `docker compose config --quiet` 通过，两个 YAML 的发件人与 SMTP 用户名一致。
- 已验证 15 个模板使用网站品牌，首页、帮助页和支付页的桌面 / 手机预览、收款人、客服 mailto 链接与布局。
- 已确认实际授权码未出现在 Git 可追踪文件中。
- 本机 Docker 构建在获取 Maven / OpenJDK 基础镜像时，被已配置镜像源的 EOF 连接错误阻断；当时没有完成 Java 构建，未修改 Docker 镜像源设置。随后在邮件机制改造中通过临时 JDK 8 / Maven 完成测试与可执行 JAR 打包；未声称 Docker 镜像构建通过。

## 上线

管理员邮件机制已改为客户主动确认后通知，详见 [管理员邮件触发机制：实施与上线说明](01-管理员邮件触发机制/实施与上线说明.md)。已有数据库必须先执行该文列出的增量迁移，再同步后端和模板。将源码、外置 config / qr 目录以及本地 `.env` 单独同步到服务器，然后在项目目录执行：

```bash
docker compose up -d --build
```

私密 `.env` 不会随 Git 提交或拉取传递。已有 `.env` 应保留其他配置，仅更新 MAIL_PASSWORD；首次安装可从 `.env.example` 创建。授权码更新后使用 `docker compose up -d pay` 让环境变量进入重新创建的容器，单纯 restart 不会更新容器环境变量。

本轮只完成本地修改与上述验证，线上尚未部署。
