# It does this by working out which letters are in even or odd positions. Then it swaps the
# position of each pair of letters in the message, starting with the first two, then the next two, and so on. The program also
# makes encrypted messages readable again by switching the letters back to where they started.
from tkinter import Tk, messagebox, simpledialog

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    # sourcery skip: inline-immediately-returned-variable
    even_letters = [ message[counter] for counter in range(len(message)) if is_even(counter) ] 
    return even_letters
    
#  even_letters = []
#  for counter in range(0, len(message)):
#  if is_even(counter):
#  even_letters.append(message[counter])

def get_odd_letters(message):
    # sourcery skip: inline-immediately-returned-variable
    odd_letters = [message[counter] for counter in range(len(message)) if not is_even(counter)]
    return odd_letters

#odd_letters = []
#for counter in range(0, len(message)):
#if not is_even(counter):
#odd_letters.append(message[counter])

def swap_letters(message):
    # sourcery skip: inline-immediately-returned-variable, remove-zero-from-range
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ' '.join(letter_list)
    return new_message   
    
   
def get_task(): #open a dialogue box that asks the user whether they want to encrypt or decrypt a message
    # sourcery skip: inline-immediately-returned-variable
    task =  simpledialog.askstring('task', 'Do you want to encrypt or decrypt? ')
    return task

def get_message():  # sourcery skip: inline-immediately-returned-variable
        #Opens a dialogue box asking the user to type in the message they want to encrypt or decrypt
    message = simpledialog.askstring('message', 'Type in the secret message you want to pass ')
    return message

root = Tk()
while True:
    task = get_task()
    task = task.capitalize()
    if task == 'Encrypt':
        message = get_message()
        messagebox.showinfo('Message to encrypt is :', message)
        encrypted = swap_letters(message)
    elif task == 'Decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Plain text if the encrypted message is :', decrypted)
    else:
        break
    
root.mainloop()
    
