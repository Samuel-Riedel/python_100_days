from blackJack_logo import blackJackCards
import random

blackJackCards()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#randomNumber = int(random.random)#no se usa esta linea

user = []
npc = []

def userCardGenerator():
    for i in range(2):
        randomCardGenerator = random.choice(cards)
        user.append(randomCardGenerator)
    print(user)


def npcCardGenerator():
    for i in range(2):
        randomCardGenerator = random.choice(cards)
        npc.append(randomCardGenerator)
    print(npc)

userCardGenerator()
npcCardGenerator()


