#import sys, timer
import sys, timer2
reps = 10000
repslist = list(range(reps))

def forLoop():
    res = []
    for x in repslist:
        res.append(x + 1)
    return res

def listComp():
    return [x + 1 for x in repslist]

def mapCall():
    return list(map((lambda x: x + 1), repslist))

def genExpr():
    return list(x + 1 for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield x + 1
    return list(gen())

print(sys.version)
"""
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
            (test.__name__, bestof, result[0], result[-1]))
"""
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (total, result) = timer2.bestoftotal(test, _reps1=5, _reps=1000)
    (total, result) = timer2.bestof(test, _reps=5)
    (total, result) = timer2.total(test, _reps = 1000)
    (bestof,(total, result)) = timer2.bestof(timer2.total,test, _reps=5)

print('%-9s: %.5f => [%s...%s]' %
        (test.__name__, total, result[0], result[-1]))
