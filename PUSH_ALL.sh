#!/bin/bash
# git-ai-commit.sh - 使用AI自动生成commit信息并推送到所有远程仓库

# 配置
LM_STUDIO_URL="http://172.28.240.1:1234"
MODEL="local-model"  # 修改为你的模型名称

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 函数：打印带颜色的信息
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 函数：检查命令是否存在
check_command() {
    if ! command -v $1 &> /dev/null; then
        print_error "需要安装 $1"
        exit 1
    fi
}

# 函数：使用AI生成commit信息
generate_commit_message() {
    print_info "正在分析代码变更，生成commit信息..."
    
    # 获取git状态信息
    local git_status=$(git status --porcelain)
    local git_diff=$(git diff --cached --stat 2>/dev/null || git diff --stat)
    local staged_files=$(git diff --cached --name-only 2>/dev/null)
    
    if [ -z "$staged_files" ] && [ -z "$(git diff --name-only)" ]; then
        print_error "没有检测到变更，请先添加文件或修改代码"
        return 1
    fi
    
    # 构建提示词
    local prompt="基于以下Git变更信息，生成一个简洁、专业、符合约定式提交(Conventional Commits)的commit信息。格式：类型(范围): 描述

变更状态：
$git_status

文件变更统计：
$git_diff

已暂存文件：
$staged_files

请只返回commit信息，不要有其他解释。类型可以是：feat, fix, docs, style, refactor, test, chore等。"

    # 调用LM Studio API
    local response=$(curl -s -X POST "$LM_STUDIO_URL/v1/chat/completions" \
        -H "Content-Type: application/json" \
        -d '{
            "model": "'"$MODEL"'",
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个专业的Git助手，专门生成简洁、清晰、符合约定的commit信息。"
                },
                {
                    "role": "user",
                    "content": "'"$prompt"'"
                }
            ],
            "temperature": 0.7,
            "max_tokens": 100
        }' 2>/dev/null)

    if [ $? -ne 0 ] || [ -z "$response" ]; then
        print_warning "无法连接到AI服务，使用备用方案生成commit信息"
        generate_fallback_commit
        return $?
    fi

    # 提取AI返回的内容
    local commit_msg=$(echo "$response" | grep -o '"content":"[^"]*"' | head -1 | sed 's/"content":"//' | sed 's/"$//')
    
    if [ -z "$commit_msg" ]; then
        print_warning "AI返回内容为空，使用备用方案"
        generate_fallback_commit
        return $?
    fi

    # 清理commit信息（移除可能的markdown格式）
    commit_msg=$(echo "$commit_msg" | sed 's/^```//' | sed 's/```$//' | sed 's/^commit message: //i' | tr -d '\n' | sed 's/^"//' | sed 's/"$//')
    
    echo "$commit_msg"
    return 0
}

# 函数：备用方案生成commit信息
generate_fallback_commit() {
    print_info "使用备用方案生成commit信息..."
    
    local changed_files=$(git diff --name-only 2>/dev/null)
    local staged_files=$(git diff --cached --name-only 2>/dev/null)
    
    if [ -n "$staged_files" ]; then
        files="$staged_files"
    else
        files="$changed_files"
    fi
    
    # 分析文件类型
    local has_js=$(echo "$files" | grep -E '\.(js|ts|jsx|tsx)$' | head -1)
    local has_py=$(echo "$files" | grep -E '\.py$' | head -1)
    local has_go=$(echo "$files" | grep -E '\.go$' | head -1)
    local has_java=$(echo "$files" | grep -E '\.(java|kt)$' | head -1)
    local has_html=$(echo "$files" | grep -E '\.(html|htm|css|scss)$' | head -1)
    local has_md=$(echo "$files" | grep -E '\.(md|markdown)$' | head -1)
    local has_config=$(echo "$files" | grep -E '\.(json|yaml|yml|toml|xml)$' | head -1)
    
    # 确定commit类型
    local commit_type="chore"
    local scope=""
    
    if [ -n "$has_js" ]; then
        commit_type="feat"
        scope="javascript"
    elif [ -n "$has_py" ]; then
        commit_type="feat"
        scope="python"
    elif [ -n "$has_go" ]; then
        commit_type="feat"
        scope="go"
    elif [ -n "$has_html" ]; then
        commit_type="style"
        scope="ui"
    elif [ -n "$has_md" ]; then
        commit_type="docs"
        scope="documentation"
    elif [ -n "$has_config" ]; then
        commit_type="chore"
        scope="config"
    fi
    
    # 获取第一个修改的文件作为描述参考
    local first_file=$(echo "$files" | head -1)
    local filename=$(basename "$first_file")
    
    echo "${commit_type}(${scope}): 更新 ${filename}"
}

# 函数：交互式确认commit信息
confirm_commit_message() {
    local commit_msg="$1"
    
    echo ""
    print_info "AI生成的commit信息："
    echo -e "${GREEN}$commit_msg${NC}"
    echo ""
    
    while true; do
        read -p "是否使用这个commit信息？(y:使用/n:重新生成/e:手动编辑/q:退出): " choice
        
        case $choice in
            y|Y|"")
                print_info "使用AI生成的commit信息"
                echo "$commit_msg"
                return 0
                ;;
            n|N)
                print_info "重新生成commit信息..."
                return 1
                ;;
            e|E)
                print_info "手动编辑commit信息..."
                read -p "请输入新的commit信息: " manual_msg
                if [ -n "$manual_msg" ]; then
                    echo "$manual_msg"
                    return 0
                else
                    print_warning "输入为空，保持原信息"
                    echo "$commit_msg"
                    return 0
                fi
                ;;
            q|Q)
                print_info "退出脚本"
                exit 0
                ;;
            *)
                print_warning "无效选择，请重新输入"
                ;;
        esac
    done
}

# 函数：自动添加文件
auto_add_files() {
    print_info "检测变更文件..."
    
    local modified=$(git status --porcelain | grep -E '^ M|^MM' | cut -c4-)
    local untracked=$(git status --porcelain | grep -E '^\?\?' | cut -c4-)
    local deleted=$(git status --porcelain | grep -E '^ D' | cut -c4-)
    
    if [ -n "$modified" ] || [ -n "$untracked" ] || [ -n "$deleted" ]; then
        echo "检测到以下变更："
        [ -n "$modified" ] && echo "  修改: $modified"
        [ -n "$untracked" ] && echo "  新增: $untracked"
        [ -n "$deleted" ] && echo "  删除: $deleted"
        echo ""
        
        read -p "是否自动添加所有变更文件？(y:全部/n:交互选择): " add_choice
        
        if [[ $add_choice =~ ^[Yy]$ ]] || [ -z "$add_choice" ]; then
            print_info "添加所有变更文件..."
            git add .
        else
            print_info "交互式添加文件..."
            git add -p
        fi
    else
        print_warning "没有检测到变更文件"
        return 1
    fi
}

# 主函数
main() {
    print_info "🚀 开始智能Git提交流程..."
    echo ""
    
    # 检查是否在git仓库中
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        print_error "当前目录不是Git仓库"
        exit 1
    fi
    
    # 检查必要命令
    check_command git
    check_command curl
    
    # 1. 自动添加文件
    if ! auto_add_files; then
        print_error "没有文件可提交"
        exit 1
    fi
    
    # 2. 生成commit信息（最多尝试3次）
    local commit_msg=""
    local attempts=0
    local max_attempts=3
    
    while [ $attempts -lt $max_attempts ]; do
        attempts=$((attempts + 1))
        
        commit_msg=$(generate_commit_message)
        
        if [ $? -eq 0 ] && [ -n "$commit_msg" ]; then
            if confirm_commit_message "$commit_msg"; then
                break
            fi
        fi
        
        if [ $attempts -ge $max_attempts ]; then
            print_error "多次尝试失败，使用默认commit信息"
            commit_msg="chore: 自动提交变更"
            break
        fi
    done
    
    # 3. 执行commit
    print_info "执行提交..."
    if git commit -m "$commit_msg"; then
        print_success "✅ 提交成功: $commit_msg"
    else
        print_error "提交失败"
        exit 1
    fi
    
    echo ""
    print_info "📤 开始推送代码..."
    
    # 4. 推送到所有远程仓库
    local current_branch=$(git branch --show-current)
    local remotes=$(git remote)
    
    if [ -z "$remotes" ]; then
        print_warning "没有配置远程仓库"
        exit 0
    fi
    
    for remote in $remotes; do
        echo ""
        print_info "推送分支 '$current_branch' 到 $remote..."
        
        if git push "$remote" "$current_branch"; then
            print_success "✅ $remote 推送成功"
        else
            print_warning "⚠️  $remote 推送失败，继续下一个..."
        fi
    done
    
    echo ""
    print_success "🎉 Git流程完成！"
    echo ""
    
    # 显示最后的状态
    print_info "最终状态："
    git log --oneline -3
    echo ""
    git status --short
}

# 执行主函数
main "$@"