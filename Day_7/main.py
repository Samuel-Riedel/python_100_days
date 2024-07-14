import random

words = ["hola","adios","comida"]
display = []

guess = input("Please select one letter from the alphabet:\n").lower()
chosen_word = random.choice(words) # this selects a random word from the list called words this is step 2


#-------------------------------------------------------------------------#

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


for x in range(len(chosen_word)):
    display.append("_")

print(display)
    

#-------------------------------------------------------------------------#
