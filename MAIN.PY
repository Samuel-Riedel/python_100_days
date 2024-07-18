import random

words = ["adidas"]
display = []
space = "_"

while space in display is not False:
    guess = input("Please select one letter from the alphabet:\n").lower()
    chosen_word = random.choice(words) # this selects a random word from the list called words this is step 2
    print(display)





    lives = 6
#Testing code
    print(f'Pssst, the solution is {chosen_word}.')

#This is adding the underscores to the display list
    for x in range(len(chosen_word)):
        display.append("_")
    
#print(display)
#-------------------------------------------------------------------------#
#the for loop is checking if the chosen letter is equal to the letters of the random picked word from the list

    print(f"Hello the space is still here ")
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

