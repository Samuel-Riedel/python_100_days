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
    elif age >=18:
        bill = 12
        print("Adult tickets are 12$")
    wants_photo = input("Do you want a photo taken? Y or N.\n").lower()
    if wants_photo == "y":
            bill += 3
    print(f"The price of the photo is 3$, your total is: {bill}")
else:
    print("Sorry, you have to grow taller before you can ride")
    