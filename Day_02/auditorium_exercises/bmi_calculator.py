"""
Instructions
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

BMI Wikipedia Page

The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.

Example Input 1
1.75
80
means: weight = 80 and height = 1.75

"""


# 1st input: enter height in meters e.g: 1.65
print("Please enter your height: ")
height = input()
# 2nd input: enter weight in kilograms e.g: 72
print("Please enter your weight: ")

weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

height_conver = float(height)
weight_conver = int(weight)

bmi = weight_conver / height_conver **2

bmi_int = int(bmi)

if bmi_int >= 30:
    print("Your Body Mass Index is: " + str(bmi_int) + " You are Obese!")
elif bmi_int >=25 or bmi_int <=29.9:
        print("Your Body Mass Index is: " + str(bmi_int) + " You are Overweight!")
elif bmi_int >= 18.5 or bmi_int <=24.9:
        print("Your Body Mass Index is: " + str(bmi_int) + " You are Obese!")
else:
        print("Your Body Mass Index is: " + str(bmi_int) + " You are Obese!")


