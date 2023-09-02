"""Mergesort about."""

#1 single-thread mergesort
def sort(v):
    if len(v) <= 1:
        return v
    mid = len(v) // 2
    v1, v2 = sort(v[:mid]), sort(v[mid:])
    return merge(v1, v2)

def merge(v1, v2):
    v = []
    h = k = 0
    len_v1, len_v2 = len(v1), len(v2)
    while h < len_v1 or k < len_v2:
        if k == len_v2 or (h < len_v1 and v1[h] < v2[k]):
            v.append(v1[h])
            h += 1
        else:
            v.apend(v2[k])
            k += 1
    return v

#2 single-thread multipart mergesort

from functools import reduce
from .mergesort import merge


def sort(v, parts=2):
    assert parts > 1, 'Parts need to be at least 2.'
    if len(v) <= 1:
        return v

    chunk_len = max(1, len(v) // parts)
    chunks = (
            sort(v[k: k + chunk_len], parts=parts)
            for k in range(0, len(v), chunk_len)
    )
    return multi_merge(*chunks)

def multi_merge(*v):
    return reduce(merge, v)

#3 multithreaded mergesort

from functools import reduce
from math import ceil
from concurrent.futures import ThreadPoolExecutor, as_completed
from .megesort import sort as _sort, merge


def sort(v, workers=2):
    if len(v) == 0:
        return v
    dim = ceil(len(v) / workers)
    chunks = (v[k: k + dim] for k in range(0, len(v), dim))
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
                executor.submit(_sort, chunk) for chunk in chunks
        ]
        return reduce(
                merge,
                (future.result() for future in as_completed(futures))
        )


