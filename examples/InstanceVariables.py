#!/usr/bin/env python

# --------------------
# InstanceVariables.py
# --------------------

class A (object) :
    def f (self) :
#       self.v                        # AttributeError: 'A' object has no attribute 'v0'
        self.v0     = 0
        self.v1     = self.v0     + 1
        self.__v2   = self.v1     + 1
        self._A__v3 = self.__v2   + 1
        self._A__v3 = self._A__v2 + 1

print "InstanceVariables.py"

x = A()
assert     hasattr(x, "f")
assert not hasattr(x, "v0")

x.f()
assert     hasattr(x, "v0")
assert     hasattr(x, "v1")
assert not hasattr(x, "__v2")
assert     hasattr(x, "_A__v2")
assert     hasattr(x, "_A__v3")
assert not hasattr(x, "v4")
assert     hasattr(x, "__dict__")

assert x.v0     == 0
assert x.v1     == 1
assert x._A__v2 == 2
assert x._A__v3 == 3
#assert x.v4    == 4 # AttributeError: 'A' object has no attribute 'v4'

assert x.__dict__["v0"]     == 0
assert x.__dict__["v1"]     == 1
assert x.__dict__["_A__v2"] == 2
assert x.__dict__["_A__v3"] == 3
#assert x.__dict__["v4"]    == 4 # KeyError: '__v4'

y = A()
y.f()

x.v4 = [2, 3, 4]
assert     hasattr(x, "v4")
assert not hasattr(y, "v4")
assert x.v4             == [2, 3, 4]
assert x.__dict__["v4"] == [2, 3, 4]

y.v4 = [2, 3, 4]
assert x.v4 ==     y.v4
assert x.v4 is not y.v4

del x.v0
assert not hasattr(x, "v0")
assert     hasattr(y, "v0")

#assert A.v1 == 1 # AttributeError: type object 'A' has no attribute 'v1'

class B (object) :
    v = [2]

x = B()
y = B()

assert "v"     in B.__dict__
assert "v" not in x.__dict__
assert "v" not in y.__dict__

B.v = [3]

assert "v"     in B.__dict__
assert "v" not in x.__dict__
assert "v" not in y.__dict__

assert B.v is x.v is y.v

x.v = [4]

assert "v"     in B.__dict__
assert "v"     in x.__dict__
assert "v" not in y.__dict__

assert B.v is not x.v
assert B.v is     y.v

print "Done."
