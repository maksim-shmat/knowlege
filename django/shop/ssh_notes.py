""" About SSH."""

# Add a code phrase
ssh-keygen -p
Start the SSH key creation process
Enter file in which the key is (/home/jack/.ssh/id_rsa): 
Key has comment 'jack@Cesar'
Enter new passphrase (empty for no passphrase): ******** lock&key in your door
Enter same passphrase again: ********
Your identification has been saved with the new passphrase.

# Make a new ssh-key from github tutorial
$ ssh-keygen -t ed25519 -C "***@gmail.com"
# or ssh-keygen -t rsa -b 4096 -C "mail@example.com"  for old system
> Generating public/private ed25519 key pair.
> Enter a file in which to save the key(/User/you/.ssh/id_ed25519): [Press enter]
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]

# Check ssh how you have
$ ls -al ~/.ssh  # list the files in your .ssh directory, if they exist
# Check public keys. Default:
                            id_rsa.pub
                            id_ecdsa.pub
                            id_ed25519.pub
# Add ssh-key to ssh-agent.
$ eval "$(ssh-agent -s)"
> Agent pid ******
$ ssh-add ~/.ssh/maksim-shmat_github_openssh
>Enter passphrase for /home/jack/.ssh/maksim-shmat_github_openssh: 
Identity added: /home/jack/.ssh/maksim-shmat_github_openssh (***@gmail.com)

