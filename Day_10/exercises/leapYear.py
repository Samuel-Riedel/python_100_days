def leapYear(year):
    if (year % 400==0) and (year % 100 ==0):
        print(f"{year} is a leap year")
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        print(f"{year} is a leap year")
        return True
   
    else:
        print(f"{year} is not a leap year")
        return False
   

leapYear(2100)
