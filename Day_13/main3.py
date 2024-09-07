from game_data import data
import random

print("Welcome") # place holder for more graphics
print("\n"*3)


EXECUTE = True
SAVEDANSWER = {}
POINTS = 0


def execution():
    global POINTS
    global EXECUTE
    global SAVEDANSWER


    RANDOMSELECTOR1 = random.choice(data)

    RANDOMSELECTOR2 = random.choice(data)

#This loop shows all the key and values from the dictionary data
    for i in RANDOMSELECTOR1:
            #print(f"{i}: {RANDOMSELECTOR1[i]}")
            pass
        #print("\n"*2)
        
    for i in RANDOMSELECTOR2:
            #print(f"{i}: {RANDOMSELECTOR2[i]}")
            pass

    print("\n"*2)
        #user selection is an input that lets the user pick who has more followers he has 2 option 
    user_selection = int(input(f"Who has more followers {RANDOMSELECTOR1["name"]} or {RANDOMSELECTOR2["name"]}? Type 1 for {RANDOMSELECTOR1["name"]} /2 for {RANDOMSELECTOR2["name"]}\n"))
    print("\n"*2)
        
        
        #here i change the user_selection variable depending on what option he picks (1 or 2)
    if user_selection == 1:
              user_selection = int(RANDOMSELECTOR1["follower_count"])
              SAVEDANSWER.append(RANDOMSELECTOR1)

    elif user_selection ==2:
              user_selection = int(RANDOMSELECTOR2["follower_count"])
              SAVEDANSWER.append(RANDOMSELECTOR2)



        #this part i need to check it  more since it should be that if the user picks one of those it means he won 
    if user_selection > int(RANDOMSELECTOR1["follower_count"]) or user_selection > int(RANDOMSELECTOR2["follower_count"]):
                POINTS = POINTS + 1
                print("User has Won!!")
                print("\n"*2)  
                print(SAVEDANSWER)
               

    elif user_selection < RANDOMSELECTOR1["follower_count"] or user_selection < RANDOMSELECTOR2["follower_count"]:
                print("NPC has Won! You lost!")
                print("\n"*2)
                print(f"You had a total of {POINTS} points.")
                EXECUTE = False




def logic():
    global POINTS
    global EXECUTE
    global SAVEDANSWER

    while EXECUTE == True:
        RANDOMSELECTOR1 = random.choice(data)

        RANDOMSELECTOR2 = random.choice(data)

#This loop shows all the key and values from the dictionary data
        for i in RANDOMSELECTOR1:
            #print(f"{i}: {RANDOMSELECTOR1[i]}")
            pass
        #print("\n"*2)
        
        for i in RANDOMSELECTOR2:
            #print(f"{i}: {RANDOMSELECTOR2[i]}")
            pass

        print("\n"*2)
        #user selection is an input that lets the user pick who has more followers he has 2 option 
        user_selection = int(input(f"Who has more followers {SAVEDANSWER["name"]} or {RANDOMSELECTOR2["name"]}? Type 1 for {SAVEDANSWER["name"]} /2 for {RANDOMSELECTOR2["name"]}\n"))
        print("\n"*2)
        
        
        #here i change the user_selection variable depending on what option he picks (1 or 2)
        if user_selection == 1:
              user_selection = int(RANDOMSELECTOR1["follower_count"])
              SAVEDANSWER.pop(0)
              SAVEDANSWER.append(RANDOMSELECTOR1)
              print(SAVEDANSWER)

        elif user_selection ==2:
              user_selection = int(RANDOMSELECTOR2["follower_count"])
              SAVEDANSWER.pop(0)
              SAVEDANSWER.append(RANDOMSELECTOR2)
              print(SAVEDANSWER)




        #this part i need to check it  more since it should be that if the user picks one of those it means he won 
        if user_selection > int(SAVEDANSWER["follower_count"]) or user_selection > int(SAVEDANSWER["follower_count"]):
                POINTS = POINTS + 1
                print("User has Won!!")
                print("\n"*2)  
                print(SAVEDANSWER)
               

        elif user_selection < SAVEDANSWER["follower_count"] or user_selection < SAVEDANSWER["follower_count"]:
                print("NPC has Won! You lost!")
                print("\n"*2)
                print(f"You had a total of {POINTS} points.")
                EXECUTE = False


                
execution()
logic()



