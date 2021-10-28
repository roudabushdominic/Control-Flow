# Developer : Dominic Roudabush
# Date: 10.11.2021
# Program: ATM Bank Transaction

"""
This Program simulates an ATM utilizing If, ELif, and Else statements
Nesting out If statements and refresh our Comparison & Logical Operators
"""

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users for their first and last name using variables
firstName = input("What is your first name: ") 
lastName = input("What is your last name: ")

print("Welcome to Cash-R-Us", firstName, lastName + ", we will now set up a security PIN on your account.\n")

# Set up a pin -Personal Identification Number
pin = input("Please choose a 4 digit Personal Identification Number:")

print("\nThank you", firstName + ",we see that you set you pin to", pin)

print("\nWould you like to make a transaction through our Automated Teller Machine")
atm = input("Yes or No: ").lower()

if atm == "yes":
    print("\n*********************************************************\n")

    # This part of the program will be asking users to complete a transaction through the ATM
    print("Please enter your ATM Card\n")
    print("Welcome to Cash-R-Us ATM",firstName,lastName,"\n")
    userPIN = input("What is your 4 digit PIN: ")

    if pin == userPIN:
        balance = 674
        print("\nYour Balance: $" + str(balance))
        
        # Ask users what type of transaction they want - Withdrawal - Deposit 
        typeOfTransaction = input("\nWould you like to make a Withdrawal or a Deposit\nW = Withdrawal or D = Deposit: ").lower
        if typeOfTransaction == "W":
            withdrawalAmount = int(input("Enter amount of Withdrawal: "))
            balance = balance - withdrawalAmount
            print("Your new balance is: $" + str(balance))
        
        
        
        
        
    else:
        print("Sorry",firstName,lastName,"your pin doesnt match our records")

else:
    print("\nHave a wonderful day",firstName,lastName + ", please come back and visit soon.")




