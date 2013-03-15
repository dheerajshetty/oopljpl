#!/usr/bin/env python

"""
OOPL JPL: Quiz #5
"""

""" ----------------------------------------------------------------------
1. Define MyPriorityQueue such that it emulates Queue.PriorityQueue.
"""

from Queue import PriorityQueue

class MyPriorityQueue (object) :
    def __init__ (self) :
        self.a = []

    def empty (self) :
        return self.qsize() == 0

    def get (self) :
        v = min(self.a)
        self.a.remove(v)
        return v

    def put (self, v) :
        self.a.append(v)

    def qsize (self) :
        return len(self.a)

def test_priority_queue (c) :
    x = c()
    assert x.qsize() == 0
    assert x.empty()

    x.put(3)
    x.put(4)
    x.put(2)
    assert x.qsize() == 3
    assert not x.empty()

    v = x.get()
    assert v         == 2
    assert x.qsize() == 2
    assert not x.empty()

test_priority_queue(MyPriorityQueue)
test_priority_queue(  PriorityQueue)
