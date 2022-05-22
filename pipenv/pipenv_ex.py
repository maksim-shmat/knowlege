"""About  pipenv that mean pip + venv in one place."""

--------------------
# next 9
Short instruction:
    $ cd myproject
    $ pipenv install
    $ pipenv install <package>
    
    $ pipenv shell  # or pipenv run
    $ python --version
    $ deactivate

---------------------
$ pipenv graph # show a graph of your installed dependencies 
$ pipenv graph --reverse  # all dependencies
$ pipenv -h  # help
$ pipenv install --help

$ sudo apt install pipenv
$ sudo upgrade pipenv


$ pip install --user pipenv
$ pip install --user --upgrade pipenv

$ pipenv install pytest --dev  # e.g. install pytest into dev pack programs
-----------
# next 1
$ cd myproject
$ pipenv install requests # add all default programm

# next 2 --- how using Requests ---
touch main.py

import requests
response = requests.get('https://http bin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))

$ pipenv run python main.py
Your IP is 8.8.8.8

# next 3
init Python3 in virtual environment:
    $ pipenv --three

# next 4

deactivated:
    exit  # heay it close vim tab (shell exit? or run exit? or pipenv exit?)

#5 Run

pipenv open psycopg2  # open program into edior
pipenv run <insert command here>
run:
    pipenv run python3
    pipenv run pip freeze

# next 6
pipenv check  # check your installed dependencies for security PEP 508

# next 7
Pipfiles   - is some other requirements.txt(old style)
add Pipfiles to git  and then other unit run $ pipenv install

# next 8
keep both Pipfile and Pipfile.lock in git

Specify your target Python version in your Pipfile [requests] section.

pipenv install  is fully compatable with pip install


# next 10
Upgrade:
    $ pipenv update --outdated
    $ pipenv update  # for everything
    $ pipenv update <pkg>  # for each outdated package

#11 Generate/Import requirements.txt from Pipenv

pipenv lock -r > requirements.txt  # generate
pipenv lock -r -d > dev-requirements.txt

Importing from requirements.txt

$ pipenv install -r path/to/requirements.txt
$ pipenv lock --keep-outdated  (for keep programms old versions)

# next 12
Specifying versions of a package

$ pipenv install requests~=1.2 # ver 1.2 and update old, but not 2.0 ver
$ pipenv install "requests>=1.4" # equal and larger than 1.4.0
$ pipenv install "requests<=2.13" # equal and lower than 2.13.0
$ pipenv install "requests>2.19" # 2.19.1 but not 2.19.0

$ pipenv install "requests~=2.2" locks the major version of the package (this is equivalent to using ==2.*)

$ pipenv install "requests!=1.0" avoid this version

# next 13
Python version
$ pipenv --python 3.6
$ pipenv --python # currently version
or by default in your operating system

# next 14
more parameters with pipenv
$ pipenv install --dev # install both develop an default packages form Pipfile
$ pipenv --deploy # check Pipfile.lock
$ pipenv --ignore-lock # ignore the Pipfile and install from Pipfile.lock
$ pipenv --skip-lock # ignore the Pipfile.lock and install from Pipfile. Do not write changes to the Pipfile

# next 15
Uninstall
$ pipenv uninstall --all # purge all files an leave th Pipfile untouched
$ pipenv uninstall --all-dev # remove all files and all from Pipfile

# next 17
If you`d like a requirements.txt 
$ pipenv lock -r # with hashes
$ pipenv run pip freeze # without hashes

#18 Install packages with pipenv from git and other Version Control System(VCS)
$<vcs_type>+<scheme>://<location>/<user_or_organization>/<repository>@<branch_or_tag>#<package_name>

$ pipenv install -e git+https://github.com/...

$ pipenv open background # and now I read it with vim?

# next 19
$ pipenv lock --clear # clear cache resolver

###### scripts for Pipfile
# pipenv run python manage.py runserver  --it is not convenient
[scripts]
server = "python manage.py runserver"
# and now:   $pipenv run server

#20 Create a new project using Python 3.7, specifically:

$ pipenv --python 3.7

#21 Remove project virualenv (interred from current directory)

$ pipenv --rm

#22 Generate a lockfile, and lockfile containing pre-releases e.g.

$ pipenv lock

$ pipenv lock --pre

#23 Install a local setup.py into your virtual environment/Pipfile

$ pipenv install -e .

#24 Lower-level pip command

$ pipenv run pip freeze
                 check
                 clean
                 graph

                 install
                 lock
                 open
                 run

                 scripts
                 shell
                 sync
                 uninstall

#25
