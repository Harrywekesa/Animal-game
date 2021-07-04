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
c.pack()
root.after(1000, blink)
c.mainloop()