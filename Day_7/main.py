import random

words = ["adidas"]
display = []


guess = input("Please select one letter from the alphabet:\n").lower()
chosen_word = random.choice(words) # this selects a random word from the list called words this is step 2

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#This is adding the underscores to the display list
for x in range(len(chosen_word)):
    display.append("_")
    
#print(display)
#-------------------------------------------------------------------------#
#the for loop is checking if the chosen letter is equal to the letters of the random picked word from the list
for position in range(0,len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        print("Right")
        display[position] = letter
    else:
        print("Wrong")
        pass





"""for letter in chosen_word:
    if letter == guess:
        print("Right")
        findingIndex = chosen_word.index(guess) #this line finds the index in which the letter is right
        #print(findingIndex)
        display.insert(findingIndex,guess) #This line inserts the chosen word depending in the index of the letter  if its found
            
    else:
        print("Wrong")
        pass"""

#-------------------------------------------------------------------------#


print(display)







"""for letter in range(0,1,1):
            print(letter.index(guess))
            findingIndex = letter.index(guess)
            display.append(findingIndex)
            
            
"""


"""for x in range(0,len(chosen_word)+1,1):

"""



#---------ToDo----------#
#Need to insert two letters not just one

#revisar porque el texto se traduce solo con la aPI de google translate ( ver como se quita )
