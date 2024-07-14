import random

words = ["hola","adios","comida","aaaaa"]
display = []


guess = input("Please select one letter from the alphabet:\n").lower()
chosen_word = random.choice(words) # this selects a random word from the list called words this is step 2

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#-------------------------------------------------------------------------#
#the foor loop is checking if the chosen letter is equal to the letters of the random picked word from the list
for letter in chosen_word:
    if letter == guess:
        print("Right")
        findingIndex = chosen_word.index(guess)
        print(findingIndex)
        #display.insert(findingIndex,guess)
    else:
        print("Wrong")

#-------------------------------------------------------------------------#

#This is adding the underscores to the display list
for x in range(len(chosen_word)):
    display.append("_")
print(display)







"""for letter in range(0,1,1):
            print(letter.index(guess))
            findingIndex = letter.index(guess)
            display.append(findingIndex)"""




#---------ToDo----------#
#revisar porque el texto se traduce solo con la aPI de google translate ( ver como se quita )
