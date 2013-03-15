#!/usr/bin/env python

# -------------
# Generators.py
# -------------

import math
import operator
import sys
import time

class xrange_1 (object) :
    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        return self

    def next (self) :
        if self.b == self.e :
            raise StopIteration()
        p = self.b
        self.b += 1
        return p

def factorial_1 (n) :
    return reduce(operator.mul, xrange_1(1, n + 1), 1)

def xrange_2 (b, e) :
    while b != e :
        yield b
        b += 1

def factorial_2 (n) :
    return reduce(operator.mul, xrange_2(1, n + 1), 1)

def factorial_3 (n) :
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

print "Generators.py"
print

print sys.version
print

test(factorial_1, "xrange_1")
test(factorial_2, "xrange_2")
test(factorial_3, "xrange")

print "Done."

"""
Factorial.py

Generators.py

2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

factorial_1 (xrange_1)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.154 milliseconds

factorial_2 (xrange_2)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.060 milliseconds

factorial_3 (xrange)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
0.039 milliseconds

Done.
"""
