from asciCalculator import calculator

calculator()
execution = True

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

def symbols():
    for i in aritmetica:
        print(i)

firstNumber = float(input("Please type the first number for your operation:\n"))

while execution == True:
    #operation = input("Please select your type of operation, it can be:\n+ = Add\n- = Subtract\n* = Multiply\n/ = Divide\n")
    print(symbols())
    operation = input(f"Please select your type of operation:")
    secondNumber = float(input("Please type the second number for your operation:\n"))

    result = aritmetica[f"{operation}"](firstNumber,secondNumber)
    print(f"{firstNumber} {operation} {secondNumber} = {result}")
    

    question = input("Would you like to continue using the last result? Yes/No\n")
    if question == "no":
        print("I Will Stop Execution")
        print("\n"*20)
        firstNumber = float(input("Please type the first number for your operation:\n"))
        execution = True
       

    elif question == "yes":
        print("I will Continue Execution")
        execution = True
        firstNumber = result

