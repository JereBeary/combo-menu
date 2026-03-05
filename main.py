print("Welcome to the Durham Transportation System!")
bus_price = 2.50
train_price = 3.00
running_total = 0
first_choice = input("Would you like to take the bus or the train? Please Enter 'bus' or 'train':")
while True:
    if first_choice == "bus":
        running_total = bus_price
        print("You have picked the bus ticket. Your total is now $2.50.")
        break
    elif first_choice == "train":
        running_total = train_price
        print("You have chosen the train ticket. Your total is now $3.00.")
        break
    else: 
        print("Invalid Choice. Please enter either 'bus' or 'train' to select your transportation method.")
        break


daypass_price = 5.00
second_choice = input("Would you like to purchase a day pass for $5.00? It allows for free rides on both the bus and train for the entire day. Please enter yes or no:")
while True:
    if second_choice == "yes":
        running_total += daypass_price
        print("You have chosen the day pass. Your total is now $" + str(running_total) + ".")
        break
    elif second_choice == "no":
        print("You have chosen to not purchase the day pass. Your total is still $" + str(running_total) + ".")
        break
    else:
        print("Invalid Choice. Please enter either 'yes' or 'no' to select whether you would like to purchase the day pass.")
        break

audio_price = 1.00
physical_price = 1.00
third_choice = input("Would you like to have an audio tour or a map tour? Please enter 'audio', 'map', or 'none':")
while True:
    if third_choice == "audio":
        running_total += audio_price
        print("You have picked the audio tour. Your total is now $" + str(running_total) + ".")
        break
    elif third_choice == "map":
        running_total += physical_price
        print("You have chosen the map tour. Your total is now $" + str(running_total) + ".")
        break
    elif third_choice == "none":
        print("You have chosen to not purchase a tour. Your total is still $" + str(running_total) + ".")
        break
    else: 
        print("Invalid Choice. Please enter either 'audio', 'map', or 'none' to select your tour option.")
        break

print("You have chosen " + first_choice + " as your transportation method, " + second_choice + " for the day pass, and " + third_choice + " for your tour option.")
print("Is this correct?")
while True:
    fourth_choice = input("Please enter 'yes' or 'no':")
    break
    if fourth_choice == "yes":
        print("Great! We will now process your order.")
        break
        if running_total > 8:
            running_total -= 1.50
            print("Thank you for your purchase! We have removed $1.50 from your total for being a loyal customer. Your final total is $" + str(running_total) + ".")
            print("Have an amazing day and thank you for using the Durham Transportation System!")
            break
        else:
            print("Thank you for your purchase! Your final total is $" + str(running_total) + ".")
            print("Have an amazing day and thank you for using the Durham Transportation System!")
            break
    elif fourth_choice == "no":
        print("We are sorry for the inconvenience. Please restart the program to make your selections again.")
        break
    else:
        print("Invalid Choice. Please enter either 'yes' or 'no' to confirm your order.")
        break