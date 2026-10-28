"""Export PayPro documentation inventories and CodeGraph using only the standard library.

Run from any working directory. Requires an existing .codegraph/codegraph.db.
No application, payment endpoint, mailbox, or database server is contacted.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sqlite3
import struct
import subprocess
from urllib.parse import unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
DB = ROOT / ".codegraph" / "codegraph.db"
SNAPSHOT_DATE = "2026-10-28"
EXCLUDED = {".git", ".codegraph", "docs", "target", "node_modules", ".idea", "applogs", "dump", "__pycache__"}
TEXT_SUFFIXES = {".java", ".html", ".js", ".css", ".xml", ".yml", ".yaml", ".md", ".sh", ".sql"}

PURPOSES = {
    "PayApplication.java": "Spring Boot 入口，开启缓存、异步、调度与 Mapper 扫描",
    "Config.java": "CORS、Thymeleaf 全局变量、分页插件与 Snowflake Bean",
    "PayProConfig.java": "paypro 配置绑定、配置商品检索、外置二维码映射",
    "RedisConfig.java": "Object RedisTemplate 与 Jackson 序列化配置",
    "OrderController.java": "订单、审核、统计、OpenAPI 和支付方式路由",
    "ProductController.java": "按 ID / 类型公开读取配置商品",
    "PageController.java": "根页与通用模板路由，支付宝页状态副作用",
    "Order.java": "订单持久化实体及邮件管理 URL 临时属性",
    "Product.java": "配置商品实体，非数据库表",
    "OrderMapper.java": "订单 BaseMapper、聚合统计、过期与实际金额查询",
    "OrderService.java": "订单业务接口",
    "ProductService.java": "商品业务接口",
    "OrderServiceImpl.java": "普通 / 外部下单、减额、审核、分页、统计与回调",
    "ProductServiceImpl.java": "YAML 商品转实体，公开接口清除下载链接",
    "OpenApiSignUtil.java": "OpenAPI MD5 签名、验签及五分钟时间戳验证",
    "ResponseVO.java": "通用 code / msg / data 响应封装",
    "ApiException.java": "业务异常与错误码常量",
    "GlobalExceptionHandler.java": "业务、参数与通用异常转换为 ResponseVO",
    "OrderStatesEnum.java": "订单状态 0 / 1 / 2 / 4 / 5",
    "WeChatMsgDTO.java": "微信消息结构，当前未接入到账业务入口",
    "MsgContentsDTO.java": "消息内容与付款方备注正则提取",
    "DateUtils.java": "日期起止、统计窗口、日期差和日期集合工具",
    "StringUtils.java": "空白检查、日期转换、Bean 转 Map、四位备注码",
    "IpInfoUtils.java": "从代理头和请求读取客户端 IP",
    "EmailUtils.java": "异步 Thymeleaf HTML 邮件与邮箱格式校验",
    "GetOrderListReq.java": "订单分页、状态、关键词与排序请求",
    "GetProductListReq.java": "商品类型列表请求",
    "OrderReq.java": "普通下单请求模型",
    "OpenApiOrderReq.java": "外部下单与签名参数模型",
    "AddOrderResp.java": "普通下单支付信息响应",
    "OpenApiOrderResp.java": "外部下单、二维码与支付页响应",
    "CountResp.java": "成功订单原价统计响应",
}
TOP_PURPOSES = {
    "README.md": "原项目介绍、开源 / 高级版说明和截图",
    "OPEN_API.md": "原 OpenAPI 说明，与当前实现存在差异",
    "一键启动说明.md": "原 Linux 部署与二维码使用说明",
    "pom.xml": "Maven 坐标、父 POM、依赖、编译与打包插件",
    "settings.xml": "Maven central 镜像配置",
    "Dockerfile": "Maven 构建 + JDK8 运行的多阶段镜像",
    "docker-compose.yml": "MySQL / Redis / pay 三服务与卷、健康检查",
    "docker-compose": "Linux x86-64 ELF Compose 可执行文件（非文本）",
    "install.sh": "Linux 一键部署与 Compose 安装",
    ".gitignore": "IDE、构建产物和本地配置排除规则",
    ".dockerignore": "排除私密环境、Git、图谱、文档与本地构建产物的 Docker 上下文规则",
    ".env.example": "QQ SMTP 授权码环境变量示例，不含真实凭据",
    ".gitattributes": "文本 LF 规则和 Compose 二进制标记",
    "获取支付宝userId.jpg": "支付宝收款用户 ID 配置辅助图片",
    "config/application-prod.yml": "外置生产配置，含部署账号与业务参数",
    "src/main/resources/application.yml": "包内基础 Spring 与 paypro 配置",
    "src/main/resources/Dockerfile": "从预构建 JAR 构建运行镜像的旧入口",
    "src/main/resources/start.sh": "容器 JVM、profile、日志与 JMX 启动参数",
    "src/main/resources/sql/pay.sql": "订单表初始化、减额迁移和索引",
    "src/main/resources/favicon.ico": "站点图标资源",
    "src/main/resources/static/css/common.css": "全站主题、布局、按钮与动画",
    "src/main/resources/static/assets/js/api-config.js": "API 基址、端点和超时配置",
    "src/main/resources/static/assets/js/http-util.js": "fetch 请求类和全局单例封装",
    "src/main/resources/static/assets/js/qcode.min.js": "第三方 qrcode@1.5.1 浏览器二维码库",
}


def md(value):
    return str(value or "").replace("|", "&#124;").replace("\r", "").replace("\n", " ")


def save(name, text):
    (DOCS / name).write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def source_files():
    try:
        output = subprocess.check_output(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT
        )
        paths = [ROOT / p.decode("utf-8") for p in output.split(b"\0") if p]
    except (subprocess.CalledProcessError, FileNotFoundError):
        paths = list(ROOT.rglob("*"))
    return sorted({p for p in paths if p.is_file() and not any(
        part in EXCLUDED for part in p.relative_to(ROOT).parts
    )}, key=lambda p: p.relative_to(ROOT).as_posix())


def purpose(path):
    rel = path.relative_to(ROOT).as_posix()
    if rel in TOP_PURPOSES:
        return TOP_PURPOSES[rel]
    if path.suffix == ".java":
        return PURPOSES.get(path.name, "Java 源文件")
    if rel.startswith("src/main/resources/templates/"):
        return "HTML / Thymeleaf 页面或邮件模板，详见前端说明"
    if rel.startswith("qr/"):
        return "运行时外置支付二维码：" + rel[3:]
    if "/assets/qr/" in rel:
        return "随 JAR 打包的支付二维码：" + rel.split("/assets/qr/", 1)[1]
    if rel.startswith("images/"):
        return "原 README 功能截图"
    if "/assets/images/" in rel:
        return "页面支付图标、备注说明或状态图片"
    return "项目辅助文件"


def file_records(paths):
    records = []
    for p in paths:
        data = p.read_bytes()
        is_text = p.suffix in TEXT_SUFFIXES or p.name in {"Dockerfile", ".gitignore", ".gitattributes", ".dockerignore", ".env.example"}
        extra = ""
        if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
            w, h = struct.unpack(">II", data[16:24])
            extra = f"PNG {w}×{h}"
        elif data.startswith(b"\x7fELF"):
            extra = "ELF 64-bit x86-64" if data[4] == 2 and data[18:20] == b">\x00" else "ELF"
        elif data.startswith(b"\xff\xd8"):
            extra = "JPEG"
        text = data.decode("utf-8-sig") if is_text else None
        records.append({
            "path": p.relative_to(ROOT).as_posix(), "bytes": len(data),
            "lines": len(text.splitlines()) if text is not None else None,
            "sha256": hashlib.sha256(data).hexdigest(), "format": extra,
            "purpose": purpose(p),
        })
    return records


def inventory(records):
    counts = Counter(Path(r["path"]).suffix or "无扩展名" for r in records)
    out = ["# 全量文件清单", "", f"项目原始文件共 **{len(records)}** 个；不包含本轮 docs 与 .codegraph 产物。",
           "", "从工作区实际内容计算 SHA-256。文本行数按 UTF-8 读取；图片 / 二进制不按文本计行。此清单不复制配置值或收款二维码内容。",
           "", "## 文件类型统计", "", "| 扩展名 | 数量 |", "| --- | ---: |"]
    out += [f"| {md(k)} | {v} |" for k, v in sorted(counts.items())]
    out += ["", "## 文件与用途", "", "| 文件 | 字节 | 行数 | 格式 / 用途 |", "| --- | ---: | ---: | --- |"]
    out += [f"| [{md(r['path'])}](../{r['path']}) | {r['bytes']} | {r['lines'] if r['lines'] is not None else '—'} | {md(r['format'] + ' ' + r['purpose'])} |" for r in records]
    out += ["", "## 文件哈希", "", "| 文件 | SHA-256 |", "| --- | --- |"]
    out += [f"| `{r['path']}` | `{r['sha256']}` |" for r in records]
    save("09-file-inventory.md", "\n".join(out))


def catalog(nodes, records):
    out = ["# Java 源码符号目录", "", "由本项目 CodeGraph 静态索引生成。列出所有 Java 文件中的类型、显式方法、字段和枚举；不包括 Lombok 运行注解处理后生成的 getter/setter。",
           "", "签名使用索引原始类型 / 参数，方法名单独列出；省略可能包含配置值的 docstring。行号对应当前工作区源码，不代表运行覆盖率。"]
    kinds = {"class", "interface", "enum", "method", "field", "enum_member", "function"}
    for record in records:
        path = record["path"]
        if not path.endswith(".java"):
            continue
        p = Path(path)
        out += ["", f"## {p.name}", "", f"[{path}](../{path}) — {PURPOSES.get(p.name, 'Java 源文件')}",
                "", "| 类别 | 名称 | 签名 / 类型 | 行号 |", "| --- | --- | --- | --- |"]
        selected = sorted((n for n in nodes if n["file_path"] == path and n["kind"] in kinds),
                          key=lambda n: (n["start_line"], n["kind"], n["name"]))
        for n in selected:
            out.append(f"| {n['kind']} | `{md(n['name'])}` | `{md(n.get('signature') or n['qualified_name'])}` | {n['start_line']}–{n['end_line']} |")
    save("08-source-catalog.md", "\n".join(out))


class ExternalAssets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = set()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"src", "href"} and value and value.startswith(("https://", "http://", "//")):
                self.urls.add((tag, value))


def config_and_dependencies(nodes):
    ns = {"m": "http://maven.apache.org/POM/4.0.0"}
    pom = ET.parse(ROOT / "pom.xml").getroot()
    out = ["# 依赖、配置键与外部资源目录", "", "本页自动读取 POM 与 CodeGraph 配置键，不解析在线依赖树，不重复账号、口令和配置值。未显式写版本的依赖由父 POM 管理。",
           "", "## Maven 直接依赖", "", "| groupId | artifactId | 声明版本 | optional / scope |", "| --- | --- | --- | --- |"]
    for d in pom.findall("m:dependencies/m:dependency", ns):
        get = lambda name: d.findtext("m:" + name, default="", namespaces=ns)
        out.append(f"| {get('groupId')} | {get('artifactId')} | {md(get('version') or '父 POM 管理')} | {md(' / '.join(filter(None, [get('optional'), get('scope')])))} |")
    out += ["", "## 构建插件", "", "| 插件 | 配置 |", "| --- | --- |"]
    for d in pom.findall("m:build/m:plugins/m:plugin", ns):
        artifact = d.findtext("m:artifactId", namespaces=ns)
        cfg = d.find("m:configuration", ns)
        values = [] if cfg is None else [f"{c.tag.split('}')[-1]}={c.text}" for c in cfg]
        out.append(f"| {artifact} | {md(', '.join(values))} |")
    out += ["", "## YAML 配置键", "", "按索引中的 YAML 常量节点列出；列表项目的同名键会在不同源码行重复出现。Compose YAML 在当前索引没有标量节点，其服务 / 环境变量已在部署文档完整列出。Java 默认属性和 YAML 未声明字段见源码符号目录。",
            "", "| 文件 | 行号 | 配置路径 |", "| --- | ---: | --- |"]
    for n in sorted((n for n in nodes if n["language"] == "yaml" and n["kind"] == "constant"), key=lambda n: (n["file_path"], n["start_line"])):
        out.append(f"| [{n['file_path']}](../{n['file_path']}) | {n['start_line']} | `{md(n['qualified_name'])}` |")
    out += ["", "## 页面外部引用", "", "只记录 HTML 标签和 CSS 中实际声明的外链，不表示已验证可用或认可站点说明。", "", "| 文件 | 标签 | URL |", "| --- | --- | --- |"]
    for p in sorted((ROOT / "src/main/resources/templates").glob("*.html")):
        parser = ExternalAssets()
        parser.feed(p.read_text(encoding="utf-8-sig"))
        for tag, url in sorted(parser.urls):
            out.append(f"| {p.name} | {tag} | `{md(url)}` |")
    css = ROOT / "src/main/resources/static/css/common.css"
    for url in sorted(set(re.findall(r"url\(['\"]?(https?://[^)'\"]+)", css.read_text(encoding="utf-8")))):
        out.append(f"| common.css | @import | `{md(url)}` |")
    save("10-dependencies-and-config.md", "\n".join(out))


def qlabel(value):
    return str(value).replace('"', "'").replace("\n", " ").replace("\r", "")


def graphs(nodes, edges, records):
    java = [r["path"] for r in records if r["path"].endswith(".java")]
    identifiers = {path: f"J{i}" for i, path in enumerate(java)}
    packages = {}
    for path in java:
        content = (ROOT / path).read_text(encoding="utf-8-sig")
        match = re.search(r"^package\s+([\w.]+)\s*;", content, re.M)
        if match:
            packages[match.group(1) + "." + Path(path).stem] = path
    dep = ["flowchart LR", "    %% Static imports only; not runtime calls."]
    dep += [f'    {identifiers[path]}["{Path(path).stem}"]' for path in java]
    for path in java:
        content = (ROOT / path).read_text(encoding="utf-8-sig")
        matches = re.findall(r"^import\s+(?:static\s+)?([\w.*]+)\s*;", content, re.M)
        targets = set()
        for imported in matches:
            if imported.endswith(".*"):
                package = imported[:-2]
                targets.update(p for key, p in packages.items() if key.rsplit(".", 1)[0] == package)
            elif imported in packages:
                targets.add(packages[imported])
        dep += [f"    {identifiers[path]} --> {identifiers[target]}" for target in sorted(targets) if target != path]
    save("codegraph-dependencies.mmd", "\n".join(dep))
    by_id = {n["id"]: n for n in nodes}
    calls = [e for e in edges if e["kind"] == "calls"]
    ids = sorted({e[key] for e in calls for key in ("source", "target")})
    call_ids = {key: f"C{i}" for i, key in enumerate(ids)}
    call_lines = ["flowchart LR", "    %% Raw CodeGraph inferred call edges; confidence is in codegraph.json."]
    for key in ids:
        n = by_id[key]
        label = qlabel(f"{Path(n['file_path']).stem}.{n['name']} L{n['start_line']}")
        call_lines.append(f'    {call_ids[key]}["{label}"]')
    call_lines += [f"    {call_ids[e['source']]} --> {call_ids[e['target']]}" for e in calls]
    save("codegraph-calls.mmd", "\n".join(call_lines))


def graph_doc(stats, files, nodes, edges):
    overview = (DOCS / "codegraph.mmd").read_text(encoding="utf-8").strip()
    java_files = sum(f["language"] == "java" for f in files)
    kinds = Counter(n["kind"] for n in nodes)
    edge_kinds = Counter(e["kind"] for e in edges)
    langs = Counter(f["language"] for f in files)
    out = ["# PayPro CodeGraph", "", f"阅读日期 {SNAPSHOT_DATE}（Asia/Shanghai）。工具版本 0.9.9；索引绑定当前项目根目录。",
           "", "## 原生索引结果", "", f"- 已索引 **{len(files)} 文件**，包含 **{java_files} Java 文件**。",
           f"- **{len(nodes)} 节点、{len(edges)} 关系**；文件解析错误数 **{stats['parse_error_files']}**。",
           f"- 原始项目 **{stats['source_files']} 文件**；HTML、CSS、SQL、Shell、Markdown、图片和二进制未全部进入原生符号索引，见全量文件清单。",
           "- 本地 SQLite：`.codegraph/codegraph.db`；该目录内自带 .gitignore 排除数据库，应通过命令重新生成。",
           "- 保留关系 metadata 的 confidence / resolvedBy；静态解析中的同名、重载、fuzzy 匹配不能等同于运行时真实调用。",
           f"- 原生 unresolved_refs 为 {stats['unresolved_refs']}；待解析引用或空表都不能证明第三方调用、框架注入和动态关系已完整解析。",
           "- 增量同步也会索引 docs/tools 中的 Python 文档生成脚本；全量 JSON 和 calls 图保留这些辅助脚本节点，Java 依赖图只包含业务 Java 文件。",
           "", "## 经源码核对的架构图", "", "```mermaid", overview, "```", "", "架构图中的 Spring 注入、资源和外部服务关系是阅读源码后的补充，并非全部来自原生边。",
           "", "## 图谱文件", "", "| 文件 | 用途 |", "| --- | --- |",
           "| [codegraph.json](codegraph.json) | 全部原生节点 / 边、文件元数据与原始文件哈希；省略 docstring、decorators 等潜在敏感配置值 |",
           "| [codegraph.mmd](codegraph.mmd) | 上方运行架构的 Mermaid 原文件 |",
           "| [codegraph-dependencies.mmd](codegraph-dependencies.mmd) | 所有 Java 文件的内部 import 依赖，通配导入保守展开，不代表每个类型都实际调用 |",
           "| [codegraph-calls.mmd](codegraph-calls.mmd) | 原生 calls 关系的 Mermaid 导出，包括可能的低置信度边 |",
           "| [源码符号目录](08-source-catalog.md) | 所有 Java 显式符号与源码位置 |",
           "", "## 节点类别", "", "| kind | 数量 |", "| --- | ---: |"]
    out += [f"| {key} | {value} |" for key, value in sorted(kinds.items())]
    out += ["", "## 关系类别", "", "| kind | 数量 |", "| --- | ---: |"]
    out += [f"| {key} | {value} |" for key, value in sorted(edge_kinds.items())]
    out += ["", "## 索引语言", "", "| 语言 | 文件数 |", "| --- | ---: |"]
    out += [f"| {key} | {value} |" for key, value in sorted(langs.items())]
    out += ["", "## 路由节点", "", "原生索引的 16 个节点，favicon 的第二个 URL 别名需以接口文档为准。", "", "| 路由 | 源码 | 行 |", "| --- | --- | ---: |"]
    for n in sorted((n for n in nodes if n["kind"] == "route"), key=lambda n: (n["file_path"], n["start_line"])):
        out.append(f"| `{md(n['name'])}` | [{Path(n['file_path']).name}](../{n['file_path']}) | {n['start_line']} |")
    out += ["", "## 查询与刷新", "", "在项目根目录执行：", "", "```powershell",
            "codegraph status .", "codegraph query OrderServiceImpl --path . --json", "codegraph callers pass --path .", "codegraph callees createOpenApiOrder --path .", "codegraph impact OrderMapper --path .",
            "codegraph index . --force --quiet", "& 'D:\\Work\\Python\\conda\\python.exe' -X utf8 docs/tools/generate_project_index.py", "& 'D:\\Work\\Python\\conda\\python.exe' -X utf8 docs/tools/generate_project_index.py --check", "```",
            "", "没有索引时先执行 `codegraph init .`。只更新索引不会自动更新人工编写的业务说明。本次 MCP 传输不可用后使用 CLI 和 SQLite 只读导出，未使用其他工作区的索引数据。",
            "", "Mermaid 代码可在支持 Mermaid 的 Markdown 编辑器中查看，或把 .mmd 导入渲染工具。原生索引不会自动生成浏览器交互界面。本次未安装图形渲染器，校验覆盖结构与文件一致性，未进行图片渲染验证。"]
    save("codegraph.md", "\n".join(out))


def load_graph():
    if not DB.is_file():
        raise SystemExit("Missing .codegraph/codegraph.db; run codegraph init . first")
    conn = sqlite3.connect(DB.resolve().as_uri() + "?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    nodes = [dict(r) for r in conn.execute("SELECT id,kind,name,qualified_name,file_path,language,start_line,end_line,start_column,end_column,signature,visibility,is_exported,is_async,is_static,is_abstract FROM nodes ORDER BY id")]
    edges = [dict(r) for r in conn.execute("SELECT * FROM edges ORDER BY id")]
    for edge in edges:
        if edge.get("metadata"):
            edge["metadata"] = json.loads(edge["metadata"])
    files = [dict(r) for r in conn.execute("SELECT * FROM files ORDER BY path")]
    return conn, files, nodes, edges


def generate():
    conn, files, nodes, edges = load_graph()
    records = file_records(source_files())
    try:
        revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        revision = None
    stats = {
        "source_files": len(records), "indexed_files": len(files), "nodes": len(nodes), "edges": len(edges),
        "parse_error_files": sum(bool(f["errors"] and f["errors"] != "[]") for f in files),
        "unresolved_refs": conn.execute("SELECT count(*) FROM unresolved_refs").fetchone()[0],
    }
    payload = {"schema": "paypro-codegraph-export-v1", "source": "CodeGraph SQLite 0.9.9",
               "snapshot_date": SNAPSHOT_DATE, "timezone": "Asia/Shanghai", "git_revision": revision,
               "limitations": ["Static inferred edges, not runtime traces", "docstring and decorators omitted to avoid copying configuration values", "HTML inline scripts are not indexed", "Wildcard Java imports conservatively expanded only in dependency Mermaid"],
               "stats": stats, "files": files, "nodes": nodes, "edges": edges, "source_inventory": records}
    save("codegraph.json", json.dumps(payload, ensure_ascii=False, indent=2))
    inventory(records)
    catalog(nodes, records)
    config_and_dependencies(nodes)
    graphs(nodes, edges, records)
    graph_doc(stats, files, nodes, edges)
    conn.close()
    print(json.dumps({"generated": True, **stats}, ensure_ascii=False, indent=2))


def check():
    conn, files, nodes, edges = load_graph()
    exported = json.loads((DOCS / "codegraph.json").read_text(encoding="utf-8"))
    errors = []
    if conn.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
        errors.append("Native SQLite integrity check failed")
    if len(exported["nodes"]) != len(nodes) or len(exported["edges"]) != len(edges):
        errors.append("Graph export counts do not match native index")
    if exported["nodes"] != nodes or exported["edges"] != edges or exported["files"] != files:
        errors.append("Graph export content differs from native index; regenerate")
    if any(f["errors"] and f["errors"] != "[]" for f in files):
        errors.append("Native parser recorded errors")
    for indexed_file in files:
        path = ROOT / indexed_file["path"]
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != indexed_file["content_hash"]:
            errors.append(f"Stale native source hash: {indexed_file['path']}; run codegraph index first")
    node_ids = {n["id"] for n in nodes}
    for e in edges:
        if e["source"] not in node_ids or e["target"] not in node_ids:
            errors.append(f"Dangling graph edge {e['id']}")
    paths = source_files()
    current_records = file_records(paths)
    if exported["source_inventory"] != current_records:
        errors.append("Source inventory or hash changed; regenerate")
    java_paths = {p.relative_to(ROOT).as_posix() for p in paths if p.suffix == ".java"}
    indexed_java = {f["path"] for f in files if f["language"] == "java"}
    if java_paths != indexed_java:
        errors.append("Native Java index does not cover every source file")
    catalog_text = (DOCS / "08-source-catalog.md").read_text(encoding="utf-8")
    for path in java_paths:
        if f"](../{path})" not in catalog_text:
            errors.append(f"Missing Java catalog entry: {path}")
    for n in nodes:
        path = ROOT / n["file_path"]
        if not path.is_file():
            errors.append(f"Missing indexed source: {n['file_path']}")
        elif n["start_line"] > len(path.read_text(encoding="utf-8-sig").splitlines()):
            errors.append(f"Invalid node line: {n['id']}")
    route_nodes = [n for n in nodes if n["kind"] == "route"]
    mapping_count = 0
    for path in (ROOT / "src/main/java/com/wendao/controller").glob("*.java"):
        text = path.read_text(encoding="utf-8-sig")
        class_match = re.search(r"\bclass\s+\w+", text)
        body = text[class_match.end():] if class_match else text
        count = len(re.findall(r"@(?:RequestMapping|GetMapping|PostMapping|PutMapping|DeleteMapping|PatchMapping)\b", body))
        mapping_count += count
    if mapping_count != len(route_nodes):
        errors.append(f"Controller handler mappings {mapping_count} != route nodes {len(route_nodes)}")
    checked_links = 0
    md_files = sorted(DOCS.glob("*.md"))
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        if "\ufffd" in text or "\x00" in text:
            errors.append(f"Invalid text encoding: {path.name}")
        if sum(line.startswith("```") for line in text.splitlines()) % 2:
            errors.append(f"Unbalanced Markdown fences: {path.name}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0].strip("<>"))
            checked_links += 1
            if not (path.parent / target).exists():
                errors.append(f"Broken local link in {path.name}: {target}")
    for p in DOCS.glob("*.mmd"):
        text = p.read_text(encoding="utf-8")
        if not text.startswith("flowchart "):
            errors.append(f"Missing Mermaid flowchart header: {p.name}")
        declared = set(re.findall(r"\b([A-Za-z][A-Za-z0-9_]*)\[", text))
        for a, b in re.findall(r"^\s+([A-Za-z][A-Za-z0-9_]*)\s+-->\s+([A-Za-z][A-Za-z0-9_]*)\s*$", text, re.M):
            if a not in declared or b not in declared:
                errors.append(f"Undefined Mermaid node in {p.name}: {a} --> {b}")
    result = {"ok": not errors, "source_files": len(paths), "java_files": len(java_paths),
              "markdown_files": len(md_files), "local_links_checked": checked_links,
              "native_index_files": len(files), "nodes": len(nodes), "edges": len(edges),
              "route_handler_methods": mapping_count, "mermaid_files": len(list(DOCS.glob('*.mmd'))), "errors": errors}
    conn.close()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate existing artifacts without rewriting them")
    args = parser.parse_args()
    check() if args.check else generate()
