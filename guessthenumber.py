import random

print("number guessing game")

number=int(random.randint(1,9))

turns=0

print("guess a number between 1 to 9")

while(turns<5):
    guess=int(input("enter your guess"))

    if(guess==number):
        print("YOU WON!")
        break
    elif(guess<number):
        print("Guess is too low! try higher than ",guess)
    else:
        print("Guess is too high! try a num lower than ",guess)
    turns=turns+1
if(turns==5):
    print("DEFEAT! The number is ",number)        
