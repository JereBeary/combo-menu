print("Welcome to the Durham Transportation System!")
bus_price = 2.50
train_price = 3.00
running_total = 0
first_choice = input("Would you like to take the bus or the train? Please Enter 'bus' or 'train':")
if first_choice == "bus":
    running_total = bus_price
    print("You have picked the bus ticket. Your total is now $2.50.")
elif first_choice == "train":
    running_total = train_price
    print("You have chosen the train ticket. Your total is now $3.00.")
else: 
    print("Invalid Choice. Please enter either 'bus' or 'train' to select your transportation method.")


daypass_price = 5.00
second_choice = input("Would you like to purchase a day pass for $5.00? It allows for free rides on both the bus and train for the entire day. Please enter yes or no:")
if second_choice == "yes":
    running_total += daypass_price
    print("You have chosen the day pass. Your total is now $" + str(running_total) + ".")
elif second_choice == "no":
    print("You have chosen to not purchase the day pass. Your total is still $" + str(running_total) + ".")
else:
    print("Invalid Choice. Please enter either 'yes' or 'no' to select whether you would like to purchase the day pass.")

audio_price = 1.00
physical_price = 1.00
third_choice = input("Would you like to have an audio tour or a map tour? Please enter 'audio', 'map', or 'none':")
if third_choice == "audio":
    running_total += audio_price
    print("You have picked the audio tour. Your total is now $" + str(running_total) + ".")
elif third_choice == "map":
    running_total += physical_price
    print("You have chosen the map tour. Your total is now $" + str(running_total) + ".")
elif third_choice == "none":
    print("You have chosen to not purchase a tour. Your total is still $" + str(running_total) + ".")
else: 
    print("Invalid Choice. Please enter either 'audio', 'map', or 'none' to select your tour option.")

if running_total > 8:
    running_total -= 1.50
    print("Thank you for your purchase! We have removed $1.50 from your total for being a loyal customer. Your final total is $" + str(running_total) + ".")
    print("Have an amazing day and thank you for using the Durham Transportation System!")
else:
    print("Thank you for your purchase! Your final total is $" + str(running_total) + ".")
    print("Have an amazing day and thank you for using the Durham Transportation System!")