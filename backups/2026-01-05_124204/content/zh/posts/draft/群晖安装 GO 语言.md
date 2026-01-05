+++
title = '群晖安装 GO 语言'
date = 2025-12-24T11:04:31+08:00
draft = true
author = "simons"
categories = ["编程"]
tags = ["GO"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

查看架构
- arm
- x86_64
```bash
uname -a
```
> `Linux DS923plus 4.4.302+ #69057 SMP Mon Jul 21 23:26:13 CST 2025 x86_64 GNU/Linux synology_r1000_923+`

我的是 x86_64 也就是 amd64

> 这里简单说一下，`x86_64` 和 `amd64` 是同义词，指代由 AMD 创立、现由英特尔和 AMD 共同主导的 64 位 PC / 服务器架构。ARM 是另一个竞争架构。

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
