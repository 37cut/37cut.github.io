git init
git remote add origin git@github.com:37cut/37cut.github.io.git
git add .
git commit -m "Project submit on $(date +'%Y-%m-%d %H:%M:%S')"
git branch --set-upstream-to=origin/main main
