#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
question = input("Would you like to scramble your random generated password? Type Y/N").lower()
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomized:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
sum = nr_letters + nr_numbers + nr_symbols

randomizerLetters= random.sample(letters,nr_letters)
randomizerNumbers= random.sample(numbers,nr_numbers)
randomizerSymbols= random.sample(symbols,nr_symbols)


storage = randomizerLetters,randomizerNumbers, randomizerSymbols
#shuffleList = random.shuffle(storage)

if question =="n":
        for i in storage:
            for x in i:
                randomGenerator = print(x, end ="")
else:
        for i in storage:
            for j in storage:
             randomGenerator = print(list(j), end ="")
             print(type(randomGenerator))
             shuffleGenerator = list(j)
             print(type(shuffleGenerator))


               





























"""
randomizerLettersPicker = letters[randomizerLetters]
randomizerNumberPicker = numbers[randomizerNumber]
randomizerSymbolPicker = symbols[randomizerSymbols]

print(randomizerNumberPicker)
print(randomizerLettersPicker)
print(randomizerSymbolPicker)

"""