"""
total(spam, 1, 2, a=3, b=4, _reps=1000) вызывает и хронометрирует spam(1, 2, a=3, 
b=4) _reps раз и возвращает суммарное время для всех прогонов с финальным резуль-
татом.

bestof(spam, 1, 2, a=3, b=4, _repsl=5, _reps=1000) запускает тест лучшего из N в 
попытке избавиться от влияния колебаний загрузки системы и возвращает лучшее вре-
мя среди _reps тестов.

bestoftotal(spam, 1, 2, a=3, b=4, _repsl=5, _reps=1000) запускает тест лучшего 
(суммарного времени _reps прогонов);
"""
import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
