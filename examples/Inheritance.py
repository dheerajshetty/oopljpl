#!/usr/bin/env python

# --------------
# Inheritance.py
# --------------

print "Inheritance.py"

class Shape (object) :
    def __init__ (self, x, y) :
        super(Shape, self).__init__()
#       object.__init__(self)
        self.x = x
        self.y = y

    def area (self) :
        return 0

    def __eq__ (self, rhs) :
        return (self.x == rhs.x) and (self.y == rhs.y)

    def move (self, x, y) :
        self.x = x
        self.y = y

    def __str__ (self) :
        return str(self.x) + ", " + str(self.y)

class Circle (Shape) :
    def __init__ (self, x, y, r) :
        super(Circle, self).__init__(x, y) # doesn't mention Shape
#       Shape.__init__(self, x, y)
        self.r = r

    def area (self) :
        return 3.14 * self.r * self.r

    def __eq__ (self, rhs) :
        return super(Circle, self).__eq__(rhs) and (self.r == rhs.r)
#       return Shape.__eq__(self, rhs)         and (self.r == rhs.r)

    def radius (self) :
        return self.r

    def __str__ (self) :
        return "(" + super(Circle, self).__str__() + ", " + str(self.r) + ")"
#       return "(" + Shape.__str__(self)           + ", " + str(self.r) + ")"

class PseudoCircle1 (Shape) :
    pass

class PseudoCircle2 (Shape) :
    def __init__ (self, r) :
        self.r = r

x = Shape(2, 3)
assert x.area()          == 0
assert str(x)            == "2, 3"
x.move(5, 6)
assert str(x)            == "5, 6"
#assert x.radius()       == 0      # AttributeError: 'Shape' object has no attribute 'radius'
#assert Circle.radius(x) == 0      # TypeError: unbound method radius() must be called with Circle instance as first argument (got Shape instance instead)

x = Shape(2, 3)
y = Shape(2, 3)
assert x is not y
assert x ==     y

x = Circle(2, 3, 4)
assert x.area()   == 3.14 * 4 * 4
assert str(x)     == "(2, 3, 4)"
x.move(5, 6)
assert str(x)     == "(5, 6, 4)"
assert x.radius() == 4

x = Circle(2, 3, 4)
y = Circle(2, 3, 4)
assert x is not y
assert x ==     y

x = PseudoCircle1(2, 3)
assert x.area() == 0
assert str(x)   == "2, 3"
x.move(5, 6)
assert str(x)   == "5, 6"

#x = PseudoCircle2(2, 3) # TypeError: __init__() takes exactly 2 arguments (3 given)

x = PseudoCircle2(4)
assert x.area() == 0
#assert str(x) == "5, 6" # AttributeError: 'PseudoCircle1' object has no attribute 'x'
x.move(5, 6)
assert str(x) == "5, 6"

print "Done."
