time=$(date +%Y-%m-%d)
printf "publish at $time\n"
hugo --minify
vercel --prod
git add .
git commit -m "$time"
git push
# hugo server -D
