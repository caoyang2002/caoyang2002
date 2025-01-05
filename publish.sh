#!/bin/bash
set -e # 遇到错误立即退出

# 颜色输出函数
green() { echo -e "\033[32m$1\033[0m"; }
red() { echo -e "\033[31m$1\033[0m"; }
yellow() { echo -e "\033[33m$1\033[0m"; }

# 检查必需命令
check_commands() {
  for cmd in hugo vercel git; do
    if ! command -v $cmd &>/dev/null; then
      red "错误: 需要 $cmd 但未安装"
      exit 1
    fi
  done
}

# 部署函数
deploy() {
  time=$(date +%Y-%m-%d)
  green "开始部署 - $time"

  # 清理缓存和之前的构建
  yellow "清理缓存..."
  rm -rf public/ resources/ .hugo_build.lock

  # Hugo 构建
  yellow "Hugo 构建中..."
  if hugo --minify --gc; then
    green "Hugo 构建成功"
  else
    red "Hugo 构建失败"
    exit 1
  fi

  # Vercel 部署
  yellow "Vercel 部署中..."
  if vercel --prod; then
    green "Vercel 部署成功"
  else
    red "Vercel 部署失败"
    exit 1
  fi

  # Git 操作
  yellow "Git 提交中..."
  cd themes/hugo-focus
  git pull origin main
  cd ../..
  git add .
  git commit -m "Deploy: $time" || true
  git push

  green "部署完成!"
}

# 开发服务器函数
dev() {
  green "启动开发服务器..."
  hugo server -D --disableFastRender
}

# 命令行参数处理
case "$1" in
"--dev" | "-d")
  dev
  ;;
"--help" | "-h")
  echo "用法:"
  echo "  ./deploy.sh         # 部署到生产环境"
  echo "  ./deploy.sh --dev   # 启动开发服务器"
  echo "  ./deploy.sh --help  # 显示帮助信息"
  ;;
*)
  check_commands
  deploy
  ;;
esac
