""" Connect terminal to github by ssh."""


#1 Configure git to use ssh

git config --global gpg.format ssh

It added a string is "format = ssh", maybe ssh is a sort of gpg

git config --global user.signingkey /PATH/TO/.SSH/KEY.PUB

#2 Generate pair keys

ssh-keygen -t ed25519 -C "your_email@example.com"

#3 Add ssh key to ssh-agent

$ eval "$(ssh-agent -s)"

#4 copy publick key to github.settings

~/.ssh/ id_ed25519 copy how into

#5 change user.signingkey in .gitconfig

$ git config --global user.signingkey <gpg-key-id>

#5.1 Or maybe create ~/.ssh/config file

~/.ssh/config
chmod 600 ~/.ssh/config

Host *  # for all hosts
    IgnoreUnknown UseKeychain  # ???
    UseKeychain yes  # ???

#6 Testing your ssh connection

$ ssh -T git@github.com

# Docs
man ssh_config

#7 If you have change passfrase to no

ssh-keygen -p -f ~/.ssh/id_ed25519
