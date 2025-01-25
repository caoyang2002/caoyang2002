#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

source venv/bin/activate
pip3 install requests
python3 transfer.py

create_post() {
   local filename=${1:-$(date +%s | sha256sum | head -c 8)}
   hugo new "posts/draft/${filename}.md"
   printf "\n"
}

get_taxonomies() {
   printf "${GREEN}Categories:${NC}\n"
   find public/categories -type d -maxdepth 1 -mindepth 1 -exec basename {} \; | sort | column

   printf "\n${RED}Tags:${NC}\n"
   find public/tags -type d -maxdepth 1 -mindepth 1 -exec basename {} \; | sort | column
}

create_post "$1"
get_taxonomies
