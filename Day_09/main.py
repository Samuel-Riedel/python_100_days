print("LOGO from art.py")

answer = "yes"

dictionary = {}

while answer == "yes":
    name = input("What is your name?\n")
    bid = int(input("How much are you going to bid?\n"))
    answer = input("yes or no \n")
    dictionary[name] = bid



    if answer == "no":

        print("The Highest Bidder is:\n")
        highest_bidder = max(dictionary, key=dictionary.get)
        highest_bid = dictionary[highest_bidder]
    
        print(f"\nThe Highest Bidder is {highest_bidder} with a bid of ${highest_bid}")
        answer = "no"

    elif answer == "yes":
        pass

    





