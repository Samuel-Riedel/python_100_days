from game_data import data
import random

print("Welcome") # place holder for more graphics


EXECUTE = True

def option():
    
    global EXECUTE

    while EXECUTE == True:
        RANDOMSELECTOR1 = random.choice(data)

        RANDOMSELECTOR2 = random.choice(data)

#This loop shows all the key and values from the dictionary data
        for i in RANDOMSELECTOR1:
            print(f"{i}: {RANDOMSELECTOR1[i]}")
        
        for i in RANDOMSELECTOR2:
            print(f"{i}: {RANDOMSELECTOR2[i]}")
        #user selection is an input that lets the user pick who has more followers he has 2 option 
        user_selection = input(f"Who has more followers {RANDOMSELECTOR1["name"]} or {RANDOMSELECTOR2["name"]}? Type 1 for {RANDOMSELECTOR1["name"]} /2 for {RANDOMSELECTOR2["name"]}")
        
        
        #here i change the user_selection variable depending on what option he picks (1 or 2)
        if user_selection == "1":
              user_selection = int(RANDOMSELECTOR1["follower_count"])
        elif user_selection =="2":
              user_selection = int(RANDOMSELECTOR2["follower_count"])


        #this part i need to check it  more since it should be that if the user pisck one of those it means he won 
        if user_selection > int(RANDOMSELECTOR1["follower_count"]):
                print("User has Won!!")
                print("\n"*5)
        elif user_selection > int(RANDOMSELECTOR2["follower_count"]):
                print("User has Won!!")
                print("\n"*5)
        elif user_selection < RANDOMSELECTOR1["follower_count"] or user_selection < RANDOMSELECTOR2["follower_count"]:
                print("NPC has Won! You lost!")
                print("\n"*5)
                #input("Type something 01")
                EXECUTE = False
        if RANDOMSELECTOR1["follower_count"] == RANDOMSELECTOR2["follower_count"]:
                print("Its a Tie!!")
                #input("Type something 02")
                pass



        
"""        if RANDOMSELECTOR1["follower_count"] > RANDOMSELECTOR2["follower_count"]:
                print("01 has Won!!")
                EXECUTE = False
        elif RANDOMSELECTOR2["follower_count"] > RANDOMSELECTOR1["follower_count"]:
                print("02 has Won!!")
                input("Tpe something 01")
                pass
        if RANDOMSELECTOR1["follower_count"] == RANDOMSELECTOR2["follower_count"]:
                print("Its a Tie!!")
                input("Tpe something 02")
                pass
"""
    

print(EXECUTE)



    
    
    
option()

#print(RANDOMSELECTOR1["follower_count"])
#print(RANDOMSELECTOR2["follower_count"])

