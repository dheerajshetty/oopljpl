#!/usr/bin/env python

"""
OOPL JPL: Quiz #1
"""

""" ----------------------------------------------------------------------
1. What is the output of the following program?
"""

class A (BaseException) : # extends BaseException
    pass

class B (A) :             # extends A
    pass

def f (b) :
    print "f1",
    if b :
        raise A()
    print "f2",

try :
    print "m1",
    f(False)
    print "m2",
except A :
    print "m3",
except B :
    print "m4",
finally :
    print "m5",
print "m6"

try :
    print "m1",
    f(True)
    print "m2",
except A :
    print "m3",
except B :
    print "m4",
finally :
    print "m5",
print "m6"
