+++
title = 'Git: 从入门到精通'
date = 2025-01-26T10:50:22+08:00
draft = true
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
+++

# Git: 从入门到精通

很多人用 Git 只会 `add/commit/push` 三板斧，遇到冲突就抓瞎。今天我们从原理到实战，彻底搞懂Git。

## Git的本质

Git本质上是个内容寻址的文件系统。它把你的代码转成一棵对象树：

```bash
# 看看Git的底层对象
echo 'test' > test.txt
git add test.txt
git cat-file -p HEAD
```

核心概念就三个：
1. Workspace：工作区
2. Index/Stage：暂存区
3. Repository：仓库区

## 为什么用Git？

对比一下传统SVN：
- SVN是集中式，Git是分布式
- SVN每次提交都需要网络，Git可以本地提交
- SVN分支是复制，Git分支是指针

```bash
# SVN的分支
svn copy trunk branches/feature

# Git的分支
git branch feature  # 只是创建一个指针
```

## 深入原理

Git的分支模型：

```bash
# master分支
A -> B -> C
           \
            D -> E  # feature分支
```

每个 commit 都是一个节点，分支只是指向节点的指针。这就是为什么 Git 分支如此轻量。

## 实战经验

1. 分支管理

```bash
# 创建开发分支
git checkout -b dev
# 提交代码
git add .
git commit -m "feat: new feature"
# 合并到主分支
git checkout main
git merge dev
```

2. 解决冲突

```bash
# 发生冲突时
git status  # 看看冲突文件
vim conflict.txt  # 手动解决冲突
git add .
git commit -m "fix: resolve conflict"
```

3. 撤销操作

```bash
# 撤销工作区修改
git checkout -- file

# 撤销暂存区
git reset HEAD file

# 撤销提交
git reset --hard HEAD^
```

## 高级技巧

1. 交互式 rebase

```bash
# 合并最近3个提交
git rebase -i HEAD~3
```

2. cherry-pick

```bash
# 把某个提交应用到当前分支
git cherry-pick commit_id
```

3. stash
```bash
# 临时保存工作区
git stash
# 切换分支处理紧急bug
git checkout hotfix
# 回来继续工作
git stash pop
```

## 工作流最佳实践

1. 分支策略
- `master` ：稳定版本
- `develop` ：开发主线
- `feature/*` ：新功能
- `hotfix/*` ：紧急修复

2. 提交规范

```bash
feat: 新功能
fix: 修复bug
docs: 文档更新
style: 格式调整
refactor: 重构
test: 测试代码
chore: 其他修改
```

记住几个原则：
1. commit 要原子化，一个提交做一件事
2. 分支要及时清理，不要留太多
3. 冲突要谨慎解决，不要盲目覆盖

## 总结

Git 不难，难的是理解它的思维方式：
- 分支是指针，创建分支不会复制代码
- commit 是不可变的，reset只是移动指针
- 冲突不可怕，理解原理就简单了

工具用不好不是工具的问题，而是你对它理解不够深入。理解了原理，Git就是一个很好用的时光机。

别再停留在 `add/commit/push` 的层面了，Git能做的远比你想象的多。

# 用了很长时间 Git，但不敢操作 git 命令？

Git 本质就是个典型的分布式版本控制系统。但很多人用了这么多年Git，还是停留在`add/commit/push`的层面，这就好比开着兰博基尼却只把它当电动车来用。今天就来扒一扒Git的内部机制和那些你应该知道但可能不知道的骚操作。

先说Git的本质 - 它就是个内容寻址文件系统，用一个巨大的key-value存储来管理你的代码。每次commit，Git都会给你的代码生成一个SHA-1哈希值作为索引。

```bash
# 看看Git的本质
$ git init
$ echo 'hello' > test.txt
$ git add test.txt
$ git commit -m "first commit"
$ git cat-file -p HEAD
tree 517d952c5850bc2fccc48ef8eb2f80372d760ac0
author caoyang2002 <cy12968@163.com> 1738337558 +0800
committer caoyang2002 <cy12968@163.com> 1738337558 +0800

first commit
```

重点来了，Git 有三个核心概念:

1. Working Directory (工作目录)
2. Staging Area (暂存区)
3. Repository (仓库)

这就像三个不同的空间。你写代码在工作目录，`git add`后代码进暂存区，`git commit`后代码才进仓库。这不是重点，重点是下面这些实战技巧:

```bash
# 1. 后悔药 - 撤销修改
git checkout -- file    # 撤销工作区修改
git reset HEAD file    # 撤销暂存区修改
git reset --hard HEAD^ # 撤销最近一次提交

# 2. 分支操作 - 救命稻草
git branch feature    # 创建分支
git checkout -b fix   # 创建并切换分支
git merge feature     # 合并分支

# 3. 黑科技 - 交互式rebase
git rebase -i HEAD~3  # 重写最近3次提交历史
```

说到分支，很多人都怕merge冲突。其实冲突不可怕，可怕的是不懂原理。Git merge有三种策略:

1. Fast-forward：最简单，直接把指针移动
2. Recursive：最常用，自动合并
3. Octopus：多分支合并，不常用

合并冲突时，把文件内容改成这样:
```
<<<<<<< HEAD
你的修改
=======
别人的修改
>>>>>>> feature
```

解决冲突就是要决定保留谁的修改。不要怕弄乱，因为还有后悔药:
```bash
git merge --abort  # 中断合并，回到合并前状态
```

还有一些高级玩法:

```bash
# 1. 储藏修改
git stash
git stash pop

# 2. 挑拣提交
git cherry-pick commit-id

# 3. 重写历史
git filter-branch --tree-filter 'rm -f password.txt' HEAD
```

最后说点Git的设计思想 - 不可变性。一旦commit，内容就被永久保存。就算你用`reset`删除了commit，内容还在，只是找不到了。用`git reflog`可以找回"删除"的commit。

记住，Git就是个点对点的分布式系统，每个仓库都是平等的，都包含完整的历史记录。这也是为什么它比SVN强大 - 你可以在本地进行所有操作，不依赖中央服务器。

Git常用操作其实就那么几个，但要真正用好，还得理解背后的原理。

1. 分支管理（最常用）
```bash
# 创建分支 - 就是创建一个指针指向当前commit
git branch feature

# 切换分支 - 移动HEAD指针，更新工作区
git checkout feature
# 或者一步到位
git checkout -b feature

# 删除分支 - 删除指针而已，commit还在
git branch -d feature
```

2. 状态查看（必备技能）
```bash
# 当前状态
git status

# 查看历史 - 加点料
git log --graph --pretty=format:'%h -%d %s (%cr) <%an>'
```

3. 撤销修改（救命三招）
```bash
# 工作区撤销
git checkout -- file

# 暂存区撤销
git reset HEAD file

# 提交后撤销
git reset --hard HEAD^
```

4. 远程协作（团队必备）
```bash
# 添加远程
git remote add origin git@github.com:xxx.git

# 推送分支 - 记住远程分支也是指针
git push origin master

# 拉取更新 - fetch+merge的简写
git pull origin master
```

5. 解决冲突（不要怕）
```bash
# 手动解决冲突后
git add .
git commit -m "fix conflict"
```

最骚的操作 - rebase。很多人不敢用，其实很简单：
```bash
# 变基 - 本质就是重新设置基线
git rebase master

# 交互式rebase - 可以修改历史
git rebase -i HEAD~3
```

记住几个原则：
1. 分支操作随意，因为分支就是指针
2. 本地修改随意，因为都是本地的
3. 远程分支要谨慎，因为涉及团队协作

不要死记命令，理解原理。Git的设计很优雅，每个命令都在操作这些基本要素：
- 对象（blob/tree/commit）
- 引用（分支/HEAD）
- 索引（暂存区）

来看几个实际工作中的场景。

场景1：改了一堆代码突然后悔了
```bash
# 完蛋，刚改了20个文件，现在想全部恢复
git status   # 先看看现在的惨状
git reset --hard HEAD  # 一键还原，爽！
```

场景2：糟糕，提交信息写错了
```bash
git commit --amend -m "fix: 正确的提交信息"
```

场景3：老板说要紧急修复线上bug
```bash
# 当前在开发新功能，代码写到一半
git stash  # 先存起来
git checkout master  # 切到主分支
git checkout -b hotfix  # 新建修复分支
# 修复bug
git commit -m "fix: 紧急修复"
git checkout feature  # 切回去
git stash pop  # 继续之前的开发
```

场景4：代码写烂了，想回到三天前
```bash
# 看看三天前的commit
git log --since="3 days ago"
# 找到想回到的版本，强制回归
git reset --hard commit_id
```

场景5：需求改了，要把A分支的某个提交应用到B分支
```bash
# 在A分支上找到那个提交
git log --oneline
# 切到B分支，应用那个提交
git cherry-pick commit_id
```

场景6：合并代码时冲突了
```bash
git merge feature
# 出现冲突，打开文件
# <<<<<<< HEAD
# 你的代码
# =======
# 别人的代码
# >>>>>>> feature
# 解决冲突，保存
git add .
git commit -m "解决冲突"
```

场景7：线上代码出bug了，需要紧急回滚
```bash
# 找到上一个稳定版本
git reset --hard HEAD^
# 强制推送到远程
git push -f origin master  # 慎用，先和同事沟通
```

记住，Git就是个时光机。只要提交过的代码就永远不会丢，不要怕搞砸。即使删错了分支、reset错了版本，用`git reflog`都能找回来。

关键是要理解Git的思维方式：
- 分支就是指针，创建删除都很轻松
- commit是永久的，reset只是移动指针
- 本地仓库是完整的，想怎么折腾都行

这些都是实战中经常遇到的场景。理解了这些，基本就能应付 80% 的情况了。剩下的 20% 都是这些基本操作的组合。

最后说一句：多用`git status`和`git log`看看当前状态，不要盲目操作。工具不会坑你，坑你的是自己的无知。
