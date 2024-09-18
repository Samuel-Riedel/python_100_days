from dollars import total_quarters, total_dimes,total_nickles,total_pennies
#create a print welcoming  print for the user **
print("Welcome user to the Coffee Machine")


#Ask the user what would he like, use an input here and call it user_coffee /// Here we will make the secret word from point number 3 **
#Admin enters the word "report" it will create a report with all the remaining materials  and total money made to create coffee
#admin must answer with report on the variable user_coffee to prompt secret menu
#USER_COFFEE = input("What would you like to drink? (Espresso / Latte / Cappuccino)").lower()

#User must see his picked item, this will be created by suing a print() with the variable user_coffee**
#print(f"You have selected {USER_COFFEE}, please wait while we server your order.")

#This variable will control if the coffee is turned off or on, it will be used a condition for the while loop**
"""
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
"""
TOTAL_LIST = []
COFFEE_POWER = True


def total_quarters():
        QUARTERS = 0.25
        user_quarters = int(input("please how many quarters?"))
        sub_totalquartes = QUARTERS * user_quarters
        total_quarters = round(sub_totalquartes,2)
        print(total_quarters)
        global TOTAL_LIST
        TOTAL_LIST.append(total_quarters)

def total_dimes():
        DIMES = 0.10
        user_dimes = int(input("please how many dimes?"))
        sub_totaldimes = DIMES * user_dimes
        total_dimes = round(sub_totaldimes,2)
        print(total_dimes)
        global TOTAL_LIST
        TOTAL_LIST.append(total_dimes)

def total_nickles():
        NICKLES = 0.05
        user_nickles = int(input("please how many nickles?"))
        sub_totalnickles = NICKLES * user_nickles
        total_nickles = round(sub_totalnickles,2)
        print(total_nickles)
        global TOTAL_LIST
        TOTAL_LIST.append(total_nickles)

def total_pennies():
        PENNIES = 0.01
        user_pennies = int(input("please how many pennies?"))
        sub_totalpennies = PENNIES * user_pennies
        total_pennies = round(sub_totalpennies,2)
        print(total_pennies)
        global TOTAL_LIST
        TOTAL_LIST.append(total_pennies)


while COFFEE_POWER == True:
    user_coffee = input("What would you like to drink? (Espresso / Latte / Cappuccino)").lower()
    print(f"You have selected {user_coffee}, please wait while we server your order.")
    print("Please Insert Coins.")

    total_quarters()
    total_dimes()
    total_nickles()
    total_pennies()

    total = sum(TOTAL_LIST,2)
    print(total)



    
   





