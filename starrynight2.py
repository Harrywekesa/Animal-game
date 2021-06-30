import turtle as t
from random import randint, random

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180/points)
    t.color(col)
    t.begin_fill()
    for _ in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()
    t.Screen().bgcolor('black')
while True:
    rndpts = randint(2, 5) * 2 + 1
    rndsize = randint(10, 50)
    randcol = (random(), random(), random())
    ranx = randint(-350, 300)
    rany = randint(-250, 250)
    draw_star(rndpts, rndsize, randcol, ranx, rany)
    
# draw_star(5, 50, 'silver', 0, 0)