#!/usr/bin/env python

"""
OOPL JPL: Quiz #2
"""

""" ----------------------------------------------------------------------
1. What is the output of the following program?
"""

def f (n) :
    return n + (n >> 1) + 1

print f(3)
print f(7)

""" ----------------------------------------------------------------------
2. In the context of Project #1: Collatz, what is f() computing?
"""

""" ----------------------------------------------------------------------
3. Given positive integers, b and e, let m = e / 2. If b < m, then
   max_cycle_length(b, e) = max_cycle_length(m, e). True or False?
"""
