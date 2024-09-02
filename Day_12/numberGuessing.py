import random

print("Welcome to the guessing number game!")

LIFES = 10
RANDOMNUMBER = random.randint(1,100)
DIFFICULTY = input("Which difficulty you want to play? Normal/Hard")

print(f"CHEATIING TIME {RANDOMNUMBER}")



#This is the function normal
def normal():
    global LIFES
    print("You have selected the normal difficulty")

#code will keep executing until user has 0 lifes
while LIFES > 0:
    userNumber = int(input("Please guess a number from 1 to 100"))
    if userNumber == RANDOMNUMBER: 
        print("you guessed the right number!")
        print("GAME OVER!")
        break
    if userNumber != RANDOMNUMBER:
        print("You guessed the wrong number, try again!")
        LIFES = LIFES -1
        print(f"You have {LIFES} lifes left!")



        







#This is the function hard
def hard():
    print("You have selected the hard difficulty")
    print(f"You have {LIFES} lifes left!")


#This code will execute one of the functions depending on the user input "normal or hard"
if DIFFICULTY == "normal":
    normal()
else:
    hard()