+++
# 页面基础配置
title = "区块链技术"
description = "涵盖区块链共识机制、密码学、扩容、DeFi、Web3等核心技术与应用的研究专题"

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
    "共识机制",
    "密码学",
    "可扩展性",
    "智能合约",
    "跨链技术",
    "DeFi",
    "Web3",
    "区块链安全",
    "通证经济学",
    "隐私计算"
  ]
  
  categories = [
    "基础协议层",
    "扩展与互操作层", 
    "应用与生态层",
    "前沿交叉领域"
  ]
  
  # 布局配置
  [cascade._target]
    kind = "page"
    path = "**"
+++
