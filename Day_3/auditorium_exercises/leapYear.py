print("Hello and welcome to the leap year checker")
year = int(input("Please input a year \n"))

if year % 400 == 0:
  print("Leap year")
elif year % 100 == 0:
  print("Not leap year")
elif year % 4 == 0:
  print("Leap year")
else:
  print("Not leap year")