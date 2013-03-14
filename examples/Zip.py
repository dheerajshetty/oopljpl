#!/usr/bin/env python

# ------
# Zip.py
# ------

def zip_1 (*a) :
    if not a :
        return []
    s = len(iter(a).next())
    x = s * [()]
    for r in a :
        for i in range(s) :
            x[i] += (r[i],)
    return x

def zip_2 (*a) :
    if not a :
        return []
    return map(lambda *a : a, *a)

def test (f) :
    assert f()                       == []
    assert f([])                     == []
    assert f((), ())                 == []
    assert f([2, 3])                 == [(2,), (3,)]
    assert f((2, 3), (4, 5), (6, 7)) == [(2, 4, 6), (3, 5, 7)]
    assert f([2, 3, 4], [5, 6, 7])   == [(2, 5), (3, 6), (4, 7)]

print "Zip.py"

test(zip_1)
test(zip_2)
test(zip)

print "Done."
