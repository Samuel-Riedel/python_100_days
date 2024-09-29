print("Bienvenido al calculador de promedios")

number_list = []
average = 0
total =0

power = True

while power == True:
    user_number = input("Please type a value to create an average \n" ) # this takes the users input number and will stop executing if you type "stop"
    number_list.append(user_number) #This sends the user_number that was typed to number_list

    if user_number == "stop": #when stopped the program will turn of the variable called power to false, delete the word stop from the lis and calculate the average
        number_list.pop() # this deletes the stop msg you input

        for i in number_list: # this is adding all the number from the list to the variable called average
            average += int(i)

        for i in number_list: # this divides the number the items in the list top create an average
            total = average / len(number_list)
        
        print(f"Your average is: {total}")


        power = False # turn off the while loop 


    print(number_list)
