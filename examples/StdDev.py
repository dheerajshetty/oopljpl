#!/usr/bin/env python

# -------
# StDv.py
# -------

import math
import operator
import sys
import time

def mean (a) :
    return sum(a, 0.0) / len(a)

def stddev_1 (a) :
    """
    O(1n) in space
    O(2n) in time
    """
    m = sum(a, 0.0) / len(a)
    s = len(a)
    i = 0
    v = 0.0
    while i != s :
        v += (a[i] - m) ** 2
        i += 1
    return math.sqrt(v / s)

def stddev_2 (a) :
    """
    O(1n) in space
    O(2n) in time
    """
    m = sum(a, 0.0) / len(a)
    s = len(a)
    v = 0.0
    for u in a :
        v += (u - m) ** 2
    return math.sqrt(v / s)

def stddev_3 (a) :
    """
    O(1n) in space
    O(2n) in time
    """
    m = sum(a, 0.0) / len(a)
    s = len(a)
    v = reduce(lambda w, u : w + (u - m) ** 2, a, 0.0)
    return math.sqrt(v / s)

def stddev_4 (a) :
    """
    O(2n) in space
    O(2n) in time
    """
    m = sum(a, 0.0) / len(a)
    s = len(a)
    v = sum(map(lambda x, y : (x - y) ** 2, a, s * [m]), 0.0)
    return math.sqrt(v / s)

def stddev_5 (a) :
    """
    mean of the squares minus the square of the mean
    O(1n) in space
    O(1n) in time
    """
    s = 0
    v = 0.0
    w = 0.0
    for u in a :
        s += 1
        v += u
        w += u ** 2
    return math.sqrt((w / s) - (v / s) ** 2)

def stddev_6 (a) :
    """
    mean of the squares minus the square of the mean
    O(2n) in space
    O(3n) in time
    """
    return math.sqrt(sum(map(lambda x : x ** 2, a), 0.0) / len(a) - (sum(a, 0.0) / len(a)) ** 2)

def test (f, s) :
    print f.__name__ + " (" + s + ")"
    assert f([2, 2, 2]) == 0
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
test(stddev_3, "reduce")
test(stddev_4, "sum")
test(stddev_5, "math for")
test(stddev_6, "math")

print "Done."

"""
StandardDeviation.py

2.6.1 (r261:67515, Jun 24 2010, 21:47:49)
[GCC 4.2.1 (Apple Inc. build 5646)]

2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

stddev_1 (while)
0.674 milliseconds

stddev_2 (for)
0.497 milliseconds

stddev_3 (reduce)
0.732 milliseconds

stddev_4 (sum)
0.745 milliseconds

stddev_5 (math for)
0.601 milliseconds

stddev_6 (math)
0.353 milliseconds
Done.
"""
