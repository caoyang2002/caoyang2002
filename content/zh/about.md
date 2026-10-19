+++
title = "Simons"
layout = "about"
date = 2026-01-30T10:00:00+08:00
draft = false

# ======================================================================== 个人简介
name = "明明如月"                              # 真实姓名（mock）
nickname = "Simons"
job_intent = "插话艺术家"               # 求职意向
bio = "在每一个不该插话的时候，插每一句不该插的话。"
job_status = "在职，一个月内可到岗"         # 求职状态
expected_city = "成都 / 远程"               # 期望城市
expected_salary = "面议"                    # 期望薪资（可选）
birth = "2001.03"                           # 出生年月（可选）
gender = "男"                               # 性别（可选）
website = "https://example.com"             # 个人网站/博客（mock）

motto = "难事必作于易，天下大事必作于细。"
address = "四川省成都市"
avatar = "/about/avatar.jpg"

# ======================================================================== 自我评价
[[summary]]
text = "3 年前端开发经验，熟练 Vue3/React 技术栈，主导过单页应用性能优化，首屏加载提升 40%。"

[[summary]]
text = "具备 UI/UX 设计意识，能与设计团队高效协作，注重细节与用户体验。"

[[summary]]
text = "熟悉前端工程化与 CI/CD，有组件库封装与团队效率提升经验。"

# # ======================================================================== 教育经历
[[education]]
school = "示例大学"
major = "计算机科学与技术"
degree = "本科"
period = "2019.09 - 2023.06"
rank = "专业前 10%"  
details = [
    "主修课程：数据结构、算法设计、计算机网络、数据库原理、Web 开发",
    "GPA 3.6/4.0，连续两年获校级奖学金",
    "毕业设计：基于 Vue3 的可视化数据分析平台，获校级优秀毕业论文"
]
 

[[education]]
school = "示例交换学院（交换）"
major = "软件工程"
degree = "交换生"
period = "2021.09 - 2022.01"
rank = "专业前 10%"   
details = [
    "参与国际交换项目，学习人机交互与前端工程化课程",
    "与团队合作完成移动端应用开发，获课程项目一等奖"
]

# # ======================================================================== 荣誉
[[awards]]
name = "校级一等奖学金"
period = "2021 - 2022"

[[awards]]
name = "校级优秀毕业论文"
period = "2023.06"

[[awards]]
name = "课程项目一等奖（移动端应用开发）"
period = "2022.01"


# # ======================================================================== 证书
[[certificates]]
name = "CET-6"
score = "560"
date = "2021.12"

[[certificates]]
name = "CET-4"
score = "580"
date = "2020.12"

# # ======================================================================== 技能列表（icon为font-awesome4图标，可自行替换）
[[skills]]
name = "前端开发"
icon = "fa-code"
description = "构建高性能、响应式的现代网页，兼顾体验与性能"
tags = ["HTML/CSS", "JavaScript", "Vue", "React", "TailwindCSS"]
level = 9

[[skills]]
name = "UI/UX 设计"
icon = "fa-paint-brush"
description = "从用户角度出发，设计简洁、易用的产品界面"
tags = ["Figma", "原型设计", "视觉设计", "用户研究"]
level = 7

[[skills]]
name = "后端开发"
icon = "fa-server"
description = "轻量级后端服务开发，实现前后端数据交互"
tags = ["Go", "Node.js", "MySQL", "Redis", "RESTful API"]
level = 3

[[skills]]
name = "工具与效率"
icon = "fa-cogs"
description = "熟练使用开发工具，提升工作效率，保障开发质量"
tags = ["Git", "Docker", "CI/CD", "VS Code", "性能优化"]
level = 1

# ======================================================================== 经历/项目列表
[[experiences]]
title = "前端开发工程师"
company = "示例科技有限公司"
period = "2023.01 - 至今"
details = [
    "负责公司核心产品前端开发与维护，基于Vue3+Vite构建单页应用",
    "优化页面加载性能，首屏加载速度提升40%，用户留存率提升15%",
    "参与UI组件库封装，沉淀通用组件20+，提升团队开发效率30%",
    "与产品、设计团队协作，完成多个版本的需求迭代与上线"
]

[[experiences]]
title = "前端开发实习生"
company = "示例互联网公司"
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

# # ======================================================================== 作品列表（视错觉空间展示）
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
cover = "/images/project-mock-1.png"     # 详情头图（mock）
url = "https://example.com/project/1"    # 项目地址（mock）
intro = "企业官网重构项目整体介绍（mock）：围绕品牌形象与访问性能进行改版，重构信息架构并统一设计语言，适配多端访问场景。"
[projects.star]                         
situation = "旧官网加载慢、样式不统一，移动端体验较差"
task = "在不影响业务的前提下完成官网重构并提升首屏性能"
action = "采用React+Tailwind重构页面结构，拆分路由与组件，接入图片懒加载与代码分割"
result = "首屏加载时间下降60%，移动端跳出率明显降低"

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
cover = "/images/project-mock-2.png"     # 详情头图（mock）
url = "https://example.com/project/2"    # 项目地址（mock）
intro = "电商小程序项目整体介绍（mock）：面向移动端的轻量购物应用，覆盖商品浏览、购物车与支付流程。"
[projects.star]                         
situation = "需要快速上线一套可复用的电商小程序方案"
task = "完成核心购物流程与基础运营能力"
action = "使用Vue3+UniApp搭建页面与状态管理，封装通用商品卡片与购物车逻辑，对接示例支付接口"
result = "按时完成多端适配与上线，核心流程可用性通过验收"

[[projects]]
name = "数据可视化平台"
desc = "ECharts+TS开发，多维度数据展示，支持自定义筛选"
tags = ["TypeScript", "ECharts", "数据可视化"]
svg = '''<svg viewBox="0 0 100 100" fill="currentColor">
  <rect x="10" y="10" width="80" height="80" rx="4" stroke="currentColor" stroke-width="2" fill="none"/>
  <polyline points="20,70 30,50 40,60 50,30 60,45 70,20 80,35" stroke="currentColor" stroke-width="2" fill="none"/>
  <line x1="20" y1="80" x2="80" y2="80" stroke="currentColor" stroke-width="1.5"/>
</svg>'''
cover = "/images/project-mock-3.png"     # 详情头图（mock）
url = "https://example.com/project/3"    # 项目地址（mock）
intro = "数据可视化平台项目整体介绍（mock）：面向运营与业务分析的多维数据看板，支持筛选、联动与导出。"
[projects.star]                         
situation = "业务数据分散，缺少统一的可视化分析入口"
task = "搭建可配置的数据看板并支持常见筛选维度"
action = "使用TypeScript组织数据模型，基于ECharts封装图表组件，提供筛选器与联动逻辑"
result = "形成可复用的看板模板，减少重复开发工作量"

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
cover = "/images/project-mock-4.png"     # 详情头图（mock）
url = "https://example.com/project/4"    # 项目地址（mock）
intro = "个人博客系统项目整体介绍（mock）：基于静态站点生成器的个人写作与展示平台，强调加载速度与阅读体验。"
[projects.star]                         
situation = "需要一个低成本维护的个人内容发布站点"
task = "实现文章分类、标签与搜索，并保证多端阅读体验"
action = "使用Hugo生成静态页面，Tailwind定制主题与响应式布局，配置自动化构建与部署"
result = "站点可稳定静态部署，内容更新流程自动化"

# ======================================================================== 开源
[[opensource]]
name = "GitHub"
desc = "个人开源仓库与项目源码"
url = "https://example.com/github"

[[opensource]]
name = "技术博客"
desc = "前端工程化与性能优化实践文章"
url = "https://example.com/blog"

# ======================================================================== 联系信息
[[contacts]]
name = "邮箱"
icon = "fa-envelope"
value = "mock@example.com"
url = "mailto:mock@example.com"

[[contacts]]
name = "GitHub"
icon = "fa-github"
value = "mock-user"
url = "https://example.com/github"

[[contacts]]
name = "微信"
icon = "fa-weixin"
value = "mock_wechat"
qr = "/images/contact/WeChatQR.JPG"

[[contacts]]
name = "电话"
icon = "fa-phone"
value = "138-0000-0000"
url = "tel:13800000000"
+++
