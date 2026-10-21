+++
title = '使用 Ngrok 进行内网穿透'
date = 2026-10-21T14:03:56+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

查看原文：https://juejin.cn/post/7694936746132750379

# ngrok 内网穿透新手教程（亲测可用版）

> 本文档基于 2026 年 8 月实际操作编写，所有步骤均亲测通过，适合完全零基础的新手。
>
> 测试环境：Windows 11 + ngrok 3.39.11 + Java 8 / Python 3.13

## 一、什么是内网穿透？什么是 ngrok？

### 1.1 内网穿透是什么？

简单说：**你电脑上跑的网站/接口，别人在外面也能访问到。**

正常情况下，你家里的电脑没有公网 IP，外面的人访问不到你电脑上跑的服务。内网穿透就是在你电脑和公网之间搭一条"隧道"，让外面的请求能通过这条隧道到达你电脑上的服务。

### 1.2 ngrok 是什么？

ngrok 是目前最流行的内网穿透工具之一，特点是：

- **一行命令启动**，不需要复杂配置
- **自动分配 HTTPS 域名**，不用自己买证书
- 支持 HTTP、HTTPS、TCP 等多种协议
- 有免费版，适合开发测试和临时演示

### 1.3 ngrok 能用来干嘛？

- 把本地写的网站/项目发给别人看
- 微信公众号、支付宝支付等需要公网回调的开发调试
- 远程访问家里的电脑（远程桌面、SSH）
- 手机 APP 连接电脑上的后端接口调试
- 临时演示 Demo 给客户看

## 二、注册 ngrok 账号（官方渠道）

ngrok 需要注册账号才能使用，免费版就够用了。

### 2.1 打开官网注册页

浏览器访问：

```bash
https://dashboard.ngrok.com/signup
```

### 2.2 选择注册方式

推荐用 **GitHub** 或 **Google** 账号一键登录，最快最方便：

- 点 `Sign up with GitHub`（推荐，程序员都有 GitHub 账号）
- 点 `Sign up with Google`

也可以用邮箱注册，填邮箱、密码、姓名即可。

### 2.3 确认创建账号

用 GitHub 登录后，会跳转到一个确认页面：

> Do you want to create an ngrok account for [xxx@xxx.com]?

操作步骤：

1. 勾选 `I accept the terms of service and privacy policy`（我接受服务条款）
2. 点黑色按钮 `Create Account`（创建账号）

### 2.4 GitHub 授权

接着会跳到 GitHub 的授权页面，点绿色按钮 `Authorize ngrok-private` 即可。

> ngrok 只请求读取你的邮箱地址，不会访问你的代码库，放心授权。

### 2.5 可能遇到的问题：登录报错

如果报错 `Your login session could not be verified`（会话验证失败），解决方法：

1. 按 `Ctrl + Shift + N` 打开**无痕窗口**
2. 在无痕窗口重新访问 `https://dashboard.ngrok.com/login`
3. 重新登录即可

> 原因是浏览器 Cookie 冲突，无痕模式没有旧 Cookie，成功率最高。

## 三、下载安装 ngrok（官方渠道）

### 方式一：winget 一键安装（推荐，Win10/11 自带）

Windows 10/11 自带 winget 包管理器，打开 PowerShell 直接执行：

```bash
winget install ngrok.ngrok
```

等待下载安装完成即可，全程自动配置环境变量。

验证安装：

```bash
ngrok version
```

看到版本号就说明安装成功了。

### 方式二：手动下载安装（通用）

如果 winget 用不了，手动下载：

1. 打开官方下载页：https://ngrok.com/download
2. 页面会自动识别你的系统，点击下载 Windows 版（`ngrok-v3-stable-windows-amd64.zip`）
3. 解压到一个固定目录，比如 `C:\tools\ngrok`
4. 配置环境变量（让任意目录都能用 ngrok 命令）：
   - 按 `Win + S` 搜索「环境变量」→ 打开「编辑系统环境变量」
   - 点「环境变量」按钮
   - 在「用户变量」里找到 `Path`，双击编辑
   - 点「新建」，填入 ngrok.exe 所在目录，比如 `C:\tools\ngrok`
   - 一路确定保存
5. **关掉所有 PowerShell 窗口，重新打开一个**（环境变量才会生效）
6. 验证：`ngrok version`

------

## 四、升级到最新版本（必做！）

> ⚠️ 重要：ngrok 官方对旧版本有最低版本要求。如果用 winget 安装的版本太旧，会启动失败。

### 4.1 检查当前版本

```
代码解读
复制代码ngrok version
```

### 4.2 如果版本低于 3.20.0，必须升级

执行升级命令：

```bash
ngrok update
```

等待升级完成，会提示：

```bash
Update available! Updating to version 3.xx.x ...
Update to version 3.xx.x successful!
```

### 4.3 验证升级后的版本

```bash
ngrok version
```

确认版本号 ≥ 3.20.0 即可（本文档测试时是 3.39.11）。

> 如果 `ngrok update` 命令被安全软件拦截，手动去官网下载最新版覆盖安装即可。

## 五、配置 Authtoken（绑定账号）

安装完 ngrok 后，需要绑定你的账号才能启动隧道。

### 5.1 获取 Authtoken

1. 登录 ngrok Dashboard：`https://dashboard.ngrok.com`
2. 在左侧菜单找到 **Your Authtoken**（Getting Started 下面）
3. 页面上会显示你的 Token（一串以 `2` 开头的字符）
4. 点 Token 右边的复制按钮

### 5.2 执行绑定命令

在 PowerShell 里执行：

```bash
ngrok config add-authtoken 这里粘贴你刚复制的Token
# ngrok config add-authtoken xxxxxxxxxxxxxxxxxx
```

成功后会提示：

```bash
Authtoken saved to configuration file: C:\Users\你的用户名\AppData\Local\ngrok\ngrok.yml
```

配置完成，只需要做一次，以后不用再配。

------

## 六、启动第一个隧道（HTTP 服务）

### 6.1 先启动本地服务

ngrok 是把你本地的服务暴露到公网，所以首先你本地得有一个服务在跑。

#### 示例一：Python 快速启动一个静态网站

如果你有一个 HTML 页面，在页面所在目录执行：

```bash
python -m http.server 8080
```

这样本地 8080 端口就有一个 Web 服务了。

#### 示例二：Spring Boot 后端项目

```bash
mvn spring-boot:run
```

默认跑在 8080 端口（可以在 application.properties 里改）。

### 6.2 启动 ngrok 隧道

新开一个 PowerShell 窗口（不要关跑本地服务的那个窗口），执行：

```bash
ngrok http 8080
```

把 `8080` 换成你本地服务实际的端口号。

### 6.3 启动成功后你会看到

```bash
Session Status                online
Account                       你的用户名 (Plan: Free)
Version                       3.39.11
Region                        Japan (jp) 或 Asia Pacific (ap)
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://xxxx.ngrok-free.dev -> http://localhost:8080

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

关键信息：

- `Session Status: online` → 隧道连接成功
- `Forwarding` 那一行 → `https://xxxx.ngrok-free.dev` 就是你的**公网地址**

### 6.4 访问公网地址

把 `https://xxxx.ngrok-free.dev` 发给别人，或者用手机流量访问，就能访问到你本地的服务了。

### 6.5 停止隧道

在 ngrok 窗口按 `Ctrl + C` 即可停止隧道。

> ⚠️ 注意：免费版每次重启 ngrok，公网地址都会变！需要固定地址要升级付费版。

------

## 七、免费版访问确认页（首次访问必看）

ngrok 免费版有一个安全机制：**首次用浏览器访问公网地址时，会显示一个确认页**，而不是直接显示你的网站。

### 7.1 确认页长什么样

页面标题是 `ERR_NGROK_6024`，内容大概是：

> You are about to visit xxxx.ngrok-free.dev... This website is served for free through ngrok.com...

下面有一个按钮 `Visit Site`。

### 7.2 怎么进去

点页面上的 `Visit Site` 按钮，就能进入真正的网站了。

> 每个设备/浏览器只需要点一次，之后再访问就直接进页面了。

### 7.3 为什么有时候是空白页？

国内网络环境下，确认页的资源有时候加载不出来，会显示空白页。解决方法：

1. 多刷新几次（`Ctrl + F5` 强制刷新）
2. 在地址栏末尾加个 `?`，比如 `https://xxxx.ngrok-free.dev/?`
3. 换个浏览器试试
4. 用手机流量访问（手机端确认页一般能正常显示）

### 7.4 接口调试怎么跳过确认页？

如果你是用代码/Postman 调用接口，可以在请求头里加：

```bash
ngrok-skip-browser-warning: true
```

加了这个头就不会返回确认页了，直接返回你的接口数据。

------

## 八、Windows Defender 误报解决（必看）

ngrok 因为有"网络穿透"行为，经常被 Windows Defender（Windows 自带杀毒）误报为病毒或潜在不安全软件。

### 8.1 误报现象

启动 ngrok 时报错：

```bash
"ngrok.exe"无法运行：无法成功完成操作，因为文件包含病毒或潜在的垃圾软件。
```

或者 Windows 安全中心弹出"发现威胁"的提示。

### 8.2 解决方法：把 ngrok 加入白名单

#### 第一步：还原被隔离的文件

1. 点击右下角 Windows 安全中心图标（盾牌）
2. 进入「病毒和威胁防护」
3. 点「保护历史记录」
4. 找到关于 ngrok.exe 的威胁记录
5. 点进去，选择「还原」（或"允许在设备上"）

#### 第二步：添加排除项（关键）

1. 在「病毒和威胁防护」页面，找到「病毒和威胁防护设置」→ 点「管理设置」
2. 拉到最下面，找到「排除项」
3. 点「添加或删除排除项」→ 点「添加排除项」
4. 选择「进程」，输入 `ngrok.exe`，确定

#### 第三步（可选）：排除安装目录

如果还报错，可以再排除 ngrok 的配置目录：

```bash
C:\Users\你的用户名\AppData\Local\ngrok
```

添加完排除项后，重新启动 ngrok 就正常了。

------

## 九、常用命令速查

### 9.1 基础命令

| 命令                                   | 作用                           |
| -------------------------------------- | ------------------------------ |
| `ngrok version`                        | 查看版本                       |
| `ngrok update`                         | 升级到最新版                   |
| `ngrok config add-authtoken 你的Token` | 绑定账号                       |
| `ngrok http 8080`                      | 暴露本地 8080 端口的 HTTP 服务 |
| `ngrok http 3000`                      | 暴露本地 3000 端口             |
| `ngrok tcp 22`                         | 暴露 TCP 服务（如 SSH）        |
| `ngrok tcp 3389`                       | 暴露远程桌面                   |

### 9.2 进阶命令

| 命令                                           | 作用                                 |
| ---------------------------------------------- | ------------------------------------ |
| `ngrok http --auth="用户名:密码" 8080`         | 给网站加密码保护，防止别人乱访问     |
| `ngrok http --domain=自定义子域名 8080`        | 指定子域名（付费版）                 |
| `ngrok http --host-header=localhost:8080 8080` | 重写 Host 头（解决本地虚拟主机问题） |
| `ngrok http --region=jp 8080`                  | 指定节点区域（us/eu/ap/jp 等）       |

### 9.3 本地调试面板

ngrok 启动后，在浏览器打开：

```url
http://127.0.0.1:4040
```

可以看到：

- 所有经过隧道的请求和响应（头、Body、状态码）
- 请求耗时
- 可以重放请求（Replay）

调试 Webhook、接口联调时非常好用。

------

## 十、多隧道配置（同时暴露多个服务）

免费版一个账号同时只能跑一个 ngrok 进程，但一个进程可以配置多个隧道。

### 10.1 编辑配置文件

配置文件路径：

``` bash
C:\Users\你的用户名\AppData\Local\ngrok\ngrok.yml
```

用记事本打开，添加多个隧道配置：

```yaml
authtoken: 你的Token
tunnels:
  web:
    addr: 8080
    proto: http
  api:
    addr: 8081
    proto: http
  ssh:
    addr: 22
    proto: tcp
```

### 10.2 启动指定隧道

```bash
ngrok start web
```

### 10.3 启动所有隧道

```bash
ngrok start --all
```

启动后每个隧道会分配一个独立的公网地址。

------

## 十一、免费版 vs 付费版

| 特性         | 免费版                    | 付费版（起步 $8/月）  |
| ------------ | ------------------------- | --------------------- |
| 隧道数量     | 1 个进程，可配多隧道      | 更多                  |
| 域名         | 随机，每次重启变          | 固定子域名/自定义域名 |
| 访问确认页   | 有（首次需点 Visit Site） | 无                    |
| 带宽         | 有限                      | 更高                  |
| 并发连接     | 有限                      | 更高                  |
| 节点选择     | 自动分配                  | 可指定                |
| TCP/TLS 隧道 | 支持                      | 支持                  |

### 怎么选？

- **开发测试、临时演示** → 免费版够用
- **给客户长期访问、生产环境** → 建议付费版或换国内方案

------

## 十二、国内替代方案推荐

ngrok 服务器在海外，国内使用有三个痛点：

1. 访问速度慢、延迟高
2. 首次访问弹确认页
3. 偶尔被墙或连接不稳定

如果需要长期在国内使用，推荐以下替代方案：

### 12.1 花生壳（最省心）

- 国内服务器，速度快稳定
- 免费版有固定域名（花生壳二级域名）
- **没有访问确认页**
- 图形化界面，配置简单
- 免费版有流量限制（1GB/月），付费版不限
- 官网：[hsk.oray.com/](https://link.juejin.cn/?target=https%3A%2F%2Fhsk.oray.com%2F)

### 12.2 FRP 自建（最灵活，推荐技术人员）

- 买一台国内轻量云服务器（腾讯云/阿里云，几十块/年）
- 自己部署 FRP（开源免费），完全掌控
- **固定域名 + 无确认页 + 速度快 + 不限流量**
- 还能同时穿透多个服务（门禁、监控、后台等）
- 一次配置，长期使用
- FRP 官网：[github.com/fatedier/fr…](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffatedier%2Ffrp)

### 12.3 SAKURA FRP（免费国内节点）

- 基于 FRP 的公共服务，国内节点
- 免费，不需要自己买服务器
- 有固定域名，无确认页
- 公共节点稳定性不如自建，适合轻度使用
- 官网：[www.natfrp.com/](https://link.juejin.cn/?target=https%3A%2F%2Fwww.natfrp.com%2F)

### 12.4 Tailscale（P2P 组网，非传统穿透）

- 零配置，基于 WireGuard
- 设备之间点对点直连，速度快
- 适合多设备互联、远程办公
- 不适合给陌生用户访问网站（需要装客户端）
- 官网：[tailscale.com/](https://link.juejin.cn/?target=https%3A%2F%2Ftailscale.com%2F)

------

## 十三、常见问题 FAQ

### Q1：启动 ngrok 报错 `authentication failed: Your ngrok-agent version is too old`

**原因**：ngrok 版本太旧，官方要求最低版本。

**解决**：执行 `ngrok update` 升级到最新版。如果升级被拦截，手动去官网下载最新版覆盖。

### Q2：启动 ngrok 报错 `文件包含病毒或潜在的垃圾软件`

**原因**：Windows Defender 误报。

**解决**：按本文第八章步骤，把 ngrok.exe 加入 Defender 排除项。

### Q3：公网地址访问是空白页

**原因**：免费版确认页资源加载失败。

**解决**：

1. 多刷新几次
2. 地址末尾加 `?`
3. 换浏览器或用手机流量访问
4. 接口调用加 `ngrok-skip-browser-warning: true` 请求头

### Q4：公网地址每次重启都变

**原因**：免费版限制，随机分配域名。

**解决**：

1. 付费版可以固定域名
2. 换国内方案（花生壳/FRP 自建），免费就有固定域名

### Q5：手机能访问，电脑不能访问（或反过来）

**原因**：可能是网络环境问题，或者确认页缓存。

**解决**：

1. 确认手机和电脑不在同一个 WiFi（手机用流量才是真正的公网访问）
2. 清除浏览器缓存
3. 换无痕窗口访问

### Q6：ngrok 启动了，但访问报错 `502 Bad Gateway`

**原因**：ngrok 隧道连不上本地服务。

**解决**：

1. 确认本地服务已经启动（先访问 `http://localhost:端口` 试试）
2. 确认端口号写对了
3. 确认本地服务没有被防火墙拦截

### Q7：免费版流量/连接数有限制吗？

有，但具体限制官方没有明确公布。一般开发测试、小流量演示完全够用。大流量、高并发建议付费或自建。

### Q8：ngrok 安全吗？会泄露数据吗？

ngrok 是正规公司产品，隧道传输是加密的。但免费版的公网地址是公开的，知道地址的人都能访问。建议：

1. 敏感服务加密码保护（`--auth` 参数）
2. 不要长期暴露敏感服务
3. 用完及时关闭隧道

------

## 十四、快速上手清单（照着做就行）

第一次使用，按这个顺序来：

- 1. 注册 ngrok 账号：[dashboard.ngrok.com/signup](https://link.juejin.cn/?target=https%3A%2F%2Fdashboard.ngrok.com%2Fsignup)
- 1. 安装 ngrok：`winget install ngrok.ngrok`
- 1. 升级到最新版：`ngrok update`
- 1. 获取 Authtoken：Dashboard → Your Authtoken → 复制
- 1. 绑定 Token：`ngrok config add-authtoken 你的Token`
- 1. 启动本地服务（比如 `python -m http.server 8080`）
- 1. 启动隧道：`ngrok http 8080`
- 1. 浏览器访问 `Forwarding` 显示的公网地址，点 `Visit Site`
- 1. 完成！🎉

------

## 十五、官方资源

- ngrok 官网：[ngrok.com/](https://link.juejin.cn/?target=https%3A%2F%2Fngrok.com%2F)
- 注册/登录：[dashboard.ngrok.com/](https://link.juejin.cn/?target=https%3A%2F%2Fdashboard.ngrok.com%2F)
- 下载页：[ngrok.com/download](https://link.juejin.cn/?target=https%3A%2F%2Fngrok.com%2Fdownload)
- 官方文档：[ngrok.com/docs](https://link.juejin.cn/?target=https%3A%2F%2Fngrok.com%2Fdocs)
- 状态页：[status.ngrok.com/](https://link.juejin.cn/?target=https%3A%2F%2Fstatus.ngrok.com%2F)（查看服务是否正常）

> 本教程基于 ngrok 3.39.11 + Windows 11 编写，其他版本和系统操作类似。 如有问题，先看第十三章常见问题，90% 的问题都能在里面找到答案。
