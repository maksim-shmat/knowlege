import sys, os
from socket import *
from tkinter import Tk
from launchmodes import PortableLauncher
from guiStreams import GuiOutput

myport = 50008
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind(('', myport))
sockobj.listen(5)

print('starting')
PortableLauncher('nongui', 'socket-nongui.py -gui')()
print('accepting')
conn, addr = sockobj.accept()
conn.setblocking(False)                 # unblocked socket (False=0)
print('accepted')

def checkdata():
    try:
        message = conn.recv(1024)
        #output.write(message + '\n')   # may sys.stdout=output
        print(message, file=output)
    except ettor:
        print('no data')
    root.after(1000, checkdata)

root = Tk()
output = GuiOutput(root)
checkdata()
root.mainloop()
'''Socket not gui.'''

import time, sys
if len(sys.argv) > 1:
    from socket_stream_redirect0 import *
    redirectOut()

while True:
    print(time.asctime())
    sys.stdout.flush()
    time.sleep(2.0)
