pip freeze > requirementes/_base.txt  # write all names installed pip prgrms
                                      # in file
pip install -r requirements/dev.txt

 file secrets.json with all passwords need put to .gitignore file, and __pycache too.
Символ / в начале строки - игнор файлов в той же папке где .gitignore
*.py - ignor file type
git rm --cached <file>  - rm git cached before push

ls -la  - views hide dir .git

Сделал отчёты в виде timestamp in file last_update.txt
make executable file pre-commit in django-myproject/.git/hooks/pre-commit
chmod u+x pre-commit
make executabel fle  in myproject/settings/last-update.txt
chmod u+x last-update.txt

gitignore file: from place where is manage.py make "touch .gitignore", or from github site

Make deleter or .py[co] files from bash:
    vim ~/.bash_profile:
        alias delpyc='        it's nothing,just closed comma -> ()
        find . -name "*.py[co]" -delete
        find . -type d -name "__pycache__" -delete'      closed comma (')
    source ~/.bash_profile
And voila!
(env)$ delpyc
