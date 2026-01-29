---
# 专题基本信息
title: "编程专题"
slug: "programming"
description: "计算机组成、计算机网络、操作系统等内容"
weight: 10

# SEO 优化
keywords: ["Programming", "编程"]
author: "Simons"
date: 2026-01-15

# 专题封面（可选）
image: "/images/socket-cover.png"

# 专题级联设置 - 这些设置会影响所有子页面
cascade:
  # 自动为所有子页面添加标签和分类
  tags: ["programming", "code"]
  categories: ["programming"]
  
  # 页面参数
  params:
    # 系列名称
    series: "编程专题"
    
    # 子页面默认布局设置
    showToc: true
    showAuthor: false
    showReadingTime: true
    layout: "doc"
    
    # 评论设置
    comments: true

# 列表页面参数
params:
  # 列表样式：docs | default | grid | compact
  listStyle: "docs"
  
  # 是否显示文章摘要
  showSummary: true
  
  # 排序方式：weight | date | title
  orderBy: "weight"
  
  # 文档图标（可选）
  icon: "🌐"
  
  # 相关链接（可选）
  links:
    - name: "官方文档"
      url: "https://example.com/docs"
      icon: "📚"
    - name: "示例代码"
      url: "https://github.com/example/socket"
      icon: "💻"
---
