+++
title = '用群晖 MailPlus 管理多个邮箱'
date = 2026-01-26T14:09:44+08:00
draft = false
author = "simons"
categories = ["效率工具", "系统配置", "邮件管理"]
tags = ["群晖", "Synology", "MailPlus", "邮件服务器", "邮件聚合", "多邮箱管理", "配置指南", "问题排查"]
description = "本文详细介绍在群晖 NAS 上使用 MailPlus Server 和 MailPlus 套件进行多邮箱（QQ、163、Gmail等）聚合管理的配置步骤，包含 POP3 设置、授权码使用以及通过 Cloudflare 和 resend.com 实现邮件发送的初步思路，并记录了 Outlook 邮箱配置目前存在的问题。"
cover = "https://shoplineimg.com/59c87e98d4e395c686000d2a/5ee981517f4cac0045186508/800x.png?"
+++

注意目前管理 outlook 邮箱存在问题。

# 下载套件

下载 MailPlus 和 MailPlus Server 套件。

# 配置 MailPlus Server

打开 MailPlus Server，如果没有公网 IP，最开始的配置其实无所谓，随便填写都行，毕竟无论如何都发不出邮件。

然后点击 `服务` 选项，在点击顶部的 `MailPlus 客户端` 标签，全部勾选即可。

![image](/assets/mailplus_client_pop_settings.png)

# 配置 MailPlus

## 打开 `设置`
点击右上角的用户名，打开 MailPlus 的 `设置`，然后找到 `POP3 收取`，然后点击 `新增`。根据自己的情况添加就可以了。

![image](/assets/mailplus_add_pop.png)

踩坑：
1. 大多数情况下，电子邮件和用户名是一样的。
2. 密码是授权码、或者专用密码。

比如国内的邮箱就是授权码，国外的邮箱就是专用密码
> 使用专用密码前一般需要打开两步验证

outlook 无法登录，目前我还没有解决这个问题。

目前测试 QQ、163、Gmail 是可以正常登录并接收邮件的。

# 发邮件

如果想要发邮件，至少需要一个域名。

需要使用 Cloudflare 的服务

先配置邮件路由，设置转发服务来接收邮件。然后通过 resend.com 发送邮件。
