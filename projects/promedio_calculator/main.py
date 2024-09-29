print("Bienvenido al calculador de promedios")

number_list = []
average = 0
total =0

power = True

while power == True:
    user_number = input("Please type a value to create an average or type stop to finish calculation\n" ) # this takes the users input number and will stop executing if you type "stop"
    number_list.append(user_number) #This sends the user_number that was typed to number_list

    if user_number == "stop": #when stopped the program will turn of the variable called power to false, delete the word stop from the lis and calculate the average
        number_list.pop() # this deletes the stop msg you input

        #for i in number_list: 
            

        for i in number_list: # for loop divides the number of items in the list top create an average
            average += float(i)# this variable  is adding all the number from the list to the variable called average
            total = average / len(number_list)
        
        print(f"Your average is: {round(total,2)}")

        power = False # turn off the while loop
