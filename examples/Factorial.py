#!/usr/bin/env python

# ------------
# Factorial.py
# ------------

import math
import operator
import sys
import time

def factorial_1 (n) :
    if n < 2 :
        return 1
    return n * factorial_1(n - 1)

def factorial_2 (n) :
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

def factorial_3 (n) :
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

def factorial_4 (n) :
    v = 1
    for i in xrange(1, n + 1) :
        v *= i
    return v

def factorial_5 (n) :
    return reduce(operator.mul, xrange(1, n + 1), 1)

def test (f, s) :
    print f.__name__ + " (" + s + ")"
    assert f(0) ==   1
    assert f(1) ==   1
    assert f(2) ==   2
    assert f(3) ==   6
    assert f(4) ==  24
    assert f(5) == 120

    b = time.clock()
    print f(100)
    e = time.clock()
    print "%5.3f" % ((e - b) * 1000), "milliseconds"
    print

print "Factorial.py"
print

print sys.version
print

test(factorial_1,    "recursion")
test(factorial_2,    "iteration")
test(factorial_3,    "range")
test(factorial_4,    "xrange")
test(factorial_5,    "reduce")
test(math.factorial, "python")

print "Done."

"""
Factorial.py

2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

factorial_1 (recursion)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.144 milliseconds

factorial_2 (iteration)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.052 milliseconds

factorial_3 (range)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.040 milliseconds

factorial_4 (xrange)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.040 milliseconds

factorial_5 (reduce)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.044 milliseconds

factorial (python)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.027 milliseconds

Done.
"""
