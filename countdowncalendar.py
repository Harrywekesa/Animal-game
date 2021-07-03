#the program shows a list of future events and tells you how many days there are until each one
import tkinter   #Canvas is a blank rectangle where we can place the different shapes and graphics
from datetime import date, datetime

def get_events():
    list_events = []
    with open('events.txt') as file: #pen the file called events.txt so the program can read it
        for line in file:  #loop to bring information from the text file into your program
            line = line.rstrip('\n')  #tells Python to ignore these invisible characters when it reads the text file.
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d%m%y').date()  #Turns the second item in the list from a string into a date.
            current_event[1] = event_date  #Set the second item in the list to be the date of the event.
            list_events.append(current_event)  #After this line is run, the program loops back to read the next line from the file.
        return list_events #fter all the lines have been read, the function hands over the complete list of events to the program.
def days_btn_dates(date1, date2):
    time_btn = str(date1 -date2)
    number_of_days = time_btn.split(' ')
    return number_of_days[0]
    
     
root = tkinter.Tk()
c = tkinter.Canvas(root, width = 800, height = 800, bg = 'black')
c.pack()
# This line adds text onto the c canvas. The text starts at x = 100, y = 50. The starting coordinate
# is at the left (west) of the text.
c.create_text(100, 50, anchor='w', fill = 'orange', font = 'Arial 28 bold underline', text = 'My countdown calendar')

events = get_events()
today = date.today()

for event in events:
    event_name = event[0]
    days_until = days_btn_dates(event[1], today)
    display = 'It is %s days until %s ' %(days_until, event_name)
    c.create_text(100, 100,anchor = 'w', fill = 'lightblue', font = 'Arial 28 bold', text = display) 
root.mainloop()