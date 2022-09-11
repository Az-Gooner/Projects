print("Welcome to the Quiz")

playing = input("Do you want to play a game ")

if playing.lower() != "yes":
    quit()

print ("Let's go")
score = 0
answer = input("What is 10+10? ")

if answer == "20":
    print ("Well done")
    score += 1
else: 
    print(("incorrect!"))

answer = input("what is the square root of 4? ")

if answer == "2":
    print ("Well done")
    score += 1
else: 
    print(("incorrect!"))

answer = input("What planet are we on? ")

if answer.lower() == "earth":
    print ("Well done")
    score += 1
else: 
    print(("incorrect!"))

answer = input("what is the currency in the UK? ")

if answer == "£":
    print ("Well done")
    score += 1
else: 
    print(("incorrect!"))

print("Well done! Your score is " + str(score))