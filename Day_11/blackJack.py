from blackJack_logo import blackJackCards
import random

blackJackCards()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#randomNumber = int(random.random)#no se usa esta linea

def npcCardGenerator():
    """Function generates a random number for the NPC and checks if it got
       Blackjack before User gets it."""
#--------------------------------------------------------
    npc = []
    for i in range(2):
        randomCardGenerator = random.choice(cards)
        npc.append(randomCardGenerator)
#---------------------------------------------------------
        sumNpc = sum(npc)
        if sumNpc == 21:
            print("BlackJack! NPC Won!")
            break # Program will stop executing if NPC gets Blackjack before User
        
    print(f"NPC has the cards: {npc[0]} and {npc[1]}")#Prints the randomly picked cards 
    print(f"Making it a total of: {sumNpc}")# Prints the sum of both cards
    print("\n"*3) 

#----------------------------------------------------------------------------------------------------
#In eed to fix the user part, i left where its trying toget a third card and sum it making it total of the cards---------

def userCardGenerator():
    """Function  picks two random  numbers from list and generates a sum to if user gets Blackjack."""
    user = []
    execution = True
    for i in range(2):
        randomCardGenerator = random.choice(cards)
        user.append(randomCardGenerator)
    sumUser = sum(user)
    print(f"You have the cards {user[0]} and {1}")# Prints the randomly picked cards 
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
                user.append(randomCardGenerator)
                print(f"You draw the card:{user[2+1]}")
                sumUser = sum(user)
                print(f"Making it a total of: {sumUser}")

npcCardGenerator()
userCardGenerator()






