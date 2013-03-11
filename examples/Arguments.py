#!/usr/bin/env python

# ------------
# Arguments.py
# ------------

print "Arguments.py"

def f (j) :
    j += 1

i = 2
f(i)
assert i is 2

def f (t) :
    t += "def"

s = "abc"
f(s)
assert s is "abc"

def f (b) :
    b[1] += 1

a = [2, 3, 4]
f(a)
assert a is not [2, 4, 4]
assert a ==     [2, 4, 4]

a = [2, 3, 4]
f(a[:])
assert a is not [2, 3, 4]
assert a ==     [2, 3, 4]

def f (b) :
    b += [5]

a = [2, 3, 4]
f(a)
assert a is not [2, 3, 4, 5]
assert a ==     [2, 3, 4, 5]

a = [2, 3, 4]
f(a[:])
assert a is not [2, 3, 4]
assert a ==     [2, 3, 4]

def f (b) :
    b += (5,)

a = (2, 3, 4)
f(a)
assert a is not (2, 3, 4)
assert a ==     (2, 3, 4)

print "Done."
