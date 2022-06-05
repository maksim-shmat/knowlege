""" How make good commits?"""

docs:     documentation only changes
feat:     a new feature
fix:      a bug fix
perf:     a code change that improves performance.
refactor: a code change that neither fixes a bug nor adds a future
style:    changes that do not affect the meaning of the code (white-space, formatting, miss semi-colons)
chore:    updating grunt tasks etc; no production code change.
test:     adding missing tests or correcting existing tests

build:   changes that affect the build system or external dependencies
scopes:  gulp, broccoli, npm)
Ci:      changes to our CI configuration files and scripts (example scopes: Travis,Circle, BrowserStack, SauceLabs)

man gitignore  # справочка

git commit -a  # without add .

rm file
first rm from index and then commit
git rm log/\*.log (\ ecran)

git rm --cached file # rm from commit but hold in working dir

git rm \*~  # rm file where over for tilde
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
git push -u origin ming
git remote add nahui https://github.com... # name remote repo
if you change repo in site github
use git pull before git push
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

### --- troubles with merge ---

git config merge.tool vimdiff3

git diff

git mergetool
git commit
git push

### make a left branch
git branch dev
git branch        # check branches
git checkout dev  # move to new branch
git checkout -b newbranch # make and go to new branch

git checkout king # go back
git merge dev

#
git branch -d dev  --- delete left branch ---

# переименовал дир с bel => app и хочу вернуть
git restore bel

######1 change last commit

git commit --amend

######2 How back del file

git rm jill.db  # del it
# how revert?
git reset --hard HEAD
git add .
git commit
git pull

######3 Add all files to commit

git add -u
git add -A
######4 Remove dir from git defense

rm -r -f broken dir/

######5 Change .gitconfig for gpg verification
[commit]
        gpgsign = true
[user]
        signingkey = <KehID>
[gpg]
        program = /usr/bin/gpg
and then add your pub key into github: options > ssh/gpg

#6
