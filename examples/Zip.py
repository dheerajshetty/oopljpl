#!/usr/bin/env python

# ------
# Zip.py
# ------

def zip_1 (*a) :
    if not a :
        return []
    s = len(a[0])
    i = xrange(s)
    x = s * [()]
    for r in a :
        for j in i :
            x[j] += (r[j],)
    return x

def zip_2 (*a) :
    if not a :
        return []
    b = [iter(v) for v in a]
    return [tuple([p.next() for p in b]) for w in iter(a).next()]

def zip_aux_3 (*b) :
    try :
        w = tuple([p.next() for p in b])
    except StopIteration :
        return []
    return [w] + zip_aux_3(*b)

def zip_3 (*a) :
    if not a :
        return []
    return zip_aux_3(*[iter(v) for v in a])

def zip_4 (*a) :
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
test(zip_3)
test(zip_4)
test(zip)

print "Done."
