"""Tidy it is lib for scrapping HTML."""

# pip3 search tidy

# pop3 install pytidylib

from subprocess import Popen, PIPE

text = open('messy.html').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
tidy.stdin.write(text.encode())
tidy.stdin.close()
print(tidy.stdout.read().decode())

#2
