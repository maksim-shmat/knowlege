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
