#!/usr/bin/env python

"""
OOPL JPL: Quiz #1
"""

""" ----------------------------------------------------------------------
1. What does the following program do?

1. <type 'bool'>
2. <type 'type'>
3. <type 'exceptions.NameError'>
4. <type 'type'>
5. <type 'type'>
g1 f1 f2 g2 g4 g5 g6
g1 f1 g3 g5 g6
g1 f1 g5
Traceback (most recent call last):
  File "./Quiz1.py", line 40, in <module>
    g(2)
  File "./Quiz1.py", line 28, in g
    f(b)
  File "./Quiz1.py", line 22, in f
    raise TypeError()
TypeError
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

def g (n) :
    try :
        print "g1",
        f(n)
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
