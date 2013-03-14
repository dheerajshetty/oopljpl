#!/usr/bin/env python

# --------------------------
# ConstructorsDestructors.py
# --------------------------

class A (object) :
    def __init__ (self, i) :
        self.i = i
        print "A.A(i)"

class B (object) :
    def __init__ (self, i) :
        self.x = A(i)
        print "B.B(i)"

print "ConstructorsDestructors.py"

x = A(2)
print

y = B(2)

print "Done."

"""
ConstructorsDestructors.py
A.A(i)

A.A(i)
B.B(i)
Done.
"""
