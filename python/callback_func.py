"""Callback func about."""

def callbackFunc(s):
    print("Length of the text file is : ", s)

def printFileLength(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)

if __name__ == '__main__':
    printFileLength("alarm.py", callbackFunc)

######

def callbackFunc1(s):
    print('Callback Function 1: Length of the file is : ', s)

def callbackFunc2(s):
    print('Callback Function 2: Length of the text file is : ', s)

def printFileLength(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)

if __name__ == '__main__':
    printFileLength("mins.py", callbackFunc1)
    printFileLength("mins.py", callbackFunc2)
