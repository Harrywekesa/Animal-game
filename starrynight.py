# Fill your screen with beautiful stars! This
# project uses Python’s turtle module
# to draw star shapes. Random numbers
# scatter the stars over the screen and
# vary their color, size, and shape.
import turtle as t

size = 300
points = 5
angle = 180 - (180/points)

t.color('silver')
t.begin_fill()

for _ in range(points):
    t.forward(size)
    t.right(angle)
    
t.end_fill()