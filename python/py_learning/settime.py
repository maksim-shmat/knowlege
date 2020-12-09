""" Check the power sets """

import timer, sys
import set, fastset

def setops(Class):
    a = Class(range(50))
    b = Class(range(20))
    c = Class(range(10))
    d = Class(range(5))
    for i in range(5):
        t = a & b & c & d     # three crossroads
        t = a | b | c | d     # three sum?

if __name__ == '__main__':
    rept = int(sys.argv[1])
    print('set =>', timer.test(rept, setops, fastset.Set))
    print('fastset =>', timer.test(rept, setops, fastset.Set))
