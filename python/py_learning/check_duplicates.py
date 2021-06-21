"""Check duplicates."""

def check_duplicate(lst):
    return len(lst) != len(set(lst))
print(check_duplicate([1,2,3,4,5,4,6]))
check_duplicate([1,2,3])
check_duplicate([1,2,3,4,9])
