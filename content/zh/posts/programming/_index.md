+++
# 专题基本信息
title = "软件开发与编程技术"
slug = "software-programming"
description = "涵盖智能化软件开发、程序分析、软件架构、DevOps、编程语言与安全等核心研究方向"
weight = 10

# SEO 优化
keywords = ["Software Engineering", "Programming", "软件开发", "编程", "AI4SE", "DevOps"]
author = "Simons"
date = 2026-01-15

# 专题封面（可选）
image = "/images/programming-cover.png"

# 专题级联设置 - 这些设置会影响所有子页面
[cascade]
  # 自动为所有子页面添加标签和分类
  tags = [
    "AI4SE",
    "程序分析与验证",
    "软件架构",
    "DevOps",
    "编程语言",
    "软件安全",
    "低代码",
    "开发者体验"
  ]
  
  categories = ["Software Engineering", "Programming"]
  
  # 页面参数
  [cascade.params]
    # 系列名称
    series = "软件开发与编程技术专题"
    
    # 子页面默认布局设置
    showToc = true
    showAuthor = false
    showReadingTime = true
    layout = "doc"
    
    # 评论设置
    comments = true

# 列表页面参数
[params]
  # 列表样式：docs | default | grid | compact
  listStyle = "docs"
  
  # 是否显示文章摘要
  showSummary = true
  
  # 排序方式：weight | date | title
  orderBy = "weight"
  
  # 文档图标（可选）
  icon = "💻"
  
  # 相关链接（可选）
  [[params.links]]
    name = "智能化软件开发 (AI4SE) 资源"
    url = "https://github.com/microsoft/Codex"
    icon = "🤖"
  
  [[params.links]]
    name = "程序分析工具集合"
    url = "https://github.com/facebook/infer"
    icon = "🔍"
  
  [[params.links]]
    name = "现代软件架构模式"
    url = "https://github.com/ddd-crew"
    icon = "🏗️"
  
  [[params.links]]
    name = "DevOps 实践指南"
    url = "https://github.com/cncf/toc"
    icon = "🚀"
+++
