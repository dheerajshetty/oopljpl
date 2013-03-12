#!/usr/bin/env python

# ------
# Sum.py
# ------

import operator
import sys
import time

def sum_1 (a) :
    if not a :
        return 0
    return a[0] + sum_1(a[1:])

def sum_2 (a) :
    v = 0
    i = 0
    s = len(a)
    while i != s :
        v += a[i]
        i += 1
    return v

def sum_3 (a) :
    v = 0
    for i in range(len(a)) :
        v += a[i]
    return v

def sum_4 (a) :
    v = 0
    p = iter(a)
    while True :
        try :
            v += p.next()
        except StopIteration :
            break
    return v

def sum_5 (a) :
    v = 0
    for w in a :
        v += w
    return v

def sum_6 (a) :
    return reduce(lambda x, y : x + y, a, 0)

def sum_7 (a) :
    return reduce(operator.add, a, 0)

def test_1 (f, c) :
    assert f(c())          == 0
    assert f(c([2]))       == 2
    assert f(c([2, 3]))    == 5
    assert f(c([2, 3, 4])) == 9

def test_2 (f, s) :
    print f.__name__ + " (" + s + ")"
    a = 500 * [1]
    b = time.clock()
    assert f(a) == 500
    e = time.clock()
    print "%5.3f" % ((e - b) * 1000), "milliseconds"
    print

print "Sum.py"
print

test_1(sum_1, list)
test_1(sum_1, tuple)
#test_1(sum_1, set) # TypeError: 'set' object does not support indexing

test_1(sum_2, list)
test_1(sum_2, tuple)
#test_1(sum_2, set) # TypeError: 'set' object does not support indexing

test_1(sum_3, list)
test_1(sum_3, tuple)
#test_1(sum_3, set) # TypeError: 'set' object does not support indexing

test_1(sum_4, list)
test_1(sum_4, tuple)
test_1(sum_4, set)

test_1(sum_5, list)
test_1(sum_5, tuple)
test_1(sum_5, set)

test_1(sum_6, list)
test_1(sum_6, tuple)
test_1(sum_6, set)

test_1(sum_7, list)
test_1(sum_7, tuple)
test_1(sum_7, set)

test_1(sum,   list )
test_1(sum,   tuple)
test_1(sum,   set)

print sys.version
print

test_2(sum_1, "recursion")
test_2(sum_2, "while")
test_2(sum_3, "for in range")
test_2(sum_4, "while iter")
test_2(sum_5, "for in")
test_2(sum_6, "reduce lambda")
test_2(sum_7, "reduce operator")
test_2(sum,   "")

print "Done."

"""
Sum.py

2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)]

sum_1 (recursion)
4.310 milliseconds

sum_2 (while)
0.119 milliseconds

sum_3 (for in range)
0.076 milliseconds

sum_4 (while iter)
0.185 milliseconds

sum_5 (for in)
0.046 milliseconds

sum_6 (reduce lambda)
0.119 milliseconds

sum_7 (reduce operator)
0.058 milliseconds

sum ()
0.009 milliseconds

Done.
"""
