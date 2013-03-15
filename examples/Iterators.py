#!/usr/bin/env python

# ------------
# Iterators.py
# ------------

print "Iterators.py"

class List_1 (object) :
    class Iterator (object) :
        def __init__ (self, y) :
            self.i = iter(y.x)

        def __iter__ (self) :
            return self

        def next (self) :
            try :
                return self.i.next()
            except StopIteration :
                raise

    def __init__ (self) :
        self.x = []

    def __getitem__ (self, i) :
        return self.x[i]

    def __iter__ (self) :
        return List_1.Iterator(self)

    def __len__ (self) :
        return len(self.x)

    def append (self, v) :
        self.x.append(v)

class List_2 (object) :
    def __init__ (self) :
        self.x = []

    def __getitem__ (self, i) :
        return self.x[i]

    def __iter__ (self) :
        for v in self.x :
            yield v

    def __len__ (self) :
        return len(self.x)

    def append (self, v) :
        self.x.append(v)

class List_3 (object) :
    def __init__ (self) :
        self.x = []

    def __getitem__ (self, i) :
        return self.x[i]

    def __iter__ (self) :
        return (v for v in self.x)

    def __len__ (self) :
        return len(self.x)

    def append (self, v) :
        self.x.append(v)

def test (c) :
    x = c()
    x.append(2)
    x.append(3)

    assert hasattr(x, "__len__")
    assert x.__len__() == 2
    assert len(x)      == 2

    assert hasattr(x, "__getitem__")
    assert x.__getitem__(1) == 3
    assert x[1]             == 3

    assert hasattr(x, "__iter__")
    i = x.__iter__()
    i = iter(x)

    assert i is iter(i)
    assert i.next() == 2
    assert i.next() == 3

    try :
        assert i.next() == 4
        assert False
    except StopIteration :
        pass

test(List_1)
test(List_2)
test(List_3)
test(list)

print "Done."
