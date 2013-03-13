#!/usr/bin/env python

"""
OOPL JPL: Quiz #3
"""

""" ----------------------------------------------------------------------
1. What is the output of the following?

10
-7
0
abcdef
[2, 3, 4]
(2, 3, 4)
"""

print reduce(lambda x, y : x + y, [2, 3, 4], 1)
print reduce(lambda x, y : x - y, [2, 3, 4], 2)
print reduce(lambda x, y : y - x, [2, 3, 4], 3)

print reduce(lambda x, y : x + y, ["abc", "def"],     "")
print reduce(lambda x, y : x + y, [[2], [3], [4]],    [])
print reduce(lambda x, y : x + y, [(2,), (3,), (4,)], ())
