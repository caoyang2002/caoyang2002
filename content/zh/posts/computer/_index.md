+++
# 网站基础配置
title = "计算机科学"
description = "涵盖计算机图形学、人工智能、体系结构等主流与前沿研究方向"

# 页面参数
[params]
  listStyle = "docs"
  showSummary = true
  orderBy = "weight"
  showToc = true

  
  # 侧边栏配置
  [params.sidebar]
    enabled = true
    sticky = true
  
  # 阅读进度条
  progress = true

# 级联配置
[cascade]
  tags = [
    "计算机图形学",
    "人工智能", 
    "机器学习",
    "体系结构",
    "软件工程",
    "网络与安全",
    "人机交互"
  ]
  
  categories = [
    "理论计算机科学",
    "应用计算机科学",
    "交叉学科"
  ]
  
  # 布局配置
  [cascade._target]
    kind = "page"
    path = "**"
+++
