# ==========================================================
# Hugo 站点工具集 Makefile
# 布局: 本 Makefile 在仓库根目录，辅助脚本在 scripts/
# 用法: make <target> [VAR=value ...]
# 注意: 脚本会自动切换到仓库根目录，相对路径均以仓库根目录为基准
# ==========================================================

SHELL := /bin/bash
.DEFAULT_GOAL := help

# ---------- 脚本路径（相对仓库根目录） ----------
SCRIPTS     := scripts
UPDATE_SH   := $(SCRIPTS)/update.sh
RUN_SH      := $(SCRIPTS)/RUN.sh
CREATE_SH   := $(SCRIPTS)/create.sh
GENKEY_SH   := $(SCRIPTS)/generate-key.sh
TENCLOUD_PY := $(SCRIPTS)/tencloud.py
TRANSFER_PY := $(SCRIPTS)/transfer.py
PUSH_PY     := $(SCRIPTS)/push_all.py
MDIMG_PY    := $(SCRIPTS)/md_image_downloader.py
IMG_CONFIG  := $(SCRIPTS)/hugo_image_config.json
PYTHON      ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)

# ---------- 可选参数（make VAR=value 传入） ----------
NAME     ?=
YEAR     ?=
MONTH    ?=
DAY      ?=
MD       ?=
TXT      ?=
SLUG     ?=
STORAGE  ?=
PREFIX   ?=
FILE     ?=
AI_URL   ?=

# ==========================================================
# 帮助
# ==========================================================
.PHONY: help
help:
	@printf '\n'
	@printf '  Hugo 站点工具集 Makefile（脚本位于 %s/）\n' "$(SCRIPTS)"
	@printf '  ───────────────────────────────────────────────────────\n'
	@printf '  make deploy              备份 + 构建 + 推送（CI 自动发布）\n'
	@printf '  make build               本地生产构建 (hugo --minify)\n'
	@printf '  make run                 开发服务器 (RUN.sh, hugo server -D)\n'
	@printf '  make dev                 开发服务器 (update.sh --dev, 0.0.0.0:1313)\n'
	@printf '  make git                 仅提交并推送\n'
	@printf '  make backup              仅创建备份\n'
	@printf '  make clean               清理旧的备份和日志\n'
	@printf '  make check               依赖 + 健康检查\n'
	@printf '  make version             显示 update.sh 版本\n'
	@printf '\n'
	@printf '  make new NAME=xxx        新建文章 content/zh/posts/tech/xxx.md\n'
	@printf '\n'
	@printf '  make key YEAR=2024 MONTH=01 DAY=25   生成 4 位密码\n'
	@printf '\n'
	@printf '  make tencloud            腾讯云 TC3 签名演示（需环境变量）\n'
	@printf '  make translate TXT="你好"           zh -> en 机器翻译\n'
	@printf '  make push [AI_URL=...]              AI 生成 commit 并推送\n'
	@printf '\n'
	@printf '  make img MD=path.md                下载 md 中的网络图片\n'
	@printf '     可选: SLUG=xxx STORAGE=dir PREFIX=/path\n'
	@printf '  make img-init FILE=cfg.json         生成图片下载器配置模板\n'
	@printf '\n'
	@printf '  make env-check           检查腾讯云密钥环境变量\n'
	@printf '\n'

# ==========================================================
# 部署 / 构建
# ==========================================================
.PHONY: deploy build run dev git backup clean check version
deploy:
	@bash $(UPDATE_SH)

build:
	@hugo --environment production --minify

run:
	@bash $(RUN_SH)

dev:
	@bash $(UPDATE_SH) --dev

git:
	@bash $(UPDATE_SH) --git

backup:
	@bash $(UPDATE_SH) --backup

clean:
	@bash $(UPDATE_SH) --clean

check:
	@bash $(UPDATE_SH) --test

version:
	@bash $(UPDATE_SH) --version

# ==========================================================
# 内容创作
# ==========================================================
.PHONY: new
new:
	@test -n "$(NAME)" || { echo '用法: make new NAME=<filename>'; exit 1; }
	@bash $(CREATE_SH) "$(NAME)"

# ==========================================================
# 密码生成
# ==========================================================
.PHONY: key
key:
	@test -n "$(YEAR)" -a -n "$(MONTH)" -a -n "$(DAY)" || \
		{ echo '用法: make key YEAR=2024 MONTH=01 DAY=25'; exit 1; }
	@bash $(GENKEY_SH) "$(YEAR)" "$(MONTH)" "$(DAY)"

# ==========================================================
# 腾讯云工具（需 TENCENTCLOUD_SECRET_ID / TENCENTCLOUD_SECRET_KEY）
# ==========================================================
.PHONY: env-check
env-check:
	@if [ -z "$$TENCENTCLOUD_SECRET_ID" ] || [ -z "$$TENCENTCLOUD_SECRET_KEY" ]; then \
		echo '错误: 请先导出 TENCENTCLOUD_SECRET_ID 和 TENCENTCLOUD_SECRET_KEY'; \
		exit 1; \
	fi

.PHONY: tencloud
tencloud: env-check
	@$(PYTHON) $(TENCLOUD_PY)

.PHONY: translate
translate: env-check
	@test -n "$(TXT)" || { echo '用法: make translate TXT="待翻译文本"'; exit 1; }
	@$(PYTHON) $(TRANSFER_PY) "$(TXT)"

# ==========================================================
# 推送
# ==========================================================
.PHONY: push
push:
	@if [ -n "$(AI_URL)" ]; then \
		AI_URL="$(AI_URL)" $(PYTHON) $(PUSH_PY); \
	else \
		$(PYTHON) $(PUSH_PY); \
	fi

# ==========================================================
# Markdown 图片下载
# ==========================================================
.PHONY: img img-init
img:
	@test -n "$(MD)" || { echo '用法: make img MD=<markdown-file>'; exit 1; }
	@EXTRA=""; \
	if [ -n "$(SLUG)" ];    then EXTRA="$$EXTRA --post-slug $(SLUG)"; fi; \
	if [ -n "$(STORAGE)" ]; then EXTRA="$$EXTRA -s $(STORAGE)"; fi; \
	if [ -n "$(PREFIX)" ];  then EXTRA="$$EXTRA -p $(PREFIX)"; fi; \
	$(PYTHON) $(MDIMG_PY) -c "$(IMG_CONFIG)" $$EXTRA "$(MD)"

img-init:
	@test -n "$(FILE)" || { echo '用法: make img-init FILE=cfg.json'; exit 1; }
	@$(PYTHON) $(MDIMG_PY) --init-config "$(FILE)"
