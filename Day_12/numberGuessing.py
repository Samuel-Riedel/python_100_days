import random
from art import gameOver

print("Welcome to the guessing number game!")

LIFES = 10
RANDOMNUMBER = random.randint(1,100)
DIFFICULTY = input("Which difficulty you want to play? Normal/Hard\n").lower()

#This is the function normal
def normal():
    """Function will initialize with 10 lifes for the user"""

    global LIFES
    print("You have selected the normal difficulty")

#code will keep executing until user has 0 lifes
    while LIFES > 0:
        userNumber = int(input("Please guess a number from 1 to 100\n"))
        if userNumber == RANDOMNUMBER: 
            print("you guessed the right number!")
            print("GAME OVER!")
            break
        if userNumber != RANDOMNUMBER:
            print("You guessed the wrong number, try again!")
            LIFES = LIFES -1
            print(f"You have {LIFES} lifes left!")
            if userNumber >  RANDOMNUMBER:
                print("Your number is too high!")
            elif userNumber <  RANDOMNUMBER:
                print("Your number is too low!")
            elif LIFES == 0:
                gameOver()
                print(f"The secret number was: {RANDOMNUMBER}")

#This is the function hard
def hard():
    """Function will initialize with 5 lifes for the user"""
    global LIFES
    LIFES = 5
    print("You have selected the hard difficulty\n")

    while LIFES > 0:
        userNumber = int(input("Please guess a number from 1 to 100\n" ))
        if userNumber == RANDOMNUMBER: 
            print(f"you guessed the right number! {RANDOMNUMBER}")
            print("GAME OVER!")
            break
        if userNumber != RANDOMNUMBER:
            print("You guessed the wrong number, try again!")
            LIFES = LIFES -1
            print(f"You have {LIFES} lifes left!")
            if userNumber >  RANDOMNUMBER:
                print("Your number is too high!")
            elif userNumber <  RANDOMNUMBER:
                print("Your number is too low!")
            if LIFES == 0:
                gameOver()
                print(f"The secret number was: {RANDOMNUMBER}")



#This code will execute one of the functions depending on the user input "normal or hard"

if DIFFICULTY == "normal":
    normal()
else:
    hard()

