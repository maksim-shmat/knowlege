"""Thread and process pools about."""


#1
'''
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import randint
import threading


def run(name):
    value = randint(0, 10**2)
    tname = threading.current_thread().name
    print(f'Hi, I am {name} ({tname}) and my value is {value}')
    return (name, value)

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
            executor.submit(run, f'T{name}') for name in range(5)
    ]
    for future in as_completed(futures):
        name, value = future.result()
        print(f'Thread {name} returned {value}')
'''
'''
Hi, I am T0 (ThreadPoolExecutor-0_0) and my value is 65
Hi, I am T1 (ThreadPoolExecutor-0_1) and my value is 45
Hi, I am T2 (ThreadPoolExecutor-0_1) and my value is 20
Thread T2 returned 20
Thread T1 returned 45
Thread T0 returned 65
Hi, I am T3 (ThreadPoolExecutor-0_0) and my value is 10
Hi, I am T4 (ThreadPoolExecutor-0_0) and my value is 90
Thread T3 returned 10
Thread T4 returned 90
'''
'''
Hi, I am T0 (ThreadPoolExecutor-0_0) and my value is 63
Hi, I am T1 (ThreadPoolExecutor-0_0) and my value is 4
Hi, I am T2 (ThreadPoolExecutor-0_0) and my value is 63
Thread T2 returned 63
Thread T1 returned 4
Thread T0 returned 63
Hi, I am T3 (ThreadPoolExecutor-0_0) and my value is 68
Hi, I am T4 (ThreadPoolExecutor-0_0) and my value is 92
Thread T3 returned 68
Thread T4 returned 92
'''

#2 pool multiprocess

from concurrent.futures import ProcessPoolExecutor, as_completed
from random import randint
from time import sleep


def run(name):
    sleep(.05)
    value = randint(0, 10**2)
    print(f'Hi, I am {name} and my value is {value}')
    return (name, value)

with ProcessPoolExecutor(max_workers=3) as executor:
    futures = [
            executor.submit(run, f'P{name}') for name in range(5)
    ]
    for future in as_completed(futures):
        name, value = future.result()
        print(f'Process {name} returned {value}')

'''
Hi, I am P1 and my value is 4
Hi, I am P0 and my value is 88
Hi, I am P3 and my value is 67
Hi, I am P2 and my value is 5
Hi, I am P4 and my value is 7
Process P0 returned 88
Process P2 returned 5
Process P1 returned 4
Process P3 returned 67
Process P4 returned 7
'''

Hi, I am P2 and my value is 92
Hi, I am P0 and my value is 20
Hi, I am P3 and my value is 88
Hi, I am P1 and my value is 90
Hi, I am P4 and my value is 11
Process P0 returned 20
Process P1 returned 90
Process P2 returned 92
Process P3 returned 88
Process P4 returned 11
