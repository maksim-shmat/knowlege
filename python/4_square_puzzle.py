"""4 square puzzle."""

import itertools

def all_equal(a, b, c, d, e, f, g):
    return a+b == b+c+d == d+e+f == f+g

def foursquares(lo, hi, unique, show):
    solutions = 0
    if unique:
        uorn = "unique"
        citer = itertools.combinations(range(lo, hi+1), 7)
    else:
        uorn = "non_unique"
        citer = itertools.combinations_with_replacement(range(lo, hi+1), 7)
    for c in citer:
        for p in set(itertools.permutations(c)):
            if all_equal(*p):
                solutions += 1
                if show:
                    print(str(p)[1:-1])

    print(str(solutions) + " " + uorn + " solutions in " + str(lo) + " to " + str(hi))

#z = foursquares(1,7,True,True)
#print(z)

#ze = foursquares(3, 9, True, True)
#print(ze)

#zed = foursquares(0, 9, False, False)
#print(zed)
