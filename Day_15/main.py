from dollars import total_quarters, total_dimes,total_nickles,total_pennies, TOTAL_LIST
from inventory import resources, MENU
#create a print welcoming  print for the user **
print("Welcome user to the Coffee Machine")


#Ask the user what would he like, use an input here and call it user_coffee /// Here we will make the secret word from point number 3 **
#Admin enters the word "report" it will create a report with all the remaining materials  and total money made to create coffee
#admin must answer with report on the variable user_coffee to prompt secret menu
#USER_COFFEE = input("What would you like to drink? (Espresso / Latte / Cappuccino)").lower()

#User must see his picked item, this will be created by suing a print() with the variable user_coffee**
#print(f"You have selected {USER_COFFEE}, please wait while we server your order.")

#This variable will control if the coffee is turned off or on, it will be used a condition for the while loop**


COFFEE_POWER = True


while COFFEE_POWER == True:
    user_coffee = input("What would you like to drink? (Espresso / Latte / Cappuccino)").lower()
    if user_coffee =="report": # Created this early if statement so admin can access remaining resources by typing "report"
        print(f"Our remaining resources are: Water: {int(resources["water"])}, Milk:{int(resources["milk"])}, Coffee: {int(resources["coffee"])}")
        break

    print(f"You have selected {user_coffee}, please wait while we server your order.")
    print("Please Insert Coins.")

    
    total_quarters()
    total_dimes()
    total_nickles()
    total_pennies()
    
    total = sum(TOTAL_LIST)

    coffee_water = int(MENU[f"{user_coffee}"]["ingredients"]["water"])
    coffee_coffee = int(MENU[f"{user_coffee}"]["ingredients"]["coffee"])
    coffee_milk = int(MENU[f"{user_coffee}"]["ingredients"]["milk"])

    resources_water = int(resources["water"])
    resources_milk = int(resources["milk"])
    resources_coffee = int(resources["coffee"])

    remaining_water = resources_water - coffee_water
    remaining_milk = resources_milk - coffee_milk
    remaining_coffee = resources_coffee - coffee_coffee

    if total < MENU[f"{user_coffee}"]["cost"]:
        print(f"Not Enough Money!")
        break

    if user_coffee == "latte" or user_coffee == "cappuccino":
        user_return_money = total - MENU[user_coffee]["cost"]
        print(f"Your total credits are: {total}")
        print(f"The price is {MENU["latte"]["cost"]} and your total money back is: {user_return_money}")
        print(f"Our remaining resources are: Water: {remaining_water}, Milk: {remaining_milk}, Coffee: {remaining_coffee}")

    if user_coffee == "espresso":
        user_return_money = total - MENU[user_coffee]["cost"]
        print(f"Your total credits are: {total}")
        print(f"The price is {MENU["latte"]["cost"]} and your total money back is: {user_return_money}")
        print(f"Our remaining resources are: Water: {remaining_water}, Milk: {remaining_milk}, Coffee: {remaining_coffee}")
    
    



    



#TODO 
# need to create a module or function to clean my main.py on the part where im calling the if about latte dictionary 
# Need to create the if for report i want to import it from the file inventory
# Turn off coffee machine
# Reset List after the user has payed for the coffee
# create the dictionary with prices of each coffee