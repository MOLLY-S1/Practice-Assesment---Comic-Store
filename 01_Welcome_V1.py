"""Version 1
This code will create a welcome screen without using TKinter"""

print("Welcome to the Comic Book Store")

user_choice = input("Please enter an option:\n"
                    "1) Sell Comic\n"
                    "2) Show Stock\n"
                    "3) Restock Comics\n"
                    "4) Exit\n")

if user_choice == "1":
    print("Sell Comic")

elif user_choice == "2":
    print("Show Stock")

elif user_choice == "3":
    print("Restock Comics")

elif user_choice == "4":
    print("Goodbye")
