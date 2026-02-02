+++
# 专题基本信息
title = "社会学理论与研究方法"
slug = "sociology"
description = "涵盖社会学理论、研究方法、社会分层、文化社会学、政治社会学及前沿交叉领域"
weight = 10

# SEO 优化
keywords = ["Sociology", "社会学", "社会理论", "社会研究方法", "社会结构", "文化研究"]
author = "Simons"
date = 2026-01-15

# 专题封面（可选）
image = "/images/sociology-cover.png"

# 专题级联设置 - 这些设置会影响所有子页面
[cascade]
  # 自动为所有子页面添加标签和分类
  tags = [
    "古典社会学理论",
    "现代社会学理论",
    "社会研究方法论",
    "社会分层与流动",
    "文化社会学",
    "政治社会学",
    "经济社会学",
    "城市社会学",
    "性别研究",
    "社会学定量分析",
    "社会学定性研究",
    "社会网络分析",
    "全球化研究"
  ]
  
  categories = ["Sociology Theory", "Research Methods", "Applied Sociology"]
  
  # 页面参数
  [cascade.params]
    # 系列名称
    series = "社会学核心理论与研究方法专题"
    
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
  icon = "🏛️"
  
  # 相关链接（可选）
  [[params.links]]
    name = "美国社会学协会 (ASA)"
    url = "https://www.asanet.org/"
    icon = "🌐"
  
  [[params.links]]
    name = "社会学经典文献库"
    url = "https://sociology.mit.edu/sociology-lectures"
    icon = "📚"
  
  [[params.links]]
    name = "社会调查数据资源 (ICPSR)"
    url = "https://www.icpsr.umich.edu/"
    icon = "📊"
  
  [[params.links]]
    name = "社会学研究工具与方法"
    url = "https://methods.sagepub.com/"
    icon = "🔧"
+++
