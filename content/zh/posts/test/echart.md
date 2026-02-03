+++
title = 'Echarts 基本使用教程'
date = 2026-02-03T10:19:15+08:00
draft = false
author = "simons"
categories = ["前端开发", "数据可视化"]
tags = ["Echarts", "JavaScript", "图表", "数据可视化", "教程"]
description = "详细的 Echarts 数据可视化库使用教程，涵盖基本概念、环境搭建、常用图表类型、进阶配置和最佳实践。"
+++

{{< echarts width="100%" height="500px" >}}
{
    title: {
        text: '示例图表'
    },
    tooltip: {},
    xAxis: {
        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20, 15]
    }]
}
{{< /echarts >}}

# Echarts 基本使用教程

## 一、Echarts 简介

Echarts 是百度开源的一个基于 JavaScript 的数据可视化图表库，它提供了丰富的图表类型和高度可定制化的配置选项，能够满足大多数数据可视化需求。


## 二、基本使用步骤

### 1. 初始化实例

```javascript
// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('main'));
```

### 2. 准备配置项

```javascript
// 指定图表的配置项和数据
var option = {
    title: {
        text: 'ECharts 入门示例'
    },
    tooltip: {},
    legend: {
        data: ['销量']
    },
    xAxis: {
        data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
};
```

### 3. 渲染图表

```javascript
// 使用刚指定的配置项和数据显示图表
myChart.setOption(option);
```

## 四、常用图表类型

### 1. 柱状图 (Bar Chart)

```javascript
var option = {
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [120, 200, 150, 80, 70, 110, 130],
        type: 'bar'
    }]
};
```

### 2. 折线图 (Line Chart)

```javascript
var option = {
    xAxis: {
        type: 'category',
        data: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [150, 230, 224, 218, 135, 147, 260],
        type: 'line',
        smooth: true  // 平滑曲线
    }]
};
```

### 3. 饼图 (Pie Chart)

```javascript
var option = {
    series: [{
        type: 'pie',
        data: [
            { value: 335, name: '直接访问' },
            { value: 310, name: '邮件营销' },
            { value: 234, name: '联盟广告' },
            { value: 135, name: '视频广告' },
            { value: 1548, name: '搜索引擎' }
        ],
        radius: '50%'  // 饼图大小
    }]
};
```

### 4. 散点图 (Scatter Chart)

```javascript
var option = {
    xAxis: {},
    yAxis: {},
    series: [{
        symbolSize: 20,
        data: [
            [10.0, 8.04],
            [8.0, 6.95],
            [13.0, 7.58],
            [9.0, 8.81],
            [11.0, 8.33],
            [14.0, 9.96],
            [6.0, 7.24],
            [4.0, 4.26],
            [12.0, 10.84],
            [7.0, 4.82],
            [5.0, 5.68]
        ],
        type: 'scatter'
    }]
};
```

## 五、进阶配置

### 1. 响应式图表

```javascript
// 窗口大小改变时重绘图表
window.addEventListener('resize', function() {
    myChart.resize();
});
```

### 2. 主题设置

```javascript
// 使用内置主题
var myChart = echarts.init(document.getElementById('main'), 'dark');
// 或
var myChart = echarts.init(document.getElementById('main'), 'light');
```

### 3. 事件处理

```javascript
myChart.on('click', function(params) {
    console.log('点击了图表元素：', params);
});

myChart.on('legendselectchanged', function(params) {
    console.log('图例选择变化：', params);
});
```

### 4. 异步数据加载

```javascript
// 异步加载数据
myChart.showLoading();
fetch('/api/data')
    .then(response => response.json())
    .then(data => {
        myChart.hideLoading();
        myChart.setOption({
            series: [{
                data: data
            }]
        });
    });
```

## 六、最佳实践

### 1. 性能优化
- 大数据量时考虑使用 `large` 模式
- 合理使用 `sampling` 采样
- 避免频繁调用 `setOption`

### 2. 代码组织
```javascript
// 推荐的组织方式
function initChart() {
    // 1. 初始化实例
    const chart = echarts.init(document.getElementById('chart'));
    
    // 2. 定义配置
    const option = getChartOption();
    
    // 3. 设置配置
    chart.setOption(option);
    
    // 4. 返回实例便于后续操作
    return chart;
}

function getChartOption() {
    return {
        // 配置项...
    };
}
```

### 3. 错误处理
```javascript
try {
    myChart.setOption(option);
} catch (error) {
    console.error('图表渲染错误：', error);
    // 显示错误提示
}
```

## 七、资源推荐

### 官方资源
- [Echarts 官方文档](https://echarts.apache.org/zh/index.html)
- [Echarts 示例](https://echarts.apache.org/examples/zh/index.html)
- [Echarts 配置项手册](https://echarts.apache.org/zh/option.html)
