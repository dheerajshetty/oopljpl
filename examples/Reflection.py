#!/usr/bin/env python

# -------------
# Reflection.py
# -------------

print "Reflection.py"

class A (object) :
    def f (self) :
        return "A.f()"

class B (object) :
    def f (self) :
        return "B.f()"

class C (object) :
    def __init__ (self, v) :
        self.v = v

def test (a, b) :
    assert a().f() == "A.f()"
    assert b().f() == "B.f()"

test(A,              B)
test(type(A()),      type(B()))
test(A().__class__,  B().__class__)
test(globals()["A"], globals()["B"])

try :
    globals()["C"]()
except TypeError, e :
    assert type(e)      is     TypeError
    assert type(e.args) is     tuple
    assert len(e.args)  is     1
    assert e.args       is not ('__init__() takes exactly 2 arguments (1 given)',)
    assert e.args       ==     ('__init__() takes exactly 2 arguments (1 given)',)

try :
    globals()["D"]
except KeyError, e :
    assert type(e)      is     KeyError
    assert type(e.args) is     tuple
    assert len(e.args)  is     1
    assert e.args       is not ('D',)
    assert e.args       ==     ('D',)

print "Done."
