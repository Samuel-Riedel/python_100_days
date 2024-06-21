print("Welcome to the Rollercoatser")

height = int(input("Please input your height\n"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age <12:
        print("Child tickets are 5$")
    elif age <= 17:
        print("Youth tickets are 7$")
    elif age >=18:
        print("Adult tickets are 12$")
else:
    print("Sorry, you have to grow taller before you can ride")