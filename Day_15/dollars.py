TOTAL_LIST = []

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


