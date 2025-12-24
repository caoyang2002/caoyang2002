+++
title = '群晖安装 GO 语言'
date = 2025-12-24T11:04:31+08:00
draft = true
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

# 安装 go

```bash
cd /tmp && \
wget -q https://go.dev/dl/go1.22.10.linux-amd64.tar.gz && \
sudo rm -rf /usr/local/go && \
sudo tar -C /usr/local -xzf go1.22.10.linux-amd64.tar.gz && \
export PATH=/usr/local/go/bin:$PATH && \
go version && \
```

# 安装到 jupyter

```bash
go clean -cache -modcache && \
cd ~/go-module/gophernotes && \
rm -f ~/go/bin/gophernotes && \
GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -v -o ~/go/bin/gophernotes && \
chmod +x ~/go/bin/gophernotes && \
~/go/bin/gophernotes install && \
echo "✅ 安装完成！" && \
jupyter kernelspec list
```
