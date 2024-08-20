def formatName(fName,lName):
    formatted_fName = fName.title()
    formatted_lName = lName.title()

    return f"{formatted_fName} {formatted_lName}"

print(formatName(input("Please type your first name: "),input("Please type your last name:")))