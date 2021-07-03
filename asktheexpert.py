#An input box asks you to enter the name of a country. When you type in your answer, the program tells you
# what the capital city is. If the program doesn’t know, it asks you to teach it the correct answer. The more
# people use the program, the smarter it gets!
from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capita_data.txt') as file:
        for line in file:
            line = line.rstrip('\n') #This removes the newline character.
            country, city = line.split('/')
            the_world[country] = city #Adds data to the dictionary
def write_to_file(country_name, city_name):
    with open('new_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)
    
print("ASk  the experts capital cities of the world")
root = Tk()
root.withdraw()

the_world = {}
read_from_file()

while True:
    query_country  = simpledialog.askstring('Country', 'Type the name of a country :') #County is the title of the box
    query_country = query_country.capitalize() #turns the first letter in a string into a capital letter.
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + 'is ' + result + ' !')
    else:
        new_city = simpledialog.askstring('Teach me', 'I do not  know what is the capital city of ' + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

root.mainloop()


