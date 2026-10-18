Hugo 文档: https://www.gohugo.org/doc/

# 初始化（首次克隆）

```bash
git submodule update --init --recursive
```

# 站点地址

https://simons.qzz.io

# 基本命令

```bash
hugo new content/zh/posts/tech/name.md
```

或使用脚本：

```bash
./create.sh my-article-name
```

# 下载图片到本地

## 使用方法：

### 1. 基本使用：

```bash
python3 md_image_downloader.py content/zh/posts/tech/name.md
```
这会：
- 下载图片到 `static/assets/post_images/`
- 替换Markdown链接为 `/assets/post_images/filename.png`

详细输出

```bash
python3 md_image_downloader.py content/zh/posts/tech/test_image.md --verbose
```

文章 slug 作为前缀

```bash
python3 md_image_downloader.py content/zh/posts/tech/test_image.md --post-slug "your-article-slug" #  使用你自定义的 slug 
```

### 2. 指定自定义路径：
```bash
python3 md_image_downloader.py article.md \
  --storage-dir "static/images/posts" \
  --path-prefix "/images/posts"
```

### 3. 使用文章slug：
```bash
python3 md_image_downloader.py article.md --post-slug "my-article"
```
生成的文件名会是：`my-article_001.png`, `my-article_002.jpg` 等

### 4. 使用配置文件：
```bash
# 生成配置文件
python3 md_image_downloader.py --init-config config.json

# 使用配置文件
python3 md_image_downloader.py -c config.json article.md
```

## 使用配置文件 `hugo_image_config.json`:

```json
{
  "md_file": "content/zh/posts/tech/my-article.md",
  "storage_dir": "static/assets/post_images",
  "md_path_prefix": "/assets/post_images",
  "naming_method": "sequential",
  "use_post_slug": true,
  "post_slug": "my-article",
  "overwrite_existing": false,
  "download_timeout": 30,
  "delay_between_requests": 0.3,
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
  "referer": "https://www.cnblogs.com/",
  "backup_original": true,
  "verbose": true
}
```

## 路径映射示例：

```
原始Markdown:
![图片描述](https://example.com/image.png)

处理过程:
1. 下载到: static/assets/post_images/my-article_001.png
2. 替换为: ![图片描述](/assets/post_images/my-article_001.png)

Hugo服务:
当访问 /assets/post_images/my-article_001.png 时
Hugo会自动从 static/assets/post_images/my-article_001.png 提供文件
```

## 项目结构：

```
caoyang2002/
├── archetypes/
├── config/                   # 站点配置（_default + production）
├── content/
│   └── zh/
│       └── posts/
│           └── tech/
│               └── article.md   # 处理后使用 /assets/post_images/xxx.png
├── static/
│   └── assets/
│       └── post_images/        # 图片实际存储在这里
│           ├── my-article_001.png
│           └── my-article_002.jpg
└── themes/
    └── hugo-focus/             # git submodule
```
