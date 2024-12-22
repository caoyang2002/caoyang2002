time=$(date +%Y-%m-%d)
printf "publish at $time\n"

hexo generate
vercel --prod

git add .
git commit -m "$time"
git push
