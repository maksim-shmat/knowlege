"""
Homegrown timing tools for function calls;
Does total time, best-of time, and best-of-totals time
Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время.
"""

import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    Суммарное время выполнения функции func() reps раз
    Возвращает (суммарное время, последний результат)
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    Самая быстрая функция func() среди reps запусков.
    Возвращает (лучшее время, последний результат)
    """
    best = 2 ** 32    # 136 лет представляется достаточным
    for i in range(reps): # Использование range при измерении времени не учитывает
        start = timer()
        ret = func(*pargs, ** kargs)
        elapsed = timer() - start # Или вызвать total() с reps=1
        if elapsed < best: best = elapsed # Или добавить в список и найти min()
    return (best, ret)
def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    Лучшее суммарное время:
    (лучшее время из reps1, total, reps2, func, *pargs, **kargs)
    """
    return bestof(reps1,total, reps2, func, *pargs, **kargs)
