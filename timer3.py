"""
Используется в точности как timer2.py, но для получения более простого кода 
применяет аргументы с передачей только по ключевым словам и стандартными
значениями Python 3.X.
Выносить вызов range() за пределы тестов в Python 3.X нет нужды, т.к. он 
всегда даёт генератор; данная версия не будет работать в Python 2.X.
"""

import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, _reps=1000, **kargs):
    start = timer()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, _reps=5, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, _reps1=5, **kargs):
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
