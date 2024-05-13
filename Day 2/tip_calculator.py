print("Welcome to the tip calculator")

bill = float(input("What was the total bill? \n"))

tip = float(input("How much would you like to give? 10, 12, or 15? \n"))
tip /= 100
percentage = bill * tip

split_bill = float(input("How many people to split the bill? \n"))

subTotal = (bill + percentage) / split_bill
total = round(subTotal,2)

print(f"Each person should pay: {total} $")

