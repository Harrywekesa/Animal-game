import turtle as t #Loads the entire turtle module
from itertools import cycle #cycle() function, which takes a list of values as its parameter and returns a special type of list that you can cycle through endlessly using the next() function

colors  = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple',  'pink'])

def draw_circle(size, angle, shift):
    t.pencolor(next(colors)) #Use the next color in the cycle.
    t.circle(size)
    t.right(angle) #Turtle turns clockwise
    t.forward(shift) #Turtle moves forward
    draw_circle(size + 10, angle + 10, shift + 1) #Recursion fucntion ie a a function calling itself

t.bgcolor('black')
t.speed('fast')
t.pensize(4)

#Calling the function for the first time
draw_circle(30, 0, 1)
