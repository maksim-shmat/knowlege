"""About  pipenv that mean pip plas enviroment in one place."""

$ pipenv graph # chech your installed programs 
$ pipenv install --help

$ sudo apt install pipenv
$ sudo upgrade pipenv
$ pip --version

$ pip install --user pipenv
$ pip install --user --upgrade pipenv

# next 1
$ cd myproject
$ pipenv install requests

# next 2 --- how using Requests ---
touch main.py

import requests
response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))

$ pipenv run python main.py
Your IP is 8.8.8.8

$ pipenv run
$ pipenv shell # start a virt
for Pipfile.lock  commands:
    pipenv install
    pipenv uninstall
    pipenv lock

# next 3
init Python3 in virtual environment:
    $ pipenv --three

# next 4
deactivated:
    exit (shell exit? or run exit? or pipenv exit?)

# next 5
run:
    pipenv run python3
    pipenv run pip freeze

# next 6
check    - it command checked PEP 508 security

# next 7
Pipfiles   - is some other requirements.txt(old style)
add Pipfiles to git  and then other unit run $ pipenv install

# next 8
keep both Pipfile and Pipfile.lock in git

Specify your target Python version in your Pipfile [requests] section.

pipenv install  is fully compatable with pip install

# next 9
Short instruction:
    $ cd myproject
    $ pipenv install
    $ pipenv install <package>
    
    $ pipenv shell
    $ python --version
    $ exit

# next 10
Upgrade:
    $ pipenv update --outdated
    $ pipenv update  # for everything
    $ pipenv update <pkg>  # for each outdated package

# next 11
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
or by default in your operating system

# next 14

