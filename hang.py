import random

words = ["adidas"]#This list stores words to be picked randomly
display = []# this stores all the underscores and is equal to the amount of the chosen_word variable
space = "_"#This variable is used to check in the while loop if it has "_" in display list
chosen_word = random.choice(words) # this selects a random word from the list called words this is step 2
lives = 6
end_Game = False
#-------------------------------------------------------------------------#
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''',]
#-------------------------------------------------------------------------#

for x in range(len(chosen_word)): # this loop takes the length of the variable chosen_word and loops through it
    display.append("_") # it appends all the underscores by times it loops the selected word

#-------------------------------------------------------------------------#

while space in display is not False: # this while loop will the code indented below while the underscores variable is not False
    guess = input("Please select one letter from the alphabet:\n").lower() #This variable stores the input the users does in a variable guess which is used to check if its correct or wrong

    for position in range(0,len(chosen_word)):
        letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        
    if letter != guess:
        lives = lives -1
        print(lives)
        print(stages[lives])

    if lives <=0:
        print("Game Over, you dont have any more attempts")
        break
    print(display)



   

#-------------------------------------------------------------------------#


