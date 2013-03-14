#!/usr/bin/env python

# ---------------
# InnerProduct.py
# ---------------

import operator
import sys
import time

def inner_product_1 (a, b) :
    s = len(a)
    i = 0
    v = 0
    while i != s :
        v += a[i] * b[i]
        i += 1
    return v

def inner_product_2 (a, b) :
    v = 0
    for x, y in zip(a, b) :
        v += x * y
    return v

def inner_product_3 (a, b) :
    return reduce(lambda v, (x, y) : v + (x * y) , zip(a, b), 0)

def inner_product_4 (a, b) :
    return sum(map(lambda (x, y) : x * y, zip(a, b)))

def inner_product_5 (a, b) :
    return sum([x * y for x, y in zip(a, b)])

def inner_product_6 (a, b) :
    return sum(map(operator.mul, a, b))

def test (f, s) :
    print f.__name__ + " (" + s + ")"
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert f(a, b) == 32
    a = 500 * [1]
    b = time.clock()
    assert f(a, a) == 500
    e = time.clock()
    print "%5.3f" % ((e - b) * 1000), "milliseconds"
    print

print "InnerProduct.py"
print

print sys.version
print

test(inner_product_1, "while")
test(inner_product_2, "for")
test(inner_product_3, "reduce")
test(inner_product_4, "map unary")
test(inner_product_5, "list comprehension")
test(inner_product_6, "map binary")

print "Done."

"""
InnerProduct.py

2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

inner_product_1 (while)
0.167 milliseconds

inner_product_2 (for)
0.148 milliseconds

inner_product_3 (reduce)
0.415 milliseconds

inner_product_4 (map unary)
0.221 milliseconds

inner_product_5 (list comprehension)
0.143 milliseconds

inner_product_6 (map binary)
0.100 milliseconds

Done.
"""
