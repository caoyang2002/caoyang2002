+++
title = "航空航天好者"
layout = "aerospace"
bio = "探索航空航天制造技术，连接全球航空航天爱好者社区"
email = "reggiesimons2cy@gmail.com"
wechat = "thomelgo"

[[actions]]
name = "查看专题"
url = "/posts/rocket"
target = "_self"

[[actions]]
name = "返回博客"
url = "/"
target = "_self"

# 知名火箭制作博客
[[blogs]]
name = "BPS.space"
url = "https://bps.space"
description = "Joe Barnard 的火箭项目，专注于模型火箭的推力矢量控制和自主着陆技术"
tags = ["推力矢量控制", "自主着陆", "开源硬件", "视频教程"]

[[blogs]]
name = "Copenhagen Suborbitals"
url = "https://copenhagensuborbitals.com"
description = "丹麦民间航天组织，致力于建造载人亚轨道火箭"
tags = ["载人航天", "液体火箭", "开源设计", "众筹项目"]

[[blogs]]
name = "Rocket Lab Blog"
url = "https://www.rocketlabusa.com/about-us/updates/"
description = "商业火箭公司 Rocket Lab 的技术博客，分享火箭设计与发射经验"
tags = ["商业航天", "Electron火箭", "3D打印引擎", "案例研究"]

[[blogs]]
name = "The Rocketry Forum"
url = "https://www.rocketryforum.com"
description = "全球最大的火箭爱好者论坛，涵盖从模型火箭到高功率火箭的各类讨论"
tags = ["社区论坛", "技术讨论", "项目分享", "新手指南"]

[[blogs]]
name = "Nakka Rocketry"
url = "http://www.nakka-rocketry.net"
description = "Richard Nakka 的经典火箭制作网站，提供详细的固体和液体火箭设计资料"
tags = ["固体火箭", "液体火箭", "理论计算", "测试数据"]

[[blogs]]
name = "Apogee Components"
url = "https://www.apogeerockets.com/education"
description = "火箭零件供应商的教育资源，包含大量火箭制作教程和技术文章"
tags = ["教程", "零件供应", "设计软件", "初学者友好"]

[[blogs]]
name = "SpaceX Updates"
url = "https://www.spacex.com/updates/"
description = "SpaceX 官方更新，了解最前沿的火箭技术和发射任务"
tags = ["Starship", "Falcon 9", "可回收火箭", "火星计划"]

[[blogs]]
name  = "科创网"
url = "https://www.kechuang.org/f/74"
description = "科创网的火箭板块，但是这个板块有很多技术知识被禁了"
tags = ["论坛" , "中国大陆"]

# 火箭制作技术栈
[[technologies]]
icon = "🔥"
name = "推进系统"
description = "火箭的核心动力来源"
details = [
    "固体火箭发动机：KNDX、KNSB等糖基推进剂",
    "液体火箭发动机：LOX/煤油、LOX/甲烷组合",
    "混合火箭发动机：固体燃料+液体氧化剂",
    "推力矢量控制（TVC）系统"
]

[[technologies]]
icon = "🧭"
name = "导航与控制"
description = "实现火箭稳定飞行和精确着陆"
details = [
    "惯性测量单元（IMU）：陀螺仪+加速度计",
    "GPS定位与跟踪系统",
    "飞行控制算法：PID、卡尔曼滤波",
    "舵机与执行机构"
]

[[technologies]]
icon = "📡"
name = "遥测与通信"
description = "实时监控火箭状态"
details = [
    "无线电遥测系统（900MHz、2.4GHz）",
    "数据记录器（黑匣子）",
    "地面站接收与数据分析",
    "视频下传系统"
]

[[technologies]]
icon = "🛠️"
name = "结构与材料"
description = "轻量化与高强度设计"
details = [
    "碳纤维复合材料箭体",
    "玻璃纤维翼面",
    "3D打印部件（PLA、PETG、尼龙）",
    "铝合金机械加工件"
]

[[technologies]]
icon = "💻"
name = "软件与仿真"
description = "设计、测试与优化工具"
details = [
    "OpenRocket：火箭飞行仿真",
    "RASAero：气动设计与分析",
    "Arduino/PlatformIO：飞控编程",
    "MATLAB/Python：数据分析"
]
communities = [
    { name = "OpenRocket", description = "Open Rocket", icon = "🚀", url = "https://openrocket.info/" },
    { name = "Meter", description = "Meteor", icon = "🚀", url = "https://meteor.open-sky.fr/" },
]

[[technologies]]
icon = "🔌"
name = "电子系统"
description = "火箭的神经中枢"
details = [
    "飞控主板：Arduino、STM32、Teensy",
    "传感器：气压计、磁力计、温度计",
    "电源管理：锂电池、降压模块",
    "点火控制电路"
]

# 技术演示项目
[[demos]]
title = "推力矢量控制演示"
description = "使用舵机控制喷管方向，实现火箭姿态调整，模拟 SpaceX 的网格翼控制技术"
video_url = "https://www.youtube.com/watch?v=example1"
tags = ["TVC", "姿态控制", "Arduino"]

[[demos]]
title = "自主着陆实验"
description = "基于 GPS 和 IMU 的火箭垂直着陆系统，灵感来自 Falcon 9"
video_url = "https://www.youtube.com/watch?v=example2"
tags = ["自主着陆", "传感器融合", "PID控制"]

[[demos]]
title = "固体火箭发动机测试"
description = "自制糖基推进剂发动机的静态点火测试，包含推力曲线测量"
video_url = "https://www.youtube.com/watch?v=example3"
tags = ["固体发动机", "推进剂", "测试"]

[[demos]]
title = "数据遥测系统"
description = "实时无线传输火箭飞行数据到地面站，并绘制飞行轨迹"
video_url = "https://www.youtube.com/watch?v=example4"
tags = ["遥测", "无线通信", "数据可视化"]

[[demos]]
title = "双级火箭分离机制"
description = "演示火箭级间分离和二级点火技术"
video_url = "https://www.youtube.com/watch?v=example5"
tags = ["多级火箭", "分离机制", "点火控制"]

# 社区与交流平台
[[communities]]
icon = "🌐"
name = "国际火箭爱好者论坛"
description = "The Rocketry Forum - 全球最活跃的火箭制作社区，超过 10 万注册用户"
url = "https://www.rocketryforum.com"

[[communities]]
icon = "💬"
name = "Discord 火箭频道"
description = "实时聊天与技术交流，适合快速提问和项目讨论"
url = "https://discord.gg/rocketry"

[[communities]]
icon = "📺"
name = "YouTube 火箭频道"
description = "BPS.space、Everyday Astronaut 等知名频道，提供丰富的视频教程"
url = "https://www.youtube.com/results?search_query=model+rocket+DIY"

[[communities]]
icon = "🐦"
name = "Reddit r/rocketry"
description = "Reddit 火箭制作板块，分享项目进展和技术问题"
url = "https://www.reddit.com/r/rocketry/"

[[communities]]
icon = "📚"
name = "开源火箭项目库"
description = "GitHub 上的开源火箭设计、飞控代码和数据分析工具"
url = "https://github.com/topics/rocketry"

[[communities]]
icon = "🇨🇳"
name = "中国火箭爱好者社区"
description = "国内火箭爱好者交流平台，分享本土化的制作经验和资源"
url = "#"
+++
