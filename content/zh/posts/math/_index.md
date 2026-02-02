+++
# 数学主题配置
title = "数学"
description = "数学基础与理论"



# 级联设置
[cascade]
tags = ["algebra", "calculus", "geometry", "analysis", "statistics"]
categories = ["foundation", "advanced", "applied"]
# 设置布局目标
[cascade._target]
kind = "page"
path = "**"

# 布局参数
[params]
# 文档布局（适用于数学教材、定理证明等）
listStyle = "docs"
# 显示摘要（便于快速浏览定义和定理）
showSummary = true
# 按权重排序（适用于从基础到高级的数学课程）
orderBy = "weight"
# 显示目录（便于导航复杂的数学内容）
showToc = true

# 侧边栏设置
[params.sidebar]
enabled = true
sticky = true

# 阅读进度指示器（适用于长篇幅的数学证明）
progress = true

# 或者另一种格式（使用数组的数组）：
[[params.resources.links]]
name = "人工智能的数学基础"
url = "https://datawhalechina.github.io/math-for-ai/"

[[params.resources.links]]
name = "MIT 18.06 线性代数笔记"
url = "https://linalg.apachecn.org"

+++
