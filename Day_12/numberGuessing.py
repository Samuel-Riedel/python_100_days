import random

print("Welcome to the guessing number game!")

LIFES = 10
RANDOMNUMBER = random.randint(1,100)
DIFFICULTY = input("Which difficulty you want to play? Normal/Hard")



#This is the function normal
def normal():
    print("You have selected the normal difficulty")
    print(f"You have {LIFES} lifes left!")

    #while LIFES >0:
        







#This is the function hard
def hard():
    print("You have selected the hard difficulty")
    print(f"You have {LIFES} lifes left!")


#This code will execute one of the functions depending on the user input "normal or hard"
if DIFFICULTY == "normal":
    normal()
else:
    hard()