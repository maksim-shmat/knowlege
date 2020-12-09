""" Only! for lists """
def reverse(list):    # recursively
    if list == []:
        return []
    else:
        return reverse(list[1:]) + list[:1]

def ireverse(list):   # iteratively
    res = []
    for x in list: res = [x] + res
    return res
