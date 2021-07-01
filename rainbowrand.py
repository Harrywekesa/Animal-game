import turtle as t
import random as r

def get_line_len():  # sourcery skip: lift-return-into-if, switch
    choice = input("Enter line length(Long, medium, short)").lower()
    if choice == 'long':
        line_len = 250
        
    elif choice == 'medium':
        line_len = 200
        
    else:
        line_len = 100
    
    return line_len

def get_line_width():  # sourcery skip: lift-return-into-if, switch
    choice = input("Choose line thickness(Superthick, Thick, Thin)").lower()
    if choice == 'superthick':
        line_width = 40
        
    elif choice == 'thick':
        line_width = 250
        
    else:
        line_width = 10          
        
    return line_width  
line_len = get_line_len()
line_width = get_line_width()

#Keeping the turtle inside the main screen
def inside_window():  # sourcery skip: inline-immediately-returned-variable
    left_limit = (-t.window_width() / 2) + 100 
    right_limit = (-t.window_width() / 2) - 100
    top_limit = (-t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    
    (x, y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

#This function makes the turtle turn and move forward in a new direction, drawing a single line of random
#color as it goes. Your main program will use it over and over again todraw mutant rainbows.
def move_turtle(line_length):
    pen_colors = ['Red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    t.pencolor(r.choice(pen_colors))
    if inside_window(): #This checks if the turtle is inside the set limits.
        angle = (r.randint(0, 180))
        t.right(angle)
        t.forward(line_len) #The turtle moves forwards in line_ length steps.
    else:
        t.backward(line_len) #If the turtle is outside the limits, it moves backward.
        
#Summoning the turtle
t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_width)

while True:
    move_turtle(line_len)

