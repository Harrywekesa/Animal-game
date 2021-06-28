
print("Make a guess...")
def check_guess(guess, answer):  # sourcery skip: aug-assign
    global score
    attempt = 0
    still_guessing = True
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer")
            score = score + 3 - attempt
            still_guessing = False
        elif attempt < 2:
            guess = input("Sorry wrong answer try again :")
        attempt = attempt + 1
    if attempt == 3:
        print("The correct answer is ", answer)
score = 0
        
guess1 = input("What is the fastest animal on land?")
check_guess(guess1, 'Cheetah')

guess2 = input("What is the slowest animal on land?")
check_guess(guess2, 'Tortoise')

guess3 = input("What is the only flying mammal?")
check_guess(guess3, 'Bat')

print("Your score is: ", score)