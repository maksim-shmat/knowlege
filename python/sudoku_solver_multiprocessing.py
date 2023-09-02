"""It with sudoku-solver.py, use multiprocessing."""

import os
from functools import reduce
from operator import concat
from math import ceil
from time import time
from contextlib import contextmanager
from concurrent.futures import ProcessPoolExecutor, as_completed
from unittest import TestCase
from sudoku_solver import solve


@contextmanager
def timer():
    t = time()
    yield
    tot = time() - t
    print(f'Elapsed time: {tot:.3f}s')

def batch_solve(puzzles):
    # Single thread batch solve.
    return [solve(puzzle) for puzzle in puzzles]

def parallel_single_solver(puzzles, workers=4):
    # Parallel solve - 1 process per each puzzle
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = (executor.submit(solve, puzzle) for puzzle in puzzles)
        return [future.result() for future in as_completed(futures)]

def parallel_batch_solver(puzzles, workers=4):
    # Parallel batch solve - Puzzles are chunked into 'workers'
    # chunks. A process for each chunk.
    assert len(puzzles) >= workers
    dim = ceil(len(puzzles) / workers)
    chunks = (puzzles[k: k + dim] for k in range(0, len(puzzles), dim))
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = (executor.submit(batch_solve, chunk) for chunk in chunks)
        results = (furure.result() for future in as_completed(futures))
        return reduce(concat, results)

#puzzle_file = os.path.join('puzzles', 'jill_sudoku.txt')
with open('jill_sudoku.txt') as stream:
    puzzles = [puzzle.strip() for puzzle in stream]

# single thread solve
with timer():
    res_batch = batch_solve(puzzles)

# parallel solve, 1 process per puzzle
with timer():
    res_parallel_single = parallel_single_solver(puzzles)

# parallel batch solve, 1 batch per process
with timer():
    res_parallel_batch = parallel_batch_solver(puzzles)

# Quick way to verify that the results are the same, but
# possibly in a different order, as they depend on how the
# processes have been scheduled.
assert_items_equal = TestCase().assertCountEqual
assert_items_equal(res_batch, res_parallel_single)
assert_items_equal(res_batch, res_parallel_batch)
print('Done.')


