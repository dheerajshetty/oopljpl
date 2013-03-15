#!/usr/bin/env python

# -------------
# Reflection.py
# -------------

print "Reflection.py"

class A (object) :
    def f (self) :
        return "A.f()"

class B (object) :
    def __init__ (self, v) :
        self.v = v

def test (a) :
    assert a().f() == "A.f()"

test(A)
test(type(A()))
test(A().__class__)
test(globals()["A"])

try :
    globals()["B"]()
except TypeError, e :
    assert type(e)      is     TypeError
    assert type(e.args) is     tuple
    assert len(e.args)  is     1
    assert e.args       is not ('__init__() takes exactly 2 arguments (1 given)',)
    assert e.args       ==     ('__init__() takes exactly 2 arguments (1 given)',)

try :
    globals()["C"]
except KeyError, e :
    assert type(e)      is     KeyError
    assert type(e.args) is     tuple
    assert len(e.args)  is     1
    assert e.args       is not ('C',)
    assert e.args       ==     ('C',)

print "Done."
