""" How make good commits?
build: Changes that affect the build system or external dependencies (example

scopes: gulp, broccoli, npm)

ci: Changes to our CI configuration files and scripts (example scopes: Travis,
    Circle, BrowserStack, SauceLabs)

docs: Documentation only changes

feat: A new feature

fix: A bug fix

perf: A code change that improves performance.

refactor: A code change that neither fixes a bug nor adds a future

style: Changes that do not affect the meaning of the code (white-space,
    formatting, missing semi-colons, etc)

test: Adding missing tests or correcting existing tests
"""

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

echo "# Book_markus" >> README.md
git init
git add README.md
git commit -m "The man in black fled across the desert, and the gunslinger followed."
git branch -M dictator
git remote add origin https://github.com/maksim-shmat/Book_markus.git
git push -u origin dictator
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

