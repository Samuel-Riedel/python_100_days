from treasureIslandObjects import welcome, axe, dog, sword, cave, troll, tree, tunnel, gameOver, safeMarging
import time
welcome()

start= input("                         Press Y to start \n").lower() #25 spaces to center

if start =="y":
    print("You are in a island alone, where do you want to go, Left or Right? \n")
    leftOrRight = input().lower()
    if leftOrRight == "left":
        tree()
        forrest = input("You see a forrest, do you want to walk and go find some shelter? Y/N \n").lower()
        if forrest == "y":
           foundDog = input("You can hear a weird sound, want to go see what is the sound? Y/N \n").lower()
           if foundDog == "y":
               print("You found a small dog called Wolfie, you found the treasure in the island. \n")
               pickDog= input("Would you like to take the dog? Y/N\n").lower()
               if pickDog == "y":
                   time.sleep(2)
                   print("The dog exploded!!!")
                   time.sleep(1)
                   safeMarging()
                   time.sleep(3)
                   gameOver(); 
    else:
        dog()