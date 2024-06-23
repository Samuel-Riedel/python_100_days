print("The Love Calculator is calculating your score...")
name1 = input().lower() # What is your name?
name2 = input().lower() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


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

c

print(trueNumber+loveNumber)


