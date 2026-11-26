#!/usr/bin/env python3
"""Normalize page-bundle image names and fix their Markdown links.

Usage:
    make img-rename
    make watch-images

Naming rule:
    <bundle-slug>-<original-name>
"""

import argparse
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

IMAGE_REF = re.compile(r'(?<![\w/])((?:\./)?images/)([^)\s"\']+)')
SLUG_FIELD = re.compile(r'(?m)^\s*slug\s*[:=]\s*["\']?([^"\'\n]+?)["\']?\s*$')


def bundle_slug(bundle):
    index = bundle / "index.md"
    if index.exists():
        try:
            head = index.read_text(encoding="utf-8")[:2000]
        except OSError:
            head = ""
        match = SLUG_FIELD.search(head)
        if match:
            slug = match.group(1).strip()
            if slug:
                slug = re.sub(r"\s+", "-", slug)
                slug = re.sub(r'[\\/:*?"<>|]+', "-", slug).strip("-")
                if slug:
                    return slug
    return bundle.name


def iter_bundles():
    for index in CONTENT.rglob("index.md"):
        if any(part.startswith(".") for part in index.parts):
            continue
        yield index.parent


def rename_images(bundle, slug, dry_run):
    images = bundle / "images"
    renamed = {}
    if not images.is_dir():
        return renamed
    prefix = f"{slug}-"
    for image in sorted(images.iterdir()):
        if not image.is_file() or image.name.startswith("."):
            continue
        if image.name.startswith(prefix):
            continue
        target = images / f"{prefix}{image.name}"
        if target.exists():
            print(f"跳过（目标已存在）：{target.relative_to(ROOT)}")
            continue
        action = "将重命名" if dry_run else "已重命名"
        print(f"{action}：{image.relative_to(ROOT)} -> {target.name}")
        renamed[image.name] = target.name
        if not dry_run:
            image.rename(target)
    return renamed


def fix_links(bundle, slug, dry_run, renamed):
    images = bundle / "images"
    if not images.is_dir():
        return
    existing = {p.name for p in images.iterdir() if p.is_file()}
    existing.update(renamed.values())

    def replace(match):
        prefix, name = match.group(1), match.group(2)
        if name in renamed:
            return prefix + renamed[name]
        if name in existing:
            return match.group(0)
        candidate = f"{slug}-{name}"
        if candidate in existing:
            return prefix + candidate
        return match.group(0)

    for md in bundle.rglob("*.md"):
        if any(part.startswith(".") for part in md.parts):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        updated = IMAGE_REF.sub(replace, text)
        if updated != text:
            action = "将修复链接" if dry_run else "已修复链接"
            print(f"{action}：{md.relative_to(ROOT)}")
            if not dry_run:
                md.write_text(updated, encoding="utf-8")


def process(dry_run=False):
    for bundle in sorted(iter_bundles()):
        slug = bundle_slug(bundle)
        renamed = rename_images(bundle, slug, dry_run)
        fix_links(bundle, slug, dry_run, renamed)


def watch(interval):
    print(f"监听图片目录，按 Ctrl+C 退出（间隔 {interval}s）")
    try:
        while True:
            process()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n已停止")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--watch", action="store_true")
    parser.add_argument("--interval", type=float, default=2.0)
    args = parser.parse_args()

    if args.watch:
        watch(args.interval)
    else:
        process(args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
