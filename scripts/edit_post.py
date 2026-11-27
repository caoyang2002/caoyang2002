#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按 slug 或标题（完整/部分）查找文章并用 open 打开。

用法:
    make edit Q="tcp_ip"
    make edit Q="TCP/IP 协议"
    make edit Q="改变我人生"
    python scripts/edit_post.py --print "changed_my_life"
"""

import argparse
import difflib
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "content" / "zh" / "posts"


def normalize(text):
    text = unicodedata.normalize("NFKC", text or "").lower()
    return re.sub(r"[\W_]+", "", text)


def read_title(path):
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""
    match = re.search(r'(?m)^title\s*[:=]\s*["\']?(.+?)["\']?\s*$', text)
    return match.group(1).strip() if match else ""


def load_posts():
    posts = []
    for index in POSTS.rglob("index.md"):
        if any(part.startswith(".") for part in index.parts):
            continue
        posts.append(
            {
                "path": index,
                "slug": index.parent.name,
                "title": read_title(index),
                "section": index.parent.parent.name,
            }
        )
    return posts


def score(post, query):
    raw = query.strip().lower()
    norm = normalize(query)
    slug = post["slug"].lower()
    title = post["title"].lower()
    nslug = normalize(post["slug"])
    ntitle = normalize(post["title"])
    if not norm:
        return 0
    if raw == slug or raw == title:
        return 100
    if norm == nslug or norm == ntitle:
        return 95
    if norm in nslug:
        return 80 + len(norm) / max(len(nslug), 1)
    if norm in ntitle:
        return 80 + len(norm) / max(len(ntitle), 1)
    if raw in slug or raw in title:
        return 70
    ratio = max(
        difflib.SequenceMatcher(None, norm, nslug).ratio(),
        difflib.SequenceMatcher(None, norm, ntitle).ratio(),
    )
    return ratio * 60 if ratio >= 0.55 else 0


def pick(matches, first):
    if len(matches) == 1 or first:
        return matches[0]
    print("找到多个匹配：")
    for i, (_, post) in enumerate(matches, 1):
        print(f"  {i}) {post['title']}  [{post['section']}/{post['slug']}]")
    if not sys.stdin.isatty():
        print("非交互环境，请加 --first 或输入更精确的关键词。", file=sys.stderr)
        return None
    while True:
        raw = input(f"选择序号 [1-{len(matches)}]: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(matches):
            return matches[int(raw) - 1]
        print("请输入有效序号。")


def open_path(path):
    if sys.platform == "darwin":
        subprocess.run(["open", str(path)], check=False)
        return
    opener = shutil.which("xdg-open")
    if opener:
        subprocess.run([opener, str(path)], check=False)
        return
    print(path)


def main():
    parser = argparse.ArgumentParser(description="按 slug 或标题打开文章")
    parser.add_argument("query", nargs="?", help="slug 或标题（完整或部分）")
    parser.add_argument("--print", dest="print_only", action="store_true", help="只打印路径")
    parser.add_argument("--first", action="store_true", help="多个匹配时直接使用第一个")
    args = parser.parse_args()

    if not args.query:
        print("用法: make edit Q=\"slug 或标题片段\"", file=sys.stderr)
        return 1

    direct = Path(args.query).expanduser()
    if direct.exists():
        target = direct / "index.md" if direct.is_dir() else direct
        if args.print_only:
            print(target)
        else:
            open_path(target)
        return 0

    matches = []
    for post in load_posts():
        value = score(post, args.query)
        if value > 0:
            matches.append((value, post))
    matches.sort(key=lambda item: (-item[0], item[1]["title"]))

    if not matches:
        print(f"未找到匹配文章：{args.query}", file=sys.stderr)
        return 1

    chosen = pick(matches, args.first)
    if not chosen:
        return 1
    path = chosen[1]["path"]
    if args.print_only:
        print(path)
    else:
        open_path(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
