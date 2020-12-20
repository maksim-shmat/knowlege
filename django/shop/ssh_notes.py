""" About SSH."""

# Make a new ssh-key from github tutorial
$ ssh-keygen -t ed25519 -C "***@gmail.com"

# Check ssh how you have
$ ls -al ~/.ssh  # list the files in your .ssh directory, if they exist

1.$ eval "$(ssh-agent -s)" # start agent

# Add ssh-key to ssh-agent.
2.$ ssh-add ~/.ssh/id_ed25519
or ssh-add  # add all keys in dir ssh

# connect to github
$ ssh -T git@github.com

# change https to ssh
git remote -v (chech http or ssh)

copy ssh-address repo in github <green button"Code">

git remote set-url origin <ssh-address> # for concreet repo
