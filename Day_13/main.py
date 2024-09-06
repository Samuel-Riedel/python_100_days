from game_data import data
import random

print("Welcome") # place holder for more graphics

RANDOMSELECTOR1 = random.choice(data)
RANDOMSELECTOR2 = random.choice(data)
EXECUTE = True
def option1():
    for i in RANDOMSELECTOR1:
        print(f"{i}: {RANDOMSELECTOR1[i]}")
    if RANDOMSELECTOR1[i] == RANDOMSELECTOR1[i]:
            print("Its the same shit bro")

def option2():
    for i in RANDOMSELECTOR2:
        print(f"{i}: {RANDOMSELECTOR2[i]}")
    if RANDOMSELECTOR1["follower_count"] > RANDOMSELECTOR2["follower_count"]:
            print("Its the same shit bro")
     
    
    
    
option2()

print(RANDOMSELECTOR1["follower_count"])
print(RANDOMSELECTOR2["follower_count"])

