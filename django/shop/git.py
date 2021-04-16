""" How make good commits?"""

build:   changes that affect the build system or external dependencies (example
scopes:  gulp, broccoli, npm)
ci:      changes to our CI configuration files and scripts (example scopes: Travis,Circle, BrowserStack, SauceLabs)

docs:     documentation only changes
feat:     a new feature
fix:      a bug fix
perf:     a code change that improves performance.
refactor: a code change that neither fixes a bug nor adds a future
style:    changes that do not affect the meaning of the code (white-space,
    formatting, missing semi-colons, etc)
chore:    updating grunt tasks etc; no production code change.
test:     adding missing tests or correcting existing tests


$ cat .gitignore

*.[oa]  # Игнорируй файлы заканчивающиеся на .о или .а
*~   # Игнор все файлы заканчивающиеся на ~
man gitignore  # справочка

git commit -v  # v добавить дульту изменений
git commit -a  # without add .

rm file
first rm from index and then commit
git rm log/\*.log (\ ecran)

git rm --cached file # rm from commit but hold in working dir

git rm \*~  # rm file where ower for tilda
################

How create new repository.

echo "Beralusian_Kingdom" >> README.md
git init
git add README.md
git commit -m "Start a project"
git branch -M king
Go to github and create new project "Beralusian_Kingdom" without README.md and
copy link
git remote add origin git@github.com:maksim-shmat/Beralusian_Kingdom.git
git push -u origin king
git remote add nahui https://github.com... # name remote repo
################

How clone another repo.

git clone https://...
cd ...
git checkout -b shop2  # add new branch
git init 
git add .
git commit
git remote add origin https:// ...
git fetch
git branch --set-upstream-to=origin/master 
git remote add shop2 https://github.com/maksim-shmat/...
git push --set-upstream origin shop2

###########
# from one com git push
# and from other com git pull origin

To many trubles:
1. add dir to git in com
2. add  files to git in A50
3. git push - no
4. git pull - no
5. git pull origin --rebase  (files from A50 is lost!)

##########
# cache username and pswd for 15 min
$ git config --global credential.helper cache (but data will be git-credentials file?)

########
# time machine
git reflog
git reset HEAD@{index}
###
# Change the last commit
git commit --amend
###

