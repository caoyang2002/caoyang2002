+++
title = 'Openwrt_failed_to_install_1panel'
date = 2025-01-29T08:28:43+08:00
draft = true
author = "simons"
categories = ["运维"]
tags = ["openwrt"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

解决在 openwrt 中自动安装 1panel 失败的问题：

```error
Multiple packages (libgcc1 and libgcc1) providing same name marked HOLD or
PREFER. Using latest.
Multiple packages (libgcc1 and libgcc1) providing same name marked HOLD or PREFER. Using latest.
Installing app-meta-istorepanel (1.0.6-20250116) to root...
Downloading https://istore.istoreos.com/repo/all/meta/app-meta-istorepanel_1.0.6-20250116_all.ipk
Collected errors:
 * pkg_hash_check_unresolved: cannot find dependency zoneinfo-asia for luci-app-istorepanel
 * pkg_hash_fetch_best_installation_candidate: Packages for luci-app-istorepanel found, but incompatible with the architectures configured
 * satisfy_dependencies_for: Cannot satisfy the following dependencies for app-meta-istorepanel:
 *      zoneinfo-asia
 * opkg_install_cmd: Cannot install package app-meta-istorepanel.
```

存在的问题：

1. 缺少依赖包 `zoneinfo-asia`
2. 架构不兼容的问题
3. 存在重复的 `libgcc1` 包

> 如果之前安装过 1panel 那么这个失败原因可能是因为之前安装的包没有被完全清理
>
> 在命令行中，检查 `/opt/` 和 `/opt/containerd` 下是否有 `1Panel` 的目录，如果有就删除，再重新安装



# 后面的没写完，因为我删除 1Panel 目录后就可以在 istore  中安装了



# 方法一：检查是否可以手动通过 docker 的方式安装

https://github.com/xeath/1panel-in-docker

# 命令行

```bash
docker run -dt \
    --name 1panel \
    --restart always \
    --network host \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /var/lib/docker:/var/lib/docker \
    -v /opt:/opt \
    -e TZ=Asia/Shanghai \
    xeath/1panel-in-docker:latest
```

## 部署文件

创建一个 `docker-compose.yml` 文件，内容类似如下

```bash
version: '3'
services:
  1panel:
    container_name: 1panel # 容器名
    restart: always
    ports:
      - "8080:1990"  # 将容器内的 80 端口映射到宿主机的 8080 端口
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /var/lib/docker:/var/lib/docker
      - /opt:/opt
    environment:
      - TZ=Asia/Shanghai
    image: xeath/1panel-in-docker:latest
    labels:  
      createdBy: "Apps"
```



然后 `docker-compose up -dt` 运行



如果提示找不到命令 `docker-compose`

https://mirror-03.infra.openwrt.org/releases/22.03.5/packages/x86_64/packages/

```bash
wget https://mirror-03.infra.openwrt.org/releases/22.03.5/packages/x86_64/packages/docker-compose_2.15.1-1_x86_64.ipk
opkg install ./docker-compose_2.15.1-1_x86_64.ipk 
```





# 方法二：手动安装

## 解决 zoneinfo 的问题

在该地址复制包的链接 https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/packages/

```bash
# 安装 core
wget https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/packages/zoneinfo-core_2023c-2_x86_64.ipk
opkg install ./zoneinfo-core_2023c-2_x86_64.ipk

# 安装 asia
wget https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/packages/zoneinfo-asia_2023c-2_x86_64.ipk
opkg install ./zoneinfo-asia_2023c-2_x86_64.ipk
```







# 方法三：opkg 安装

1. 首先更新软件包列表:
```bash
opkg update
```

2. 安装缺少的依赖包:
```bash
opkg install zoneinfo-asia
```

3. 如果上面的命令报错,可以尝试添加更多的软件源。编辑 `/etc/opkg/customfeeds.conf`,添加:
```
src/gz openwrt_base https://downloads.openwrt.org/releases/{你的系统版本}/packages/{你的架构}/base
src/gz openwrt_packages https://downloads.openwrt.org/releases/{你的系统版本}/packages/{你的架构}/packages
```

4. 解决 libgcc1 冲突:
```bash
opkg remove libgcc1
opkg install --force-reinstall libgcc1
```

5. 然后重新尝试安装:
```bash
opkg install app-meta-istorepanel
```

如果还是不行,可以尝试:
1. 确认你的系统架构(运行 `opkg print-architecture`)
2. 检查是否有合适你架构的版本
3. 或者考虑手动下载对应架构的 ipk 包进行安装

如果需要更具体的帮助,请提供:
1. 系统版本信息(运行 `cat /etc/openwrt_release`)
2. 系统架构信息(运行 `opkg print-architecture`)

# 方法二：手动安装

从错误信息来看，`opkg update` 无法从多个软件源下载 `Packages.gz` 文件，导致更新失败。这可能是由于以下原因之一：

1. **网络连接问题**：你的设备可能无法访问这些软件源。
2. **软件源 URL 失效**：某些软件源可能已经失效或不可用。
3. **DNS 解析问题**：设备可能无法正确解析软件源的域名。
4. **软件源配置错误**：软件源的 URL 可能配置错误或不适合你的 OpenWrt 版本。

以下是解决这些问题的步骤：

---

### 1. 检查网络连接
确保你的设备可以访问互联网。尝试使用 `ping` 命令测试网络连接：

```bash
ping mirrors.cloud.tencent.com
ping istore.istoreos.com
```

如果无法 ping 通，检查网络配置（如 DNS 设置或网关配置）。

---

### 2. 更换软件源
某些软件源可能暂时不可用。你可以尝试更换为其他可用的软件源。编辑 `/etc/opkg/distfeeds.conf` 或 `/etc/opkg/customfeeds.conf` 文件，将软件源替换为以下推荐的源之一：

#### 推荐软件源（适用于 OpenWrt 22.03 或更新版本）：
```bash
src/gz openwrt_core https://downloads.openwrt.org/releases/22.03.5/targets/x86/64/packages
src/gz openwrt_base https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/base
src/gz openwrt_luci https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/luci
src/gz openwrt_packages https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/packages
src/gz openwrt_routing https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/routing
src/gz openwrt_telephony https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/telephony
```

#### 保存后，更新软件包列表：
```bash
opkg update
```

---

### 3. 手动下载 `zoneinfo-asia`
如果软件源问题无法解决，你可以手动下载 `zoneinfo-asia` 包并安装。以下是步骤：

#### 下载 `zoneinfo-asia`：
访问 [OpenWrt 官方软件包仓库](https://downloads.openwrt.org/) 或 [iStoreOS 软件包仓库](https://istore.istoreos.com/repo/all/)，找到适合你架构的 `zoneinfo-asia` 包。

例如，下载 `zoneinfo-asia`：
```bash
wget https://downloads.openwrt.org/releases/22.03.5/packages/x86_64/base/zoneinfo-asia_2022c-1_x86_64.ipk
```

#### 安装 `zoneinfo-asia`：
```bash
opkg install ./zoneinfo-asia_2022c-1_x86_64.ipk
```

---

### 4. 检查 OpenWrt 版本和架构
确保你使用的软件源与你的 OpenWrt 版本和架构匹配。运行以下命令检查系统信息：

```bash
cat /etc/openwrt_release
uname -m
```

例如，如果你的架构是 `x86_64`，确保下载的包也是 `x86_64` 架构。

---

### 5. 手动安装 `app-meta-istorepanel`
如果 `zoneinfo-asia` 安装成功，但仍然无法通过 `opkg` 安装 `app-meta-istorepanel`，可以尝试手动下载并安装：

#### 下载 `app-meta-istorepanel`：
```bash
wget https://istore.istoreos.com/repo/all/meta/app-meta-istorepanel_1.0.6-20250116_all.ipk
```

#### 安装 `app-meta-istorepanel`：
```bash
opkg install ./app-meta-istorepanel_1.0.6-20250116_all.ipk
```

---

### 6. 检查依赖关系
如果安装过程中仍然提示依赖问题，可以使用以下命令检查依赖关系：

```bash
opkg info app-meta-istorepanel
```

确保所有依赖包都已安装。如果缺少依赖包，手动下载并安装它们。

### 7. 清理缓存
如果问题仍然存在，尝试清理 `opkg` 缓存并重新更新：

```bash
rm -rf /var/opkg-lists/*
opkg update
```





# 其他命令

```bash
docker-compose up -d # 启动
docker-compose down # 停止

docker logs 1panel # 查看日志
docker exec -it 1panel /bin/bash # 进入容器
docker ps -a # 查看进程
docker stop 1panel # 停止容器
docker rm 1panel # 删除镜像
```



