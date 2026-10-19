+++
title = "简介及作品集"
layout = "about"
date = 2026-01-30T10:00:00+08:00
draft = false

# ======================================================================== 个人简介
name = "明明如月"                               # 真实姓名（mock）
nickname = "Simons"
job_intent = "插话艺术家"                       # 求职意向
bio = "在每一个不该插话的时候，插每一句不该插的话。"  
job_status = "在职"               # 求职状态
expected_city = "义乌 / 远程"                   # 期望城市
expected_salary = "面议"                    # 期望薪资（可选）
birth = "2002.01"                           # 出生年月（可选）
gender = "男"                               # 性别（可选）
website = "https://simons.qzz.io"             # 个人网站/博客（mock）
motto = "难事必作于易，天下大事必作于细。" # 签名
address = "浙江省｜义乌市" # 居住地址
avatar = "/about/avatar.jpg" # 头像

# ======================================================================== 自我评价
[[self_eval]]
text = "3 年全栈开发经验，熟练 React/ 技术栈，主导过单页应用性能优化，首屏加载提升 40%。"

[[self_eval]]
text = "具备 UI/UX 设计意识，能与设计团队高效协作，注重细节与用户体验。"

[[self_eval]]
text = "熟悉前端工程化与 CI/CD，有组件库封装与团队效率提升经验。"

# # ======================================================================== 技能列表（icon为font-awesome4图标，可自行替换）
[[skills]]
name = "前端开发"
icon = "fa-code"
description = "构建高性能、响应式的现代网页，兼顾体验与性能"
tags = ["HTML/CSS", "JavaScript", "Vue", "React", "TailwindCSS"]
level = 7

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
level = 5

[[skills]]
name = "平面设计"
icon = "fa-picture-o"
description = "具备视觉设计能力，能独立完成海报、品牌物料等平面设计工作"
tags = ["Photoshop", "Illustrator", "版式设计", "品牌视觉", "色彩构成"]
level = 6

[[skills]]
name = "版式设计"
icon = "fa-align-left"
description = "掌握栅格与排版原则，兼顾信息层级与阅读体验"
tags = ["栅格系统", "字体排印", "信息层级", "视觉节奏"]
level = 6

[[skills]]
name = "平面摄影"
icon = "fa-camera"
description = "熟悉摄影构图与布光，能完成产品与场景拍摄及后期"
tags = ["构图", "布光", "Lightroom", "后期修图", "产品摄影"]
level = 5

[[skills]]
name = "影视制作"
icon = "fa-film"
description = "掌握视频拍摄与剪辑流程，能独立完成短片制作"
tags = ["达芬奇", "After Effects", "剪辑", "调色", "分镜"]
level = 7

[[skills]]
name = "导演"
icon = "fa-video-camera"
description = "具备视听语言与叙事意识，能统筹拍摄现场与内容表达"
tags = ["分镜脚本", "场面调度", "叙事结构", "团队协作"]
level = 4

# ======================================================================== 项目经历
[[experiences]]
title = "部署解决方案"
company = "T**基金会"
period = "2024.07 - 2024.08"
details = [
    "解决基金会官网部署问题，优化桌面端和移动端适配"
]
[[experiences]]
title = "前端解决方案"
company = "吾乡（南塘DAO）"
period = "2025.04 - 2025.05"
details = [
    "负责吾乡成都及雅安区域的乡村地图项目建设和部署"
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

# ======================================================================== 作品列表
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

# # ======================================================================== 教育经历
[[education]]
school = "成都大学"
major = "艺术设计"
degree = "专科"
period = "2019.09 - 2023.06"
rank = "专业前 30%"  
details = [
    "主修课程：平面设计、平面构成",
    "GPA 3.6/4.0，连续两年获校级奖学金",
    "毕业设计：“七巷子葛根酥”品牌广告设计"
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

# ======================================================================== 荣誉
[[awards]]
name = "校级一等奖学金"
period = "2021 - 2022"

[[awards]]
name = "校级优秀毕业论文"
period = "2023.06"

[[awards]]
name = "课程项目一等奖（移动端应用开发）"
period = "2022.01"


# ======================================================================== 证书
[[certificates]]
name = "2022 未来设计师大赛"
score = "全国二等奖"
date = "2022.12"

[[certificates]]
name = "四川好创意大赛"
score = "四川省三等奖"
date = "2023.6"

# ======================================================================== 联系信息
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
value = "simons1768"
qr = "/images/contact/WeChatQR.JPG"

[[contacts]]
name = "电话"
icon = "fa-phone"
value = "176-2835-6759"
url = "tel:17628356759"
+++
