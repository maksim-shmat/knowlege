""" Connect terminal to github by ssh."""

#1 Configure git to use ssh

git config --global gpg.format ssh

added a string is "format = ssh", maybe ssh is a sort of gpg

#2 Generate pair keys

ssh-keygen -t ed25519 -C "your_email@example.com"

#3 Add ssh key to ssh-agent

$ eval "$(ssh-agent -s)"

#4 copy publick key to github.settings

~/.ssh/ id_ed25519 copy how into

#5 Testing your ssh connection

$ ssh -T git@github.com
