#!/usr/bin/env python

# -----------------
# ClassVariables.py
# -----------------

class A (object) :
#   v                   # NameError: name 'v' is not defined
    v0     = 0
#   v1     =   A.v0 + 1 # NameError: name 'A' is not defined
    v1     =     v0 + 1
    __v2   =     v1 + 1
    _A__v3 =   __v2 + 1
    _A__v3 = _A__v2 + 1
    __v3   =   __v2 + 1

print "ClassVariables.py"

assert     hasattr(A, "v0")
assert     hasattr(A, "v1")
assert not hasattr(A, "__v2")
assert     hasattr(A, "_A__v2")
assert     hasattr(A, "_A__v3")
assert not hasattr(A, "v4")
assert     hasattr(A, "__dict__")

assert A.v0     == 0
assert A.v1     == 1
assert A._A__v2 == 2
assert A._A__v3 == 3
#assert A.v4    == 4 # AttributeError: type object 'A' has no attribute 'v4'

assert A.__dict__["v0"]     == 0
assert A.__dict__["v1"]     == 1
assert A.__dict__["_A__v2"] == 2
assert A.__dict__["_A__v3"] == 3
#assert A.__dict__["v4"]    == 4 # KeyError: 'v4'

A.v4 = [2, 3, 4]
assert hasattr(A, "v4")
assert A.v4             == [2, 3, 4]
assert A.__dict__["v4"] == [2, 3, 4]

del A.v0
assert not hasattr(A, "v0")

x = A()
y = A()
assert x.v4 is y.v4

print "Done."
