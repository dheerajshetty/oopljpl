#!/usr/bin/env python

# ---------
# Reduce.py
# ---------

import operator

def reduce_1 (bf, a, v) :
    i = 0
    s = len(a)
    while i != s :
        v = bf(v, a[i])
        i += 1
    return v

def reduce_2 (bf, a, v) :
    p = iter(a)
    while True :
        try :
            v = bf(v, p.next())
        except StopIteration :
            break
    return v

def reduce_3 (bf, a, v) :
    for w in a :
        v = bf(v, w)
    return v

def test (f) :
    assert f(operator.add, [], 0) == 0

    a = [2, 3, 4]
    assert f(operator.add, a, 0) ==  9
    assert f(operator.sub, a, 0) == -9
    assert f(operator.mul, a, 1) == 24

    a = ([2, 3, 4], [5, 6])
    assert f(operator.add, a, []) == [2, 3, 4, 5, 6]

    a = [(2, 3, 4), (5, 6)]
    assert f(operator.add, a, ()) == (2, 3, 4, 5, 6)

    a = ("abc", "de")
    assert f(operator.add, a, "") == "abcde"

print "Reduce.py"

test(reduce_1)
test(reduce_2)
test(reduce_3)
test(reduce)

print "Done."
