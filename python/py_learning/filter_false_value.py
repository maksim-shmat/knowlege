"""Remove all false values: false, 0, None, " "."""

def Filtering(lst):
    return list(filter(None,lst))
lst=[None,1,3,0,"",5,7]
Filtering(lst)
