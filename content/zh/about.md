+++
title = "Simons"
layout = "about"
date = 2026-01-30T10:00:00+08:00
draft = false

# 个人简介
bio = "一名热爱技术与生活的开发者/设计师，专注于前端开发、用户体验设计。"

# 个人头像（支持本地静态文件或网络链接，本地文件放 static/imgs/ 下）
avatar = "/about/avatar.jpg"

# 技能列表（icon为font-awesome4图标，可自行替换）
[[skills]]
name = "前端开发"
icon = "fa-code"
description = "构建高性能、响应式的现代网页，兼顾体验与性能"
tags = ["HTML/CSS", "JavaScript", "Vue", "React", "TailwindCSS"]

[[skills]]
name = "UI/UX 设计"
icon = "fa-paint-brush"
description = "从用户角度出发，设计简洁、易用的产品界面"
tags = ["Figma", "原型设计", "视觉设计", "用户研究"]

[[skills]]
name = "后端开发"
icon = "fa-server"
description = "轻量级后端服务开发，实现前后端数据交互"
tags = ["Go", "Node.js", "MySQL", "Redis", "RESTful API"]

[[skills]]
name = "工具与效率"
icon = "fa-cogs"
description = "熟练使用开发工具，提升工作效率，保障开发质量"
tags = ["Git", "Docker", "CI/CD", "VS Code", "性能优化"]

# 经历/项目列表
[[experiences]]
title = "前端开发工程师"
company = "XX科技有限公司"
period = "2023.01 - 至今"
details = [
    "负责公司核心产品前端开发与维护，基于Vue3+Vite构建单页应用",
    "优化页面加载性能，首屏加载速度提升40%，用户留存率提升15%",
    "参与UI组件库封装，沉淀通用组件20+，提升团队开发效率30%",
    "与产品、设计团队协作，完成多个版本的需求迭代与上线"
]

[[experiences]]
title = "前端开发实习生"
company = "XX互联网公司"
period = "2022.07 - 2022.12"
details = [
    "协助开发公司官网与营销活动页面，兼容多终端设备",
    "参与前端代码评审，修复线上bug30+，提升页面稳定性",
    "学习并应用TailwindCSS、Pinia等技术，完成独立模块开发"
]

[[experiences]]
title = "个人项目 - 极简博客系统"
period = "2025.01 - 2026.01"
details = [
    "基于Hugo+TailwindCSS构建静态博客，支持文章分类、标签、搜索",
    "自定义主题样式，实现响应式布局，适配电脑、平板、手机等设备",
    "部署至GitHub Pages，配置自动化构建，实现提交代码自动更新"
]

# 作品列表（视错觉空间展示）
[[projects]]
name = "企业官网重构"
desc = "基于React+Tailwind构建，响应式设计，首屏加载优化60%"
tags = ["React", "性能优化", "响应式"]
svg = '''<svg viewBox="0 0 100 100" fill="currentColor">
  <rect x="10" y="10" width="80" height="80" rx="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <line x1="30" y1="30" x2="70" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="50" x2="80" y2="50" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="70" x2="60" y2="70" stroke="currentColor" stroke-width="1.5"/>
</svg>'''

[[projects]]
name = "电商小程序"
desc = "Vue3+UniApp开发，支持商品分类、购物车、支付对接"
tags = ["Vue3", "UniApp", "小程序"]
svg = '''<svg viewBox="0 0 100 100" fill="currentColor">
  <rect x="20" y="15" width="60" height="70" rx="6" stroke="currentColor" stroke-width="2" fill="none"/>
  <circle cx="35" cy="30" r="2" fill="currentColor"/>
  <circle cx="45" cy="30" r="2" fill="currentColor"/>
  <circle cx="55" cy="30" r="2" fill="currentColor"/>
  <circle cx="65" cy="30" r="2" fill="currentColor"/>
  <rect x="30" y="45" width="40" height="35" rx="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>'''

[[projects]]
name = "数据可视化平台"
desc = "ECharts+TS开发，多维度数据展示，支持自定义筛选"
tags = ["TypeScript", "ECharts", "数据可视化"]
svg = '''<svg viewBox="0 0 100 100" fill="currentColor">
  <rect x="10" y="10" width="80" height="80" rx="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <polyline points="20,70 30,50 40,60 50,30 60,45 70,20 80,35" stroke="currentColor" stroke-width="2" fill="none"/>
  <line x1="20" y1="80" x2="80" y2="80" stroke="currentColor" stroke-width="1.5"/>
</svg>'''

[[projects]]
name = "个人博客系统"
desc = "Hugo+Tailwind构建，静态部署，支持文章搜索/分类"
tags = ["Hugo", "静态站点", "TailwindCSS"]
svg = '''<svg viewBox="0 0 100 100" fill="currentColor">
  <rect x="15" y="15" width="70" height="70" rx="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <line x1="25" y1="30" x2="65" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <line x1="25" y1="40" x2="75" y2="40" stroke="currentColor" stroke-width="1.5"/>
  <line x1="25" y1="50" x2="60" y2="50" stroke="currentColor" stroke-width="1.5"/>
  <line x1="25" y1="60" x2="70" y2="60" stroke="currentColor" stroke-width="1.5"/>
</svg>'''

# 联系信息
[[contacts]]
name = "邮箱"
icon = "fa-envelope"
value = "reggiesimons2cy@gmail.com"
url = "mailto:reggiesimons2cy@gmail.com"

[[contacts]]
name = "GitHub"
icon = "fa-github"
value = "caoyang2002"
url = "https://github.com/caoyang2002"

[[contacts]]
name = "微信"
icon = "fa-weixin"
value = "thomelgo"
url = "javascript:;"

[[contacts]]
name = "电话"
icon = "fa-phone"
value = "186-8324-1961"
url = "tel:18683241961"
+++
