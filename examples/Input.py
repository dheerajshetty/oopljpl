#!/usr/bin/env python

# --------
# Input.py
# --------

import StringIO
import sys
import types

print "Input.py"

def my_read (x) :
    assert hasattr(x, "readline")
    return x.readline()

s = "Nothing to be done.\n"
assert type(s) is str

r = StringIO.StringIO(s)
assert type(r) == types.InstanceType
t = my_read(r)
assert t is s

r = sys.stdin
assert type(r) == types.FileType
t = my_read(r)
assert t is not s
assert t ==     s

print "Done."

"""
Input.py
Nothing to be done.
Done.
"""
