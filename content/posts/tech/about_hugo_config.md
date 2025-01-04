+++
date = '2024-12-29T09:31:37+08:00'
draft = true
title = 'Go'
toc = true
+++

---
title : 配置
date : '2024-12-22T18:12:52+08:00'
draft : false
---

```toml
# 基础优化配置
enableGitInfo = true                # 启用 Git 信息,可以显示文章的最后修改时间
hasCJKLanguage = true              # 启用中日韩文字支持,能准确统计字数
summaryLength = 140                # 文章摘要长度

# SEO 优化
[params]
keywords = ["博客","技术","编程"]    # 网站关键词
description = "个人技术博客"        # 网站描述
images = ["site-feature-image.jpg"] # 默认社交媒体分享图片
# 自定义 Open Graph 信息
[params.og]
title = "我的博客"
type = "website"
images = ["og-image.jpg"]

# 性能优化
[minify]
  disableCSS = false               # 启用 CSS 压缩
  disableHTML = false              # 启用 HTML 压缩
  disableJS = false                # 启用 JS 压缩
  disableJSON = false              # 启用 JSON 压缩
  minifyOutput = true              # 压缩 HTML 输出

# 图片处理
[imaging]
  quality = 75                     # JPEG 图片质量
  resampleFilter = "Lanczos"       # 图片重采样过滤器
  anchor = "Smart"                 # 图片裁剪锚点

# 内容安全策略
[params.csp]
  childsrc = ["'self'"]
  fontsrc = ["'self'", "https://fonts.gstatic.com", "https://cdn.jsdelivr.net"]
  formaction = ["'self'"]
  framesrc = ["'self'"]
  imgsrc = ["'self'"]
  objectsrc = ["'none'"]
  stylesrc = ["'self'", "'unsafe-inline'"]
  scriptsrc = ["'self'", "'unsafe-inline'", "'unsafe-eval'"]

# 文章配置
[permalinks]
  posts = "/post/:year/:month/:slug/"    # 自定义文章 URL 结构

# 自定义输出格式
[outputs]
  home = ["HTML", "RSS", "JSON"]         # 支持 JSON API 输出
  section = ["HTML", "RSS"]
  taxonomy = ["HTML", "RSS"]
  term = ["HTML", "RSS"]

# RSS 订阅配置
[params.rss]
  limit = 20                             # RSS 文章数量限制
  fullContent = true                     # RSS 包含完整文章内容

# 站内搜索配置
[outputs]
  home = ["HTML", "RSS", "JSON", "SearchIndex"]
[outputFormats.SearchIndex]
  mediaType = "application/json"
  baseName = "searchindex"
  isPlainText = true
  notAlternative = true

# 文章目录配置
[markup.tableOfContents]
  endLevel = 3                           # 目录最大深度
  ordered = false                        # 使用无序列表
  startLevel = 2                         # 目录开始层级

# 代码高亮配置
[markup.highlight]
  codeFences = true                      # 启用代码围栏
  guessSyntax = true                    # 自动推测代码语言
  lineNoStart = 1                        # 起始行号
  lineNos = true                         # 显示行号
  lineNumbersInTable = true              # 使用表格式行号
  tabWidth = 4                           # 制表符宽度
  style = "monokai"                      # 代码高亮主题
```

一些重要的最佳实践建议：

1. 内容组织
```
content/
├── posts/                # 博客文章
│   ├── tech/            # 技术文章
│   └── life/            # 生活随笔
├── about/               # 关于页面
├── projects/            # 项目展示
└── notes/               # 学习笔记
```

2. 图片资源管理
```
static/
├── images/
│   ├── posts/           # 文章配图
│   ├── avatars/         # 头像
│   └── icons/           # 图标
└── assets/              # 其他资源
```

3. 文章 Front Matter 模板
```yaml
---
title: "文章标题"
date: 2024-03-21T15:04:05+08:00
lastmod: 2024-03-21T15:04:05+08:00
draft: false
weight: 1
categories: ["分类"]
tags: ["标签1", "标签2"]
author: "作者"
description: "文章描述"
featuredImage: "featured-image.jpg"
toc: true                # 是否显示目录
autoCollapseToc: true    # 自动折叠目录
---
```

4. 安全性建议：
- 开启 HTTPS
- 配置适当的 CSP(Content Security Policy)
- 定期更新主题和依赖
- 使用 robots.txt 控制爬虫访问
- 实现基本的 DDoS 防护

5. 性能优化：
- 使用 CDN 加速静态资源
- 开启图片懒加载
- 合理设置缓存策略
- 压缩静态资源
- 优化关键渲染路径

6. SEO 优化：
- 编写清晰的 robots.txt
- 创建 sitemap.xml
- 优化 meta 标签
- 实现结构化数据
- 使用规范的 URL 结构
- 确保移动端适配

7. 备份策略：
- 使用 Git 进行版本控制
- 定期备份数据库
- 导出重要配置
- 多平台备份

以上配置和建议可以帮助你搭建一个更完善的 Hugo 博客站点。根据实际需求，你可以选择性地采用这些配置。记住定期维护和更新，确保站点的安全性和性能。
