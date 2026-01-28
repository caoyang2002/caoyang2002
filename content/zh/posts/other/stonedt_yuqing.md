+++
title = '思通舆情安装和配置'
date = 2026-01-27T18:51:52+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

[Github](https://github.com/stonedtman/stonedt-yuqing)

注意：思通舆情只能安装在 amd64 的设备上。

# DOcker 安装

```bash
docker run -itd --name stonedt_yuqing -p 8085:8085 crpi-8mxxyq37t3w9t2kj.cn-hangzhou.personal.cr.aliyuncs.com/stonedtx/stonedt_yuqing:1.0.10
```

如果没有提示错误，就是安装成功了

访问你安装设备的 8085 端口，例如 http://localhost:8085

- 用户名 `13900000000` 
- 密码 `stonedt`

这时候，你打开页面只能看到一个方案。

#   创建一个舆情检测方案

## 新建方案组

左上角 `新建舆情检测` -> `新建舆情方案组` -> 输入方案组名称

## 新建舆情方案

在页面的右上角，点击 `新建`, `方案名称` 自行设置。然后在 `高级创建` 中, 方案主题关键词语法是:

`|`: 或
`+`: 与
`()`：运算优先级

以下表示：汤圆和水饺出现任意一个就会被检测。

```bash
汤圆|水饺
```

以下表示：汤圆和水饺同时出现才会被检测。

```bash
汤圆+水饺
```
以下表示，汤圆和睡觉或者是汤圆和混沌出现时，才会被检测。

```bash
汤圆+(水饺|混沌)
```

## 预警

点击下方的预警开关可以进行预警的信息配置。

# 最后

目前账号是无法更改的。