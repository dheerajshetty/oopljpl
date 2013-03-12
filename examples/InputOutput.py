#!/usr/bin/env python

# --------------
# InputOutput.py
# --------------

import sys

print "Enter: "

assert type(sys.stdin) is file
s = sys.stdin.readline()
assert type(s) is str

print "x" + s + "y"

"""
Enter:
abc
xabc
y
"""
