# UV
## Update the uv to its last version
> UV self update

## Create the env
> uv sync

# GIT
git status

git diff --stat "week1/Studant_Exercices/Day 1.ipynb"
output:
week1/Studant_Exercices/Day 1.ipynb | 2 ++
 1 file changed, 2 insertions(+)

git add "week1/Studant_Exercices/Day 1.ipynb" && git commit -m "$(cat <<'EOF'
Update Day 1 student exercises notebook
EOF
)" && git push