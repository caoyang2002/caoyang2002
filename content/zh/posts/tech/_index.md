+++
# 专题基本信息
title = "软件工具教程"
slug = "software-tools-guide"
description = "涵盖科研、设计、办公、多媒体、开发等全领域的核心软件工具深度教程与行业最佳实践"
weight = 10

# SEO 优化
keywords = ["Software Tools", "Tutorial", "Best Practices", "Productivity", "科研工具", "设计工具", "办公工具", "效率工具", "技能提升"]
author = "Simons"
date = 2026-01-15

# 专题封面（可选）
image = "/images/tools-cover.png"

# 专题级联设置 - 这些设置会影响所有子页面
[cascade]
  # 自动为所有子页面添加标签和分类
  
  
  # 页面参数
  [cascade.params]
    # 系列名称
    series = "软件工具教程与最佳实践"
    
    # 子页面默认布局设置
    showToc = true
    showAuthor = false
    showReadingTime = true
    layout = "doc"
    
    # 评论设置
    comments = true

    # 新增：教程元数据
    difficulty = "beginner"  # beginner | intermediate | advanced
    prerequisites = ["basic programming knowledge"]
    tools_mentioned = []

# 列表页面参数
[params]
  # 列表样式：docs | default | grid | compact
  listStyle = "docs"
  
  # 是否显示文章摘要
  showSummary = true
  
  # 排序方式：weight | date | title
  orderBy = "weight"
  
  # 文档图标（可选）
  icon = "🛠️"
  
  # 相关链接（可选）
  [[params.links]]
    name = "官方工具文档"
    url = "https://example.com/tools-docs"
    icon = "📚"
  
  [[params.links]]
    name = "最佳实践示例仓库"
    url = "https://github.com/example/tools-best-practices"
    icon = "⭐"
  
  [[params.links]]
    name = "工具对比与选型指南"
    url = "https://example.com/tools-comparison"
    icon = "📊"

 
+++
