import os

from multiprocessing import Pool

def power(x):
    return 2 ** x
if __name__ == '__main__':
    workers = Pool(processes=5)
    results = workers.map(power, [2]*100)
    print(results[:16])
    print(results[-2:])
    results = workers.map(powers, range(100))
    print(results[:16])
    print(results[-2:])
