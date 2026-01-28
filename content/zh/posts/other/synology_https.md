+++
title = "群晖安装 Vaultwarden 并配置 https"
date = 2026-01-25T11:33:19+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "群晖安装 Vaultwarden 并，通过 OpenWrt 配置 https 访问（无需公网和Let's证书）"
+++

> 前提条件：
> - 群晖 NAS（Vaultwarden + 反向代理）
> - OpenWrt 路由器（域名劫持）

# 1. 在套件中心下载 Vaultwarden

`套件中心` -> `设置` -> `套件来源` 

添加

```url
https://spk.bobohome.store:8880
```

# 2. 安装 Vaultwarden

`套件中心` -> `社区` -> `Vaultwarden` -> `安装套件`

# 3. 在主菜单中点击打开 Vaultwarden

配置可以不改，然后点击 `管理`，这会打开一个页面，这个页面会提示你需要使用 https 访问

![http 访问](/assets/vaultwarden_https_error.png)

这里默认打开的是 `http://192.168.5.151:8507`，需要确保防火墙对 `8507` 是放行的（我自己是关了防火墙了）。

# 4. 添加域名劫持

打开 `OpenWrt`，找到 `网络`，然后打开 `DHCP/DNS` 选项。

在 `自定义挟持域名` 中添加：

![域名劫持](/assets/openwrt_dns_add_domain.png)

`ds220j` 是我的 NAS，为了便于记忆，我使用的是 `ds220j.com`，你也可以使用其他任何域名。

`192.168.5.151` 是我的 NAS 的 IP 地址。后续我会使用这个域名作为介绍，你可以替换为你自己的域名。

备注任意文字。

域名劫持后，你仍然需要使用 `域名:端口` 访问 NAS，你可以选择在 NAS 上配置一下域名。

打开 NAS 的 `控制面板`，找到 `登陆门户` 选项，在选择顶部的 `DSM` 标签，找到 `域` -> `自定义域`

输入 `ds220j.com`，等待 NAS 自动完成配置即可。

配置完成后，你就可以使用 `ds220j.com` 访问到 NAS 了。

# 3.配置反向代理

现在其实可以使用 `https://ds220j.com`  和 `http://ds220j.com` 了，但是添加端口后，即 `https://ds220j.com:8508` 无法访问。

这要通过反向代理来解决。

```bahs
来源：
  协议：HTTPS
  主机名：ds220j.com
  端口：8508

目的地：
  协议：HTTP
  主机名：ds220j.com 或 localhost 或 127.0.0.1 或群晖的 IP
  端口：8507
```

如下

![ds220j_nginx_vaultwarden_config](/assets/ds220j_nginx_vaultwarden_config.png)

确保 `8508` 在防火墙里是放行的。

通过 `ds220j.com:8508` 访问即可。

![https 访问](/assets/vaultwarden_https_pass.png)
