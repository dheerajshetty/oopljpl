#!/usr/bin/env python

# ------------
# Sequences.py
# ------------

def test_1 (c) :
    assert not c()

    a = c("01234")
    assert len(a) == 5

    a = c("01234")
    assert a[2] == "2"
    try :
        assert a[5] == 0                               # index error
        assert False
    except IndexError, e :
        assert type(e.args)    is tuple
        assert len(e.args)     == 1
        assert e.args[0][-18:] == "index out of range"

    a = c("54321")
    assert a[-3] == "3"
    try :
        assert a[-6] == 0                              # index error
        assert False
    except IndexError, e :
        assert type(e.args)    is tuple
        assert len(e.args)     == 1
        assert e.args[0][-18:] == "index out of range"

    a = c("01234")
    i = iter(a)
    assert str(type(i))[-10:-2] == "iterator"
    assert i is iter(i)

    a = c("01234")
    assert "1"     in a
    assert "5" not in a

    a = c("01234")
    assert not (a != a)
    assert     (a == a)
    assert not (a <  a)
    assert     (a <= a)
    assert not (a >  a)
    assert     (a >= a)

    a = c("01234")
    assert (a + a) == c("0123401234")
    b  = c("01234")
    b += a
    assert b == c("0123401234")

    a = c("01234")
    assert (3 * a) == c("012340123401234")
    b  = c("01234")
    b *= 3
    assert b == c("012340123401234")

    a = c("01234")
    assert a[ 1: 4] == c("123")
    assert a[-4:-1] == c("123")
    assert a[ 1:  ] == c("1234")
    assert a[-4:  ] == c("1234")
    assert a[  : 4] == c("0123")
    assert a[  :-1] == c("0123")
    assert a[ 0: 5] == c("01234")
    assert a[-5: 5] == c("01234")
    assert a[-9: 9] == c("01234")
    assert a[  :  ] == c("01234")
    assert a[ 4: 1] == c("")

    a = c("01234")
    assert a[ 1: 4: 2] == c("13")
    assert a[-4:-1: 2] == c("13")
    assert a[ 1:  : 2] == c("13")
    assert a[-4:  : 2] == c("13")
    assert a[  : 4: 2] == c("02")
    assert a[  :-1: 2] == c("02")
    assert a[ 0: 5: 2] == c("024")
    assert a[-5: 5: 2] == c("024")
    assert a[-9: 9: 2] == c("024")
    assert a[  :  : 2] == c("024")
    assert a[ 4: 1: 2] == c("")

    a = c("01234")
    assert a[ 4: 1:-2] == c("42")
    assert a[-1:-4:-2] == c("42")
    assert a[ 4:  :-2] == c("420")
    assert a[-1:  :-2] == c("420")
    assert a[  : 1:-2] == c("42")
    assert a[  :-4:-2] == c("42")
    assert a[ 4:-6:-2] == c("420")
    assert a[-1:-6:-2] == c("420")
    assert a[ 9:-9:-2] == c("420")
    assert a[  :  :-2] == c("420")
    assert a[ 1: 4:-2] == c("")

    a = c("01234")
    assert a[ :  :-1] == c("43210")
    assert a[4:-6:-1] == c("43210")

def test_2 (c) :
    a = c([2, 3, 4])
    assert sum(a, 0) == 9
    assert sum(a)    == 9

    a = c([[2, 3, 4], [5, 6]])
    assert sum(a, []) == [2, 3, 4, 5, 6]
#   assert sum(a)     == [2, 3, 4, 5, 6] # TypeError: unsupported operand type(s) for +: 'int' and 'list'

    a = c([(2, 3, 4), (5, 6)])
    assert sum(a, ()) == (2, 3, 4, 5, 6)
#   assert sum(a)     == (2, 3, 4, 5, 6) # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

    a = c(["abc", "de"])
#   assert sum(a, "") == "abcde"; # TypeError: sum() can't sum strings [use "".join(seq) instead]
    assert "".join(a) == "abcde"

print "Sequences.py"

test_1(str)
test_1(list)
test_1(tuple)

test_2(list)
test_2(tuple)

print "Done."
