"""Tricks and hints on the Bash."""

#1 Check bash environment
$ env

#2 Change variables of bash environment

LANGUAGE=he FOO=bar gedit  # change lang and start gedit
LANGUAGE=be vim  # start with new lang but for one session

#3 How add check problem with PATH on the new Ubuntu
WARNING: The script virtualenv is installed in '/home/jack/.local/bin' which is not on PATH.

echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin

vim ~/.bashrc
# add on the end of file
export PATH="$HOME/.local/bin:$PATH"

source ~/.bashrc  # commit

echo $PATH
/home/jack/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin

#4
