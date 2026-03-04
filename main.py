print("Welcome to the Durham Transportation System!")
bus_price = 2.50
train_price = 3.00
running_total = 0
user_choice = input("Would you like to take the bus or the train? Please Enter 'bus' or 'train':")
if user_choice == "bus":
    running_total = bus_price
    print("You have picked the bus ticket. Your total is now $2.50.")
elif user_choice == "train":
    running_total = train_price
    print("You have chosen the train ticket. Your total is now $3.00.")
else: 
    print("Invalid Choice. Please enter either 'bus' or 'train' to select your transportation method.")

daypass_price = 5.00
print("Would you like to purchase a day pass for $5.00? It allows for free rides on both the bus and train for the entire day. Please enter yes or no:")
if user_choice == "yes":
    running_total += daypass_price
    print("You have chosen the day pass.")
elif user_choice == "no":
    print("You have chosen to not purchase the day pass.")
else:
    print("Invalid Choice. Please enter either 'yes' or 'no' to select whether you would like to purchase the day pass.")

