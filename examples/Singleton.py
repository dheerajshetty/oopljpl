#!/usr/bin/env python

# ------------
# Singleton.py
# ------------

import types

print "Singleton.py"

class A (object) :
    def f (self) :
        return "A.f()"

assert str(type(A)) ==     "<type 'type'>"
x = A()
assert str(type(x)) ==     "<class '__main__.A'>"
assert x.f()        is not "A.f()"
assert x.f()        ==     "A.f()"
y = type(x)()
assert str(type(y)) ==     "<class '__main__.A'>"
assert y            is not x
assert y.f()        is not "A.f()"
assert y.f()        ==     "A.f()"

assert str(type(A)) ==     "<type 'type'>"
A = A()
assert str(type(A)) ==     "<class '__main__.A'>"
assert A.f()        is not "A.f()"
assert A.f()        ==     "A.f()"
y = type(A)()
assert str(type(y)) ==     "<class '__main__.A'>"
assert y            is not A
assert y.f()        is not "A.f()"
assert y.f()        ==     "A.f()"



def BDecorator (c) :
    x = c()
    return lambda : x

class B1 (object) :
    def f (self) :
        return "B1.f()"
assert str(type(B1))   ==     "<type 'type'>"
B1 = BDecorator(B1)
assert str(type(B1))   ==     "<type 'function'>"
assert str(type(B1())) ==     "<class '__main__.B1'>"
assert B1()            is     B1()
assert B1().f()        is not "B1.f()"
assert B1().f()        ==     "B1.f()"
y = type(B1())()
assert str(type(y))    ==     "<class '__main__.B1'>"
assert y               is not B1
assert y.f()           is not "B1.f()"
assert y.f()           ==     "B1.f()"

@BDecorator
class B2 (object) :
    def f (self) :
        return "B2.f()"
assert str(type(B2))   ==     "<type 'function'>"
assert str(type(B2())) ==     "<class '__main__.B2'>"
assert B2()            is     B2()
assert B2().f()        is not "B2.f()"
assert B2().f()        ==     "B2.f()"
y = type(B2())()
assert str(type(y))    ==     "<class '__main__.B2'>"
assert y               is not B2
assert y.f()           is not "B2.f()"
assert y.f()           ==     "B2.f()"



def CDecorator (c) :
    x = []
    def g () :
        if x == [] :
            x.append(c())
        return x[0]
    return g

class C1 (object) :
    def f (self) :
        return "C1.f()"
assert str(type(C1))   ==     "<type 'type'>"
C1 = BDecorator(C1)
assert str(type(C1))   ==     "<type 'function'>"
assert str(type(C1())) ==     "<class '__main__.C1'>"
assert C1()            is     C1()
assert C1().f()        is not "C1.f()"
assert C1().f()        ==     "C1.f()"
y = type(C1())()
assert str(type(y))    ==     "<class '__main__.C1'>"
assert y               is not C1
assert y.f()           is not "C1.f()"
assert y.f()           ==     "C1.f()"

@CDecorator
class C2 (object) :
    def f (self) :
        return "C2.f()"
assert str(type(C2))   ==     "<type 'function'>"
assert str(type(C2())) ==     "<class '__main__.C2'>"
assert C2()            is     C2()
assert C2().f()        is not "C2.f()"
assert C2().f()        ==     "C2.f()"
y = type(C2())()
assert str(type(y))    ==     "<class '__main__.C2'>"
assert y               is not C2
assert y.f()           is not "C2.f()"
assert y.f()           ==     "C2.f()"



class D (object) :
    __d = {}

    def __init__ (self):
        self.__dict__ = self.__d

    def f (self) :
        return "D.f()"

assert D()          is not D()
assert D().__dict__ is     D ().__dict__
assert D().f()      is not "D.f()"
assert D().f()      ==     "D.f()"

print "Done."
