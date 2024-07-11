import random

words = ["hola","adios","comida"]

chosenLetter = input("Please select one letter from the alphabet:\n").lower()

chosenWord = []
randomizeWord = random.sample(words,1)

for word in randomizeWord:
    chosenWord.append(word)

for letter in chosenLetter:
   for i in letter:
       if i == chosenWord:
           print("YES")
           print(chosenWord)
       else:
           print("NOOO")


"""
question = print("Hello please choose one letter")
pickedLetter = input("Select a letter")


compareLetter = []
selectedWord = []

for letter in pickedLetter:
    compareLetter.append(letter)
    print(compareLetter)

for word in range(1):
    selectedWord.append(word)
    random.sample(selectedWord,1)
    print(selectedWord)

"""

print(chosenWord)
print(chosenLetter)