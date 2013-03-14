#!/usr/bin/env python

# -------------------
# FunctionKeywords.py
# -------------------

def f (x, y, z) :
    return [x, y, z]

print "FunctionKeywords.py"

assert f(2, 3, 4)         == [2, 3, 4]
assert f(2, z = 4, y = 3) == [2, 3, 4]
#f(z = 4, 3, x = 2)                    # SyntaxError: non-keyword arg after keyword arg
#f(2, a = 4, y = 3)                    # TypeError: f() got an unexpected keyword argument 'a'
#f(2, z = 4, y = 3, a = 5)             # TypeError: f() got an unexpected keyword argument 'a'

print "Done."
