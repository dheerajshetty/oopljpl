#!/usr/bin/env python

"""
OOPL JPL: Quiz #4
"""

""" ----------------------------------------------------------------------
1. Define my_reduce() such that it emulates reduce().
   Hint:
       p = iter(a)
       iter(p) is p
"""

import operator

def test_reduce (f) :
    try :
        assert f(operator.add, []) ==  0
        assert False
    except TypeError, e :
        assert len(e.args) == 1
        assert e.args      == ('reduce() of empty sequence with no initial value',)

    assert f(operator.add, [2, 3, 4]) ==  9 # 2 + 3 + 4
    assert f(operator.sub, [2, 3, 4]) == -5 # 2 - 3 - 4
    assert f(operator.mul, [2, 3, 4]) == 24 # 2 * 3 * 4

    assert f(operator.add, [], 0) ==  0
    assert f(operator.sub, [], 0) ==  0
    assert f(operator.mul, [], 1) ==  1

    assert f(operator.add, [2, 3, 4], 0) ==  9 # 0 + 2 + 3 + 4
    assert f(operator.sub, [2, 3, 4], 0) == -9 # 0 - 2 - 3 - 4
    assert f(operator.mul, [2, 3, 4], 1) == 24 # 1 * 2 * 3 * 4

test_reduce(my_reduce)
test_reduce(   reduce)
