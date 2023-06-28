"""How generate new ssh key for git acces."""

#1 ssh-keygen -t ed25519 -C "For Git Apr 9"

Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/jack/.ssh/id_ed25519): # Press enter
/home/jack/.ssh/id_ed25519 already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): # lockandkeys_how_key_from_your_door
Enter same passphrase again:
Your identification has been saved in /home/jack/.ssh/id_ed25519
Your public key has been saved in /home/jack/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:qXlelu7ovQ5lGnh1hiax3v9WgXsH0rMg+p1QN9JCoqM For git Apr 9
The key`s randomart image is:
+--[ED25519 256]--+
|        .        |
|         o...    |
|        o.+ooo.  |
|       oo*.o*.B. |
|      ..So+o *.=.|
|      E+.=.o ...o|
|      o +.+o.....|
|       o B. o..  |
|       .+o*. ..  |
+----[SHA256]-----+

#2 Add new SSH key to your github account

Copy public key to your clipboard

$ cat ~/.ssh/id_ed25519.pub  # or copy from your passwords and keys agent

Go to github > settings > New SSH key
