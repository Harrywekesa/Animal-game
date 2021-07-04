from tkinter import HIDDEN, NORMAL, Tk, Canvas


#t makes the eyes look closed by hiding the pupils and filling the eyes with the same color as the body.
def toggle_eyes():
    current_color = c.itemcget(eye_left,'fill') #checks the eyes’ current color: white is open, blue is closed.
    new_color = c.body_color if current_color == 'white' else 'white' #sets the eyes’ new_color to the opposite value
    current_state = c.itemcget(pupil_left, 'state') #checks if the current state of the pupils is NORMAL (visible) or HIDDEN (not visible).
    new_state = NORMAL if current_state == HIDDEN else HIDDEN #sets the pupils’ new_ state to the opposite value
    c.itemconfigure(pupil_left, state = new_state)  #This changes the visibility of the pupils.
    c.itemconfigure(pupil_right, state = new_state)  #This changes the visibility of the pupils.
    c.itemconfigure(eye_left, fill = new_color)      #This changes the eyes’ fill color
    c.itemconfigure(eye_right, fill = new_color)      #This changes the eyes’ fill color

def blink():
    toggle_eyes() #Close the eyes.
    root.after(250, toggle_eyes) #Wait 250 milliseconds, then open the eyes
    root.after(3000, blink)        #Wait 3,000 milliseconds, then blink again.
    
def toggle_pupils():  # sourcery skip: extract-duplicate-method
    if not c.eyes_crossed: #if the pupils aren’t crossed, this line moves them in.
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True #This line sets a flag variable saying the eyes are crossed.
    else:  #if the pupils are crossed, this line moves them out/back to normal.
        c.move(pupil_left, -10, -5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False  #This line sets a flag variable saying the eyes aren't crossed.
    
def toggle_tongue():  # sourcery skip: extract-duplicate-method
    if not c.tongue_out:
        #If the tongue isn’t out, these lines make it visible.
        c.itemconfigure(tongue_tip, state = NORMAL)
        c.itemconfigure(tongue_main, state = NORMAL)
        c.tongue_out = True #This line sets a flag variable saying the tongue is now out.
    else: #The tongue is already out (else).
        #These lines hide the tongue again.
        c.itemconfigure(tongue_tip, state = HIDDEN)
        c.itemconfigure(tongue_main, state = HIDDEN)
        c.tongue_out = False #This line sets a flag variable saying the tongue isn’t out.
    
def show_happy(event): #This will be an event handler
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state = NORMAL)
        c.itemconfigure(cheek_right, state = NORMAL)
        c.itemconfigure(mouth_happy, state = NORMAL)
        c.itemconfigure(mouth_normal, state = HIDDEN)
        c.itemconfigure(mouth_sad, state = HIDDEN)
        c.happy_level = 10 #This line puts the happiness level back up to 10.To recheer the pet.
    return

def hide_happy(event):
    c.itemconfigure(cheek_left, state = HIDDEN)
    c.itemconfigure(cheek_right, state = HIDDEN)
    c.itemconfigure(mouth_happy, state = HIDDEN)
    c.itemconfigure(mouth_normal, state = NORMAL)
    c.itemconfigure(mouth_sad, state = HIDDEN)
    return
#checks to see if c.happy_level is 0 yet. If it is, it changes Screen Pet’s expression
#to a sad one. If it’s not, it subtracts 1 from c.happy_level. Like
#blink(), it reminds mainloop() to call it again after 5 seconds
def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state = HIDDEN)
        c.itemconfigure(mouth_normal, state = HIDDEN)
        c.itemconfigure(mouth_sad, state = NORMAL)
    else:
        c.happy_level -= 1 #Subtract 1 from the value of c.happy_level.
    root.after(5000, sad) #Call sad() again after 5,000 milliseconds.
    
def cheecky(event):
    toggle_tongue() #Stick tongue out
    toggle_pupils() #Crosses the pupils
    hide_happy(event) #hides happy face
    root.after(1000, toggle_tongue) #Put the tongue back in after 1,000 milliseconds.
    root.after(1000, toggle_pupils) #Uncross the pupils after 1,000 milliseconds.
    return


root = Tk()    
c= Canvas(root, width = 400, height = 400)
c.configure(bg = 'darkblue', highlightthickness = 0)
c.body_color = 'skyblue'
body = c.create_oval(35, 20, 365, 350, outline = c.body_color, fill = c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color,fill=c.body_color)
foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill= c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill= c.body_color)
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)
cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)
c.pack()

#Tkinter calls the mouse-pointer moving over its window a <Motion> event. 
#You need to link this to the handler function by using Tkinter’s bind()command
c.bind('<Motion>', show_happy)

#calls hide_happy() when the mouse-pointer leaves the window. 
# It links Tkinter’s <Leave> event to hide_happy()
c.bind('Leave', hide_happy)

#To trigger Screen Pet’s cheeky expression, link any double-click event to the cheeky() function
c.bind('<Double - 1>', cheecky)

#flag variables to the code to keep track of whether Screen Pet’s eyes
#are crossed or its tongue is out
c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False

root.after(1000, blink)
root.after(5000, sad)

c.mainloop()