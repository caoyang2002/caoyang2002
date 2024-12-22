time=$(date +%Y-%m-%d)
printf "publish at $time\n"
vercel --prod
git add .
git commit -m "$time"
git push
# hugo server -D
