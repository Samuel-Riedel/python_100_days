from dollars import total_quarters, total_dimes,total_nickles,total_pennies
from inventory import resources
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
report = resources
TOTAL_LIST = []
COFFEE_POWER = True
while COFFEE_POWER == True:
    user_coffee = input("What would you like to drink? (Espresso / Latte / Cappuccino)").lower()
    print(f"You have selected {user_coffee}, please wait while we server your order.")
    print("Please Insert Coins.")

    if user_coffee == "report":
        print(report)

    total_quarters()
    total_dimes()
    total_nickles()
    total_pennies()

    total = sum(TOTAL_LIST,2)
    print(total)



#TODO 
# Need to create the if for report i want to import it from the file inventory
# Turn off coffee machine
# Reset List after the user has payed for the coffee
# create the dictionary with prices of each coffee


   





