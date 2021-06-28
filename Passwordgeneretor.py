import random
import string

user = input("What is your one name? ")
print(user, "Welcome to password generator" )

adjectives = ['sleepy','slow','wet','fat','smelly','red','orange','yellow','blue','prple','fluffy','proud','brave',]
nouns = ['dinosour','apple','ball','toaster','goat','dragon','hammer','duck','panda',user,'telephone','banana','teacher']

while True:
    adjective = random.choice(adjectives) # picks a random adjective from the list of adjectives
    noun = random.choice(nouns) #picks a random noun from the list of nouns

    number = random.randrange(0, 100) #picks random numbers from 0 to 99
    special_char = random.choice(string.punctuation) #picks a random punctuation mark

    password = adjective + noun + str(number) + special_char
    print("Your new password is: %s" % password )
    response = input("Would you like a new password? type y for yes or n for no: ")
    if response.lower() == 'n':
        break