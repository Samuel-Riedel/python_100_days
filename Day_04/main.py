import random
from rockPaperScissorsObjects import rock, paper,scissors

user = input("What do you choose?\n Type 0 for Rock \n Type 1 for paper\n Type 2 for Scissors\nType a number: ")
list = [0,1,2] #Ignore still not sure if its going to be used
objectList = [rock,paper,scissors]# this will be printed depending on the user input, its using index numbers

number_index = int(user) #this code converts the input into an int
show = objectList[number_index]# show uses the variable number_index to pick the user input and print the object from the list
print(show)
if user == "0":
    print("###################\nYou picked Rock\n###################")
elif user == "1":
    print("###################\nYou picked Paper\n###################")
elif user == "2":
    print("###################\nYou picked Scissors\n###################")


randomNumber = random.randint(0,2)
print(randomNumber)
if randomNumber == 0:
    print("###################\nBot picked Rock\n###################")
elif randomNumber == 1:
    print("###################\nBot picked Paper\n###################")
elif randomNumber == 2:
    print("###################\nBot picked Scissors\n###################")
showBot = objectList[randomNumber]# show uses the variable number_index to pick the user input and print the object from the list
print(showBot)

if user == "0" and randomNumber ==0:
    print("Its a tie!")
elif user == "1" and randomNumber ==1:
    print("Its a tie!")
elif user == "2" and randomNumber ==2:
    print("Its a tie!")

if user  == "0" and randomNumber == 1:
    print("Bot won!")
elif user == "0" and randomNumber == 2:
    print("You won!")

if user  == "1" and randomNumber == 0:
    print("Bot won!")
elif user == "1" and randomNumber == 2:
    print("You won!")

if user  == "2" and randomNumber == 0:
    print("Bot won!")
elif user == "2" and randomNumber == 1:
    print("You won!")