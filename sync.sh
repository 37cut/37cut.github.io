# Initialize git repository to local
git init

# Synchronize local repos to remote repos
# Add remote origin to local
git remote add origin git@github.com:37cut/37cut.github.io.git

# Apply all changes
git add .
# Submit to git repos
git commit -m "Project submit on $(date +'%Y-%m-%d %H:%M:%S')"

git fetch
git branch --set-upstream-to=origin/main $(git branch --show-current)
