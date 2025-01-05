#!/bin/bash

# 版本和配置
VERSION="1.0.0"
HUGO_THEME_PATH="themes/hugo-focus"
HUGO_THEME_BRANCH="main"
HUGO_PUBLIC_DIR="public"
HUGO_RESOURCE_DIR="resources"

# 错误处理
set -e
trap 'echo "错误发生在第 $LINENO 行"; exit 1' ERR
trap 'echo "收到中断信号，清理并退出..."; cleanup; exit 1' INT TERM

# 颜色输出函数
green() { echo -e "\033[32m$1\033[0m"; }
red() { echo -e "\033[31m$1\033[0m"; }
yellow() { echo -e "\033[33m$1\033[0m"; }

# 日志函数
log_file="deploy-$(date +%Y-%m-%d).log"
log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$log_file"
}

# 检查必需命令
check_commands() {
  for cmd in hugo vercel git; do
    if ! command -v $cmd &>/dev/null; then
      red "错误: 需要 $cmd 但未安装"
      exit 1
    fi
  done
}

# 健康检查
health_check() {
  yellow "执行健康检查..."
  # 检查必要文件
  if [ ! -f "hugo.toml" ] && [ ! -f "hugo.yaml" ] && [ ! -f "hugo.json" ]; then
    red "错误: 未找到 Hugo 配置文件"
    exit 1
  fi
  # 检查主题目录
  if [ ! -d "$HUGO_THEME_PATH" ]; then
    red "错误: 主题目录不存在"
    exit 1
  fi
}

# 备份函数
backup() {
  local backup_dir="backups/$(date +%Y-%m-%d_%H%M%S)"
  yellow "创建备份..."
  mkdir -p "$backup_dir"
  cp -r content "$backup_dir/" 2>/dev/null || true
  cp -r static "$backup_dir/" 2>/dev/null || true
  cp config.* "$backup_dir/" 2>/dev/null || true
  green "备份完成: $backup_dir"
  log "创建备份: $backup_dir"
}

# 清理函数
cleanup() {
  yellow "清理旧的备份和日志..."
  # 保留最近 5 个备份
  if [ -d "backups" ]; then
    ls -t backups/ | tail -n +6 | xargs -I {} rm -rf backups/{} 2>/dev/null || true
  fi
  # 保留最近 5 个日志文件
  ls -t *.log 2>/dev/null | tail -n +6 | xargs rm -f 2>/dev/null || true
}

# 部署函数
deploy() {
  time=$(date +%Y-%m-%d)
  log "开始部署 - $time"

  # 健康检查
  health_check

  # 创建备份
  backup

  # 清理缓存和之前的构建
  yellow "清理缓存..."
  rm -rf "$HUGO_PUBLIC_DIR" "$HUGO_RESOURCE_DIR" .hugo_build.lock

  # 更新主题
  yellow "更新主题..."
  (cd "$HUGO_THEME_PATH" && git pull origin "$HUGO_THEME_BRANCH") || {
    red "主题更新失败"
    log "主题更新失败"
    exit 1
  }

  # Hugo 构建
  yellow "Hugo 构建中..."
  hugo --minify --gc || {
    red "Hugo 构建失败"
    log "构建失败"
    exit 1
  }
  green "Hugo 构建成功"

  # Vercel 部署
  yellow "Vercel 部署中..."
  vercel --prod || {
    red "Vercel 部署失败"
    log "部署失败"
    exit 1
  }
  green "Vercel 部署成功"

  # Git 操作
  yellow "Git 提交中..."
  git add .
  git commit -m "Deploy: $time" || true
  git push || {
    red "Git 推送失败"
    log "推送失败"
    exit 1
  }

  # 清理旧文件
  cleanup

  green "部署完成!"
  log "部署成功"
}

# 开发服务器函数
dev() {
  green "启动开发服务器..."
  hugo server -D --disableFastRender
}

# 显示帮助信息
show_help() {
  cat <<EOF
Hugo 站点部署脚本 v${VERSION}

用法:
    $(basename "$0") [选项]

选项:
    -h, --help     显示帮助信息
    -d, --dev      启动开发服务器
    -b, --backup   仅创建备份
    -c, --clean    清理旧的备份和日志
    -v, --version  显示版本信息

示例:
    $(basename "$0")          # 部署到生产环境
    $(basename "$0") --dev    # 启动开发服务器
    $(basename "$0") --backup # 创建备份
EOF
}

# 命令行参数处理
case "$1" in
"--dev" | "-d")
  dev
  ;;
"--backup" | "-b")
  backup
  ;;
"--clean" | "-c")
  cleanup
  ;;
"--help" | "-h")
  show_help
  ;;
"--version" | "-v")
  echo "v${VERSION}"
  ;;
*)
  check_commands
  deploy
  ;;
esac
