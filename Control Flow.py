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


else:
    print("\nHave a wonderful day",firstName,lastName + ", please come back and visit soon.")


print("\nWould you like to make a transaction trough our ATM") 
