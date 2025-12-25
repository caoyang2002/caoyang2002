# 初始化

```bash
git submodule init
git submodule update --recursive
```

# 启动
```bash
hugo server -D
```

# 部署

```bash
hugo --environment production --baseURL https://caoyang2002.vercel.app --minify
vercel --prod
```
