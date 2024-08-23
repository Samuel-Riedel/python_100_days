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
        

    print(npc)#Prints the randomly picked cards 
    print(sumNpc)# Prints the sum of both cards


def userCardGenerator():
    """Function  picks two random  numbers from list and generates a sum to if user gets Blackjack."""
    user = []
    for i in range(2):
        randomCardGenerator = random.choice(cards)
        user.append(randomCardGenerator)
    sumUser = sum(user)
    print(user)# Prints the randomly picked cards 
    print(sumUser)# Prints the sum of both cards
    if sumUser == 21:
        print("BlackJack! You Win! ")
    if sumUser >= 22:
        print(f"You lost! you have {sumUser}")



userCardGenerator()
npcCardGenerator()





