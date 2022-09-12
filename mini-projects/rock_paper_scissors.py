import random
from sre_compile import isstring
from xml.etree.ElementTree import QName

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    user_move = input("Choose rock, paper or scissor or Q to quit the game: ").lower()
    if user_move == "q":
        break
    if user_move not in options:
        continue

    random_number = random.randint(0, 2)
    # rock is 0, paper is 1, scissors is 2

    computer_move = options[random_number]
    print("computer move is", computer_move)

    if user_move == "rock" and computer_move == "scissors":
        print("You Won!")
        user_score += 1

    elif user_move == "paper" and computer_move == "rock":
        print("You Won!")
        user_score += 1

    elif user_move == "scissors" and computer_move == "paper":
        print("You Won!")
        user_score += 1
    
    else:
        print("You Lost :(")
        computer_score +=1
        
print("You won", user_score, "times")
print("The computer won", computer_score, "times")
print("Thanks for playing")
