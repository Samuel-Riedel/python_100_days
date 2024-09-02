import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
symbol = ['♥ Hearts', '♦ Diamonds', '♣ Trebol', '♠ Spades']

def userCardGenerator():
    """Function  picks two random  numbers from list and generates a sum to if user gets Blackjack."""
    user = []
    execution = True
    for i in range(2):
        randomCardGenerator = random.choice(cards)
        user.append(randomCardGenerator)
        randomSymbol = random.choice(symbol)
    sumUser = sum(user)
    print(f"You have the cards {user[0]} and {user[1]}")# Prints the randomly picked cards 
    print(f"Making it a total of {sumUser}")# Prints the sum of both cards
    print("\n"*4) 

    if sumUser == 21:
        print("BlackJack! You Win! ")
    while execution == True:
        if sumUser >= 22:
            print(f"You lost! you have {sumUser}")
            execution = False
        if sumUser <= 21:
            drawCard = input("would you like to draw another card? Yes/No")
            if drawCard == "yes": # I think i need to create a loop here so the cards keeps appearing on the print in line 54 
                                  # also might create a function and import it since its making to long the code to read 
                user.append(randomCardGenerator)
                print(f"You draw the card:{user[2]}")
                sumUser = sum(user)
                print(f"Making it a total of: {sumUser}")
            elif drawCard == "no":
                for i in range(len(user)):
                    print(f"Your card is a {user[i]} of {randomSymbol}")
                print(f"Your total is: {sumUser}")
                print(f"The NPc has the cards {npc[0]} and {npc[1]}")

                    #print(f"Your cards are {user[i]} xxxx")
                break