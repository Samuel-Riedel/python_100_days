import random
from rockPaperScissorsObjects import rock, paper,scissors

position = input("What do you choose?\n Type 0 for Rock \n Type 1 for paper\n Type 2 for Scissors\nType a number: ")
list = [0,1,2] #Ignore still not sure if its going to be used
objectList = [rock,paper,scissors]# this will be printed depending on the user input, its using index numbers

number_index = int(position) #this code converts the input into an int
show = objectList[number_index]# show uses the variable number_index to pick the user input and print the object from the list
print(show)
if position == "0":
    print("###################\nYou picked Rock\n###################")
elif position == "1":
    print("###################\nYou picked Paper\n###################")
elif position == "2":
    print("###################\nYou picked Scissors\n###################")


randomNumber = random.randint(0,1)
print(randomNumber)
if randomNumber == 0:
    print("###################\nBot picked Rock\n###################")
elif randomNumber == 1:
    print("###################\nBot picked Paper\n###################")
elif randomNumber == 2:
    print("###################\nBot picked Scissors\n###################")
showBot = objectList[randomNumber]# show uses the variable number_index to pick the user input and print the object from the list
print(showBot)

if position == "0" and showBot ==0:
    print("Its a tie!")
elif position == "1" and randomNumber ==1:
    print("Its a tie!")
elif position == "2" and showBot ==2:
    print("Its a tie!")

