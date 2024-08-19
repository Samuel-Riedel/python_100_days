print("LOGO from art.py")

answer = "yes"

dictionary = {}

while answer == "yes":
    name = input("What is your name?\n")
    bid = int(input("How much are you going to bid?\n"))
    answer = input("yes or no \n")


    if answer == "no":

        print("The Highest Bidder is:\n")
        #keyValue = max(dictionary, key=dictionary.get)
        for key, value in dictionary.items():
            #print(keyValue, dictionary[keyValue])
            print(key,":", value)
        answer = "no"

    elif answer == "yes":
        dictionary["name"] = name
        dictionary["bid"] = bid

    





