import random

words = ["adidas","comida","pizza","hola"]#This list stores words to be picked randomly
display = []# this stores all the underscores and is equal to the amount of the chosen_word variable
space = "_"#This variable is used to check in the while loop if it has "_" in display list
chosen_word = random.choice(words) # this selects a random word from the list called words this is step 2
lives = 6
end_Game = False
savedLetter = []
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
    savedLetter = []
    for position in range(0,len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            savedLetter = chosen_word[position]


# Each time the user gets a wrong letter it subtract a life from the variable lives       
    if savedLetter != guess: 
        lives = lives -1
        print(lives)
        print(stages[lives])
        
# If the lives go down to  zero this code will execute and print line 92
    if lives <=0: 
        print("Game Over, you dont have any more attempts")
        print("""┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
""")
        break
# When the user guesses all the letters it will print line 97 and end the game
    if space not in display:
        end_Game = True
        print("You win!")
    print(display)



   

#-------------------------------------------------------------------------#


