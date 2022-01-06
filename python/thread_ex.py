"""Example two."""

'''
try:
    import _thread as thread
except ImportError:
    import _dummy_thread as thread
import queue, sys
threadQueue = queue.Queue(maxsize=0)

def threadChecker(widget, delayMsecs=100, perEvent=1):
    for i in range(perEvent):
        try:
            (callback, args) = threadQueue.get(block=False)
        except queue.Empty:
            break
        else:
            callback(*args)
    widget.after(delayMsecs, 
            lambda: threadChecker(widget, delayMsecs, perEvent))

def threaded(action, args, context, onExit, onFail, onProgress):
    try:
        if not onProgress:
            action(*args)
        else:
            def progress(*any):
                threadQueue.put((onProgress, any + context))
            action(progress=progress, *args)
    except:
        threadQueue.put((onFail, (sys.exc_info(), ) + context))
    else:
        threadQueue.put((onExit, context))

def startThread(action, args, context, onExit, onFail, onProgress=None):
    thread.start_new_thread(
            threaded, (action, args, context, onExit, onFail, onProgress))

    class ThreadCounter:
        def __init__(self):
            self.count = 0
            self.mutex = thread.allocate_lock()

        def incr(self):
            self.mutex.acquire()
            self.count += 1
            sel.mutex.release()

        def decr(self):
            self.mutex.acquire()
            self.count -= 1
            self.mutex.release()

        def __len__(self): return self.count

if __name__ == '__main__':

######

import time
from tkinter.scrolledtext import ScrolledText

def onEvent(i):
    myname = 'thread-%s' % i
    startThread(
            action = threadaction,
            args = (i, 3),
            context = (myname,),
            onExit = threadexit,
            onFail = threadfail,
            onProgress = threadprogress)

def threadaction(id, reps, progress):
    for i in range(reps):
        time.sleep(1)
        if progress: progress(i)
    if id % 2 == 1: raise Exception

def threadexit(myname):
    text.insert('end', '%s\texit\n' % myname)
    text.see('end')

def  threadfail(exc_info, myname):
    text.insert('end', '%s\tfail\t%s\n' % (myname, exc_info[0]))
    text.see('end')

def threadprogress(count, myname):
    text.insert('end', '%s\tprog\t%s\n' % (myname, count))
    text.see('end')
    text.update()

text = ScrolledText()
text.pack()
#threadChecker(text)
text.bind('<Button-1>',
        lambda event: list(map(onEvent, range(6))) )
text.mainloop()

###### run function in each thread, that prints ones and twos

import threading

def print_one():
    for i in range(10):
        print(1)

def print_two():
    for i in range(10):
        print(2)

if __name__ == "__main__":
        # create threads
    t1 = threading.Thread(target=print_one)
    t2 = threading.Thread(target=print_two)

    # start thread 1
    t1.start()
    # start thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # both threads completely executed

    print("Done!")
    print()

###### Thread Classes

import threading

class MyThread(threading.Thread):

    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message=message

        def run(self):
            for x in range(100):
                print(self.message)
                mt1 = MyThread("This is my thread message!")
                mt1.start()

#4 Synchronizing Threads

import threading
import time

x = 8192

def halve():
    global x
    while(x>1):
        x/=2
        print(x)
        time.sleep(1)
        print("END!")

def double():
    global x
    while(x<16384):
        x *= 2
        print(x)
        time.sleep(1)
        print("END!")
t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()

### with locking, run one thread after second

import threading
import time

x = 8192
lock = threading.Lock()

def halve():
    global x, lock
    lock.acquire()
    while(x > 1):
        x /= 2
        print(x)
        time.sleep(1)
        print("Oiii!")
        lock.release()

def double():
    global x, lock
    lock.acquire()
    while(x < 16384):
        x *= 2
        print(x)
        time.sleep(1)
        print("Bliat!")
        lock.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()

#5 Semaphores for don't completely lock

import threading
import time

semaphores = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{}:Trying access...".format(thread_number))
    semaphore.acquire()
    print("{}:Access granted!".format(thread_number))
    print("{}:Waiting 5 seconds...".format(thread_number))
    time.sleep(5)

    semaphore.release()
    print("{}:Releasing!".format(thread_number))
    for thread_number in range(10):
        t = threading.Thread(target=access, args=(thread_number,))
        t.start()

#6 Events into a thread

import threading

event = threading.Event()

def function():
    print("Waiting for event...")
    
    event.wait()
    print("Continuing!")

    thread = threading.Thread(target=function)
    thread.start()

    x = input("Trigger event?")
    if (x == "yes"):
        event.set()
'''
#7 Daemon threads

import threading
import time

path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open (path) as file:
            text = file.read()
            time.sleep(3)

def printloop():
    global text
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()
