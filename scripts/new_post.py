#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interactive new post creator for the Hugo site.

Usage:
    make new
    make new NAME=my-slug

Steps:
    1. title / description
    2. category (top 10 sections, auto-discovered directory list)
    3. directory (scanned from content/zh/posts)
    4. filename (Volcengine zh -> en translation, snake_case)
    5. tags (title-based suggestions + existing-tag autocomplete + custom)
    6. full front matter (cover, summary, keywords, series, weight,
       toc, comments, showShare, codeRunners, aliases, draft)

Optional environment variables for automatic English filenames:
    VOLCENGINE_ACCESS_KEY_ID
    VOLCENGINE_SECRET_ACCESS_KEY
    VOLCENGINE_REGION (default cn-north-1)
"""

import os
import re
import sys
import json
import subprocess
import difflib
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "content" / "zh" / "posts"

SECTION_LABELS = {
    "tech": "技术",
    "programming": "编程",
    "marketing": "商业",
    "design": "设计",
    "engineering": "工程",
    "science": "科学",
    "life": "生活",
    "notes": "笔记",
    "media": "媒体",
    "other": "其他",
}

# common abbreviations -> canonical existing tag
ALIAS = {
    "js": "JavaScript", "javascript": "JavaScript",
    "ts": "TypeScript", "typescript": "TypeScript",
    "ai": "人工智能", "ml": "机器学习", "llm": "大语言模型",
    "nlp": "自然语言处理", "cv": "计算机视觉",
    "k8s": "Kubernetes", "pg": "PostgreSQL", "mongo": "MongoDB",
    "github": "GitHub", "github actions": "GitHub Actions",
    "openwrt": "OpenWrt", "docker": "Docker",
    "vim": "Vim", "hugo": "Hugo", "hexo": "Hexo",
    "rust语言": "Rust", "go语言": "Go", "python语言": "Python",
    "c++语言": "C++", "c语言": "C语言",
    "ps": "Photoshop", "ppt": "PPT", "vscode": "VS Code",
    "pytorch": "PyTorch", "tensorflow": "TensorFlow",
    "starbucks": "星巴克", "tesla": "特斯拉", "google": "谷歌",
    "microsoft": "微软", "amazon": "亚马逊",
}

SYNONYM = {
    "消费者心理": "消费者心理学", "消费心理": "消费者心理学", "消费心理学": "消费者心理学",
    "行为经济": "行为经济学", "社会心理": "社会心理学",
    "经典案例": "案例分析", "营销案例": "案例分析",
    "品牌建设": "品牌管理", "品牌运营": "品牌管理",
    "前端": "前端开发", "后端": "后端开发", "全栈": "全栈开发",
    "性能": "性能优化", "性能调优": "性能优化",
    "网络": "计算机网络", "网络技术": "计算机网络",
    "安全": "网络安全", "信息安全": "网络安全",
    "容器化": "容器", "容器技术": "容器", "容器化部署": "容器",
    "云服务": "云计算",
    "静态网站": "静态网站生成器", "静态博客": "静态网站生成器",
    "shell脚本": "Shell", "单元测试": "测试",
    "名称": "命名", "名字": "命名", "图表": "数据可视化",
    "战略": "企业战略", "实践": "最佳实践", "茶饮": "新茶饮",
    "模拟": "模拟电路设计", "数字": "数字电路设计",
    "硬件开发": "硬件设计", "电路": "电路设计",
    "信号处理": "信号处理技术", "电力电子": "电力电子技术",
    "嵌入式": "嵌入式开发", "嵌入式系统": "嵌入式开发",
    "处理器": "处理器架构", "传感器与接口": "传感器",
    "半导体": "半导体产业", "计算机": "计算机科学",
    "航天": "航空航天", "发动机": "火箭发动机",
    "统计": "统计学", "概率": "概率论", "回归": "回归分析",
    "线代": "线性代数", "高等数学": "微积分", "贝叶斯": "贝叶斯方法",
    "心理": "心理学", "认知": "认知科学", "社会": "社会学",
    "效率提升": "效率", "时间": "时间管理", "读书": "阅读",
    "写作方法": "写作", "摄影技巧": "摄影", "旅行攻略": "旅行",
    "广告投放": "广告", "广告营销": "广告",
    "会员体系": "会员", "渠道管理": "渠道", "零售业": "零售",
    "社交媒体": "社交媒体营销", "社交": "社交媒体营销",
    "新茶饮行业": "新茶饮", "刷机": "刷机教程",
    "开源项目": "开源", "开源软件": "开源",
    "入门指南": "入门", "入门教程": "入门",
    "配置指南": "配置", "配置教程": "配置",
    "安装教程": "安装", "安装指南": "安装",
    "部署教程": "部署", "部署指南": "部署",
    "密码": "密码管理", "隐私保护": "隐私", "备份": "数据备份",
    "习惯养成": "习惯", "读书笔记": "阅读", "写作技巧": "写作",
    "健康管理": "健康", "健身计划": "健身", "睡眠质量": "睡眠",
    "美食推荐": "美食", "咖啡文化": "咖啡",
    "机器学习基础": "机器学习", "大模型": "大语言模型",
    "ui": "UI设计", "ux": "用户体验设计", "用户体验": "用户体验设计", "ui/ux": "用户体验设计",
    "交互": "交互设计", "视觉": "视觉设计", "字体": "字体设计",
    "排版": "排版设计", "配色": "配色方案",
    "定位": "品牌定位", "心智定位": "定位理论", "关联定位": "定位理论",
    "营销战略": "营销策略", "营销方法": "营销技巧",
    "社媒": "社交媒体营销", "社媒营销": "社交媒体营销",
    "私域": "私域流量", "公域": "公域流量",
    "电子商务": "电商", "供应链": "供应链管理",
    "crm": "客户关系管理", "erp": "企业资源计划",
    "关键意见领袖": "KOL", "关键意见消费者": "KOC",
    "搜索引擎优化": "SEO", "搜索引擎营销": "SEM",
    "软件即服务": "SaaS",
    "4p": "4P营销理论", "4p理论": "4P营销理论",
    "swot": "SWOT分析", "pest": "PEST分析", "stp": "STP理论",
    "定价": "定价策略", "促销": "促销策略", "促销方法": "促销策略",
    "转化": "转化率", "选品": "选品策略", "竞品": "竞品分析",
    "案例": "案例分析",
}

GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
CYAN = "\033[0;36m"
DIM = "\033[2m"
RED = "\033[0;31m"
NC = "\033[0m"


def info(msg=""):
    print(msg)


def ask(prompt, default=""):
    val = input(prompt).strip()
    return val if val else default


def split_front_matter(txt):
    m = re.match(r"^(\+\+\+|---)[ \t]*\r?\n", txt)
    if not m:
        return None
    delim = m.group(1)
    rest = txt[m.end():]
    end = re.search(r"(?m)^" + re.escape(delim) + r"[ \t]*$", rest)
    if not end:
        return None
    return delim, rest[: end.start()], rest[end.end():]


def get_arr(block, key):
    m = re.search(r"(?ms)^\s*" + key + r"\s*[:=]\s*\[(.*?)\]", block)
    if not m:
        return []
    return [x.strip().strip('"\'') for x in m.group(1).split(",") if x.strip()]


def set_arr(block, key, values, yaml=False):
    sep = ": " if yaml else " = "
    joined = ", ".join(json.dumps(v, ensure_ascii=False) for v in values)
    line = key + sep + "[" + joined + "]"
    pat = re.compile(r"(?ms)^\s*" + key + r"\s*[:=]\s*\[.*?\]")
    if pat.search(block):
        return pat.sub(line, block, count=1)
    return block.rstrip("\n") + "\n" + line + "\n"


def set_scalar(block, key, value, yaml=False):
    if yaml:
        line = key + ": " + json.dumps(value, ensure_ascii=False)
        pat = re.compile(r"(?m)^\s*" + key + r"\s*:.*$")
    else:
        line = key + " = " + json.dumps(value, ensure_ascii=False)
        pat = re.compile(r"(?m)^\s*" + key + r"\s*=.*$")
    if pat.search(block):
        return pat.sub(line, block, count=1)
    return line + "\n" + block


def get_scalar(block, key):
    m = re.search(r"(?m)^\s*" + key + r"\s*[:=]\s*(.+?)\s*$", block)
    return m.group(1).strip().strip('"\'') if m else None


def remove_scalar(block, key):
    return re.sub(r"(?m)^\s*" + key + r"\s*[:=].*\n?", "", block)


def set_raw(block, key, value, yaml=False):
    line = f"{key}: {value}" if yaml else f"{key} = {value}"
    pat = re.compile(r"(?m)^\s*" + key + r"\s*[:=].*$")
    if pat.search(block):
        return pat.sub(line, block, count=1)
    return line + "\n" + block


def read_title(path):
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return ""
    match = re.search(r'(?m)^\s*title\s*[:=]\s*["\']?(.+?)["\']?\s*$', text)
    return match.group(1).strip() if match else ""


def section_label(folder, title=""):
    if folder in SECTION_LABELS:
        return SECTION_LABELS[folder]
    return title.strip() or folder


def discover_sections():
    sections = []
    for directory in POSTS.iterdir():
        if not directory.is_dir():
            continue
        index = directory / "_index.md"
        if not index.exists():
            continue
        title = read_title(index)
        count = len(list(directory.rglob("index.md")))
        sections.append(
            {
                "folder": directory.name,
                "label": section_label(directory.name, title),
                "title": title,
                "count": count,
            }
        )
    sections.sort(key=lambda item: (-item["count"], item["folder"]))
    return sections


def label_for_folder(folder, sections, fallback):
    for section in sections:
        if section["folder"] == folder:
            return section["label"]
    return SECTION_LABELS.get(folder, fallback)


def load_tags():
    counts = Counter()
    for dp, _, fs in os.walk(POSTS):
        for f in fs:
            if not f.endswith(".md") or f.endswith("_index.md"):
                continue
            path = os.path.join(dp, f)
            try:
                txt = open(path, encoding="utf-8").read()
            except Exception:
                continue
            parts = split_front_matter(txt)
            if not parts:
                continue
            for t in get_arr(parts[1], "tags"):
                if t and t != "暂无":
                    counts[t] += 1
    return counts


def similarity(a, b):
    a = a.lower().strip()
    b = b.lower().strip()
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    ratio = difflib.SequenceMatcher(None, a, b).ratio()
    # 子串包含（如「消费心理」与「消费者心理学」）时提升相似度；
    # 单字符太容易误命中共它标签，不做子串加权
    if min(len(a), len(b)) >= 2 and (a in b or b in a):
        ratio = max(ratio, 0.85)
    return ratio


def find_suggestions(raw, counts, limit=5):
    """Return (exact_or_alias, suggestions)"""
    lc = raw.lower().strip()
    if lc in ALIAS:
        canon = ALIAS[lc]
        if canon in counts:
            return canon, []
        # alias 指向的标签还不存在时，也直接用规范名
        return canon, []
    if raw in SYNONYM:
        return SYNONYM[raw], []
    if lc in SYNONYM:
        return SYNONYM[lc], []

    best_exact = None
    for t in counts:
        if t.lower() == lc:
            best_exact = t
            break
    if best_exact:
        return best_exact, []

    scored = []
    for t in counts:
        r = similarity(raw, t)
        if r >= 0.55:
            scored.append((r, counts[t], t))
    scored.sort(key=lambda x: (-x[0], -x[1], x[2]))
    return None, scored[:limit]


def resolve_tag(raw, counts):
    exact, suggestions = find_suggestions(raw, counts)
    if exact:
        print(f"{GREEN}使用已有标签：{exact}{NC}")
        return exact

    if len(raw.strip()) < 2:
        print(f"{DIM}输入太短，将创建新标签：{raw}{NC}")
        return raw

    if not suggestions:
        print(f"{DIM}未找到相似标签，将创建新标签：{raw}{NC}")
        return raw

    best_ratio, best_count, best_tag = suggestions[0]
    if best_ratio >= 0.9:
        ans = ask(
            f"{YELLOW}最相似：{best_tag}（相似度 {best_ratio:.0%}，已有 {best_count} 篇）"
            f"\n使用它？[Y/n]: ",
            "y",
        ).lower()
        if ans in ("y", "yes", ""):
            return best_tag

    print(f"\n{YELLOW}相似标签：{NC}")
    for i, (ratio, count, tag) in enumerate(suggestions, 1):
        print(f"  {i}) {tag}  {DIM}相似度 {ratio:.0%} · 已有 {count} 篇{NC}")
    sel = ask(
        f"输入序号复用已有标签，或直接回车保留新标签「{raw}」: "
    )
    if sel.isdigit() and 1 <= int(sel) <= len(suggestions):
        tag = suggestions[int(sel) - 1][2]
        print(f"{GREEN}使用已有标签：{tag}{NC}")
        return tag
    print(f"{DIM}保留新标签：{raw}{NC}")
    return raw

def term_in_text(term, text):
    term = term.lower()
    if not term:
        return False
    if re.fullmatch(r"[a-z0-9+#.]+", term):
        pattern = r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])"
        return re.search(pattern, text) is not None
    return term in text


def suggest_tags_from_title(title, counts, limit=5):
    raw = title.lower()
    tokens = [t for t in re.split(r"[^\w\u4e00-\u9fff]+", raw) if len(t) >= 3]
    scored = {}
    for tag, count in counts.items():
        low = tag.lower()
        score = 0
        if term_in_text(low, raw):
            score = 100 + len(low) * 2
        else:
            for token in tokens:
                if len(tag) < 3:
                    continue
                ratio = similarity(token, tag)
                if ratio >= 0.85:
                    score = max(score, int(ratio * 40))
        if score:
            scored[tag] = max(scored.get(tag, (0, 0)), (score, count))
    for mapping, bonus in ((ALIAS, 20), (SYNONYM, 10)):
        for key, canonical in mapping.items():
            if term_in_text(key, raw) and canonical in counts:
                scored[canonical] = max(
                    scored.get(canonical, (0, 0)),
                    (120 + len(key) + bonus, counts[canonical]),
                )
    ranked = sorted(
        scored.items(), key=lambda item: (-item[1][0], -item[1][1], item[0])
    )
    return [tag for tag, _ in ranked[:limit]]


def add_tag(tags, seen, tag):
    key = tag.lower()
    if key in seen:
        print(f"{DIM}已添加过：{tag}{NC}")
        return
    if len(tags) >= 5:
        print(f"{YELLOW}最多 5 个标签{NC}")
        return
    tags.append(tag)
    seen.add(key)
    print(f"{GREEN}已添加：{tag}{NC}  {DIM}({len(tags)}/5){NC}")


def prompt_tags(counts, title):
    print(f"\n{CYAN}标签{NC}  {DIM}（最多 5 个，回车结束）{NC}")
    tags = []
    seen = set()
    suggested = suggest_tags_from_title(title, counts, limit=5)
    if suggested:
        print(f"{CYAN}根据标题推荐：{NC}")
        for i, tag in enumerate(suggested, 1):
            print(f"  {i}) {tag}  {DIM}已有 {counts[tag]} 篇{NC}")
        if ask("使用推荐标签？[Y/n]: ", "y").lower() in ("y", "yes", "是"):
            for tag in suggested:
                add_tag(tags, seen, tag)

    while len(tags) < 5:
        raw = ask("标签（回车结束）: ")
        if not raw:
            if not tags:
                print(f"{RED}至少需要一个标签{NC}")
                continue
            break
        add_tag(tags, seen, resolve_tag(raw, counts))
    return tags


def choose_from_all(sections):
    print(f"\n{CYAN}全部目录{NC}")
    for i, section in enumerate(sections, 1):
        print(
            f"  {i}) {section['label']}  "
            f"{DIM}（{section['folder']}，{section['count']} 篇）{NC}"
        )
    while True:
        raw = ask("输入序号: ")
        if raw.isdigit() and 1 <= int(raw) <= len(sections):
            return sections[int(raw) - 1]
        print(f"{RED}请输入 1-{len(sections)}{NC}")


def choose_category(sections):
    if not sections:
        return {"folder": "tech", "label": "技术", "count": 0}

    primary = sections[:10]
    print(f"\n{CYAN}选择分类{NC}  {DIM}（目录自动识别）{NC}")
    for i, section in enumerate(primary, 1):
        print(
            f"  {i}) {section['label']}  "
            f"{DIM}（{section['folder']}，{section['count']} 篇）{NC}"
        )

    more = len(primary) + 1
    has_more = len(sections) > len(primary)
    if has_more:
        print(f"  {more}) 更多目录...")

    limit = more if has_more else len(primary)
    while True:
        raw = ask("输入序号 [1]: ", "1")
        if raw.isdigit():
            choice = int(raw)
            if 1 <= choice <= len(primary):
                return primary[choice - 1]
            if has_more and choice == more:
                return choose_from_all(sections)
        print(f"{RED}请输入 1-{limit}{NC}")


def choose_dir(default, sections):
    existing = sorted({section["folder"] for section in sections} | {default})
    print(f"\n{CYAN}选择目录（留空使用默认）{NC}")
    print(f"{DIM}可用：{', '.join(existing)}{NC}")
    while True:
        raw = ask(f"目录 [{default}]: ", default)
        if re.match(r"^[A-Za-z0-9_-]+$", raw):
            return raw
        print(f"{RED}目录只能包含字母、数字、_、-{NC}")


def ask_int(prompt, default=0):
    while True:
        raw = ask(prompt, str(default))
        try:
            value = int(raw)
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print(f"{RED}请输入非负整数{NC}")


def ask_bool(prompt, default):
    hint = "Y/n" if default else "y/N"
    while True:
        raw = ask(f"{prompt} [{hint}]: ", "y" if default else "n").lower()
        if raw in ("y", "yes", "是", "1"):
            return True
        if raw in ("n", "no", "否", "0"):
            return False
        print(f"{RED}请输入 y 或 n{NC}")


def ask_list(prompt):
    raw = ask(prompt)
    if not raw:
        return []
    return [item.strip() for item in re.split(r"[,，、;；]", raw) if item.strip()]


def slugify(title):
    s = title.strip()
    s = re.sub(r"[\s_/\\]+", "-", s)
    s = re.sub(r"[^\w\u4e00-\u9fff\-]+", "", s, flags=re.UNICODE)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "post"


def snake_case(text):
    value = unicodedata.normalize("NFKD", text or "")
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lower()
    return re.sub(r"_+", "_", value)


def auto_slug(title):
    if re.fullmatch(r"[\x00-\x7f]+", title):
        return snake_case(title) or "post", ""
    try:
        from volc_translate import translate_text
    except Exception as exc:
        print(f"{YELLOW}自动翻译不可用：{exc}{NC}")
        return slugify(title), ""
    try:
        translated = translate_text(title, target="en", source="zh")
    except Exception as exc:
        print(f"{YELLOW}自动翻译失败：{exc}{NC}")
        return slugify(title), ""
    return snake_case(translated) or slugify(title), translated


def main():
    os.chdir(ROOT)
    counts = load_tags()
    sections = discover_sections()
    print(
        f"\n{CYAN}新建文章{NC}  "
        f"{DIM}（已有 {len(counts)} 个标签，{len(sections)} 个目录）{NC}\n"
    )

    # 1. 标题
    title = ""
    while not title:
        title = ask("文章标题: ")
        if not title:
            print(f"{RED}标题不能为空{NC}")

    # 2. 摘要
    desc = ask("摘要 description（列表卡片用，建议填写）: ")

    # 3. 分类与目录（目录自动识别）
    selected = choose_category(sections)
    folder = choose_dir(selected["folder"], sections)
    known_folders = {section["folder"] for section in sections}
    if folder in known_folders:
        category = label_for_folder(folder, sections, selected["label"])
    else:
        category = ask(f"分类名称 [{selected['label']}]: ", selected["label"])

    # 4. 文件名：火山引擎翻译为英文后转蛇形命名
    name = ""
    for arg in sys.argv[1:]:
        if arg.startswith("--name="):
            name = arg.split("=", 1)[1].strip()
    translated = ""
    if not name:
        print(f"{DIM}正在生成英文文件名...{NC}")
        name, translated = auto_slug(title)
        if translated:
            print(f"{DIM}英文标题：{translated}{NC}")
    while True:
        name = ask(f"文件名（蛇形命名，不含 .md）[{name}]: ", name).strip()
        if name.endswith(".md"):
            name = name[:-3]
        if not name or "/" in name or "\\" in name:
            print(f"{RED}文件名不合法{NC}")
            name, translated = auto_slug(title)
            continue
        rel = f"content/zh/posts/{folder}/{name}/index.md"
        legacy = f"content/zh/posts/{folder}/{name}.md"
        if (ROOT / rel).exists() or (ROOT / legacy).exists():
            print(f"{RED}content/zh/posts/{folder}/{name}/ 已存在，请换一个文件名{NC}")
            name = ""
            continue
        break

    # 5. 标签（根据标题推荐，可自定义）
    tags = prompt_tags(counts, title)

    # 6. 完整 front matter 配置
    print(f"\n{CYAN}文章配置{NC}  {DIM}（直接回车使用默认值）{NC}")
    weight = ask_int("权重 weight（>0 进首页精选）[0]: ", 0)
    cover = ask("封面 cover（绝对 URL，可选）: ")
    image = ask(
        "精选大图 image（可选，默认同 cover）: ",
        cover if weight > 0 else "",
    )
    series = ask("系列 series（可选）: ")
    summary = ask("摘要 summary（可选，精确 meta description）: ")
    keywords = ask_list("关键词 keywords（逗号分隔，可选）: ")
    toc = ask_bool("显示目录 toc", True)
    comments = ask_bool("启用评论 comments", True)
    show_share = ask_bool("显示分享 showShare", True)
    code_runners = ask_bool("代码运行按钮 codeRunners", False)
    aliases = ask_list("旧链接 aliases（逗号分隔，可选）: ")
    draft = ask_bool("保存为草稿 draft", False)

    if not desc:
        print(f"{YELLOW}建议补充 description，列表卡片和分享卡片会用到。{NC}")
    images = [cover] if cover else ([image] if image else [])

    # 7. 确认
    print(f"\n{CYAN}确认信息{NC}")
    print(f"  标题：{title}")
    print(f"  文件：content/zh/posts/{folder}/{name}/index.md")
    print(f"  分类：{category}")
    print(f"  目录：{folder}")
    print(f"  标签：{', '.join(tags)}")
    if weight:
        print(f"  权重：{weight}")
    if series:
        print(f"  系列：{series}")
    if cover:
        print(f"  封面：{cover}")
    print(
        f"  开关：toc={toc} comments={comments} "
        f"showShare={show_share} codeRunners={code_runners}"
    )
    if draft:
        print(f"  {YELLOW}草稿：true{NC}")
    ans = ask("创建文章？[Y/n]: ", "y").lower()
    if ans not in ("y", "yes", "是"):
        print("已取消")
        return 1

    # 8. 创建（使用 Hugo archetype 生成，再写入完整配置）
    rel = f"content/zh/posts/{folder}/{name}/index.md"
    try:
        res = subprocess.run(
            ["hugo", "new", rel],
            text=True,
            capture_output=True,
        )
    except FileNotFoundError:
        print(f"{RED}未找到 hugo 命令{NC}")
        return 1
    if res.returncode != 0:
        print(f"{RED}hugo new 失败：{NC}")
        print((res.stderr or res.stdout).strip())
        return 1

    path = ROOT / rel
    txt = path.read_text(encoding="utf-8")
    parts = split_front_matter(txt)
    if not parts:
        print(f"{RED}生成的文件没有 front matter，请手动检查{NC}")
        return 1
    delim, block, tail = parts
    yaml = delim == "---"
    block = set_scalar(block, "title", title, yaml)
    block = set_scalar(block, "description", desc, yaml)
    block = set_scalar(block, "summary", summary, yaml)
    block = set_scalar(block, "series", series, yaml)
    block = set_scalar(block, "cover", cover, yaml)
    block = set_scalar(block, "image", image, yaml)
    block = set_arr(block, "categories", [category], yaml)
    block = set_arr(block, "tags", tags, yaml)
    block = set_arr(block, "keywords", keywords, yaml)
    block = set_arr(block, "images", images, yaml)
    block = set_arr(block, "aliases", aliases, yaml)
    block = set_raw(block, "weight", weight, yaml)
    block = set_raw(block, "toc", str(toc).lower(), yaml)
    block = set_raw(block, "comments", str(comments).lower(), yaml)
    block = set_raw(block, "showShare", str(show_share).lower(), yaml)
    block = set_raw(block, "codeRunners", str(code_runners).lower(), yaml)
    block = set_raw(block, "draft", str(draft).lower(), yaml)
    new_txt = delim + "\n" + block.strip("\n") + "\n" + delim + tail
    path.write_text(new_txt, encoding="utf-8")

    print(f"\n{GREEN}已创建：{rel}{NC}")
    print(f"{DIM}截图后按 Paste Image 快捷键，图片会存到该目录的 images/ 并自动插入。{NC}")
    print(f"{DIM}接下来可以编辑正文，或运行 make run 预览。{NC}\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print("\n已取消")
        sys.exit(130)
