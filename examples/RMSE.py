#!/usr/bin/env python

# -------
# RMSE.py
# -------

import math
import sys
import time

def rmse_1 (a, p, v = 0.0) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    i = 0
    while i != s :
        v += (a[i] - p[i]) ** 2
        i += 1
    return math.sqrt(v / s)

def rmse_2 (a, p, v = 0.0) :
    """
    O(1n) in space
    O(2n) in time
    """
    s = len(a)
    z = zip(a, p)
    for x, y in z :
        v += (x - y) ** 2
    return math.sqrt(v / s)

def rmse_3 (a, p, v = 0.0) :
    """
    O(1n) in space
    O(2n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = reduce(lambda v, (x, y) : v + (x - y) ** 2, z, v)
    return math.sqrt(v / s)

def rmse_4 (a, p, v = 0.0) :
    """
    O(1n) in space
    O(2n) in time
    """
    s = len(a)
    v = sum(map(lambda x, y : (x - y) ** 2, a, p), v)
    return math.sqrt(v / s)

def rmse_5 (a, p, v = 0.0) :
    """
    O(1n) in space
    O(2n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = sum([(x - y) ** 2 for x, y in z], v)
    return math.sqrt(v / s)

def test (f, s) :
    print f.__name__ + " (" + s + ")"
    assert str(f((2, 3, 4), (2, 3, 4))) == "0.0"
    assert str(f((2, 3, 4), (3, 4, 5))) == "1.0"
    assert str(f((2, 3, 4), (4, 3, 2))) == "1.63299316186"
    a = 1000 * [1]
    p = 1000 * [5]
    b = time.clock()
    assert f(a, p) == 4
    e = time.clock()
    print "%5.3f" % ((e - b) * 1000), "milliseconds"
    print

print "RMSE.py"
print sys.version
print

test(rmse_1, "while")
test(rmse_2, "zip, for")
test(rmse_3, "zip, reduce")
test(rmse_4, "map, sum")
test(rmse_5, "zip, list comprehension, sum")

print "Done."

"""
RMSE.py
2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

rmse_1 (while)
0.420 milliseconds

rmse_2 (zip, for)
0.608 milliseconds

rmse_3 (zip, reduce)
0.566 milliseconds

rmse_4 (map, sum)
0.399 milliseconds

rmse_5 (zip, list comprehension, sum)
0.364 milliseconds

Done.
"""
