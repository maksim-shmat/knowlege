""" Postgres and git """


sudo apt install git
git --version
git config --global user.name "jack"
git config --global user.email johndoe@example.com
git config --global core.editor vim
git config --global difftool vimdiff3
git config --global difftol.prompt false
giy config --global push.default simple    # push only current branch


pip3 install requests
pip3 install --upgrade requests

python3.8 -m pip install psycopg2
python3.8 -m pip install django-taggit
python3.8 -m pip install markdown

git log --oneline --decorate
git checkout -b notes.left    # add left branch

git tag v0.004
git checkout -b right_branch    # add right branch


git rebase left_branch right_branch  # success to upgrade right_branch
git rm *.pyc   # trubleshooting
git rebase --continue
git add db.sqlite3   # and more
git rebase --continue
git add .
git commit


git config merge.tool vimdiff (3)?
git mergetool      # clear all conflict db.sqlite3, I'm sorry
git add .
git commit 
git pull
git fetch jill
git merge

git checkout master
git add .
git commit
git merge right_branch
git merge tool
git add
git commit   # [master 21a9e76] Merge branch 'right_branch'


sex with git cherry-pick<number or commit>  # I don't know 
git describe    # get number of commit
blat zaporol master

git pull --rebase origin master # vosstanovil s github db clear


git add *.py
git commit
git rebase master left_branch  # no trubles
git stash save  # ok
git rebase master left_branch  # hola bro you lost yor db if more
git rebase --abort
git add -u
git commit --amend    # pzdts admin site lost
git stash pop        # Aaaliluia all go back

rebase this is obmen mestami teper sitemaps.pu netu in left_branch





sudo apt update
sudo apt upgrade
sudo apt install postgresql postgresql-contrib
python3 -m pip install psycopg2
sudo apt install libpq-dev python3-dev

sudo -u postgres createdb jack
sudo -u jack psql

jack=> CREATE TABLE ...;
jack=> INSERT INTO ...;
jack=> SELECT * FROM ...;
jack=> ALTER TABLE ...ADD...; # add column
jack=> ALTER TABLE ...DROP...; # del column
jack=> UPDATE playground SET color = 'red' WHERE type = 'swing'; # change set
jack=> \q

sudo su - postgres
postgres@Cesar:~$ psql

sudo -u postgres psql
postgres=# \du    # check roles and their pormissions
postgres=# dropuser blog  # del user without table
postgres=# REASSIGN OWNED BY car_portal_app TO jack; # rn table to new owner
Ctrl - d
postgres@Cesar:~$ dropuser car_portal_app  # del user
postgres=# DROP TABLE IF EXISTS blog;    # del table
postgres=# DROP DATABASE IF EXISTS car_portal;
postgres=# ALTER ROLE jack SUPERUSER CREATEROLE CREATEDB;

sudo -u jack createdb jack    # make db for user jack
sudo -u jack psql
jack=#    # superuser

settings.py    # change db info and write pass of sistem
python manage.py migrate
puthon manage.py createsuperuser
# check site with new db and need write posts now.


psql jack
CREATE EXTENSION pg_trgm;    # add trigram
views.py
