+++
title = "日程表"
layout = "schedule"
categories = ["日程"]

[decision]
title = "决策矩阵"
xAxisLeft = "不重要"
xAxisRight = "重要"
yAxisDown= "不紧急"
yAxisUp = "紧急"
quadrant1 = "立即处理"
quadrant2 = "可能需要立即处理"
quadrant3 = "浪费时间的事情"
quadrant4 = "不需要立即处理"

[[reservation]]
title = "营销咨询"
active = true
price = "6,800"
unit = "元/小时"
remake = "具体价格按项目类型谈"

[[reservation]]
title = "开发部署"
active = true
price = "300"
unit = "元/小时"
remake = "本人已不接，可交流"
history.title = "Trantor Foundation"
history.date = "2024-08-07"
history.job = "网站部署"
history.price = "40"
history.unit = "USDT/小时"
history.amounts = "300"

[[reservation]]
title = "LOGO 设计"
active = false
price = "12,000"
unit = "元/个"
remake = "本人已不接，团队在负责"

[[reservation]]
title = "VIS 设计"
active = false
price = "98,000"
unit = "元/次"
remake = "本人已不接，团队在负责"

[[reservation]]
title = "影视摄影"
active = false
price = "1,200"
unit = "元/天"
remake = "本人已不接"

[gantt]
timeUnit = "day"
viewMode = "daily"
startDate = 2025-01-01
endDate = 2025-12-31
dateFormat = "YYYY-MM-DD"
excludes = "weekends"
axisFormat = "%m-%d" # 格式
tickInterval = "1day"  # 1week 轴刻度
todayMarker = "stroke-width:4px,stroke:#f00,opacity:0.5"
overviewAxisFormat = "%U"
overviewTickInterval = "1week"

[[events]]
title = "营销文章"
start = 2025-02-08
end = 2025-12-31
progress = 60
category = "营销管理"
status = "active" # 活动 active, 完成 done, 临界 crit, 里程碑milestone.
rate = "[0.9, 0.9]"
dependencies = []
description = '''
这是多行文本示例
可以写详细说明
'''

[[events]]
title = "CCJ-个人网站开发"
start = 2025-04-10
end = 2025-04-20
progress = 100
category = "前端开发"
dependencies = ["项目启动"]
rate = "[0.52, 0.2]"

[[events]]
title = "DNB-订房网站"
start = 2025-03-06
end = 2025-04-10
progress = 100
category = "前端开发"
dependencies = ["项目启动"]
rate = "[0.1,0.7]"

[[events]]
title = "DNB-订房网站"
start = 2025-04-10
end = 2025-04-24
progress = 100
category = "后端开发"
dependencies = ["项目启动"]
rate = "[0.2,0.7]"

[[events]]
title = "LHC-模型网站"
start = 2025-04-24
end = 2025-05-08
progress = 100
category = "前端开发"
dependencies = ["项目启动"]
rate = "[0.35, 0.78]"

[[events]]
title = "Focus-功能修改"
start = 2025-05-08
end = 2025-05-15
progress = 100
category = "前端开发"
dependencies = ["项目启动"]
rate = "[0.6, 0.10]"

[[events]]
title = "WBC-品牌设计"
start = 2025-05-16
end = 2025-05-29
progress = 100
category = "平面设计"
dependencies = ["项目启动"]
rate = "[0.6, 0.15]"

[[events]]
title = "纪录片拍摄"
start = 2025-03-03
end = 2025-06-16
progress = 100
category = "传媒影视"
status = "active"
dependencies = ["项目启动"]

[[events]]
title = "图片摄影"
start = 2025-03-04
end = 2025-06-17
progress = 100
category = "传媒影视"
status = "active"
dependencies = ["项目启动"]

[[events]]
title = "美学"
start = 2025-03-05
end = 2025-06-18
progress = 100
category = "传媒影视"
status = "active"
dependencies = ["项目启动"]

[[events]]
title = "纪实摄影"
start = 2025-03-06
end = 2025-06-19
progress = 100
category = "传媒影视"
status = "active"
dependencies = ["项目启动"]

[[events]]
title = "广告摄影"
start = 2025-03-06
end = 2025-06-19
progress = 100
category = "传媒影视"
status = "active"
dependencies = ["项目启动"]

[[events]]
title = "作品集整理"
start = 2025-06-17
end = 2025-07-11
progress = 100
category = "平面设计"
dependencies = ["项目启动"]


+++
