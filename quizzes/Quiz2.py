#!/usr/bin/env python

"""
OOPL JPL: Quiz #2
"""

""" ----------------------------------------------------------------------
1. What is the output of the following program?

5
11
"""

def f (n) :
    return n + (n >> 1) + 1

print f(3)
print f(7)

""" ----------------------------------------------------------------------
2. In the context of Project #1: Collatz, what is f() computing?

For odd n it's computing (3n + 1) / 2.
(3n + 1) / 2
3n/2 + 1/2
n + n/2 + 1/2
n + n/2 + 1, because n is odd
n + (n >> 1) + 1
"""

""" ----------------------------------------------------------------------
3. Given positive integers, b and e, let m = e / 2. If b < m, then
   max_cycle_length(b, e) = max_cycle_length(m, e). True or False?

True

Consider b = 10, e = 100.
Then m = 100 / 2 = 50.
max_cycle_length(10, 100) = max_cycle_length(50, 100)
All the numbers in the range [10, 49] can be mapped to numbers in the
range [50, 100] by one or more doublings, so none of the numbers in the
range [10, 49] could have a larger cycle length than the numbers in the
range [50, 100].
"""
