from blackJack_logo import blackJackCards
#from userCardGen import userCardGenerator
import random


blackJackCards()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
symbol = ['♥ Hearts', '♦ Diamonds', '♣ Clover', '♠ Spades']

npc = []

#randomNumber = int(random.random)#no se usa esta linea

def npcCardGenerator():
    sumNpc = sum(npc)

    """Function generates a random number for the NPC and checks if it got
       Blackjack before User gets it."""
#--------------------------------------------------------

    for i in range(2):
        randomCardGenerator = random.choice(cards)
        npc.append(randomCardGenerator)
#---------------------------------------------------------
        if sumNpc == 21:
            print("BlackJack! NPC Won!")
            break # Program will stop executing if NPC gets Blackjack before User
        
    print(f"NPC has the card: {npc[0]} and hidng the other one")#Prints the randomly picked cards 
    print(f"Making it a total of: {npc[0]}")# Prints the sum of both cards
    print("\n"*3) 

#----------------------------------------------------------------------------------------------------
#I need to fix the user part, i left where its trying to get a third card and sum it making it total of the cards---------

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
            drawCard = input("would you like to draw another card? Yes/No\n")
            if drawCard == "yes": # I think i need to create a loop here so the cards keeps appearing on the print in line 54 
                                  # also might create a function and import it since its making to long the code to read 
                user.append(randomCardGenerator)
                print(f"You draw the card:{user[2]}")
                sumUser = sum(user)
                print(f"Making it a total of: {sumUser}")
            elif drawCard == "no":
                for i in range(len(user)):
                    print(f"Your card is a {user[i]} of {random.choice(symbol)}")
                print(f"Your total is: {sumUser}")
                print("\n"*1)
                print(f"The NPC has the cards {npc[0]} of {random.choice(symbol)} and {npc[1]} of {random.choice(symbol)}")
                print(f"NPCs has total of {sum(npc)}")
                print("\n"*2)
                if sum(npc) > sumUser and sum(npc) < 21:
                    print("NPC Won")
                if sum(npc) == sumUser:
                    print("its a Draw!")
                if sumUser > sum(npc) and sumUser < 21:
                    print("You won!!!!")
                break



npcCardGenerator()
userCardGenerator()






