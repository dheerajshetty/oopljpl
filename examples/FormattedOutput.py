#!/usr/bin/env python

# ------------------
# FormattedOutput.py
# ------------------

print "FormattedOutput.py"

pi = 3.14159

s = "%7.2f, %7.3f" % (pi, pi) # must be an object or a tuple
assert type(s) is str
assert s is not "   3.14,   3.142"
assert s ==     "   3.14,   3.142"

try :
    s = "%7.2f, %7.3f" % [pi, pi]
    assert False
except TypeError, e :
    assert type(e)      is TypeError
    assert type(e.args) is tuple
    assert len(e.args)  == 1
    assert e.args       == ("float argument required, not list",)

s = "%7.2f, %-7.3f" % (pi, pi)
assert type(s) is str
assert s is not "   3.14, 3.142  "
assert s ==     "   3.14, 3.142  "

s = "%7.2f, %10.6f" % (pi, pi)
assert type(s) is str
assert s is not "   3.14,   3.141590"
assert s ==     "   3.14,   3.141590"

try :
    s = "%7.2f" % (pi, pi)
    assert False
except TypeError, e :
    assert type(e)      is TypeError
    assert type(e.args) is tuple
    assert len(e.args)  == 1
    assert e.args       == ("not all arguments converted during string formatting",)

try :
    s = "%7.2f, %7.3f" % (pi)
    assert False
except TypeError, e :
    assert type(e)      is TypeError
    assert type(e.args) is tuple
    assert len(e.args)  == 1
    assert e.args       == ("not enough arguments for format string",)

try :
    s = "%7.2f, %7.3f" % (pi, "abc")
    assert False
except TypeError, e :
    assert type(e)      is TypeError
    assert type(e.args) is tuple
    assert len(e.args)  == 1
    assert e.args       == ("float argument required, not str",)

print "Done."
