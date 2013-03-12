#!/usr/bin/env python

# ---------
# Output.py
# ---------

import StringIO
import sys
import types

print "Output.py"

def my_write (x, s) :
    assert hasattr(x, "write")
    x.write(s)

s = "Nothing to be done.\n"
assert type(s) is str

w = StringIO.StringIO()
assert type(w) == types.InstanceType
my_write(w, s)
assert w.getvalue() is s

w = sys.stdout
assert type(w) == types.FileType
my_write(w, s)

print "Done."

"""
Output.py
Nothing to be done.
Done.
"""
