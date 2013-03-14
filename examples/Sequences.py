#!/usr/bin/env python

# ------------
# Sequences.py
# ------------

def test_1 (T) :
    assert not T()

    a = T("01234")
    assert len(a) == 5

    a = T("01234")
    assert a[2] == "2"
    try :
        assert a[5] == 0                               # index error
        assert False
    except IndexError, e :
        assert type(e.args)    is tuple
        assert len(e.args)     == 1
        assert e.args[0][-18:] == "index out of range"

    a = T("54321")
    assert a[-3] == "3"
    try :
        assert a[-6] == 0                              # index error
        assert False
    except IndexError, e :
        assert type(e.args)    is tuple
        assert len(e.args)     == 1
        assert e.args[0][-18:] == "index out of range"

    a = T("01234")
    i = iter(a)
    assert str(type(i))[-10:-2] == "iterator"
    assert i is iter(i)

    a = T("01234")
    assert "1"     in a
    assert "5" not in a

    a = T("01234")
    assert not (a != a)
    assert     (a == a)
    assert not (a <  a)
    assert     (a <= a)
    assert not (a >  a)
    assert     (a >= a)

    a = T("01234")
    assert (a + a) == T("0123401234")
    b  = T("01234")
    b += a
    assert b == T("0123401234")

    a = T("01234")
    assert (3 * a) == T("012340123401234")
    b  = T("01234")
    b *= 3
    assert b == T("012340123401234")

    a = T("01234")
    assert a[ 1: 4] == T("123")
    assert a[-4:-1] == T("123")
    assert a[ 1:  ] == T("1234")
    assert a[-4:  ] == T("1234")
    assert a[  : 4] == T("0123")
    assert a[  :-1] == T("0123")
    assert a[ 0: 5] == T("01234")
    assert a[-5: 5] == T("01234")
    assert a[-9: 9] == T("01234")
    assert a[  :  ] == T("01234")
    assert a[ 4: 1] == T("")

    a = T("01234")
    assert a[ 1: 4: 2] == T("13")
    assert a[-4:-1: 2] == T("13")
    assert a[ 1:  : 2] == T("13")
    assert a[-4:  : 2] == T("13")
    assert a[  : 4: 2] == T("02")
    assert a[  :-1: 2] == T("02")
    assert a[ 0: 5: 2] == T("024")
    assert a[-5: 5: 2] == T("024")
    assert a[-9: 9: 2] == T("024")
    assert a[  :  : 2] == T("024")
    assert a[ 4: 1: 2] == T("")

    a = T("01234")
    assert a[ 4: 1:-2] == T("42")
    assert a[-1:-4:-2] == T("42")
    assert a[ 4:  :-2] == T("420")
    assert a[-1:  :-2] == T("420")
    assert a[  : 1:-2] == T("42")
    assert a[  :-4:-2] == T("42")
    assert a[ 4:-6:-2] == T("420")
    assert a[-1:-6:-2] == T("420")
    assert a[ 9:-9:-2] == T("420")
    assert a[  :  :-2] == T("420")
    assert a[ 1: 4:-2] == T("")

    a = T("01234")
    assert a[ :  :-1] == T("43210")
    assert a[4:-6:-1] == T("43210")

def test_2 (T) :
    a = T([2, 3, 4])
    assert sum(a, 0) == 9
    assert sum(a)    == 9

    a = T([[2, 3, 4], [5, 6]])
    assert sum(a, []) == [2, 3, 4, 5, 6]
#   assert sum(a)     == [2, 3, 4, 5, 6] # TypeError: unsupported operand type(s) for +: 'int' and 'list'

    a = T([(2, 3, 4), (5, 6)])
    assert sum(a, ()) == (2, 3, 4, 5, 6)
#   assert sum(a)     == (2, 3, 4, 5, 6) # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

    a = T(["abc", "de"])
#   assert sum(a, "") == "abcde"; # TypeError: sum() can't sum strings [use "".join(seq) instead]
    assert "".join(a) == "abcde"

print "Sequences.py"

test_1(str)
test_1(list)
test_1(tuple)

test_2(list)
test_2(tuple)

print "Done."
