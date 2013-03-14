#!/usr/bin/env python

# ------------------
# GlobalVariables.py
# ------------------

v1 = 1
v2 = 2
v3 = 3
v4 = 4
v5 = 5

def f () :
    assert v1 == 1 # global

    v2 = 7 # local

    try :
        assert v3 == 3            # local
        assert False
    except UnboundLocalError, e :
        assert len(e.args) == 1
        assert e.args      == ("local variable 'v3' referenced before assignment",)
    v3 = 8                        # local

    try :
        v4 += 5                   # local
        assert False
    except UnboundLocalError, e :
        assert len(e.args) == 1
        assert e.args      == ("local variable 'v4' referenced before assignment",)

    global v5      # global
    assert v5 == 5
    v5 = 10

print "GlobalVariables.py"

f()

assert v1 ==  1
assert v2 ==  2
assert v3 ==  3
assert v4 ==  4
assert v5 == 10

print "Done."
