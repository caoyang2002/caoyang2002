+++
# 页面基础配置

title = "航空航天技术"
description = "涵盖飞行器设计、空气动力学、推进技术、航天工程等航空航天核心领域的系统性知识"

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
    "飞行器总体设计",
    "空气动力学",
    "推进技术",
    "结构设计与材料",
    "制导导航控制",
    "航空电子系统",
    "航天工程",
    "临近空间飞行器",
    "空天一体化",
    "绿色航空"
  ]
  
  categories = [
    "基础科学与设计",
    "关键子系统技术",
    "航天与空间技术",
    "前沿交叉与新兴领域"
  ]
  
  # 布局配置
  [cascade._target]
    kind = "page"
    path = "**"
+++
