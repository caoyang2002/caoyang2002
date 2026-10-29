#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}/.."

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

create_post() {
   local filename=${1:-$(date +%s | shasum -a 256 | head -c 8)}
   hugo new "content/zh/posts/tech/${filename}.md"
   printf "\n"
}

echo "创建"
create_post "${1:-}"
