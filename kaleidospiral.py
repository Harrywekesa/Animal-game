# Python’s turtle draws circles on the screen,one after another. Each time a circle is drawn,
# the turtle changes the position, angle, color,and size of the next circle it draws. A pattern
# gradually emerges.

import turtle as t #Loads the entire turtle module
from itertools import cycle #cycle() function, which takes a list of values as its parameter and returns a special type of list that you can cycle through endlessly using the next() function

colors  = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple',  'pink'])

def draw_circle(size):
    t.pencolor(next(colors)) #Use the next color in the cycle.
    t.circle(size)
    draw_circle(size + 5) #Recursion fucntion ie a a function calling itself

t.bgcolor('black')
t.speed('fast')
t.pensize(4)

#Calling the function for the first time
draw_circle(30)
