#!/usr/bin/env python

# -------
# StDv.py
# -------

import math
import operator
import sys
import time

def stddev_1 (a, v = 0.0) :
    """
    O(1)  in space
    O(2n) in time
    """
    if not a :
        return v
    s = len(a)
    m = sum(a, v) / s
    i = 0
    while i != s :
        v += (a[i] - m) ** 2
        i += 1
    return math.sqrt(v / s)

def stddev_2 (a, v = 0.0) :
    """
    O(1)  in space
    O(2n) in time
    """
    if not a :
        return v
    s = len(a)
    m = sum(a, v) / s
    for u in a :
        v += (u - m) ** 2
    return math.sqrt(v / s)

def stddev_3 (a, v = 0.0) :
    """
    O(2n) in space
    O(4n) in time
    """
    if not a :
        return v
    s = len(a)
    m = sum(a, v) / s
    v = sum(map(lambda u, w : (u - w) ** 2, a, s * [m]), v)
    return math.sqrt(v / s)

def stddev_4 (a, v = 0.0) :
    """
    O(1)  in space
    O(2n) in time
    """
    if not a :
        return v
    s = len(a)
    m = sum(a, v) / s
    v = reduce(lambda v, u : v + (u - m) ** 2, a, v)
    return math.sqrt(v / s)

def stddev_5 (a, v = 0.0) :
    """
    mean of the squares minus the square of the mean
    O(1)  in space
    O(1n) in time
    """
    if not a :
        return v
    s = len(a)
    w = v
    for u in a :
        v += u
        w += u ** 2
    ms = w / s
    sm = (v / s) ** 2
    return math.sqrt(ms - sm)

def stddev_6 (a, v = 0.0) :
    """
    mean of the squares minus the square of the mean
    O(1)  in space
    O(2n) in time
    """
    if not a :
        return v
    s = len(a)
    ms = reduce(lambda v, u : v + u ** 2, a, v) / s
    sm = (sum(a, v) / s) ** 2
    return math.sqrt(ms - sm)

def stddev_7 (a, v = 0.0) :
    """
    mean of the squares minus the square of the mean
    O(1n) in space
    O(3n) in time
    """
    if not a :
        return v
    s = len(a)
    ms = sum([u ** 2 for u in a], v) / s
    sm = (sum(a, v) / s) ** 2
    return math.sqrt(ms - sm)

def test (f, s) :
    print f.__name__ + " (" + s + ")"
    assert f([])             == 0
    assert f([2])            == 0
    assert f([2, 2, 2])      == 0
    assert str(f([2, 3, 4])) == "0.816496580928"
    a = 1000 * [2]
    b = time.clock()
    assert f(a) == 0
    e = time.clock()
    print "%5.3f" % ((e - b) * 1000), "milliseconds"
    print

print "StandardDeviation.py"
print

print sys.version
print

test(stddev_1, "while")
test(stddev_2, "for")
test(stddev_3, "sum map")
test(stddev_4, "reduce")
test(stddev_5, "math for")
test(stddev_6, "math reduce")
test(stddev_7, "math sum list comprehension")

print "Done."

"""
StandardDeviation.py

2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

stddev_1 (while)
0.459 milliseconds

stddev_2 (for)
0.331 milliseconds

stddev_3 (sum map)
0.551 milliseconds

stddev_4 (reduce)
0.473 milliseconds

stddev_5 (math for)
0.359 milliseconds

stddev_6 (math reduce)
0.395 milliseconds

stddev_7 (math sum list comprehension)
0.209 milliseconds

Done.
"""
