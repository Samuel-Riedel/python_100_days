import random
from rockPaperScissorsObjects import rock, paper,scissors
objectList = [rock,paper,scissors]# this will be printed depending on the user input, its using index numbers


def botOutput():
        randomNumber = random.randint(0,2)
        #print(randomNumber)
        if randomNumber == 0:
                print("###################\nBot picked Rock\n###################")
        elif randomNumber == 1:
                print("###################\nBot picked Paper\n###################")
        elif randomNumber == 2:
                print("###################\nBot picked Scissors\n###################")
                showBot = objectList[randomNumber]# show uses the variable number_index to pick the user input and print the object from the list
        print(showBot)
