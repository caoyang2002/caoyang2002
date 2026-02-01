+++
title = '计算机图形学书单'
date = 2026-02-02T06:05:16+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
cover = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSX30tWAcrtGp4xUTreeI1sr35xhPDV8pEiFw&s"
+++

[查看原文](https://www.microsoft.com/en-us/research/articles/book-recommendation-computer-graphics/)

#  计算机图形学必读的10本书

计算机图形学诞生于二十世纪六十年代，主要的研究内容是研究如何使用数学算法在计算机中有效地表达、生成、处理以及显示相关图像和图形。作为一门计算机应用科学，计算机图形学近年来的快速发展极大地促进了计算机辅助设计、虚拟现实、游戏、动画、影视特效等行业的发展。

为了帮助同学们更好地学习计算机图形学，我们邀请微软亚洲研究院网络图形组研究员董悦为大家推荐了该领域相关的经典书籍，内容涵盖图形学基础原理、渲染基础与算法、计算几何与几何处理、表观建模等。

# 计算机图形学基础

{{< book
    cover="https://www.stubbornhuang.com/wp-content/uploads/2022/03/wp_editor_md_c23fac359021c2132ef66e57637d5b29.jpg"
    title_zh="计算机图形学：原理及实践"
    title_en="Computer Graphics: Principles and Practice"
    author="John F. Hughes / Andries van Dam / Morgan Mcguire / David F. Sklar / James D. Foley / Steven K. Feiner / Kurt Akeley"
    translator="彭群生 / 刘新国 / 苗兰芳 / 吴鸿智"
    publisher="机械工业出版社"
    year="2018-11-1"
    description="本书是计算机图形学领域的著作，系统全面地介绍了计算机图形学领域的关键概念、算法、技术和应用。本书先介绍了如何创建二维和三维图像，接下来介绍了更为广泛的话题，包括图像表示和操纵、图像和信号处理、图像的缩放、纹理和纹理映射、交互技术、曲线分割、曲面分割、形状的隐式表示、网格、光、材料和散射、颜色、光传输、概率和蒙特卡洛集成、动画、空间数据结构、现代图形学硬件等内容。"
    isbn="9787111611806"
    rating="6.9"
    page="385"
    colection="计算机科学丛书"
    recommendation="本书为四位图形学界大师的经典著作。作为计算机图形学入门基础最佳教程，该书内容涵盖非常广泛，从最基础的rasterization algorithm到现代GPU设计及并行计算应有尽有。这本书之所以有名一方面是因为其全面地介绍了计算机图形学的基本概念和经典算法，另一方面也来自于这本书的历史地位。该书第一版出版于1982年，可以说这本教材见证了计算机图形学界的发展，当然，本书也多次改版增添了大量内容以适应计算机图形学的飞速发展。从任何一个角度看，本书都是值得学习的经典入门书目。"
>}}



{{< book
    cover="https://camo.githubusercontent.com/f761a66b88c375de09c2da0912ff600c2581f39388879c4386799fd3cfeaf299/68747470733a2f2f7777772e73747562626f726e6875616e672e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032332f30352f77705f656469746f725f6d645f30373834386635313936363863396637363539306531346164343139383931662e6a7067"
    title_zh="物理渲染从理论到实现"
    title_en="Physically Based Rendering: From Theory to Implementation"
    author="Greg Humpherys Matt Pharr"
    translator="李秋霞"
    publisher="清华大学出版社"
    year="2017-1"
    description="本书详细阐述了与物理渲染相关的高效解决方案，主要包括几何形状和转换，图元和相交加速计算，颜色和辐射度，相机模型，采样和重构，反射模型，材质、纹理、体散射、光源、蒙特卡罗积分、光线传输等内容。此外，本书还提供了相应的算法、代码以及伪代码，以帮助读者进一步理解相关方案的实现过程。"
    isbn="9787302449812"
    rating=""
    page="892"
    colection=""
    recommendation="基于光线追踪的渲染算法最佳教材，该教材在渲染领域如雷贯耳，曾获得软件界 Jolt 图书类大奖，在计算机图形学界鼎鼎大名！同时与该书配套的渲染系统PBRT也在计算机图形学领域被广泛应用，是学界最常用的渲染引擎之一。该书的作者也是渲染领域的几位大师级专家，该书涉及了光线追踪渲染的各个方向，同时该书的最新版也及时引入了大量新近的光线追踪渲染算法。光线追踪已经是现代电影特效工业的基础模块，同时随着基于GPU的光线追踪的发展，光线追踪在游戏中也会逐渐发挥自己的特长。该书是学习渲染的入门必读书目。"
>}}



{{< book
    cover="https://camo.githubusercontent.com/b0cc1285127c3f4f490bb21d1ec3707bcd612ad1f5d47a2bffd85b81b0fdcc75/68747470733a2f2f7777772e73747562626f726e6875616e672e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032302f30382f2545382542352538342545362542412539302545352538382538362545342542412541422d5265616c2d54696d652d52656e646572696e672d466f757274682d45646974696f6e2d5064662545382538422542312545362539362538372545352538452539462545372538392538382545342542382538422545382542442542442e706e67"
    title_zh="实时渲染（暂无中文版）"
    title_en="Real-Time Rendering, 4th Edition"
    author="Tomas Akenine-Möller / Eric Haines / Naty Hoffman"
    translator=""
    publisher="A K Peters/CRC Press"
    year="2018-8-6"
    description="Thoroughly updated, this fourth edition focuses on modern techniques used to generate synthetic three-dimensional images in a fraction of a second. With the advent of programmable shaders, a wide variety of new algorithms have arisen and evolved over the past few years. This edition discusses current, practical rendering methods used in games and other applications. It also presents a solid theoretical framework and relevant mathematics for the field of interactive computer graphics, all in an approachable style. New to this edition: new chapter on VR and AR as well as expanded coverage of Visual Appearance, Advanced Shading, Global Illumination, and Curves and Curved Surfaces."
    isbn="9781138627000"
    rating="9.9"
    page="1198"
    colection=""
    recommendation="前面那本书讲的是完全基于物理的光线追踪渲染系统，然而对于绝大多数游戏和实时交互场景，光线追踪的效率相对低下，无法满足实时计算的要求，因此在游戏引擎等实时性要求较高的应用中，人们设计了很多用于实时渲染的算法。本书出自三位具有丰富游戏引擎设计经验的大师之手，该书也是实时渲染领域的经典著作，几经再版，更新最新的实时渲染技术。当前最新的第四版也引入了很多最新游戏中使用的最新技术，值得每一位对实时渲染和游戏渲染系统感兴趣的同学学习。"
>}}



## 渲染算法进阶

下面这两本更偏向于学术著述，需要有一定的渲染基础知识才可以阅读，然而由于出自先进渲染算法的几位经典导师之手，这两本书对于想深入研究渲染系统，或者希望在渲染领域进行学术研究的同学也是必读的书目，在阅读过程中也能学习到技术之外的一些关于如何设计这些算法的深刻思考。


{{< book
    cover="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/08/04.jpg"
    title_zh="全局光照算法技术（第2版）"
    title_en="Advanced Global Illumination, 2nd Edition"
    author="Philip Dutre, Philippe Bekaert, Kavita Bala"
    translator="黄刚 等"
    publisher="清华大学出版社"
    year="2019-11-1"
    description="本书详细阐述了与全局光照算法技术相关的基本解决方案，主要包括光传输物理学、蒙特卡罗方法、计算 光传输的策略、随机路径追踪算法、随机辐射度算法、混合算法、真实感和渲染速度等内容。此外，本书还提 供了相应的示例，以帮助读者进一步理解相关方案的实现过程。 本书适合作为高等院校计算机及相关专业的教材和教学参考书，也可作为相关开发人员的自学教材和参考手册。"
    isbn="9787302522461"
    rating=""
    page="320"
    colection=""
    recommendation="本书基本围绕光线追踪这一分支下基于蒙特卡罗的光线追踪体系，根据概率计算有效提高渲染效率，同时始终对渲染结果做出无偏估计。是学习蒙特卡罗光线追踪的重要教材。"
>}}


{{< book
    cover="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/08/05.jpg"
    title_zh="使用光子映射的真实感图像合成（暂无中文）"
    title_en="Realistic Image Synthesis Using Photon Mapping, 1st Edition"
    author="Henrik Wann Jensen"
    translator=""
    publisher="AK Peters, Ltd."
    year="2001-07-15"
    description="暂无"
    isbn="9781568811475"
    rating=""
    page="181"
    colection=""
    recommendation="本书主要介绍利用Photon Mapping进行有效计算全局光照和半透明渲染的方法，Photon Mapping虽然是一种有偏估计算法，但是该算法在一些特殊的渲染过程中具有非常高的计算效率优势，因此，Photon Mapping依然是电影工业中进行渲染计算不可或缺的重要部分。该书对Photon Mapping进行了深入浅出的介绍，是学习该方法的最佳读物。"
>}}

## 计算几何与几何处理


{{< book
    cover="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/08/06.jpg"
    title_zh="计算几何：算法与应用（第3版）"
    title_en="Computational Geometry: Algorithms and Applications, 3rd Edition"
    author="Mark de Berg, Otfried Cheong, Marc van Kreveld, Mark Overmars"
    translator="邓俊辉"
    publisher="清华大学出版社"
    year="2009-6"
    description="《计算几何:算法与应用(第3版)》的前4章对几何算法进行了讨论，包括几何求交、三角剖分、线性规划等，其中涉及的随机算法也是《计算几何:算法与应用(第3版)》的一个鲜明特点。第5章至第10章介绍了多种几何结构，包括几何查找、kd树、区域树、梯形图、Voronoi图、排列、Delaunay三角剖分、区间树、优先查找树以及线段树等。第11章至第16章结合实际问题，继续讨论了若干几何算法及其数据结构，包括高维凸包、空间二分及BSP树、运动规划、网格生成及四叉树、最短路径查找及可见性图、单纯性区域查找及划分树和切分树等，这些也是对前10章内容的进一步深化。《计算几何:算法与应用(第3版)》不仅内容全面，而且紧扣实际应用，重点突出，既有深入的讲解，同时每章都设有“注释及评论”和“习题”，方便读者更深入的理解，被世界众多大学作为教材。计算几何是计算机理论科学的一个重要分支，自20世纪70年代末从算法设计与分析中独立出来起，已经有了巨大的发展，不仅产生了一系列重要的理论成果，也在众多实际领域中得到了广泛的应用。"
    isbn="9787302199380"
    rating="9.2"
    page="407"
    colection="世界著名计算机教材精选"
    recommendation="计算几何是图形学的一个重要数学基础，本书围绕计算机图形学应用总结了计算几何的经典算法，是计算几何的经典入门书目。"
>}}


{{< book
    cover="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/08/07.jpg"
    title_zh="《多边形网格处理》(暂无中文)"
    title_en="Polygon Mesh Processing, 1st Edition"
    author="Mario Botsch / Leif Kobbelt / Mark Pauly / Pierre Alliez / Bruno Levy"
    translator=""
    publisher="A K Peters"
    year="2010-9-22"
    description=""
    isbn="9781568814261"
    rating="9.5"
    page="250"
    colection=""
    recommendation="几何处理是计算机图形学的一个重要研究方向，本书出自几位当今活跃在科研一线的几何处理大师之手，基本涵盖了几何处理的各个重要研究方向，每个章节还为想深入研究该方向的同学列出了扩展阅读的材料，适合想深入学习研究几何处理的同学研读。"
>}}


## 表观建模


{{< book
    cover="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/08/08.jpg"
    title_zh="材质外观的数字建模"
    title_en="Digital Modeling of Material Appearance (The Morgan Kaufmann Series in Computer Graphics), 1st Edition"
    author="Julie Dorsey / Holly Rushmeier / François Sillion"
    translator=""
    publisher="Morgan Kaufmann"
    year="2007-12-14"
    description="这是关于材料外观数字建模的第一部全面著作：它解释了如何将物理学和工程学中的模型与敏锐的观察技能相结合，用于计算机图形渲染。本书由外观建模和渲染领域的顶尖专家撰写，适合希望了解材料建模工具通用框架的从业者，以及致力于开发新建模技术的研究人员。本书不是特定软件系统的“操作指南”，而是提供了基础知识的深入探讨和关键进展的详细覆盖。"
    isbn="9780122211812"
    rating=""
    page="336"
    colection=""
    recommendation="表观建模研究物体与光线的交互作用，体现了物体的材质属性。本书出自表观建模的几位先驱者，全面系统地介绍了表观建模的概念和领域的多个重要方向。虽然此书出版时间相对较早，但本书作为表观建模领域的入门教材依然值得每个想在这个领域进行深入研究的同学阅读。同时，由于渲染与表观密不可分，因此也建议对表观建模感兴趣的同学结合前面介绍的渲染相关的书籍进行学习。"
>}}

## 高动态范围图像

{{<book
    cover="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/08/09.jpg"
    title_zh="高动态范围成像：采集、显示与基于图像的照明（暂无中文）"
    title_en="High Dynamic Range Imaging: Acquisition, Display, and Image-Based Lighting 2nd Edition"
    author="Karol Myszkowski / Sumanta Pattanaik Wolfgang Heidrich Erik Reinhard Paul Debevec"
    translator=""
    publisher="Morgan Kaufmann"
    year="2010-06-15"
    description="这本开创性著作首次完整描述了高动态范围成像（HDRI）技术，涵盖从捕捉设备到色调还原及基于图像的照明等广泛主题。所阐述的技术使您能够生成动态范围更接近真实世界的图像，从而带来无与伦比的视觉体验。无论是作为该领域的入门指南还是权威技术参考，对于从事计算机图形学、电影、视频、摄影或照明设计等图像相关工作的专业人士而言，本书都具有不可替代的价值。"
    isbn="9780123749147"
    rating=""
    page="672"
    colection=""
    recommendation="高动态范围图像已经在当前图形学产业界有了非常广泛的应用，现在的手机相机也大多带有HDR拍照的功能。本书由HDR领域的多位先驱者共同编写，全面深入地介绍了HDR图像相关的方方面面，从理论基础到产业应用应有尽有。相信每一位对HDR技术感兴趣的同学都能在本书中找到自己需要的内容。"
>}}


## One more thing

{{< book
    cover="https://www.microsoft.com/en-us/research/wp-content/uploads/2024/08/10.jpg"
    title_zh=""
    title_en="Jim Blinn's Corner：Dirty Pixels"
    author="Jim Blinn"
    translator=""
    publisher="Morgan Kaufmann"
    year="1998-09-29"
    description="暂无"
    isbn="9781558604551"
    rating=""
    page="256"
    colection=""
    recommendation="Jim Blinn 是计算机图形学领域的泰斗级人物，在NASA和JPL制作的宇宙系列动画影响了一代人对宇宙和计算机图形学探索的向往。同时大名鼎鼎的Blinn-Phong模型在今天依然有所大量的应用。这套系列丛书一共出版了三本，分别是《Jim Blinn’s Corner: Dirty Pixels》《Jim Blinn’s Corner: A Trip Down The Graphics Pipeline》《Jim Blinn’s Corner: Notation, Notation, Notation》，该系列丛书收集了Jim Blinn在IEEE Computer Graphics & Applications写的一系列专栏文章。由于文章发表时间相对久远，很多文中涉及到领域已经有了长足的发展，因此这套书相对而言更适合学术考古、溯本追源之用。"
>}}


[查看原文](https://www.stubbornhuang.com/1256/)

# 计算几何与计算机图形学必读书单整理


有人说[计算机图形学](https://www.stubbornhuang.com/tag/计算机图形学/)一般包含几何（Geometry）、渲染（Rendering）、模拟（Simulation），也有人说计算机图形学主要包含建模（Modeling）、渲染（Rendering）、动画（Animation）、人机交互（Human-computer Interaction）。本书单想从计算几何和计算机图形学两个方面总结一下可看的书籍，计算图形学主要从图形学数学基础、渲染、动画、模拟、游戏引擎设计与开发、图形API等方面总结，计算几何主要从点、线、面等基础几何体以及相互关系总结。

> 持续更新中，本次更新时间2023年8月10日，未完待续！

Github地址：https://github.com/HW140701/Book-list-of-computational-geometry-and-computer-graphics，欢迎大家star!

我自己觉得计算几何和计算机图形学方面的书还是看纯英文原版的得劲！

### [计算机图形学书单](https://www.stubbornhuang.com/tag/计算机图形学书单/)列表

- Fundamentals of Computer Graphics
- Physically Based Rendering From Theory To Implementation
- Real-Time Rendering
- GPU Gems
- ShaderX
- GPU Pro
- GPU Zen
- GPU Pro 360
- Foundations of Game Engine Development
- 3D Math Primer for Graphics and Game Development
- Essential Mathematics for Games and Interactive Applications
- Jim Blinn's Corner
- Game Engine Gems
- Game Engine Architecture
- Graphics Gems
- Ray Tracing in One Week
- Game Programming Gems
- The HDRI Handbook
- High Dynamic Range Imaging
- Interactive Computer Graphics
- Realistic Image Synthesis Using Photon Mapping
- Ray Tracing Gems
- Efficient Illumination Algorithms for Global Illumination In Interactive and Real-Time Rendering
- Mathematics for 3D Game Programming and Computer Graphics
- Real-Time Shadows
- Advanced global illumination
- Computer Graphics Principles and Practice
- Computer Graphics Through OpenGL – From Theory to Experiments
- Game Physics Engine Development- How to Build a Robust Commercial-Grade Physics Engine for your Game
- Graphics Shaders - Theory and Practice
- Insights
- The Magic of Computer Graphics - Landmarks in Rendering
- OpenGL Programming Guide
- OpenGL SuperBible
- OpenGL 4.0 Shading Language Cookbook
- OpenGL Shading Language
- Fluid Engine Development
- Fluid Simulation for Computer Graphics
- The Nature of Code - Simulating Natural Systems with Processing
- Game Physics Pearls
- Game Physics
- Game Physics Cookbook
- Physics for Game Developers
- Physics for Game Programmers
- Physics Modeling for Game Programmers
- Physics-Based Animation
- Foundations of Physically Based Modeling and Animation
- Production Volume Rendering - Design and Implementation
- Collision Detection in Interactive 3D Environments
- Real-Time Collision Detection
- Introduction to 3D Game Programming with DirectX
- Practical Rendering and Computation with Direct3D 11
- Real-Time 3D Rendering with DirectX and HLSL - A Practical Guide to Graphics Programming
- The Art of Fluid Animation
- Ray Tracing from the Ground Up
- Character Animation With Direct3D
- Real-time 3D Character Animation with Visual C++
- Vulkan Programming Guide - The Official Guide to Learning Vulkan
- Learning Vulkan
- Vulkan Cookbook - Work through recipes to unlock the full potential of the next generation graphics API-Vulkan
- GLSL Essentials - Enrich your 3D scenes with the power of GLSL
- Computer Animation - Algorithms and Techniques
- The Ray Tracer Challenge - A Test-Driven Guide to Your First 3D Renderer
- Ray Tracing - A Tool for All
- Cloth Simulation for Computer Graphics
- Real-Time Volume Graphics
- Computer Graphics from Scratch - A Programmer's Introduction to 3D Rendering
- 3D Game Engine Design - A Practical Approach to Real-Time Computer Graphics
- 3D Game Engine Architecture - Engineering Real-Time Applications with Wild Magic
- Real-Time Cameras - A Guide for Game Designers and Developers
- Game AI Pro - Collected Wisdom of Game AI Professionals
- Game AI Pro 360
- Visualizing Quaternions
- Quaternions for Computer Graphics
- 3D Engine Design for Virtual Globes
- Texturing and Modeling - A Procedural Approach
- Level of Detail for 3D Graphics
- Non-Photorealistic Rendering
- Non-Photorealistic Computer Graphics - Modeling, Rendering, and Animation
- The Algorithms and Principles of Non-photorealistic Graphics - Artistic Rendering and Cartoon Animation
- Digital Character Development - Theory and Practice
- 3D Graphics Rendering Cookbook - A comprehensive guide to exploring rendering algorithms in modern OpenGL and Vulkan
- Tricks of the 3D Game Programming Gurus - Advanced 3D Graphics and Rasterization
- Graphics Programming Methods
- Principles of Digital Image Synthesis
- Digital Image Processing
- Game Development Tools
- Div, Grad, Curl, and All That - An Informal Text on Vector Calculus
- Game Programming Algorithms and Techniques - A Platform-Agnostic Approach
- Game Programming Patterns
- Game Programming Golden Rules
- Augmented Reality - Principles and Practice
- Practical Augmented Reality - A Guide to the Technologies, Applications, and Human Factors for AR and VR-Addison
- VR Developer Gems
- Image Objects - An Archaeology of Computer Graphics
- Advanced High Dynamic Range Imaging
- A Biography of the Pixel
- Computer Graphics Programming in OpenGL with C++
- GPGPU Programming for Games and Science
- Computer Facial Animation
- Handbook of Digital Image Synthesis - Scientific Foundations of Rendering
- Image Content Retargeting - Maintaining Color, Tone, and Spatial Consistency
- Introduction to Computer Graphics - A Practical Learning Approach
- Direct3D Rendering Cookbook
- Practical Algorithms for 3D Computer Graphics
- Computer Graphics - From Pixels to Programmable Graphics Hardware
- The History of Visual Magic in Computers - How Beautiful Images are Made in CAD, 3D, VR and AR
- WebGL Programming Guide - Interactive 3D Graphics Programming with WebGL
- Beginning DirectX 11 Game Programming
- The CUDA Handbook - A Comprehensive Guide to GPU Programming
- OpenGL Development Cookbook
- GPU Computing Gems
- 3D Graphics for Game Programming
- Light & Skin Interactions - Simulations for Computer Graphics Applications
- Video Game Optimization
- Mathematics for Computer Graphics
- An Integrated Introduction to Computer Graphics and Geometric Modeling
- Digital Modeling of Material Appearance
- Color Imaging - Fundamentals and Applications
- Data Structures and Algorithms for Game Developers
- Geometric Data Structures for Computer Graphics
- Advances in GPU Research and Practice
- Learn OpenGL - Learn modern OpenGL graphics programming in a step-by-step fashion
- Simulating Humans - Computer Graphics Animation and Control
- WebGL Gems - Learn How To Create 3D Worlds And Games For Modern Web Browsers
- Computer Graphics, C Version
- Vector Analysis for Computer Graphics
- Calculus for Computer Graphics
- Digital Lighting & Rendering
- Foundations of 3D computer graphics
- Computer Graphics with OpenGL
- Practical Linear Algebra - A Geometry Toolbox
- An Introduction to Ray Tracing
- AI Game Engine Programming
- AI Game Programming Wisdom
- Artificial Intelligence for Games
- Behavioral Mathematics for Game AI
- Cloth Modeling and Animation
- Virtual Clothing - Theory and Practice
- Computer Graphics and Geometric Modelling - Implementation and Algorithms
- Designing the User Experience of Game Development Tools
- Real-Time 3D Graphics with WebGL 2
- Rotation Transforms for Computer Graphics
- Matrix Transforms for Computer Games and Animation
- Mathematical Basics of Motion and Deformation in Computer Graphics
- Geometric and Discrete Path Planning for Interactive Virtual Worlds
- Hands-On C++ Game Animation Programming
- An Introduction to Computational Fluid Dynamics - The Finite Volume Method
- Mastering Graphics Programming with Vulkan
- Practical Shader Development - Vertex and Fragment Shaders for Game Developers
- The Modern Vulkan Cookbook - A practical guide to 3D graphics and advanced real-time rendering techniques in Vulkan

### [计算几何书单](https://www.stubbornhuang.com/tag/计算几何书单/)列表



- Polygon Mesh Processing
- Computational Geometry – Algorithms and Applications
- Handbook of Discrete and Computational Geometry
- Geometric tools for computer graphics
- Computational Geometry in C
- Computational Geometry：An Introduction
- Geometric Algebra for Computer Science - An Object-Oriented Approach to Geometry
- Isosurfaces - Geometry, Topology, and Algorithms
- Guide to Computational Geometry Processing Foundations, Algorithms, and Methods
- Discrete and Computational Geometry
- Robust and Error-Free Geometric Computing
- Implicit Curves and Surfaces - Mathematics, Data Structures and Algorithms
- Computational Geometry - An Introduction Through Randomized Algorithms
- Effective Computational Geometry for Curves and Surfaces
- Nonlinear Computational Geometry
- Handbook of Computer Aided Geometric Design
- Computational Geometry on Surfaces - Performing Computational Geometry on the Cylinder, the Sphere, the Torus, and the Cone
- Geometry for Computer Graphics - Formulae, Examples and Proofs
- Introduction to Computing with Geometry
- Curves and Surfaces for Computer Graphics
- Geometry for Programmers

## 计算机图形学

**深入探索**

书

books

Book

### Fundamentals of Computer Graphics

| 封面                                                         | 书名                                              | [下载](https://www.stubbornhuang.com/tag/下载/)链接 |
| ------------------------------------------------------------ | ------------------------------------------------- | --------------------------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_32110034d0d2bbf9efa1090cd541a0f5.jpg) | Fundamentals of Computer Graphics, Second Edition | https://www.stubbornhuang.com/1343/                 |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2020/12/%E8%B5%84%E6%BA%90%E5%88%86%E4%BA%AB-Fundamentals-of-Computer-Graphics-Third-Edition%E9%AB%98%E6%B8%85%E8%8B%B1%E6%96%87PDF%E4%B8%8B%E8%BD%BD.png) | Fundamentals of Computer Graphics, Third Edition  | https://www.stubbornhuang.com/1065/                 |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2020/12/%E8%B5%84%E6%BA%90%E5%88%86%E4%BA%AB-Fundamentals-of-Computer-Graphics-Fourth-Edition%E9%AB%98%E6%B8%85%E8%8B%B1%E6%96%87PDF%E4%B8%8B%E8%BD%BD.png) | Fundamentals of Computer Graphics, Fourth Edition | https://www.stubbornhuang.com/1071/                 |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2022/01/wp_editor_md_2bcd7899f5f369700e29047a926fa745.jpg) | Fundamentals of Computer Graphics, Fifth Edition  | https://www.stubbornhuang.com/1894/                 |

### Physically Based Rendering From Theory To Implementation

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/08/wp_editor_md_80bb20d689020fa738da83ce67907346.jpg) | Physically Based Rendering From Theory To Implementation(First Edition) | https://www.stubbornhuang.com/1208/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/03/wp_editor_md_35a54319d923c600154d257ef50b2ba3.jpg) | Physically Based Rendering From Theory To Implementation (Second Edition) | https://www.stubbornhuang.com/1198/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2020/06/%E8%B5%84%E6%BA%90%E4%B8%8B%E8%BD%BD-Physically-Based-Rendering-From-Theory-to-Implementation-3rd-edition%EF%BC%88%E8%8B%B1%E6%96%87%E7%89%88%EF%BC%89-PDF%E4%B8%8B%E8%BD%BD.png) | Physically Based Rendering From Theory To Implementation (Third Edition) | https://www.stubbornhuang.com/862/  |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2023/05/wp_editor_md_07848f519668c9f76590e14ad419891f.jpg) | Physically Based Rendering From Theory To Implementation (Fourth Edition) | https://www.stubbornhuang.com/2605/ |

### Real-Time Rendering

| 封面                                                         | 书名                                | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/08/wp_editor_md_d6a57260f6aa1789fe91053d138fc68d.jpg) | Real-Time Rendering, Second Edition | https://www.stubbornhuang.com/1503/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2020/08/%E8%B5%84%E6%BA%90%E5%88%86%E4%BA%AB-Real-Time-Rendering-Third-Edition-%E8%8B%B1%E6%96%87%E5%8E%9F%E7%89%88Pdf%E4%B8%8B%E8%BD%BD.png) | Real-Time Rendering, Third Edition  | https://www.stubbornhuang.com/896/  |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2020/08/%E8%B5%84%E6%BA%90%E5%88%86%E4%BA%AB-Real-Time-Rendering-Fourth-Edition-Pdf%E8%8B%B1%E6%96%87%E5%8E%9F%E7%89%88%E4%B8%8B%E8%BD%BD.png) | Real-Time Rendering, Fourth Edition | https://www.stubbornhuang.com/897/  |

### GPU Gems

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/03/wp_editor_md_4fdd4cb2a411739f7e4fe1d3f2324ded.jpg) | GPU Gems 1 – Programming Techniques, Tips and Tricks for Real-Time Graphics | https://www.stubbornhuang.com/1230/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/03/wp_editor_md_91d7fbbcfb179c6baf93dabbfede9c63.jpg) | GPU Gems 2 – Programming Techniques for High-Performance Graphics and General-Purpose Computation | https://www.stubbornhuang.com/1231/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/03/wp_editor_md_8c2ae03fb35f97aba34480ad4bbadc91.jpg) | GPU Gems 3                                                   | https://www.stubbornhuang.com/1233/ |

### ShaderX

| 封面                                                         | 书名                                                   | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_ff6ca46b4fc6e6517acfaa60170c8138.jpg) | ShaderX1 – Vertex and Pixel Shader Tips and Tricks     | https://www.stubbornhuang.com/1294/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_839384bc6a97dce5eb518e34141cbc8e.jpg) | ShaderX2 – Introductions and Tutorials with DirectX9.0 | https://www.stubbornhuang.com/1298/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_83d20bfc5b779fd39824cd8bb410107d.jpg) | ShaderX3 – Advanced Rendering with DirectX and OpenGL  | https://www.stubbornhuang.com/1300/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/ShaderX4-Advanced-Rendering-with-DirectX-and-OpenGL.jpg) | ShaderX4 - Advanced Rendering Techniques               | https://www.stubbornhuang.com/2877/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/ShaderX5-Advanced-Rendering-Techniques%E5%B0%81%E9%9D%A2.jpg) | ShaderX5 – Advanced Rendering Techniques               | https://www.stubbornhuang.com/1305/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/ShaderX6-Advanced-Rendering-with-DirectX-and-OpenGL.jpg) | ShaderX6 - Advanced Rendering Techniques               | https://www.stubbornhuang.com/2878/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/ShaderX7-Advanced-Rendering-Techniques%E5%B0%81%E9%9D%A2.jpg) | ShaderX7 – Advanced Rendering Techniques               | https://www.stubbornhuang.com/1312/ |

### GPU Pro

| 封面                                                         | 书名                                      | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_cecc58e7a4f4fe6c8c43ca15cd4ab26f.jpg) | GPU Pro 1 – Advanced Rendering Techniques | https://www.stubbornhuang.com/1275/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_d0faf50294efa928e455d6789fa8f6b0.jpg) | GPU Pro 2 – Advanced Rendering Techniques | https://www.stubbornhuang.com/1280/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_1a86074a29fcd0900d5d2cfa249e82cb.jpg) | GPU Pro 3 – Advanced Rendering Techniques | https://www.stubbornhuang.com/1282/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_6b01dc7285fa8186b92bc14ceca518d3.jpg) | GPU Pro 4 – Advanced Rendering Techniques | https://www.stubbornhuang.com/1285/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_5196cd3e9c8650fa041291f4baa7b325.jpg) | GPU Pro 5 – Advanced Rendering Techniques | https://www.stubbornhuang.com/1286/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_b503678382f8a2c8c8b1b0f727b64dce.jpg) | GPU Pro 6 – Advanced Rendering Techniques | https://www.stubbornhuang.com/1288/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/04/wp_editor_md_e3a87c592fa8ff06e677a5b500ebf206.jpg) | GPU Pro 7 – Advanced Rendering Techniques | https://www.stubbornhuang.com/1292/ |

### GPU Zen

| 封面                                                         | 书名                                     | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/03/wp_editor_md_86017703015ce48f221a2a34d2a43c45.jpg) | GPU Zen 1：Advanced Rendering Techniques | https://www.stubbornhuang.com/899/  |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/GPU-Zen-2%EF%BC%9AAdvanced-Rendering-Techniques%E5%B0%81%E9%9D%A2.jpg) | GPU Zen 2：Advanced Rendering Techniques | https://www.stubbornhuang.com/1341/ |

### GPU Pro 360

| 封面                                                         | 书名                                         | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_076e94699cc4999c2db5333871c85769.jpg) | GPU Pro 360 – Guide to 3D Engine Design      | https://www.stubbornhuang.com/1320/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_3fba0ee75a290f5545351fcf829ce977.jpg) | GPU Pro 360 – Guide to Geometry Manipulation | https://www.stubbornhuang.com/1321/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_1632bc7b9e7eb19e1c21ba75eccdb91a.jpg) | GPU Pro 360 – Guide to GPGPU                 | https://www.stubbornhuang.com/1322/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_727fa008e4228810218d7f0e5e6029b1.jpg) | GPU Pro 360 – Guide to Image Space           | https://www.stubbornhuang.com/1323/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_9a83eace8130464401e90c0ef4b20fb6.jpg) | GPU Pro 360 – Guide to Lighting              | https://www.stubbornhuang.com/1328/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_9990cdc0e4fe3640123ce13f50e34695.jpg) | GPU Pro 360 – Guide to Mobile Devices        | https://www.stubbornhuang.com/1333/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_0d3f112b0ccba721c7c80f30bdfdf213.jpg) | GPU Pro 360 – Guide to Rendering             | https://www.stubbornhuang.com/1337/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_1ea861e925d23f3177375e4b060df61a.jpg) | GPU Pro 360 – Guide to Shadows               | https://www.stubbornhuang.com/1339/ |

### Foundations of Game Engine Development

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_ddf2c37252533fe1fcb50bd050f90377.jpg) | Foundations of Game Engine Development, Volume 1 Mathematics | https://www.stubbornhuang.com/1345/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/Foundations-of-Game-Engine-Development-Volume-2-Rendering%E5%B0%81%E9%9D%A2.png) | Foundations of Game Engine Development, Volume 2 Rendering   | https://www.stubbornhuang.com/1347/ |

### 3D Math Primer for Graphics and Game Development

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](https://www.stubbornhuang.com/wp-content/uploads/2021/05/wp_editor_md_2be65fec5c3a96a7ae38983bfdeb59da.jpg) | 3D Math Primer for Graphics and Game Development (First Edition) | https://www.stubbornhuang.com/1356/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | 3D Math Primer for Graphics and Game Development (Second Edition) | https://www.stubbornhuang.com/1358/ |

### Essential Mathematics for Games and Interactive Applications

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Essential Mathematics for Games and Interactive Applications(First Edition) | https://www.stubbornhuang.com/1349/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Essential Mathematics for Games and Interactive Applications(Second Edition) | https://www.stubbornhuang.com/1353/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Essential Mathematics for Games and Interactive Applications(Third Edition) | https://www.stubbornhuang.com/1354/ |

### Jim Blinn's Corner

| 封面                                                         | 书名                                                   | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Jim Blinn’s Corner – A Trip Down the Graphics Pipeline | https://www.stubbornhuang.com/1316/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Jim Blinn‘s Corner – Dirty Pixels                      | https://www.stubbornhuang.com/1317/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Jim Blinn’s Corner – Notation, Notation, Notation      | https://www.stubbornhuang.com/1318/ |

### Game Engine Gems

| 封面                                                         | 书名               | 下载链接                            |
| ------------------------------------------------------------ | ------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Engine Gems 1 | https://www.stubbornhuang.com/1234/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Engine Gems 2 | https://www.stubbornhuang.com/1238/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Engine Gems 3 | https://www.stubbornhuang.com/1240/ |

### Game Engine Architecture

| 封面                                                         | 书名                                      | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Engine Architecture (First Edition)  | https://www.stubbornhuang.com/1187/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Engine Architecture (Second Edition) | https://www.stubbornhuang.com/1189/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Engine Architecture (Third Edition)  | https://www.stubbornhuang.com/1197/ |

### Graphics Gems

| 封面                                                         | 书名              | 下载链接                            |
| ------------------------------------------------------------ | ----------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Graphics Gems I   | https://www.stubbornhuang.com/1242/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Graphics Gems II  | https://www.stubbornhuang.com/1244/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Graphics Gems III | https://www.stubbornhuang.com/1249/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Graphics Gems IV  | https://www.stubbornhuang.com/1254/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Graphics Gems V   | https://www.stubbornhuang.com/1255/ |

### Ray Tracing in One Week

| 封面                                                         | 书名                                | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Ray Tracing in One Weekend          | https://www.stubbornhuang.com/1085/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Ray Tracing – The Next Week         | https://www.stubbornhuang.com/1088/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Ray Tracing – The Rest of Your Life | https://www.stubbornhuang.com/1091/ |

### Game Programming Gems

| 封面                                                         | 书名                    | 下载链接                            |
| ------------------------------------------------------------ | ----------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Gems 1 | https://www.stubbornhuang.com/1258/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Gems 2 | https://www.stubbornhuang.com/1261/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Gems 3 | https://www.stubbornhuang.com/1263/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Gems 4 | https://www.stubbornhuang.com/1267/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Gems 5 | 缺失                                |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Gems 6 | https://www.stubbornhuang.com/1271/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Gems 7 | https://www.stubbornhuang.com/1273/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Gems 8 | https://www.stubbornhuang.com/1274/ |

### The HDRI Handbook

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | The HDRI Handbook- High Dynamic Range Imaging for Photographers and CG Artists | https://www.stubbornhuang.com/1217/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | The HDRI Handbook 2.0- High Dynamic Range Imaging for Photographers and CG Artists | https://www.stubbornhuang.com/1219/ |

### High Dynamic Range Imaging

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | High Dynamic Range Imaging- Acquisition, Display, and Image-Based Lighting ( First Edition ) | https://www.stubbornhuang.com/1211/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | High Dynamic Range Imaging- Acquisition, Display, and Image-Based Lighting ( Second Edition ) | https://www.stubbornhuang.com/1214/ |

### Interactive Computer Graphics

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Interactive Computer Graphics – A top-down approach with shader-based OpenGL(Six 6th Edition) | https://www.stubbornhuang.com/1204/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Interactive Computer Graphics – A top-down approach with WebGL(Seven 7th Edition) | https://www.stubbornhuang.com/1205/ |

### Realistic Image Synthesis Using Photon Mapping

| 封面                                                         | 书名                                           | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Realistic Image Synthesis Using Photon Mapping | https://www.stubbornhuang.com/1200/ |

### Ray Tracing Gems

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Ray Tracing Gems – High-Quality and Real-Time Rendering with DXR and Other APIs | https://www.stubbornhuang.com/1185/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Ray Tracing Gems II - Next Generation Real-Time Rendering with DXR, Vulkan, and OptiX-Apress | https://www.stubbornhuang.com/1551/ |

### Efficient Illumination Algorithms for Global Illumination In Interactive and Real-Time Rendering

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Efficient Illumination Algorithms for Global Illumination In Interactive and Real-Time Rendering | https://www.stubbornhuang.com/1177/ |

### Mathematics for 3D Game Programming and Computer Graphics

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Mathematics for 3D Game Programming and Computer Graphics, Second Edition | https://www.stubbornhuang.com/1174/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Mathematics for 3D Game Programming and Computer Graphics, Third Edition | https://www.stubbornhuang.com/1175/ |

### Real-Time Shadows

| 封面                                                         | 书名              | 下载链接                            |
| ------------------------------------------------------------ | ----------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Real-Time Shadows | https://www.stubbornhuang.com/1074/ |

### Advanced global illumination

| 封面                                                         | 书名                                       | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Advanced global illumination (2nd Edition) | https://www.stubbornhuang.com/1056/ |

### Computer Graphics Principles and Practice

| 封面                                                         | 书名                                                    | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics Principles and Practice (3rd edition) | https://www.stubbornhuang.com/1054/ |

### Computer Graphics Through OpenGL – From Theory to Experiments

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics Through OpenGL – From Theory to Experiments (Second Edition) | https://www.stubbornhuang.com/1176/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics Through OpenGL – From Theory to Experiments (Third Edition) | https://www.stubbornhuang.com/1049/ |

### Game Physics Engine Development

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Physics Engine Development (First Edition)              | https://www.stubbornhuang.com/1377/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Physics Engine Development- How to Build a Robust Commercial-Grade Physics Engine for your Game (Second Edition) | https://www.stubbornhuang.com/1359/ |

### Graphics Shaders - Theory and Practice

| 封面                                                         | 书名                                                    | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Graphics Shaders – Theory and Practice (Second Edition) | https://www.stubbornhuang.com/1361/ |

### Insights

| 封面                                                         | 书名            | 下载链接                            |
| ------------------------------------------------------------ | --------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL Insights | https://www.stubbornhuang.com/1366/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | WebGL Insights  | https://www.stubbornhuang.com/1367/ |

### The Magic of Computer Graphics - Landmarks in Rendering

| 封面                                                         | 书名                                                    | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | The Magic of Computer Graphics – Landmarks in Rendering | https://www.stubbornhuang.com/1368/ |

### OpenGL Programming Guide

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL Programming Guide - The Official Guide to Learning OpenGL, Versions 3.0 and 3.1 (Seventh Edition) | https://www.stubbornhuang.com/1474/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL Programming Guide - The Official Guide to Learning OpenGL, Version 4.3 (Eighth Edition) | https://www.stubbornhuang.com/1485/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL Programming Guide - The Official Guide to Learning OpenGL, Version 4.5 with SPIR-V (Ninth Edition) | https://www.stubbornhuang.com/1488/ |

### OpenGL SuperBible

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL SuperBible - Comprehensive Tutorial and Reference (Fifth Edition) | https://www.stubbornhuang.com/1492/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL SuperBible - Comprehensive Tutorial and Reference (Sixth Edition) | https://www.stubbornhuang.com/1494/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL SuperBible - Comprehensive Tutorial and Reference (Seventh Edition) | https://www.stubbornhuang.com/1499/ |

### OpenGL 4.0 Shading Language Cookbook

| 封面                                                         | 书名                                                  | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL 4.0 Shading Language Cookbook (First Edition)  | https://www.stubbornhuang.com/1369/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL 4.0 Shading Language Cookbook (Second Edition) | https://www.stubbornhuang.com/1370/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL 4.0 Shading Language Cookbook (Third Edition)  | https://www.stubbornhuang.com/1373/ |

### OpenGL Shading Language

| 封面                                                         | 书名                                    | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL Shading Language (Third Edition) | https://www.stubbornhuang.com/1374/ |

### Fluid Engine Development

| 封面                                                         | 书名                     | 下载链接                            |
| ------------------------------------------------------------ | ------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Fluid Engine Development | https://www.stubbornhuang.com/1378/ |

### Fluid Simulation for Computer Graphics

| 封面                                                         | 书名                                                   | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Fluid Simulation for Computer Graphics, First Edition  | https://www.stubbornhuang.com/1060/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Fluid Simulation for Computer Graphics, Second Edition | https://www.stubbornhuang.com/1063/ |

### The Nature of Code - Simulating Natural Systems with Processing

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | The Nature of Code - Simulating Natural Systems with Processing | https://www.stubbornhuang.com/1610/ |

### Game Physics Pearls

| 封面                                                         | 书名                | 下载链接                            |
| ------------------------------------------------------------ | ------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Physics Pearls | https://www.stubbornhuang.com/1379/ |

### Game Physics

| 封面                                                         | 书名                          | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Physics (First Edition)  | https://www.stubbornhuang.com/1381/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Physics (Second Edition) | https://www.stubbornhuang.com/1382/ |

### Game Physics Cookbook

| 封面                                                         | 书名                  | 下载链接                            |
| ------------------------------------------------------------ | --------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Physics Cookbook | https://www.stubbornhuang.com/1746/ |

### Physics for Game Developers

| 封面                                                         | 书名                                        | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Physics for Game Developers(First Edition)  | https://www.stubbornhuang.com/1383/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Physics for Game Developers(Second Edition) | https://www.stubbornhuang.com/1385/ |

### Physics for Game Programmers

| 封面                                                         | 书名                         | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Physics for Game Programmers | https://www.stubbornhuang.com/1386/ |

### Physics Modeling for Game Programmers

| 封面                                                         | 书名                                  | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Physics Modeling for Game Programmers | https://www.stubbornhuang.com/1389/ |

### Physics-Based Animation

| 封面                                                         | 书名                    | 下载链接                            |
| ------------------------------------------------------------ | ----------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Physics-Based Animation | https://www.stubbornhuang.com/1390/ |

### Foundations of Physically Based Modeling and Animation

| 封面                                                         | 书名                                                   | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Foundations of Physically Based Modeling and Animation | https://www.stubbornhuang.com/1223/ |

### Production Volume Rendering - Design and Implementation

| 封面                                                         | 书名                                                    | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Production Volume Rendering – Design and Implementation | https://www.stubbornhuang.com/1391/ |

### Collision Detection in Interactive 3D Environments

| 封面                                                         | 书名                                               | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Collision Detection in Interactive 3D Environments | https://www.stubbornhuang.com/1392/ |

### Real-Time Collision Detection

| 封面                                                         | 书名                          | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Real-Time Collision Detection | https://www.stubbornhuang.com/1395/ |

### Introduction to 3D Game Programming with DirectX

| 封面                                                         | 书名                                                 | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Introduction to 3D Game Programming with DirectX 9.0 | https://www.stubbornhuang.com/2125/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Introduction to 3D Game Programming with DirectX 10  | https://www.stubbornhuang.com/2116/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Introduction to 3D Game Programming with DirectX 11  | https://www.stubbornhuang.com/1554/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Introduction to 3D Game Programming with DirectX 12  | https://www.stubbornhuang.com/1397/ |

### Practical Rendering and Computation with Direct3D 11

| 封面                                                         | 书名                                                 | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Practical Rendering and Computation with Direct3D 11 | https://www.stubbornhuang.com/1665/ |

### Real-Time 3D Rendering with DirectX and HLSL - A Practical Guide to Graphics Programming

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Real-Time 3D Rendering with DirectX and HLSL - A Practical Guide to Graphics Programming | https://www.stubbornhuang.com/1668/ |

### The Art of Fluid Animation

| 封面                                                         | 书名                       | 下载链接                            |
| ------------------------------------------------------------ | -------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | The Art of Fluid Animation | https://www.stubbornhuang.com/1418/ |

### Ray Tracing from the Ground Up

| 封面                                                         | 书名                           | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Ray Tracing from the Ground Up | https://www.stubbornhuang.com/1420/ |

### Character Animation With Direct3D

| 封面                                                         | 书名                              | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Character Animation With Direct3D | https://www.stubbornhuang.com/1421/ |

### Real-time 3D Character Animation with Visual C++

| 封面                                                         | 书名                                             | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Real-time 3D Character Animation with Visual C++ | https://www.stubbornhuang.com/1674/ |

### Vulkan Programming Guide - The Official Guide to Learning Vulkan

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Vulkan Programming Guide – The Official Guide to Learning Vulkan | https://www.stubbornhuang.com/1423/ |

### Learning Vulkan

| 封面                                                         | 书名            | 下载链接                            |
| ------------------------------------------------------------ | --------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Learning Vulkan | https://www.stubbornhuang.com/1501/ |

### Vulkan Cookbook - Work through recipes to unlock the full potential of the next generation graphics API-Vulkan

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Vulkan Cookbook – Work through recipes to unlock the full potential of the next generation graphics API-Vulkan | https://www.stubbornhuang.com/1502/ |

### GLSL Essentials - Enrich your 3D scenes with the power of GLSL

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | GLSL Essentials – Enrich your 3D scenes with the power of GLSL | https://www.stubbornhuang.com/1466/ |

### Computer Animation - Algorithms and Techniques

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Animation – Algorithms and Techniques (First Edition) | https://www.stubbornhuang.com/1467/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Animation – Algorithms and Techniques (Third Edition) | https://www.stubbornhuang.com/1471/ |

### The Ray Tracer Challenge - A Test-Driven Guide to Your First 3D Renderer

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | The Ray Tracer Challenge – A Test-Driven Guide to Your First 3D Renderer | https://www.stubbornhuang.com/1556/ |

### Ray Tracing - A Tool for All

| 封面                                                         | 书名                         | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Ray Tracing - A Tool for All | https://www.stubbornhuang.com/1558/ |

### Cloth Simulation for Computer Graphics

| 封面                                                         | 书名                                   | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Cloth Simulation for Computer Graphics | https://www.stubbornhuang.com/1560/ |

### Real-Time Volume Graphics

| 封面                                                         | 书名                      | 下载链接                            |
| ------------------------------------------------------------ | ------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Real-Time Volume Graphics | https://www.stubbornhuang.com/1564/ |

### Computer Graphics from Scratch - A Programmer's Introduction to 3D Rendering

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics from Scratch - A Programmer's Introduction to 3D Rendering | https://www.stubbornhuang.com/1569/ |

### 3D Game Engine Design - A Practical Approach to Real-Time Computer Graphics

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | 3D Game Engine Design - A Practical Approach to Real-Time Computer Graphics | https://www.stubbornhuang.com/1592/ |

### 3D Game Engine Architecture - Engineering Real-Time Applications with Wild Magic

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | 3D Game Engine Architecture - Engineering Real-Time Applications with Wild Magic | https://www.stubbornhuang.com/1664/ |

### Real-Time Cameras - A Guide for Game Designers and Developers

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Real-Time Cameras – A Guide for Game Designers and Developers | https://www.stubbornhuang.com/1596/ |

### Game AI Pro - Collected Wisdom of Game AI Professionals

| 封面                                                         | 书名                                                      | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game AI Pro - Collected Wisdom of Game AI Professionals   | https://www.stubbornhuang.com/1599/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game AI Pro 2 – Collected Wisdom of Game AI Professionals | https://www.stubbornhuang.com/1600/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game AI Pro 3 – Collected Wisdom of Game AI Professionals | https://www.stubbornhuang.com/1601/ |

### Game AI Pro 360

| 封面                                                         | 书名                                                | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game AI Pro 360 – Guide to Architecture             | https://www.stubbornhuang.com/1602/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game AI Pro 360 - Guide to Character Behavior       | https://www.stubbornhuang.com/1604/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game AI Pro 360 – Guide to Movement and Pathfinding | https://www.stubbornhuang.com/1605/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game AI Pro 360 - Guide to Tactics and Strategy     | https://www.stubbornhuang.com/1607/ |

### Visualizing Quaternions

| 封面                                                         | 书名                    | 下载链接                            |
| ------------------------------------------------------------ | ----------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Visualizing Quaternions | https://www.stubbornhuang.com/1609/ |

### Quaternions for Computer Graphics

| 封面                                                         | 书名                                               | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Quaternions for Computer Graphics , First Edition  | https://www.stubbornhuang.com/1612/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Quaternions for Computer Graphics , Second Edition | https://www.stubbornhuang.com/2206  |

### 3D Engine Design for Virtual Globes

| 封面                                                         | 书名                                | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | 3D Engine Design for Virtual Globes | https://www.stubbornhuang.com/1613/ |

### Texturing and Modeling - A Procedural Approach

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Texturing and Modeling – A Procedural Approach, Third Edition | https://www.stubbornhuang.com/1614/ |

### Level of Detail for 3D Graphics

| 封面                                                         | 书名                            | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Level of Detail for 3D Graphics | https://www.stubbornhuang.com/1624/ |

### Non-Photorealistic Rendering

| 封面                                                         | 书名                         | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Non-Photorealistic Rendering | https://www.stubbornhuang.com/1631/ |

### Non-Photorealistic Computer Graphics - Modeling, Rendering, and Animation

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Non-Photorealistic Computer Graphics - Modeling, Rendering, and Animation | https://www.stubbornhuang.com/1634/ |

### The Algorithms and Principles of Non-photorealistic Graphics - Artistic Rendering and Cartoon Animation

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | The Algorithms and Principles of Non-photorealistic Graphics - Artistic Rendering and Cartoon Animation | https://www.stubbornhuang.com/1635/ |

### Digital Character Development - Theory and Practice

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Digital Character Development - Theory and Practice , First Edition | https://www.stubbornhuang.com/1677/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Digital Character Development - Theory and Practice , Second Edition | https://www.stubbornhuang.com/1678/ |

### 3D Graphics Rendering Cookbook - A comprehensive guide to exploring rendering algorithms in modern OpenGL and Vulkan

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | 3D Graphics Rendering Cookbook - A comprehensive guide to exploring rendering algorithms in modern OpenGL and Vulkan | https://www.stubbornhuang.com/1679/ |

### Tricks of the 3D Game Programming Gurus - Advanced 3D Graphics and Rasterization

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Tricks of the 3D Game Programming Gurus - Advanced 3D Graphics and Rasterization | https://www.stubbornhuang.com/1682/ |

### Graphics Programming Methods

| 封面                                                         | 书名                         | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Graphics Programming Methods | https://www.stubbornhuang.com/1685/ |

### Principles of Digital Image Synthesis

| 封面                                                         | 书名                                             | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Principles of Digital Image Synthesis , Volume 1 | https://www.stubbornhuang.com/1693/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Principles of Digital Image Synthesis , Volume 2 | https://www.stubbornhuang.com/1693/ |

### Digital Image Processing

| 封面                                                         | 书名                                      | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Digital Image Processing , Second Edition | https://www.stubbornhuang.com/1714/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Digital Image Processing , Third Edition  | https://www.stubbornhuang.com/1717/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Digital Image Processing , Fourth Edition | https://www.stubbornhuang.com/1718/ |

### Game Development Tools

| 封面                                                         | 书名                   | 下载链接                            |
| ------------------------------------------------------------ | ---------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Development Tools | https://www.stubbornhuang.com/1696/ |

### Div, Grad, Curl, and All That - An Informal Text on Vector Calculus

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Div, Grad, Curl, and All That – An Informal Text on Vector Calculus , Third Edition | https://www.stubbornhuang.com/1720/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Div, Grad, Curl, and All That - An Informal Text on Vector Calculus , Forth Edition | https://www.stubbornhuang.com/1721/ |

### Game Programming Algorithms and Techniques - A Platform-Agnostic Approach

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Algorithms and Techniques - A Platform-Agnostic Approach | https://www.stubbornhuang.com/1729/ |

### Game Programming Patterns

| 封面                                                         | 书名                      | 下载链接                            |
| ------------------------------------------------------------ | ------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Patterns | https://www.stubbornhuang.com/1730/ |

### Game Programming Golden Rules

| 封面                                                         | 书名                          | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Game Programming Golden Rules | https://www.stubbornhuang.com/1731/ |

### Augmented Reality - Principles and Practice

| 封面                                                         | 书名                                        | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Augmented Reality - Principles and Practice | https://www.stubbornhuang.com/1734/ |

### Practical Augmented Reality - A Guide to the Technologies, Applications, and Human Factors for AR and VR-Addison

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Practical Augmented Reality - A Guide to the Technologies, Applications, and Human Factors for AR and VR-Addison | https://www.stubbornhuang.com/1735/ |

### VR Developer Gems

| 封面                                                         | 书名              | 下载链接                            |
| ------------------------------------------------------------ | ----------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | VR Developer Gems | https://www.stubbornhuang.com/1739/ |

### Image Objects - An Archaeology of Computer Graphics

| 封面                                                         | 书名                                                | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Image Objects - An Archaeology of Computer Graphics | https://www.stubbornhuang.com/1740/ |

### Advanced High Dynamic Range Imaging

| 封面                                                         | 书名                                                | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Advanced High Dynamic Range Imaging, First Edition  | https://www.stubbornhuang.com/1744/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Advanced High Dynamic Range Imaging, Second Edition | https://www.stubbornhuang.com/1745/ |

### A Biography of the Pixel

| 封面                                                         | 书名                     | 下载链接                            |
| ------------------------------------------------------------ | ------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | A Biography of the Pixel | https://www.stubbornhuang.com/1750/ |

### Computer Graphics Programming in OpenGL with C++

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics Programming in OpenGL with C++, First Edition | https://www.stubbornhuang.com/1753/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics Programming in OpenGL with C++, Second Edition | https://www.stubbornhuang.com/1757/ |

### GPGPU Programming for Games and Science

| 封面                                                         | 书名                                    | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | GPGPU Programming for Games and Science | https://www.stubbornhuang.com/1760/ |

### Computer Facial Animation

| 封面                                                         | 书名                                       | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Facial Animation , Second Edition | https://www.stubbornhuang.com/1762/ |

### Handbook of Digital Image Synthesis - Scientific Foundations of Rendering

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Handbook of Digital Image Synthesis - Scientific Foundations of Rendering | https://www.stubbornhuang.com/1764/ |

### Image Content Retargeting - Maintaining Color, Tone, and Spatial Consistency

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Image Content Retargeting - Maintaining Color, Tone, and Spatial Consistency | https://www.stubbornhuang.com/1767/ |

### Introduction to Computer Graphics - A Practical Learning Approach

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Introduction to Computer Graphics - A Practical Learning Approach | https://www.stubbornhuang.com/1768/ |

### Direct3D Rendering Cookbook

| 封面                                                         | 书名                        | 下载链接                            |
| ------------------------------------------------------------ | --------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Direct3D Rendering Cookbook | https://www.stubbornhuang.com/1771/ |

### Practical Algorithms for 3D Computer Graphics

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Practical Algorithms for 3D Computer Graphics, Second Edition | https://www.stubbornhuang.com/1772/ |

### Computer Graphics - From Pixels to Programmable Graphics Hardware

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics - From Pixels to Programmable Graphics Hardware | https://www.stubbornhuang.com/1774/ |

### The History of Visual Magic in Computers - How Beautiful Images are Made in CAD, 3D, VR and AR

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | The History of Visual Magic in Computers - How Beautiful Images are Made in CAD, 3D, VR and AR | https://www.stubbornhuang.com/1779/ |

### WebGL Programming Guide - Interactive 3D Graphics Programming with WebGL

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | WebGL Programming Guide - Interactive 3D Graphics Programming with WebGL | https://www.stubbornhuang.com/1781/ |

### Beginning DirectX 11 Game Programming

| 封面                                                         | 书名                                  | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Beginning DirectX 11 Game Programming | https://www.stubbornhuang.com/1782/ |

### The CUDA Handbook - A Comprehensive Guide to GPU Programming

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | The CUDA Handbook - A Comprehensive Guide to GPU Programming | https://www.stubbornhuang.com/1784/ |

### OpenGL Development Cookbook

| 封面                                                         | 书名                        | 下载链接                            |
| ------------------------------------------------------------ | --------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | OpenGL Development Cookbook | https://www.stubbornhuang.com/1786/ |

### GPU Computing Gems

| 封面                                                         | 书名                                | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | GPU Computing Gems, Jade Edition    | https://www.stubbornhuang.com/1789/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | GPU Computing Gems, Emerald Edition | https://www.stubbornhuang.com/1807/ |

### 3D Graphics for Game Programming

| 封面                                                         | 书名                             | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | 3D Graphics for Game Programming | https://www.stubbornhuang.com/1819/ |

### Light & Skin Interactions - Simulations for Computer Graphics Applications

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Light & Skin Interactions - Simulations for Computer Graphics Applications | https://www.stubbornhuang.com/1828/ |

### Video Game Optimization

| 封面                                                         | 书名                    | 下载链接                            |
| ------------------------------------------------------------ | ----------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Video Game Optimization | https://www.stubbornhuang.com/1829/ |

### Mathematics for Computer Graphics

| 封面                                                         | 书名                                               | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Mathematics for Computer Graphics , Second Edition | https://www.stubbornhuang.com/1832/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Mathematics for Computer Graphics , Third Edition  | https://www.stubbornhuang.com/1833/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Mathematics for Computer Graphics , Fourth Edition | https://www.stubbornhuang.com/1835/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Mathematics for Computer Graphics , Fifth Edition  | https://www.stubbornhuang.com/1841/ |

### An Integrated Introduction to Computer Graphics and Geometric Modeling

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | An Integrated Introduction to Computer Graphics and Geometric Modeling | https://www.stubbornhuang.com/1842/ |

### Digital Modeling of Material Appearance

| 封面                                                         | 书名                                    | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Digital Modeling of Material Appearance | https://www.stubbornhuang.com/1843/ |

### Color Imaging - Fundamentals and Applications

| 封面                                                         | 书名                                          | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Color Imaging - Fundamentals and Applications | https://www.stubbornhuang.com/1844/ |

### Data Structures and Algorithms for Game Developers

| 封面                                                         | 书名                                               | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Data Structures and Algorithms for Game Developers | https://www.stubbornhuang.com/1847/ |

### Geometric Data Structures for Computer Graphics

| 封面                                                         | 书名                                            | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Geometric Data Structures for Computer Graphics | https://www.stubbornhuang.com/1853/ |

### Advances in GPU Research and Practice

| 封面                                                         | 书名                                  | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Advances in GPU Research and Practice | https://www.stubbornhuang.com/1860/ |

### Learn OpenGL - Learn modern OpenGL graphics programming in a step-by-step fashion

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Learn OpenGL - Learn modern OpenGL graphics programming in a step-by-step fashion | https://www.stubbornhuang.com/1875/ |

### Simulating Humans - Computer Graphics Animation and Control

| 封面                                                         | 书名                                                        | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Simulating Humans - Computer Graphics Animation and Control | https://www.stubbornhuang.com/1882/ |

### WebGL Gems - Learn How To Create 3D Worlds And Games For Modern Web Browsers

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | WebGL Gems - Learn How To Create 3D Worlds And Games For Modern Web Browsers, First Edition | https://www.stubbornhuang.com/1887/ |

### Computer Graphics, C Version

| 封面                                                         | 书名                                          | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics, C Version , Second Edition | https://www.stubbornhuang.com/1888/ |

### Vector Analysis for Computer Graphics

| 封面                                                         | 书名                                                   | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Vector Analysis for Computer Graphics , First Edition  | https://www.stubbornhuang.com/1900/ |
| [![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)](https://www.stubbornhuang.com/wp-content/uploads/2022/01/wp_editor_md_f0125e18f9039ea7965c64ee3dfa5e2b.jpg) | Vector Analysis for Computer Graphics , Second Edition | https://www.stubbornhuang.com/1905/ |

### Calculus for Computer Graphics

| 封面                                                         | 书名                                            | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Calculus for Computer Graphics , First Edition  | https://www.stubbornhuang.com/1906/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Calculus for Computer Graphics , Second Edition | https://www.stubbornhuang.com/1910/ |

### Digital Lighting & Rendering

| 封面                                                         | 书名                                         | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Digital Lighting & Rendering , First Edition | https://www.stubbornhuang.com/1911/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Digital Lighting & Rendering , Third Edition | https://www.stubbornhuang.com/1915/ |

### Foundations of 3D computer graphics

| 封面                                                         | 书名                                | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Foundations of 3D computer graphics | https://www.stubbornhuang.com/1918/ |

### Computer Graphics with OpenGL

| 封面                                                         | 书名                                           | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics with OpenGL , Third Edition  | https://www.stubbornhuang.com/1922/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics with OpenGL , Fourth Edition | https://www.stubbornhuang.com/1924/ |

### Practical Linear Algebra - A Geometry Toolbox

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Practical Linear Algebra - A Geometry Toolbox , First Edition | https://www.stubbornhuang.com/1926/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Practical Linear Algebra - A Geometry Toolbox , Third Edition | https://www.stubbornhuang.com/1930/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Practical Linear Algebra - A Geometry Toolbox , Fourth Edition | https://www.stubbornhuang.com/1931/ |

### An Introduction to Ray Tracing

| 封面                                                         | 书名                           | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | An Introduction to Ray Tracing | https://www.stubbornhuang.com/1947/ |

### AI Game Engine Programming

| 封面                                                         | 书名                                        | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | AI Game Engine Programming , First Edition  | https://www.stubbornhuang.com/1954/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | AI Game Engine Programming , Second Edition | https://www.stubbornhuang.com/1956/ |

### AI Game Programming Wisdom

| 封面                                                         | 书名                         | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | AI Game Programming Wisdom   | https://www.stubbornhuang.com/1957/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | AI Game Programming Wisdom 4 | https://www.stubbornhuang.com/1959/ |

### Artificial Intelligence for Games

| 封面                                                         | 书名                                               | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Artificial Intelligence for Games , First Edition  | https://www.stubbornhuang.com/1964/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Artificial Intelligence for Games , Second Edition | https://www.stubbornhuang.com/1968/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Artificial Intelligence for Games , Third Edition  | https://www.stubbornhuang.com/2298/ |

### Behavioral Mathematics for Game AI

| 封面                                                         | 书名                               | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Behavioral Mathematics for Game AI | https://www.stubbornhuang.com/1972/ |

### Cloth Modeling and Animation

| 封面                                                         | 书名                         | 下载链接                            |
| ------------------------------------------------------------ | ---------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Cloth Modeling and Animation | https://www.stubbornhuang.com/1996/ |

### Virtual Clothing - Theory and Practice

| 封面                                                         | 书名                                   | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Virtual Clothing - Theory and Practice | https://www.stubbornhuang.com/1998/ |

### Computer Graphics and Geometric Modelling - Implementation and Algorithms

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computer Graphics and Geometric Modelling - Implementation and Algorithms | https://www.stubbornhuang.com/2020/ |

### Designing the User Experience of Game Development Tools

| 封面                                                         | 书名                                                    | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Designing the User Experience of Game Development Tools | https://www.stubbornhuang.com/2023/ |

### Real-Time 3D Graphics with WebGL 2

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Real-Time 3D Graphics with WebGL 2 - Build interactive 3D applications with JavaScript and WebGL 2 (OpenGL ES 3.0), Second Edition | https://www.stubbornhuang.com/2196/ |

### Rotation Transforms for Computer Graphics

| 封面                                                         | 书名                                                      | 下载链接                           |
| ------------------------------------------------------------ | --------------------------------------------------------- | ---------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Rotation Transforms for Computer Graphics , First Edition | https://www.stubbornhuang.com/2302 |

### Matrix Transforms for Computer Games and Animation

| 封面                                                         | 书名                                               | 下载链接                           |
| ------------------------------------------------------------ | -------------------------------------------------- | ---------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Matrix Transforms for Computer Games and Animation | https://www.stubbornhuang.com/2309 |

### Mathematical Basics of Motion and Deformation in Computer Graphics

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Mathematical Basics of Motion and Deformation in Computer Graphics , Second Edition | https://www.stubbornhuang.com/2311/ |

### Geometric and Discrete Path Planning for Interactive Virtual Worlds

| 封面                                                         | 书名                                                         | 下载链接                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Geometric and Discrete Path Planning for Interactive Virtual Worlds | https://www.stubbornhuang.com/2316 |

### Hands-On C++ Game Animation Programming

| 封面                                                         | 书名                                    | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------- | ----------------------------------- |
| [![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)](https://www.stubbornhuang.com/wp-content/uploads/2022/12/wp_editor_md_07272b7fb825157cab1bd7bdb040fb5b.jpg) | Hands-On C++ Game Animation Programming | https://www.stubbornhuang.com/2446/ |

### An Introduction to Computational Fluid Dynamics - The Finite Volume Method

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| [![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)](https://www.stubbornhuang.com/wp-content/uploads/2023/02/wp_editor_md_3f69bc69281c5854e94441bc417b764a.jpg) | An Introduction to Computational Fluid Dynamics - The Finite Volume Method (First Edition) | https://www.stubbornhuang.com/2503/ |
| [![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)](https://www.stubbornhuang.com/wp-content/uploads/2023/02/wp_editor_md_2c5265bfecce8878c9ca25d0361307b4.jpg) | An Introduction to Computational Fluid Dynamics - The Finite Volume Method (Second Edition) | https://www.stubbornhuang.com/2504/ |

### Mastering Graphics Programming with Vulkan

| 封面                                                         | 书名                                       | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Mastering Graphics Programming with Vulkan | https://www.stubbornhuang.com/2616/ |

### Practical Shader Development - Vertex and Fragment Shaders for Game Developers

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| [![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)](https://www.stubbornhuang.com/wp-content/uploads/2023/08/wp_editor_md_5d2a7c7f189dccf598b9844baf2947f2.jpg) | Practical Shader Development - Vertex and Fragment Shaders for Game Developers | https://www.stubbornhuang.com/2750/ |

### The Modern Vulkan Cookbook - A practical guide to 3D graphics and advanced real-time rendering techniques in Vulkan

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| [![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)](https://www.stubbornhuang.com/wp-content/uploads/2024/07/wp_editor_md_468c2af6dd0984352aae7c0b264ee2f1.jpg) | The Modern Vulkan Cookbook – A practical guide to 3D graphics and advanced real-time rendering techniques in Vulkan | https://www.stubbornhuang.com/3050/ |

## 计算几何

### Polygon Mesh Processing

| 封面                                                         | 书名                    | 下载链接                            |
| ------------------------------------------------------------ | ----------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Polygon Mesh Processing | https://www.stubbornhuang.com/1058/ |

### Computational Geometry – Algorithms and Applications

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computational Geometry – Algorithms and Applications, First Edition | https://www.stubbornhuang.com/1428/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computational Geometry – Algorithms and Applications, Second Edition | https://www.stubbornhuang.com/1430/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computational Geometry - Algorithms and Applications, Third Edition | https://www.stubbornhuang.com/900/  |

### Handbook of Discrete and Computational Geometry

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Handbook of Discrete and Computational Geometry, First Edition | https://www.stubbornhuang.com/1424/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Handbook of Discrete and Computational Geometry, Second Edition | https://www.stubbornhuang.com/1426/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Handbook of Discrete and Computational Geometry, Third Edition | https://www.stubbornhuang.com/1102/ |

### Geometric tools for computer graphics

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Geometric tools for computer graphics(Philip J. Schneider, and David H. Eberly) | https://www.stubbornhuang.com/1100/ |

### Computational Geometry in C

| 封面                                                         | 书名                                        | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computational Geometry in C, First Edition  | https://www.stubbornhuang.com/1432/ |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computational Geometry in C, Second Edition | https://www.stubbornhuang.com/1096/ |

### Computational Geometry：An Introduction

| 封面                                                         | 书名                                    | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computational Geometry：An Introduction | https://www.stubbornhuang.com/1093/ |

### Geometric Algebra for Computer Science - An Object-Oriented Approach to Geometry

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Geometric Algebra for Computer Science – An Object-Oriented Approach to Geometry (First Edition) | https://www.stubbornhuang.com/1360/ |

### Isosurfaces - Geometry, Topology, and Algorithms

| 封面                                                         | 书名                                             | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Isosurfaces – Geometry, Topology, and Algorithms | https://www.stubbornhuang.com/1364/ |

### Guide to Computational Geometry Processing Foundations, Algorithms, and Methods

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Guide to Computational Geometry Processing Foundations, Algorithms, and Methods | https://www.stubbornhuang.com/1431/ |

### Discrete and Computational Geometry

| 封面                                                         | 书名                                | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Discrete and Computational Geometry | https://www.stubbornhuang.com/1567/ |

### Robust and Error-Free Geometric Computing

| 封面                                                         | 书名                                      | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Robust and Error-Free Geometric Computing | https://www.stubbornhuang.com/1572/ |

### Implicit Curves and Surfaces - Mathematics, Data Structures and Algorithms

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Implicit Curves and Surfaces - Mathematics, Data Structures and Algorithms | https://www.stubbornhuang.com/1573/ |

### Computational Geometry - An Introduction Through Randomized Algorithms

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computational Geometry - An Introduction Through Randomized Algorithms | https://www.stubbornhuang.com/1574/ |

### Effective Computational Geometry for Curves and Surfaces

| 封面                                                         | 书名                                                     | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Effective Computational Geometry for Curves and Surfaces | https://www.stubbornhuang.com/1576/ |

### Nonlinear Computational Geometry

| 封面                                                         | 书名                             | 下载链接                            |
| ------------------------------------------------------------ | -------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Nonlinear Computational Geometry | https://www.stubbornhuang.com/1590/ |

### Handbook of Computer Aided Geometric Design

| 封面                                                         | 书名                                        | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Handbook of Computer Aided Geometric Design | https://www.stubbornhuang.com/1591/ |

### Computational Geometry on Surfaces - Performing Computational Geometry on the Cylinder, the Sphere, the Torus, and the Cone

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Computational Geometry on Surfaces - Performing Computational Geometry on the Cylinder, the Sphere, the Torus, and the Cone | https://www.stubbornhuang.com/1594/ |

### Geometry for Computer Graphics - Formulae, Examples and Proofs

| 封面                                                         | 书名                                                         | 下载链接                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Geometry for Computer Graphics - Formulae, Examples and Proofs | https://www.stubbornhuang.com/1820/ |

### Introduction to Computing with Geometry

| 封面                                                         | 书名                                    | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Introduction to Computing with Geometry | https://www.stubbornhuang.com/1878/ |

### Curves and Surfaces for Computer Graphics

| 封面                                                         | 书名                                      | 下载链接                            |
| ------------------------------------------------------------ | ----------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Curves and Surfaces for Computer Graphics | https://www.stubbornhuang.com/2128/ |

### Geometry for Programmers

| 封面                                                         | 书名                                    | 下载链接                            |
| ------------------------------------------------------------ | --------------------------------------- | ----------------------------------- |
| ![计算几何与计算机图形学必读书单整理-StubbornHuang Blog](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) | Geometry for Programmers, First Edition | https://www.stubbornhuang.com/2604/ |
