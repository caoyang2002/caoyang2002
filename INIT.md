# 初始化

```bash
git submodule update --init --recursive
```

# 启动
```bash
./RUN.sh
# 或
hugo server -D
```

# 部署

推送到 main 分支后由 GitHub Actions 自动构建并部署到 GitHub Pages：

```bash
git push origin main
```

也可使用一键脚本（备份 + 构建验证 + 提交推送）：

```bash
./update.sh
```
