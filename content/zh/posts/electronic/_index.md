+++
# 专题基本信息
title = "电子技术"
slug = "electronics"
description = "涵盖电路基础、模拟电路、数字电路、嵌入式系统、信号处理、电源技术及前沿应用的系统性知识体系"
weight = 10

# SEO 优化
keywords = ["Electronics", "Circuit Design", "Analog Electronics", "Digital Electronics", "Embedded Systems", "电子技术", "电路设计", "模拟电路", "数字电路", "嵌入式系统"]
author = "Simons"
date = 2026-01-15

# 专题封面（可选）
image = "/images/electronics-cover.png"

# 专题级联设置 - 这些设置会影响所有子页面
[cascade]
  # 自动为所有子页面添加标签和分类
  tags = [
    "电路基础",
    "模拟电路设计", 
    "数字电路设计",
    "电力电子技术",
    "嵌入式系统开发",
    "信号处理技术",
    "传感器与接口",
    "射频与无线技术",
    "PCB设计与制造",
    "测试与测量技术",
    "半导体器件",
    "电子系统集成"
  ]
  
  categories = ["电路与系统", "硬件设计", "嵌入式开发", "前沿技术"]
  
  # 页面参数
  [cascade.params]
    # 系列名称
    series = "电子技术核心领域专题"
    
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
  icon = "🔌"
  
  # 相关链接（可选）
  [[params.links]]
    name = "IEEE Xplore 数字图书馆"
    url = "https://ieeexplore.ieee.org"
    icon = "🏛️"
  
  [[params.links]]
    name = "EEVblog 电子论坛"
    url = "https://www.eevblog.com/forum"
    icon = "💬"
  
  [[params.links]]
    name = "KiCad 开源EDA工具"
    url = "https://www.kicad.org"
    icon = "🛠️"
  
  [[params.links]]
    name = "Hackaday 硬件项目"
    url = "https://hackaday.com"
    icon = "⚡"
+++
