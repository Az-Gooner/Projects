from curses.ascii import isdigit
import random

number = input("what number is the highest amount you want to play with? ")

if number.isdigit():
    number = int(number)

    if number <= 0:
        print("Please type in a number greator than 0!! ")
        quit()
else:
    print("Type a number next time")
    quit()
    
    

random_number = random.randint(0, number)
guess_counter = 0

while True:
    guess_counter += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time")
        continue

    if user_guess == random_number:
        print("You are a winner!")
        break
    
    elif user_guess > random_number:
        print("Your number is above the assigned number")
    else:
        print("Your number is below the assigned number")
        
        
        
    
print("You are a winner! It took you", guess_counter, "guesses")