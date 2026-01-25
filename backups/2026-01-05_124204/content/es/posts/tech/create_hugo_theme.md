+++
date = '2025-01-03T11:11:07+08:00'
draft = false
tags = ["hugo"]
title = 'Hugo 主题创建方法及简单说明'
+++

# 参考：
中文文档 https://hugo.opendocs.io/getting-started/quick-start/

博客：
- https://blog.gujiakai.top/2023/03/hugo-theme-development-diary
- https://juejin.cn/post/7151253414427492382

# 一个简单的 Hugo 主题

## 创建一个空的网站模版

```bash
hugo new site demo
```
这会在当前目录创建一个名为 `demo` 的目录，然后初始化 `hugo` 的目录结构，

## 创建一个空的主题模版

```bash
cd demo
hugo new theme hugo-zero
```

得到输出信息：

```
Creating theme at /hugo/demo/themes/hugo-zero
```

一开始的目录结构如下图所示：

```bash
hugo-zero（hugo主题）
├── archetypes（hugo主题文章模板）
├── layouts（hugo主题布局文件）
├── static（hugo主题的静态文件）
├── LICENSE（hugo主题的许可证信息）
└── themes.toml（hugo主题的元数据信息）
```
其中，重点关注layouts文件夹。剩余的文件可以慢慢补充。

layouts 文件夹的目录结构如下图所示：

```bash
layouts
├── _default（默认页面布局文件夹）
│   ├── baseof.html（所有页面的基底模板）
│   ├── list.html（列表页面的模板文件）
│   └── single.html（单页面的模板文件）
├── partials（部分页面布局文件夹）
│   ├── head.html（网页头部）
│   ├── header.html（网页的主导航栏）
│   └── footer.html（网页的页脚信息）
├── 404.html（网站的404错误页面）
└── index.html（网站的主页）
```

## 在 `config.toml` 里添加一行：

```toml
theme = "hugo-zero"
```

这样就可以加载主题 `hugo-zero`了，运行看看有没有报错：

```bash
hugo server
```

如果配置有问题会显示出错误信息，一切正常的话，能看到下面的输出：

```bash
| EN
+------------------+----+
Pages            |  3
Paginator pages  |  0
Non-page files   |  0
Static files     |  0
Processed images |  0
Aliases          |  0
Sitemaps         |  1
Cleaned          |  0

Total in 5 ms
Watching for changes in /tmp/demo/{archetypes,content,data,layouts,static,themes}
Watching for config changes in /tmp/demo/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

用浏览器访问 http://localhost:1313/ 看到一个空页面，这个时候什么内容都还没有。

index.html 是首页，single.html 是文章页面。
baseof.html 所有页面的模版，每个页面都是基于这个页面进行扩展。
css 目录用来放样式文件。
head.html用来定义<head>部分的内容，加载 CSS 样式文件就在这里添加。
footer.html一般用来展示版权信息。
header.html显示在顶部，展示网站名称。


# 使用

## 创建网站

```bash
# 创建 demo 网站
hugo new site demo
#  进入网站文件夹
cd demo
```

## 添加主题

```bash
# 初始化 git 仓库
git init
# 添加 git 子模块（主题）
git submodule add https://github.com/caoyang2002/hugo-zero.git themes/hugo-zero
```



## 在 `config.toml` 里添加一行：

```toml
theme = "hugo-zero"
```

# 创建文章

创建 `post_name.md` 文章

```bash
hugo new content/posts/post_name.md
```

生成 `post_name.md` 文件并添加元信息

```bash
+++
date = '2025-01-03T11:11:07+08:00'
draft = false
title = 'Post_name'
+++
```
## 启动

```bahs
# 不包含草稿内容
hugo server

# 包含草稿内容
hugo server -D
```

访问 `http://localhost:1313/`
