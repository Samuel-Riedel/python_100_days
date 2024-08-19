print("The Love Calculator is calculating your score...")
name1 = input("What is your name? \n") # What is your name?
name2 = input("What is their name?\n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")
trueSum1 = t+r+u+e

t = name2.count("t")
r = name2.count("r")
u = name2.count("u")
e = name2.count("e")
trueSum2 = t+r+u+e

trueNumber = str(trueSum2 + trueSum1)

l = name1.count("l")
o = name1.count("o")
v = name1.count("v")
e = name1.count("e")
loveSum1 = l+o+v+e

l = name2.count("l")
o = name2.count("o")
v = name2.count("v")
e = name2.count("e")
loveSum2 = l+o+v+e

loveNumber = str(loveSum1 + loveSum2)

mergedNumbers = int(trueNumber+loveNumber)

if mergedNumbers < 10 or mergedNumbers > 90:
  print(f"Your score is {mergedNumbers}, you go together like coke and mentos.")
elif mergedNumbers >=40 and mergedNumbers <=50:
  print(f"Your score is {mergedNumbers}, you are alright together.")
else:
  print(f"Your score is {mergedNumbers}.")

