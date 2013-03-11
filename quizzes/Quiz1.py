#!/usr/bin/env python

"""
OOPL JPL: Quiz #1
"""

""" ----------------------------------------------------------------------
1. What does the following program do?
"""

print "1.", type(False)
print "2.", type(bool)
print "3.", type(NameError())
print "4.", type(NameError)
print "5.", type(type)

def f (n) :
    print "f1",
    if (n % 3) == 1 :
        raise NameError()
    elif (n % 3) == 2 :
        raise TypeError()
    print "f2",

def g (b) :
    try :
        print "g1",
        f(b)
        print "g2",
    except NameError :
        print "g3",
    else :
        print "g4",
    finally :
        print "g5",
    print "g6"

g(0)
g(1)
g(2)
