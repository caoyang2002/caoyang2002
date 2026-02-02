+++
# 专题基本信息
title = "企业战略与市场竞争"
slug = "business-strategy"
description = "涵盖市场营销战略、企业战略规划、竞争分析、品牌管理、数字化转型等核心商业课题"
weight = 10

# SEO 优化
keywords = ["Marketing Strategy", "Business Strategy", "Competitive Analysis", "Digital Transformation", "Brand Management", "市场营销", "企业战略", "竞争分析"]
author = "Simons"
date = 2026-01-15

# 专题封面（可选）
image = "/images/business-strategy-cover.png"

# 专题级联设置 - 这些设置会影响所有子页面
[cascade]
  # 自动为所有子页面添加标签和分类
  tags = [
    "市场细分与定位",
    "竞争战略",
    "数字化营销",
    "品牌建设",
    "增长战略",
    "商业分析",
    "战略执行",
    "企业创新"
  ]
  
  categories = ["Marketing", "Strategy", "Business"]
  
  # 页面参数
  [cascade.params]
    # 系列名称
    series = "企业战略与市场竞争专题"
    
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
    name = "市场营销经典框架"
    url = "https://www.ama.org/marketing-resources/marketing-strategy/"
    icon = "📚"
  
  [[params.links]]
    name = "竞争分析工具与方法"
    url = "https://hbr.org/topic/competitive-strategy"
    icon = "🔍"
  
  [[params.links]]
    name = "数字化转型案例库"
    url = "https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights"
    icon = "💡"
  
  [[params.links]]
    name = "战略执行指南"
    url = "https://www.bcg.com/capabilities/strategy/overview"
    icon = "🎯"
+++
