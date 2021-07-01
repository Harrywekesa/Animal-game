import turtle as t

def draw_planet(col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

t.Screen().bgcolor('black')   
draw_planet('blue', 0, 0)  

    