#!/usr/bin/env python

# ------------
# Arguments.py
# ------------

def f (j) :
    j += 1

def g (t) :
    t += "def"

def h (b) :
    b[1] += 1

def x (b) :
    b += [5]

def y (b) :
    b += (5,)

print "Arguments.py"

i = 2
f(i)
assert i is 2

s = "abc"
g(s)
assert s is "abc"

a = [2, 3, 4]
h(a)
assert a is not [2, 4, 4]
assert a ==     [2, 4, 4]

a = [2, 3, 4]
h(a[:])
assert a is not [2, 3, 4]
assert a ==     [2, 3, 4]

a = [2, 3, 4]
x(a)
assert a is not [2, 3, 4, 5]
assert a ==     [2, 3, 4, 5]

a = [2, 3, 4]
x(a[:])
assert a is not [2, 3, 4]
assert a ==     [2, 3, 4]

a = (2, 3, 4)
y(a)
assert a is not (2, 3, 4)
assert a ==     (2, 3, 4)

print "Done."
