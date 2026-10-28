# PayPro 项目文档

> 阅读日期：2026-10-28（Asia/Shanghai）。基线提交：`1880afe`。本文档描述当前工作区源码的实际行为。

PayPro 是一个 Java 8 / Spring Boot 个人收款项目，以配置中的商品、个人收款二维码、MySQL 订单和邮件审核为核心。当前仓库能够生成支付页面、记录订单并提供审核入口；部分原有文档宣传的自动收款能力并未在本仓库实现。

## 阅读导航

| 文档 | 内容 |
| --- | --- |
| [项目概览](01-project-overview.md) | 定位、功能边界、技术栈、目录职责、依赖和版本 |
| [架构与业务流程](02-architecture-and-flows.md) | 应用启动、下单、减额匹配、审核、回调和状态流转 |
| [接口参考](03-api-reference.md) | 全部控制器路由、请求与响应、签名、回调和错误码 |
| [数据与缓存](04-data-and-cache.md) | 完整订单表、实体差异、SQL、Redis 键和一致性边界 |
| [配置与部署](05-configuration-and-deployment.md) | 配置优先级、环境变量、构建、容器、二维码和运维 |
| [前端与资源](06-frontend-and-assets.md) | 全部页面、脚本、样式、外部资源和前后端数据流 |
| [已知问题与验证](07-findings-and-validation.md) | 源码发现、文档差异、验证范围和后续修复顺序 |
| [源码符号目录](08-source-catalog.md) | 每个 Java 文件的类型、方法、字段及代码位置；自动生成 |
| [全量文件清单](09-file-inventory.md) | 原始项目全部文件的用途、大小、行数和 SHA-256；自动生成 |
| [依赖与配置目录](10-dependencies-and-config.md) | POM 全量直接依赖、插件、配置键和外部资源地址；自动生成 |
| [支付宝收款码更新](11-alipay-qr-update.md) | 本次上传原图、直接扫码模式、备注要求、验证与上线步骤 |
| [微信收款码更新](12-wechat-qr-update.md) | 微信通用码、原价付款、备注核对及历史链接兼容 |
| [网站与邮件配置](13-site-and-mail-configuration.md) | 网站品牌、收款人、客服邮箱、QQ SMTP、私密环境配置和部署 |
| [管理员邮件触发机制：实施与上线说明](01-管理员邮件触发机制/实施与上线说明.md) | 客户确认付款、通知去重、失败重试、数据库升级及验证 |
| [CodeGraph](codegraph.md) | 图谱统计、架构图、调用图、类依赖图、查询和更新方法 |

## 图谱产物

- 本地原生索引：项目根目录 `.codegraph/codegraph.db`，可用 `codegraph` CLI 查询。
- [完整节点与关系 JSON](codegraph.json)：从原生索引导出，保留节点位置、关系类型及置信度，省略可能含配置值的 docstring。
- [Java 类依赖图](codegraph-dependencies.mmd)：按项目内 `import` 生成，包含全部 Java 源文件。
- [方法调用图](codegraph-calls.mmd)：原生索引中的 `calls` 关系，属于静态推断。
- [架构图源文件](codegraph.mmd)：经源码核对的主要运行关系。
- [索引生成与检查脚本](tools/generate_project_index.py)：仅使用 Python 标准库，重建自动化目录和导出图谱。

## 范围和可信度

本轮阅读覆盖原始项目 151 个文件的清单，以及 Java、HTML、JavaScript、CSS、YAML、XML、SQL、Shell 和现有 Markdown 的结构与业务内容。二维码、图标、界面截图和内置 Compose 二进制按文件路径、格式、大小和哈希归档；没有将二维码识别为真实收款人，也没有运行该二进制。

“已实现”指源码存在相应路径，不能替代运行验证。当前使用临时 JDK 8 / Maven 完成打包、30 项后端测试和 3 项隔离 MySQL / Redis 集成测试，另有 7 项页面组件测试及桌面、手机浏览器预览。未执行真实支付、真实邮件发送或线上商户回调。原生 CodeGraph 完成静态索引；HTML 内联脚本和 Spring 动态绑定的关系由人工阅读补充，不能将静态图视为运行时追踪。

文档保留配置键和用途，不重复保存仓库中的真实地址、账号和口令。完整文件哈希可用于核对原始文件。前期阅读文档保留历史验证记录；当前已完成支付选项、收款码、品牌配置与管理员邮件触发机制修改，线上尚未部署。

## 更新

在项目根目录执行：

```powershell
codegraph index . --force --quiet
& 'D:\Work\Python\conda\python.exe' -X utf8 docs/tools/generate_project_index.py
& 'D:\Work\Python\conda\python.exe' -X utf8 docs/tools/generate_project_index.py --check
```

源码变化后，自动目录和图谱可以重新生成；业务说明和发现清单还需结合代码人工复核。
