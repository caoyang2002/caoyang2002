+++
title = '安装 Gitea'
date = 2025-12-28T21:09:14+08:00
draft = false
author = "simons"
categories = ["编程"]
tags = ["gitea"]
description = "安装 Gitea 的方法"
+++

> 参考：[官方文档](https://docs.gitea.com/zh-cn/category/installation)

Gitea 支持多种安装方法，这里只介绍 docker 的安装方法

# 方法一：使用Docker命令行安装（推荐）

## 1. 创建数据目录

```bash
# 创建必要的目录
sudo mkdir -p /opt/gitea/data
sudo mkdir -p /opt/gitea/config
sudo mkdir -p /opt/gitea/logs

# 设置权限（Gitea默认使用uid=1000, gid=1000的用户）
sudo chown -R 1000:1000 /opt/gitea
```

### 2. 运行Gitea容器
```bash
docker run -d \
  --name=gitea \
  --privileged=true \
  --restart=unless-stopped \
  -p 3000:3000 \
  -p 2222:22 \
  -v /opt/gitea/data:/data \
  -v /opt/gitea/config:/etc/gitea \
  -v /etc/timezone:/etc/timezone:ro \
  -v /etc/localtime:/etc/localtime:ro \
  -e USER_UID=1000 \
  -e USER_GID=1000 \
  gitea/gitea:latest
```

## 3. 验证安装
```bash
# 查看容器状态
docker ps -a

# 查看日志
docker logs gitea
```

访问：`http://your-server-ip:3000` 进行初始设置。

# 方法二：使用Docker Compose安装（更规范）

## 1. 创建docker-compose.yml文件
```yaml
version: "3"

services:
  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    restart: unless-stopped
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=sqlite3
      - GITEA__database__PATH=/data/gitea/gitea.db
      - GITEA__server__DOMAIN=your-domain.com
      - GITEA__server__ROOT_URL=http://your-domain.com:3000
      - GITEA__server__SSH_PORT=2222
      - GITEA__server__DISABLE_SSH=false
    volumes:
      - ./data:/data
      - ./config:/etc/gitea
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "2222:22"
    networks:
      - gitea-network

networks:
  gitea-network:
    driver: bridge
```

## 2. 启动服务
```bash
# 创建目录
mkdir gitea && cd gitea

# 创建数据目录
mkdir -p data config

# 设置权限
chown -R 1000:1000 data

# 启动服务
docker-compose up -d
```

# 方法三：使用MySQL数据库

如果需要使用MySQL而非SQLite：

## docker-compose.yml（带MySQL）
```yaml
version: "3"

services:
  db:
    image: mysql:8
    container_name: gitea-mysql
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: gitea
      MYSQL_USER: gitea
      MYSQL_PASSWORD: giteapassword
    volumes:
      - ./mysql:/var/lib/mysql
    networks:
      - gitea-network

  gitea:
    image: gitea/gitea:latest
    container_name: gitea
    restart: unless-stopped
    depends_on:
      - db
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=mysql
      - GITEA__database__HOST=db:3306
      - GITEA__database__NAME=gitea
      - GITEA__database__USER=gitea
      - GITEA__database__PASSWD=giteapassword
      - GITEA__server__DOMAIN=your-domain.com
      - GITEA__server__ROOT_URL=http://your-domain.com:3000
    volumes:
      - ./data:/data
      - ./config:/etc/gitea
    ports:
      - "3000:3000"
      - "2222:22"
    networks:
      - gitea-network

networks:
  gitea-network:
    driver: bridge
```

# 初始配置步骤

1. **访问Web界面**：
   - 打开浏览器访问：`http://your-server-ip:3000`

2. **数据库配置**：
   - 如果是Docker单容器：选择SQLite3
   - 如果使用MySQL：填写MySQL连接信息
   ```
   主机：db:3306
   用户名：gitea
   密码：giteapassword
   数据库名：gitea
   ```

3. **常规设置**：
   - 站点名称
   - 仓库根目录：`/data/git/repositories`
   - LFS根目录：`/data/git/lfs`
   - 运行用户名：`git`
   - SSH服务端口：`2222`

4. **管理员账户**：
   - 设置第一个管理员账户

# 常用管理命令

```bash
# 停止Gitea
docker stop gitea

# 启动Gitea
docker start gitea

# 重启Gitea
docker restart gitea

# 进入容器
docker exec -it gitea bash

# 查看日志
docker logs -f gitea

# 备份数据
docker exec -it gitea gitea dump

# 升级版本
docker pull gitea/gitea:latest
docker stop gitea
docker rm gitea
# 重新运行容器（数据卷会保留）
```

# 注意事项

1. **数据持久化**：确保正确挂载 `/data` 和 `/etc/gitea` 目录
2. **SSH端口**：如果宿主机22端口已被使用，请使用其他端口（如2222）
3. **备份**：定期备份挂载目录中的数据
4. **性能**：生产环境建议使用MySQL/PostgreSQL而非SQLite
5. **HTTPS**：生产环境应配置反向代理（如Nginx）并启用HTTPS

# 故障排查

```bash
# 检查容器状态
docker ps -a

# 查看详细日志
docker logs --tail 100 gitea

# 检查端口是否开放
sudo netstat -tulpn | grep 3000

# 检查数据目录权限
ls -la /opt/gitea/data
```
