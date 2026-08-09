#shapes is a library which contains functions for some basic shapes
#by: Navaneeth Krishna
#NomoreAI - 2025

import turtle as tu #used for testing internally no function requires it except when using in main code
import math

tester = tu.Turtle()

def polygon(t, length, sides):
    angle = 360 / sides  # Calculate angle per turn (corrected)

    for i in range(sides):
        t.fd(length)  # Move forward by length
        t.lt(angle) 

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 360
    length = circumference / n
    polygon(t, length,n )

def circleR(t, r, resolution=360):
    circumference = 2 * math.pi * r
    length = circumference / resolution
    polygon(t, length,resolution )

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360

    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def test(t):

    circle(t,50)
    t.pu()
    t.goto(100,100)
    t.pd()
    polygon(t, 100, 3)
    t.pu()
    t.goto(100,-100)
    t.pd()
    polygon(t, 50, 5)
    t.pu()
    t.goto(-130, 100)
    t.pd()
    polygon(t, 30 ,8)
    t.pu()
    t.goto(-135, -100)
    t.pd()
    polygon(t, 35, 6)



if __name__ == "__main__":
    test(tester)
