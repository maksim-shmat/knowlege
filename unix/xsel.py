"""Work in buffer of change with xsel."""

#1 Print buffer
xsel -b

#2 Clear buffer
xsel -bc

#3 Write primary buffer into file

xsel -p > message.py.gpg
