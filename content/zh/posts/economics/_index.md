+++
# 专题基本信息
title = "经济学研究"
slug = "economics"
description = "涵盖微观经济学、宏观经济学、计量经济学、行为经济学及前沿交叉领域的系统性知识体系"
weight = 10

# SEO 优化
keywords = ["Economics", "Microeconomics", "Macroeconomics", "Econometrics", "经济学", "微观经济学", "宏观经济学", "计量经济学"]
author = "Simons"
date = 2026-01-15

# 专题封面（可选）
image = "/images/economics-cover.png"

# 专题级联设置 - 这些设置会影响所有子页面
[cascade]
  # 自动为所有子页面添加标签和分类
  
  
  # 页面参数
  [cascade.params]
    # 系列名称
    series = "经济学研究核心领域专题"
    
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
  icon = "📈"
  
  # 相关链接（可选）
  [[params.links]]
    name = "美国国家经济研究局 (NBER)"
    url = "https://www.nber.org"
    icon = "🏛️"
  
  [[params.links]]
    name = "世界银行公开数据"
    url = "https://data.worldbank.org"
    icon = "🌍"
  
  [[params.links]]
    name = "经济学预印本库 (RePEc)"
    url = "https://ideas.repec.org"
    icon = "📚"
  
  [[params.links]]
    name = "国际货币基金组织 (IMF) 研究"
    url = "https://www.imf.org/en/Research"
    icon = "💱"
+++
