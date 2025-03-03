+++
title = "日程表"
layout = "schedule"
categories = ["营销管理", "前端开发", "后端开发","合约开发","平面设计","VIS 设计","摄影"]


[gantt]
timeUnit = "day"
viewMode = "daily"
startDate = 2025-01-01
endDate = 2025-12-31
dateFormat = "YYYY-MM-DD"
excludes = "weekends"
axisFormat = "%m-%d" # 格式
tickInterval = "1day"  #1week 线标记
todayMarker = "stroke-width:4px,stroke:#f00,opacity:0.5"
overviewAxisFormat = "%U"
overviewTickInterval = "1week"

[[events]]
title = "营销文章"
start = 2025-02-08
end = 2025-12-31
progress = 60
category = "营销管理"
dependencies = []
description = '''
这是多行文本示例
可以写详细说明
'''

[[events]]
title = "CCJ-个人网站开发"
start = 2025-03-14
end = 2025-03-20
progress = 100
category = "前端开发"
dependencies = ["项目启动"]

[[events]]
title = "DNB-订房网站"
start = 2025-03-21
end = 2025-04-10
progress = 100
category = "前端开发"
dependencies = ["项目启动"]

[[events]]
title = "DNB-订房网站"
start = 2025-04-10
end = 2025-04-24
progress = 100
category = "后端开发"
dependencies = ["项目启动"]

[[events]]
title = "LHC-模型网站"
start = 2025-04-24
end = 2025-05-08
progress = 100
category = "前端开发"
dependencies = ["项目启动"]

[[events]]
title = "Focus-功能修改"
start = 2025-05-08
end = 2025-05-15
progress = 100
category = "前端开发"
dependencies = ["项目启动"]

[[events]]
title = "WBC-品牌设计"
start = 2025-05-08
end = 2025-05-15
progress = 100
category = "平面设计"
dependencies = ["项目启动"]

[[events]]
title = "纪录片拍摄"
start = 2025-03-03
end = 2025-06-16
progress = 100
category = "影视创作"
dependencies = ["项目启动"]

[[events]]
title = "图片摄影"
start = 2025-03-04
end = 2025-06-17
progress = 100
category = "影视创作"
dependencies = ["项目启动"]

[[events]]
title = "美学"
start = 2025-03-05
end = 2025-06-18
progress = 100
category = "影视创作"
dependencies = ["项目启动"]

[[events]]
title = "纪实摄影"
start = 2025-03-06
end = 2025-06-19
progress = 100
category = "影视创作"
dependencies = ["项目启动"]

[[events]]
title = "广告摄影"
start = 2025-03-06
end = 2025-06-19
progress = 100
category = "影视创作"
dependencies = ["项目启动"]

[[events]]
title = "作品集整理"
start = 2025-06-17
end = 2025-07-11
progress = 100
category = "平面设计"
dependencies = ["项目启动"]
+++
