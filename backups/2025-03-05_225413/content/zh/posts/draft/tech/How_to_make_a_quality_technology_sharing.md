+++
title = '【转载】如何做一个有质量的技术分享'
date = 2025-02-12T09:28:36+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

> **转载**
> 文章作者：左耳朵耗子
> 出处：[酷 壳 – CoolShell](https://coolshell.cn/)
> 非商用

![img](https://coolshell.org/wp-content/uploads/2021/07/knowledge_sharing-300x169.jpeg)

分享信息并不难，大多数人都能做到，就算是不善言谈性格内向的技术人员，通过博客或社交媒体，或是不正式的交流，他们都能或多或少的做到。但是如果你想要做一个有质量有高度的分享，这个就难了，所谓的有质量和有高度，我心里面的定义有两点：

1）分享内容的保鲜期是很长的，

2）会被大范围的传递。我们团队内每周都在做技术分享，虽然分享的主题都很有价值，但是分享的质量参差不齐，所以，想写下这篇文章 。供大家参考。

首先，我们先扪心自问一下，我们自己觉得读到的好的技术文章是什么？我不知道大家的是什么，我个人认为的好的文章是下面这样的：

- **把复杂的问题讲解的很简单也很清楚**。比如我高中时期读到这本1978年出版的《[从一到无穷大](https://book.douban.com/subject/1441922/)》，用各种简单通俗通懂的话把各种复杂的科学知识讲的清清楚楚。还有看过的几本很好的书，有一本是《[Windows程序设计](https://book.douban.com/subject/5273955/)》，从一个hello world的程序开始一步一步教你Windows下的原生态编程。
- **有各种各样的推导和方案的比较，让你知其然知其所以然**。有了不同方案的比较，才可能让人有全面的认识。这个方面的经典作著是《[Effective C++](https://book.douban.com/subject/5387403/)》。
- **原理、为什么、思路、方法论会让人一通百通**。这里面最经典的恐怕就是《[十万个为什么](https://book.douban.com/subject/5387403/)》了，在计算机方面也有几本经典书，有《[Unix编程艺术](https://book.douban.com/subject/1467587/)》、《[设计模式](https://book.douban.com/subject/1052241/)》、《[深入理解计算机系统](https://book.douban.com/subject/1230413/)》等书，以及《[The C10K Problem](http://www.kegel.com/c10k.html)》等很多技术论文。

其实，从教科书，到专业书，再到论文，都有上面这些不错的特质。

所以，如果你想做一个好的技术分享的话，下面是我总结出来的方法，供你参考。

- **先描述好一个问题**。这样能够听众带入进来，如果这个问题是他们感同身受的，那是最好了。千万不要一上来就说What，或是直接冲进答案里。这样的分享是在灌输和填鸭。把Why说清楚。没有Why，直接谈What的技术分享，通常来说价值不大。

- How 比 What 重要

  。在讲 How 的时候，也就是如何解这个问题。

  - 先要把问题模型说清楚，有了问题模型这个框框后，方案才有意义。
  - 然后要有不同技术的比较。有了比较后，听众才会更相信你。
  - 直接上 What 的技术细节，其实没有太大意义。

- **一定要有Best Practice或方法论总结**，否则上不了档次的。也就是分享中大家可以得到的重要收获。

说明了这个模型就是：**问题 –> 方案 –> 总结。这其中是有一定的心理学模型的，具体表现如下：**

- 用问题来吸引受众，带着受众来一起思考
- 用问题模型来框住受众的思考范围，让受众聚焦
- 给出几种不同的解决方案，比较他们的优缺点，让受众有一种解决问题的参与感。
- 最后，给出最佳实践，方法论或套路，因为有了前三步的铺垫，受众欣然接受。
- 整个过程会让受众有强烈的成长感和收获感。

这里有几个示例，也是我在我司 MegaEase 内部的技术分享，供你参考（[我个人的YouTube频道](https://www.youtube.com/user/chenhaox/videhttps://www.youtube.com/channel/UCJhxX8SXcYdNWc6QMbWKs7Aos)）

技术分享：[Prometheus是怎么存储数据的](https://youtu.be/qB40kqhTyYM)（Youtube）



技术分享：[Distributed Lock Manager](https://www.youtube.com/watch?v=VnbC5RG1fEo)（Youtube）



下面是我写在我们公司内的Knowledge Sharing中的Best Practice，供参考

## Sharing Guideline

Please follow the following sharing protocols

### Understand Sharing

- Sharing is the hard way to learn knowledge. The presenter gains the biggest advantages. not audience. 分享是学习知识的最难的方式。分享者获得的好处最最多的，而不是观众。
- Sharing can open the knowledge door for the audience, but you have to walk to knowledge by yourself. 分享可以为听众打开知识的大门，但你能不能获得知识还要靠你自己。

### Best Practices

To perform a great sharing, please follow the below practices.

- Do not share a big topic, a small topic is better. A big topic could make the audience lose focus. Remember, [Less is More!](https://en.wikipedia.org/wiki/Minimalism#Minimalist_design_and_architecture)
- Sharing time less than 60 mins is the best.
- English language for slides is preferred.
- While prepare the sharing contents, it’s better to discuss with the senior people to help you to see the whole picture, understand the good side and bad side, know what you don’t know … etc.
- Strong Recommend Materials Outlines
  - What’s the Problem?
  - How to Solve the Problem?
  - The Best Solution or Practice.
  - The Mechanism, Key Techniques, and Source Code
  - Pros/Cons
  - References (Further reading)

> For example, if you want to sharing a topic about Docker. the following outlines would be good one:
>
> - What’s the major problems need to solve. (Provision, Environment, Isolation etc.)
> - The Alternative solutions. (Puppet/Chef/Ansible, VM, LXC etc.)
> - The Best Solution – Docker. Why?
> - Docker’s key techniques – image, cgroup, union fs, namespace…
> - Docker’s Pros/Cons
> - Further reading list.

![img](https://coolshell.org/wp-content/uploads/2021/07/%E6%88%AA%E5%B1%8F2021-07-13-12.53.33.png)

（全文完）
