#!/usr/bin/env python

# -------
# Draw.py
# -------

from turtle import Turtle

def draw_line (t, x1, y1, x2, y2) :
    t.up()
    t.setx(x1)
    t.sety(y1)
    t.down()
    t.goto(x2, y2)

def draw_curve (t, x1, y1, x2, y2, l) :
    if l == 0 :
        draw_line(t, x1, y1, x2, y2)
    else :
        xm = (x1 + x2 + y1 - y2) / 2
        ym = (x2 + y1 + y2 - x1) / 2
        draw_curve (t, x1, y1, xm, ym, l - 1)
        draw_curve (t, xm, ym, x2, y2, l - 1)

t = Turtle()
assert t.isdown()
assert t.pencolor() == "black"
assert t.position() == (0, 0)
t.pencolor("blue")
draw_curve(t, 50, -50, 50, 50, 10)
raw_input()
