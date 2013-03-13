#!/usr/bin/env python

# ------
# Map.py
# ------

def map_1 (uf, a) :
    x = []
    i = 0
    s = len(a)
    while i != s :
        x.append(uf(a[i]))
        i += 1
    return x

def map_2 (uf, a) :
    x = []
    p = iter(a)
    try :
        while True :
            x.append(uf(p.next()))
    except StopIteration :
        pass
    return x

def map_3 (uf, a) :
    x = []
    for v in a :
        x.append(uf(v))
    return x

def map_4 (uf, a) :
    return [uf(v) for v in a]

def test (f) :
    assert f(lambda x : x ** 2, []) == []

    a = [2, 3, 4]
    assert f(lambda x : x ** 2, a) == [4,  9, 16]
    assert f(lambda x : x ** 3, a) == [8, 27, 64]

    a = ([2], [3], [4])
    assert f(lambda x : x + [5], a) == [[2, 5], [3, 5], [4, 5]]

    a = [(2,), (3,), (4,)]
    assert f(lambda x : x + (5,), a) == [(2, 5), (3, 5), (4, 5)]

    a = ("abc", "def", "ghi")
    assert f(lambda x : x + "xyz", a) == ["abcxyz", "defxyz", "ghixyz"]

print "Map.py"

test(map_1)
test(map_2)
test(map_3)
test(map_4)
test(map)

print "Done."
