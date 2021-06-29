import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color()
    t.begin_fill()

    #This for looop draws a rectangle
    for counter in range(1, 3): #this range function maks the loop run twice
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
        
    t.end_fill()
    t.penup()
    
    t.shape('turtle')
    t.setheading(0)
    t.forward(80)
    
    t.penup()
    t.speed('slow')
    t.bgcolor('Dodger blue')

#drawing robots feet
t.goto(-100, -150 )
rectangle(50, 20, 'Blue')

t.goto(-30, -150)
rectangle(50, 20, 'Blue')

#Drawing the legs
t.goto(-25, -50) #The turtle moves to position x = –25, y = –50.
rectangle(15, 100, 'Grey') #Drawing the left leg

t.goto(-55,-50)
rectangle(-15, 100 ,'Grey')

#Drawing the body
t.goto(-90, 100)
rectangle(100, 150, 'Red') #Draw a red rectangle 100 across and 150 down.

#Drawing the arms
 #Upper right arm
t.goto(-150, 70)
rectangle(60, 15, 'Grey')
 #Lower right arm
t.goto(-150, 100)
rectangle(15, 40, 'Grey')

t.goto(-155, 130)
rectangle(25, 25, 'green')
t.goto(-147, 130)
rectangle(10, 15, t.bgcolor())

 #Upper left arm
t.goto(10, 70)
rectangle(60, 15, 'Grey')
 #Lower left arm
t.goto(55, 110)
rectangle(15, 40, 'Gold')

t.goto(50, 130)
rectangle(25, 25, 'Green')
t.goto(58, 130)
rectangle(10, 15, t.bgcolor())

#Drawing the neck
t.goto(-50, 120)
rectangle(15, 20, 'Yellow')

#Drawing the head
t.goto(-85, 170)
rectangle(80, 50, 'Red')

#Drawing the eyes
t.goto(-60, 160)
rectangle(30, 10, 'White')  #Drawing the white part of the eyes
    #Drawing the right pupil
t.goto(-55, 155)
rectangle(5, 5, 'Black')
    #Drawing the left pupil
t.goto(-40, 155)
rectangle(5, 5, 'Black')

#Mouth
t.goto(-65, 135)
rectangle(40, 5, 'Black')

# t.hideturtle()  makes the turtle invisible