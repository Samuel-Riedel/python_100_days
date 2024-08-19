from rockPaperScissorsObjects import rock, paper,scissors
def userInput():
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