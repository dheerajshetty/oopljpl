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
    O(1n) in space
    O(2n) in time
    """
    if not a :
        return v
    m = sum(a, v) / len(a)
    s = len(a)
    i = 0
    while i != s :
        v += (a[i] - m) ** 2
        i += 1
    return math.sqrt(v / s)

def stddev_2 (a, v = 0.0) :
    """
    O(1n) in space
    O(2n) in time
    """
    if not a :
        return v
    m = sum(a, v) / len(a)
    s = len(a)
    for u in a :
        v += (u - m) ** 2
    return math.sqrt(v / s)

def stddev_3 (a, v = 0.0) :
    """
    O(2n) in space
    O(2n) in time
    """
    if not a :
        return v
    m = sum(a, v) / len(a)
    s = len(a)
    v = sum(map(lambda u, w : (u - w) ** 2, a, s * [m]), v)
    return math.sqrt(v / s)

def stddev_4 (a, v = 0.0) :
    """
    O(1n) in space
    O(2n) in time
    """
    if not a :
        return v
    m = sum(a, v) / len(a)
    s = len(a)
    v = reduce(lambda v, u : v + (u - m) ** 2, a, v)
    return math.sqrt(v / s)

def stddev_5 (a, v = 0.0) :
    """
    mean of the squares minus the square of the mean
    O(1n) in space
    O(1n) in time
    """
    if not a :
        return v
    s = 0
    w = v
    for u in a :
        s += 1
        v += u
        w += u ** 2
    return math.sqrt((w / s) - (v / s) ** 2)

def stddev_6 (a, v = 0.0) :
    """
    mean of the squares minus the square of the mean
    O(2n) in space
    O(3n) in time
    """
    if not a :
        return v
    ms = sum(map(lambda u : u ** 2, a), v) / len(a)
    sm = (sum(a, v) / len(a)) ** 2
    return math.sqrt(ms - sm)

def stddev_7 (a, v = 0.0) :
    """
    mean of the squares minus the square of the mean
    O(2n) in space
    O(3n) in time
    """
    if not a :
        return v
    ms = reduce(lambda v, u : v + u ** 2, a, v) / len(a)
    sm = (sum(a, v) / len(a)) ** 2
    return math.sqrt(ms - sm)

def test (f, s) :
    print f.__name__ + " (" + s + ")"
    assert f([])             == 0
    assert f([2])            == 0
    assert f([2, 2, 2])      == 0
    assert str(f([2, 3, 4])) == "0.816496580928"
    a = 1000 * [1]
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
test(stddev_6, "math sum map")
test(stddev_7, "math reduce")

print "Done."

"""
StandardDeviation.py

2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

stddev_1 (while)
0.476 milliseconds

stddev_2 (for)
0.329 milliseconds

stddev_3 (sum map)
0.554 milliseconds

stddev_4 (reduce)
0.468 milliseconds

stddev_5 (math for)
0.410 milliseconds

stddev_6 (math sum map)
0.369 milliseconds

stddev_7 (math reduce)
0.382 milliseconds

Done.
"""
