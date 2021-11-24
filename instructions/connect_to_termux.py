"""Add new connection from termux."""

pkg up

pkg install git

git config --global user.name "j.o"
git config --global user.email "f.p@"
git config --list  # check

git remote add origin https://error.link
git remote rm origin
git remote add origin https://true.link

apt install openssh

$ ssh-keygen -t rsa -b 4096

git clone <your link>

create a personal access token (PAT)

git push
name: j.o
password:(PAT insert)
