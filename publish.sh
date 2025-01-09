#!/usr/bin/env bash

# 严格模式设置
set -euo pipefail
IFS=$'\n\t'

# 版本和配置
readonly VERSION="1.0.0"
readonly HUGO_THEME_PATH="themes/hugo-focus"
readonly HUGO_THEME_BRANCH="main"
readonly HUGO_PUBLIC_DIR="public"
readonly HUGO_RESOURCE_DIR="resources"
readonly MAX_BACKUPS=5
readonly MAX_LOGS=5
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly LOG_FILE="${SCRIPT_DIR}/logs/deploy-$(date +%Y-%m-%d).log"

# 导出 LANG 以确保正确的字符编码
export LANG=en_US.UTF-8

# 颜色输出函数
declare -r RED='\033[0;31m'
declare -r GREEN='\033[0;32m'
declare -r CYAN='\033[0;36m'
declare -r YELLOW='\033[0;33m'
declare -r NC='\033[0m' # No Color

print_colored() {
  local color=$1
  local message=$2
  printf "${color}%s${NC}\n" "$message"
}

# 改进的日志函数
log() {
  local level=$1
  local message=$2
  local timestamp
  local color

  # 根据日志级别设置颜色
  case "$level" in
  "INFO") color="$CYAN" ;;
  "ERROR") color="$RED" ;;
  "WARN") color="$YELLOW" ;;
  *) color="$NC" ;;
  esac

  timestamp=$(date +'%Y-%m-%d %H:%M:%S')
  printf "${color}[${timestamp}] [${level}] ${message}${NC}\n" | tee -a "$LOG_FILE"
}
# 错误处理函数
error_handler() {
  local line_no=$1
  local error_code=$2
  log "ERROR" "在第 ${line_no} 行发生错误 (错误码: ${error_code})"
  cleanup
  exit 1
}

# 设置错误处理
trap 'error_handler ${LINENO} $?' ERR
trap 'log "INFO" "收到中断信号，正在清理..."; cleanup; exit 1' INT TERM

# 检查系统要求
check_requirements() {
  local missing_deps=()
  local deps=("hugo" "vercel" "git")

  for dep in "${deps[@]}"; do
    if ! command -v "$dep" &>/dev/null; then
      missing_deps+=("$dep")
    fi
  done

  if [ ${#missing_deps[@]} -ne 0 ]; then
    print_colored "$RED" "错误: 以下依赖未安装: ${missing_deps[*]}"
    exit 1
  fi
}

# 改进的健康检查
health_check() {
  log "INFO" "执行健康检查..."

  # 检查配置文件
  local config_found=false
  for config in "hugo.toml" "hugo.yaml" "hugo.json"; do
    if [[ -f "$config" ]]; then
      config_found=true
      break
    fi
  done

  if ! $config_found; then
    log "ERROR" "未找到 Hugo 配置文件"
    exit 1
  fi

  # 检查主题目录
  if [[ ! -d "$HUGO_THEME_PATH" ]]; then
    log "ERROR" "主题目录不存在: $HUGO_THEME_PATH"
    exit 1
  fi

  # 检查磁盘空间
  local required_space=1048576 # 1GB in KB
  local available_space
  available_space=$(df -k . | tail -n 1 | awk '{print $4}')

  if ((available_space < required_space)); then
    log "ERROR" "磁盘空间不足"
    exit 1
  fi
}

# 改进的备份函数
backup() {
  local backup_dir="backups/$(date +%Y-%m-%d_%H%M%S)"
  local -a default_dirs=("content" "static")
  local -a config_files=("hugo.toml" "hugo.yaml" "hugo.json")

  log "INFO" "开始创建备份..."

  if ! mkdir -p "$backup_dir"; then
    log "ERROR" "无法创建备份目录"
    return 1
  fi

  # 备份默认目录
  for dir in "${default_dirs[@]}"; do
    if [[ -d "$dir" ]]; then
      if cp -r "$dir" "$backup_dir/" 2>/dev/null; then
        log "INFO" "成功备份 $dir"
      else
        log "WARN" "备份 $dir 失败"
      fi
    fi
  done

  # 备份存在的配置文件
  local config_found=false
  for config in "${config_files[@]}"; do
    if [[ -f "$config" ]]; then
      if cp "$config" "$backup_dir/" 2>/dev/null; then
        log "INFO" "成功备份 $config"
        config_found=true
      else
        log "WARN" "备份 $config 失败"
      fi
    fi
  done

  if ! $config_found; then
    log "WARN" "未找到任何 Hugo 配置文件"
  fi

  print_colored "$GREEN" "备份完成: $backup_dir"
  log "INFO" "备份完成: $backup_dir"
}

# 改进的清理函数
cleanup() {
  log "INFO" "开始清理..."

  local cleanup_dirs=("backups" "logs")

  # 清理目录
  for dir in "${cleanup_dirs[@]}"; do
      if [[ ! -d "$dir" ]]; then
           log "WARN" "目录不存在 $dir "
          continue
      fi
      log "INFO" "清理 $dir..."
      pushd "$dir" > /dev/null || continue

      # 根据目录类型使用不同的清理逻辑
      if [[ "$dir" == "backups" ]]; then
          # backups 目录的清理逻辑
          ls -t -d */ 2>/dev/null | sed 's#/$##' | tail -n +$((MAX_BACKUPS + 1)) | while read -r backup; do
              if [[ -n "$backup" ]]; then
                  log "INFO" "删除旧的备份: $backup"
                  rm -rf "$backup"
              fi
          done

      elif [[ "$dir" == "logs" ]]; then
          # logs 目录的清理逻辑
          find . -maxdepth 1 -name "deploy-*.log" -type f | sort -r | tail -n +$((MAX_LOGS + 1)) | while read -r file; do
              if [[ -n "$file" ]]; then
                  log "INFO" "准备删除日志文件: $file"
                  rm -f "$file"
              fi
          done
      fi

      popd > /dev/null || exit
      if [ $? -eq 0 ]; then
          log "INFO" "清理成功 $dir"
      else
          log "ERROR" "清理失败 $dir"
      fi
  done

  log "INFO" "清理完成"
}


# 改进的部署函数
deploy() {
  local deploy_time
  deploy_time=$(date +%Y-%m-%d_%H%M%S)

  log "INFO" "开始部署 - $deploy_time"

  # 运行前置检查
  check_requirements
  health_check
  backup

  # 清理构建缓存
  log "INFO" "清理缓存..."
  rm -rf "$HUGO_PUBLIC_DIR" "$HUGO_RESOURCE_DIR" .hugo_build.lock

  # 更新主题
  log "INFO" "更新主题..."
  (cd "$HUGO_THEME_PATH" && git pull origin "$HUGO_THEME_BRANCH") || {
    log "ERROR" "主题更新失败"
    return 1
  }

  # Hugo 构建
  log "INFO" "开始 Hugo 构建..."
  if ! hugo --minify --gc; then
    log "ERROR" "Hugo 构建失败"
    return 1
  fi

  # Vercel 部署
  log "INFO" "开始 Vercel 部署..."
  if ! vercel --prod; then
    log "ERROR" "Vercel 部署失败"
    return 1
  fi

  # Git 操作
  log "INFO" "更新 Git 仓库..."
  git submodule update --init --recursive --remote
  git add .
  git commit -m "Deploy: $deploy_time" || true
  if ! git push; then
    log "ERROR" "Git 推送失败"
    return 1
  fi

  cleanup
  print_colored "$GREEN" "部署完成!"
  log "INFO" "部署成功完成"
}

# 改进的开发服务器函数
dev() {
  log "INFO" "启动开发服务器..."
  hugo server -D --disableFastRender --bind "0.0.0.0" --port 1313
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
    -t, --test     运行测试检查

示例:
    $(basename "$0")          # 部署到生产环境
    $(basename "$0") --dev    # 启动开发服务器
    $(basename "$0") --backup # 创建备份
EOF
}

# 主函数
main() {
  case "${1:-}" in
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
  "--test" | "-t")
    check_requirements
    health_check
    ;;
  *)
    deploy
    ;;
  esac
}

# 脚本入口
main "$@"
