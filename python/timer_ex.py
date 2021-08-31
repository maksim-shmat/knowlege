""" Universal tool for chronometric. """
def test(reps, func, *args):
    import time
    start = time.clock()
    for i in range(reps):
        func(*args)
    return time.clock() - start

###### which script faster?
import time

time_start = time.perf_counter()

# YOUR SCRIPT HERE

time_end = time.perf_counter()
total_time = time_end - time_start

print(f'{total_time:0.2f} second have passed')

######
