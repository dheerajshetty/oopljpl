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

def reduce_1 (bf, a, *z) :
    if (not a) and (not z) :
        raise TypeError("reduce() of empty sequence with no initial value")
    p = iter(a)
    if not z :
        v = p.next()
    else :
        v = z[0]
    try :
        while True :
            v = bf(v, p.next())
    except StopIteration :
        pass
    return v

def reduce_2 (bf, a, *z) :
    if (not a) and (not z) :
        raise TypeError("reduce() of empty sequence with no initial value")
    if not z :
        a = iter(a)
        v = a.next()
    else :
        v = z[0]
    for w in a :
        v = bf(v, w)
    return v

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

test_reduce(reduce_1)
test_reduce(reduce_2)
test_reduce(reduce)
