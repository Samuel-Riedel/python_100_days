import random

words = ["hola","adios","comida"]

chosenLetter = input("Please select one letter from the alphabet:\n").lower()
print("Arriba de esto va esta la letra que yo hice input no se esta impriminedo")
randomizeWord = random.sample(words,1) # this selects a random word from the list called words this is step 2
guess = [] #This stores the selected letter from the user

characterList = list(randomizeWord[0])

#this appends the selected word to a new variable called chosen word this is step 1
for word in chosenLetter:
    guess.append(word)

#-------------------------------------------------------------------------#

for items in characterList:
    newItems = chosenLetter
    if newItems == characterList:
        print("y")
    else:
        print("w")
    
"""for i in randomizeWord:
    for x in i:
        print(x)
        new.append(x)
"""

#-------------------------------------------------------------------------#
"""print(randomizeWord)
print(guess)

print(type(randomizeWord))
print(type(guess))"""


"""for x in i:
        print(x)
        if x == i:
            print("YES")
        else:
            print("NOOOO")
"""

