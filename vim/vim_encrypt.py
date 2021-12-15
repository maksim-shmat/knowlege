"""Encryption files in vim with pass."""

#1 Encrypt
vim -x jill.py
pass:123
pass:123
:wq

#2 Decryption file

vim -X jill.py
pass:123
:X
pass:<Enter>
pass:<Enter>
:wq

######
