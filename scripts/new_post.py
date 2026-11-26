#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interactive new post creator for the Hugo site.

Usage:
    make new
    make new NAME=my-slug

Steps:
    1. title / description
    2. category (4 simple buckets)
    3. directory (defaults by category)
    4. tags (live autocomplete against existing tags; user-entered tags
       are NOT added to the comparison pool)
"""

import os
import re
import sys
import json
import select
import subprocess
import difflib
import unicodedata
from collections import Counter

try:
    import termios
    HAS_LIVE = True
except ImportError:
    HAS_LIVE = False
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "content" / "zh" / "posts"

CATEGORIES = [
    ("技术", "tech"),
    ("商业", "marketing"),
    ("人文", "other"),
    ("其他", "other"),
]

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


# ------------------------------------------------------------------
# 实时自动补全（TTY）：每输入一个字符就与「已有标签」比较并刷新候选
# 注意：比较池只包含站点已有标签，不包含用户本次新输入的标签
# ------------------------------------------------------------------
LIVE_HINT = "↑↓ 选择 · Tab 补全 · Esc 保留新词 · Enter 确认"
LIVE_HINT_EMPTY = "没有相似的已有标签 · Enter 创建新标签"


def disp_width(text):
    w = 0
    for ch in text:
        if unicodedata.combining(ch):
            continue
        w += 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1
    return w


def live_suggestions(text, counts):
    """Return [(tag, ratio, count, note)] against existing tags only."""
    raw = (text or "").strip()
    if not raw:
        return []
    lc = raw.lower()

    # 别名 / 同义规范名（仅当规范名确实存在于已有标签中）
    canon = ALIAS.get(lc)
    note = "别名"
    if not canon:
        canon = SYNONYM.get(raw) or SYNONYM.get(lc)
        note = "规范"
    if canon and canon in counts:
        return [(canon, 1.0, counts[canon], note)]

    # 完全匹配（忽略大小写），复用已有写法
    for t in counts:
        if t.lower() == lc:
            return [(t, 1.0, counts[t], "已有")]

    if len(raw) < 2:
        return []

    scored = []
    for t in counts:
        r = similarity(raw, t)
        if r >= 0.5:
            scored.append((t, r, counts[t], "相似"))
    scored.sort(key=lambda x: (-x[1], -x[2], x[0]))
    return scored[:5]


def render_live(prompt, text, suggestions, sel, hint):
    n = len(suggestions) + 1
    sys.stdout.write("\r\033[J")
    sys.stdout.write(prompt + text)
    for i, (tag, ratio, count, note) in enumerate(suggestions):
        marker = ">" if i == sel else " "
        sys.stdout.write(
            f"\n  {marker} {i + 1}) {tag}  {DIM}{ratio:.0%} · 已有 {count} 篇{NC}"
        )
    sys.stdout.write(f"\n  {DIM}{hint}{NC}")
    sys.stdout.write(f"\033[{n}A\r")
    sys.stdout.write("\033[" + str(disp_width(prompt + text)) + "C")
    sys.stdout.flush()


def _read_char(fd):
    b = os.read(fd, 1)
    if not b:
        return ""
    first = b[0]
    if first < 0x80:
        return chr(first)
    if first >> 5 == 0b110:
        need = 1
    elif first >> 4 == 0b1110:
        need = 2
    elif first >> 3 == 0b11110:
        need = 3
    else:
        return ""
    data = b
    for _ in range(need):
        data += os.read(fd, 1)
    return data.decode("utf-8", "replace")


def read_key(fd):
    ch = _read_char(fd)
    if ch == "":
        return "EOF"
    if ch == "\x1b":
        ready, _, _ = select.select([fd], [], [], 0.03)
        if not ready:
            return "ESC"
        seq = _read_char(fd)
        if seq == "[":
            ready, _, _ = select.select([fd], [], [], 0.03)
            if not ready:
                return "ESC"
            code = _read_char(fd)
            return {"A": "UP", "B": "DOWN", "C": "RIGHT", "D": "LEFT"}.get(
                code, "ESC"
            )
        return "ESC"
    if ch in ("\r", "\n"):
        return "ENTER"
    if ch in ("\x7f", "\x08"):
        return "BACKSPACE"
    if ch == "\t":
        return "TAB"
    if ch == "\x03":
        raise KeyboardInterrupt
    if ch == "\x04":
        return "EOF"
    if ch == "\x15":
        return "CLEAR"
    return ch


def live_input(prompt, counts):
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    text = ""
    sel = -1
    deselected = False
    try:
        new = termios.tcgetattr(fd)
        new[3] &= ~(termios.ECHO | termios.ICANON)
        new[6][termios.VMIN] = 1
        new[6][termios.VTIME] = 0
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        render_live(
            prompt, text, live_suggestions(text, counts), sel, LIVE_HINT_EMPTY
        )
        while True:
            key = read_key(fd)
            if key == "EOF":
                sys.stdout.write("\r\033[J")
                sys.stdout.flush()
                return None
            if key == "ENTER":
                sugg = live_suggestions(text, counts)
                if sel >= 0 and sel < len(sugg):
                    choice = sugg[sel][0]
                else:
                    choice = text.strip()
                sys.stdout.write("\r\033[J")
                sys.stdout.write(prompt + choice + "\n")
                sys.stdout.flush()
                return choice
            if key == "BACKSPACE":
                text = text[:-1]
                sel = -1
                deselected = False
            elif key == "TAB":
                sugg = live_suggestions(text, counts)
                if sugg:
                    idx = sel if 0 <= sel < len(sugg) else 0
                    text = sugg[idx][0]
                    sel = 0
            elif key == "UP":
                sugg = live_suggestions(text, counts)
                if sugg:
                    sel = len(sugg) - 1 if sel < 0 else (sel - 1) % len(sugg)
                    deselected = False
            elif key == "DOWN":
                sugg = live_suggestions(text, counts)
                if sugg:
                    sel = 0 if sel < 0 else (sel + 1) % len(sugg)
                    deselected = False
            elif key == "ESC":
                sel = -1
                deselected = True
            elif key == "CLEAR":
                text = ""
                sel = -1
                deselected = False
            elif key in ("LEFT", "RIGHT"):
                pass
            elif key and key.isprintable():
                text += key
                sel = -1
                deselected = False

            sugg = live_suggestions(text, counts)
            if sel < 0 and sugg and not deselected:
                sel = 0
            if sel >= len(sugg):
                sel = len(sugg) - 1 if sugg else -1
            if sugg:
                hint = LIVE_HINT
            elif len(text.strip()) < 2 and text.strip():
                hint = "继续输入以匹配已有标签"
            else:
                hint = LIVE_HINT_EMPTY
            render_live(prompt, text, sugg, sel, hint)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def prompt_tags_live(counts):
    tags = []
    seen = set()
    print(f"\n{CYAN}输入标签（至少 1 个，最多 5 个）{NC}")
    while len(tags) < 5:
        tag = live_input("标签: ", counts)
        if tag is None:
            print(f"{DIM}已结束标签输入{NC}")
            break
        tag = tag.strip()
        if not tag:
            if not tags:
                print(f"{RED}至少需要一个标签{NC}")
                continue
            break
        key = tag.lower()
        if key in seen:
            print(f"{DIM}已添加过：{tag}{NC}")
            continue
        seen.add(key)
        tags.append(tag)
        print(f"{GREEN}已添加：{tag}{NC}  {DIM}({len(tags)}/5){NC}")
    return tags


def prompt_tags_plain(counts):
    print(f"\n{CYAN}输入标签（至少 1 个，最多 5 个，直接回车结束）{NC}")
    tags = []
    seen = set()
    while len(tags) < 5:
        raw = ask("标签: ")
        if not raw:
            if not tags:
                print(f"{RED}至少需要一个标签{NC}")
                continue
            break
        tag = resolve_tag(raw, counts)
        key = tag.lower()
        if key in seen:
            print(f"{DIM}已添加过：{tag}{NC}")
            continue
        seen.add(key)
        tags.append(tag)
        print(f"{GREEN}已添加：{tag}{NC}  {DIM}({len(tags)}/5){NC}")
    return tags


def choose_category():
    print(f"\n{CYAN}选择分类：{NC}")
    for i, (name, folder) in enumerate(CATEGORIES, 1):
        print(f"  {i}) {name}  {DIM}（默认目录 {folder}）{NC}")
    while True:
        raw = ask("输入序号 [1]: ", "1")
        if raw.isdigit() and 1 <= int(raw) <= len(CATEGORIES):
            return CATEGORIES[int(raw) - 1]
        print(f"{RED}请输入 1-{len(CATEGORIES)}{NC}")


def choose_dir(default):
    existing = sorted(
        d for d in os.listdir(POSTS)
        if os.path.isdir(os.path.join(POSTS, d)) and d not in ("_index",)
    )
    print(f"\n{CYAN}选择目录（留空使用默认）{NC}")
    print(f"{DIM}可用：{', '.join(existing)}{NC}")
    while True:
        raw = ask(f"目录 [{default}]: ", default)
        if re.match(r"^[A-Za-z0-9_-]+$", raw):
            return raw
        print(f"{RED}目录只能包含字母、数字、_、-{NC}")


def slugify(title):
    s = title.strip()
    s = re.sub(r"[\s_/\\]+", "-", s)
    s = re.sub(r"[^\w\u4e00-\u9fff\-]+", "", s, flags=re.UNICODE)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "post"


def main():
    os.chdir(ROOT)
    counts = load_tags()
    print(f"\n{CYAN}新建文章{NC}  {DIM}（已有 {len(counts)} 个标签）{NC}\n")

    # 1. 标题
    title = ""
    while not title:
        title = ask("文章标题: ")
        if not title:
            print(f"{RED}标题不能为空{NC}")

    # 2. 摘要
    desc = ask("摘要（可选，回车跳过）: ")

    # 3. 分类
    cat, default_dir = choose_category()

    # 4. 目录
    folder = choose_dir(default_dir)

    # 5. 文件名
    name = ""
    for arg in sys.argv[1:]:
        if arg.startswith("--name="):
            name = arg.split("=", 1)[1].strip()
    if not name:
        name = slugify(title)
    while True:
        name = ask(f"文件名（不含 .md）[{name}]: ", name).strip()
        if name.endswith(".md"):
            name = name[:-3]
        if not name or "/" in name or "\\" in name:
            print(f"{RED}文件名不合法{NC}")
            name = slugify(title)
            continue
        rel = f"content/zh/posts/{folder}/{name}/index.md"
        legacy = f"content/zh/posts/{folder}/{name}.md"
        if (ROOT / rel).exists() or (ROOT / legacy).exists():
            print(f"{RED}content/zh/posts/{folder}/{name}/ 已存在，请换一个文件名{NC}")
            name = ""
            continue
        break

    # 6. 标签（实时自动补全，仅与已有标签比较）
    if HAS_LIVE and sys.stdin.isatty() and sys.stdout.isatty():
        tags = prompt_tags_live(counts)
    else:
        tags = prompt_tags_plain(counts)

    # 7. 确认
    print(f"\n{CYAN}确认信息{NC}")
    print(f"  标题：{title}")
    print(f"  文件：content/zh/posts/{folder}/{name}/index.md")
    print(f"  分类：{cat}")
    print(f"  标签：{', '.join(tags)}")
    ans = ask("创建文章？[Y/n]: ", "y").lower()
    if ans not in ("y", "yes"):
        print("已取消")
        return 1

    # 8. 创建（使用 Hugo archetype 生成，再覆盖分类/标签/标题）
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
    if desc:
        block = set_scalar(block, "description", desc, yaml)
    else:
        cur_desc = get_scalar(block, "description")
        if cur_desc in (None, "", "<no value>"):
            block = remove_scalar(block, "description")
    block = set_arr(block, "categories", [cat], yaml)
    block = set_arr(block, "tags", tags, yaml)
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
