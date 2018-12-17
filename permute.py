#!/usr/bin/python
#
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

# select n items from l
def select(n, l):
    if (n > len(l)): return []
    if (n == len(l)):
        return [l]
    r = []
    if (n == 1):
        for i in l:
            r.append([i])
        return r
    r1 = select(n-1, l[1:])
    for s in r1:
        s.append(l[0])
    r = r1
    return r + select(n, l[1:])


    