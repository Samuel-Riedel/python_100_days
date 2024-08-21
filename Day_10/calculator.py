
execution = True


while execution == True:
    firstNumber = int(input("Please type the first number for your operation:\n"))

    operation = input("Please select your type of operation, it can be:\n+ = Add\n- = Subtract\n* = Multiply\n/ = Divide\n")

    secondNumber = int(input("Please type the second number for your operation:\n"))

    def addNumbers(num1, num2):
        """This function is ADDING the number the user inputs"""
        return num1 + num2

    def subtractNumbers(num1,num2):
        """This function is SUBTRACTING the number the user inputs"""
        return num1 - num2

    def multiplyNumbers(num1,num2):
        """This function is MULTIPLIES the number the user inputs"""
        return num1 * num2

    def divideNumbers(num1,num2):
        """This function is DIVIDES the number the user inputs"""
        return num1/num2

    aritmetica = {"+": addNumbers,
                "-": subtractNumbers,
                "*": multiplyNumbers,
                "/": divideNumbers}

    result = aritmetica[f"{operation}"](firstNumber,secondNumber)
    print(result)
    execution = False




"""
print(aritmetica["*"](3,8))
print(aritmetica["-"](10,9))
print(aritmetica["-"](88,9))
print(aritmetica["/"](4,2))
print(aritmetica["+"](45,20))
"""


#addingVariable = addNumbers
#subtractVariable = subtractNumbers
#multiplyVariable = multiplyNumbers
#divideVariable = divideNumbers
