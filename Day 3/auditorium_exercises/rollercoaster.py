print("Welcome to the Rollercoatser")

height = float(input("Please input your height\n"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age <12:
        bill = 5
        print("Child tickets are 5$")
    elif age <= 17:
        bill = 7
        print("Youth tickets are 7$")
    elif age >=18 and age <=44:
        bill = 12
        print("Adult tickets are 12$")
    elif age >=45 and age <=55:
        bill = 0
        print(f"Midlife crisis tickets are 0$")
    wants_photo = input("Do you want a photo taken? Y or N.\n").upper()
    if wants_photo == "Y":
        bill += 3
        print(f"The price of the photo is 3$, your total is: {bill}")
    else:
        print(f"Your total bill is: {bill}")

else:
    print("Sorry, you have to grow taller before you can ride")
    