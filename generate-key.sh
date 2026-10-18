#!/bin/bash

# 全局变量存储素数缓存
declare -a PRIME_CACHE=()

# 高效的素数生成与缓存函数
initialize_prime_cache() {
    local max=10000
    local -a sieve=()

    # 仅在未初始化时生成
    if [[ ${#PRIME_CACHE[@]} -eq 0 ]]; then
        # 初始化筛选数组
        sieve=($(seq 0 $max))

        # 埃氏筛法
        for ((i=2; i*i<=max; i++)); do
            if [[ ${sieve[i]} -eq $i ]]; then
                for ((j=i*i; j<=max; j+=i)); do
                    sieve[j]=0
                done
            fi
        done

        # 收集素数
        for ((i=2; i<=max; i++)); do
            if [[ ${sieve[i]} -eq $i ]]; then
                PRIME_CACHE+=($i)
            fi
        done
    fi
}

# 二分查找找到第一个大于等于目标值的素数
find_prime_ge() {
    local target=$1
    local left=0
    local right=$((${#PRIME_CACHE[@]} - 1))

    while [[ $left -le $right ]]; do
        local mid=$(((left + right) / 2))
        if [[ ${PRIME_CACHE[mid]} -ge $target ]]; then
            right=$((mid - 1))
        else
            left=$((mid + 1))
        fi
    done

    # 目标超出素数表范围时返回表中最大的素数
    if [[ $left -ge ${#PRIME_CACHE[@]} ]]; then
        echo "${PRIME_CACHE[-1]}"
        return
    fi

    echo "${PRIME_CACHE[left]}"
}

generate_password() {
    # 参数验证
    if [[ $# -ne 3 ]]; then
        echo "Error: Expected 3 arguments (year month day), got $#" >&2
        return 1
    fi

    # 输入参数验证
    local year="$1"
    local month="$2"
    local day="$3"

    # 验证月份
    if ! [[ "$month" =~ ^(0[1-9]|1[0-2])$ ]]; then
        echo "Error: Invalid month: $month (must be 01-12)" >&2
        return 1
    fi

    # 验证日期
    if ! [[ "$day" =~ ^(0[1-9]|[12][0-9]|3[01])$ ]]; then
        echo "Error: Invalid day: $day (must be 01-31)" >&2
        return 1
    fi

    local date_num=$((10#$month * 100 + 10#$day))

    # 初始化素数缓存
    initialize_prime_cache

    # 高效查找目标素数
    local target_prime=$(find_prime_ge $date_num)

    local publish_date=$((year * 10000 + 10#$month * 100 + 10#$day))

    # 生成4位数密码（% 9000 保证结果始终为 1000-9999）
    local password=$(((target_prime * publish_date) % 9000 + 1000))

    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Generating password:"
    echo "  Target Prime: $target_prime"
    printf "  Corresponding 4-Digit Password: %04d\n" "$password"
}

# 主程序
main() {
    if [[ $# -ne 3 ]]; then
        echo "Usage: $0 <year> <month> <day>"
        echo "Example: $0 2024 01 25"
        return 1
    fi
    generate_password "$@"
}

# 使用示例
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

# 脚本生成的密码是确定性的，基于输入的日期（示例：2024年1月25日）。具体生成过程：
# 1. 月日数字：01 * 100 + 25 = 125
# 2. 最小目标素数：127
# 3. 密码计算：(127 * 20240125) % 9000 + 1000（运行脚本查看结果）
# 注意：密码完全由日期决定（4 位数字空间），仅适合低安全需求的访问屏障，
# 不能用于保护真实敏感数据。
