# File: register.py
# Author: Fatima Aguado Espinosa
# Date: 02/08/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for the member's first, middle, and last name. It also asks for the phone number,
# mailing address and then uses this information to convert the phone number into local, international,
# and North American format. It also splits the mailing address by the
# street number, street name, city, state, and zipcode.
print("Welcome to the Library Management App.")
print("Member registration")
first = input("Enter the member\'s first name: ")
# A "\" is needed so the "'" is read as ownership instead of a statement.
middle = input("Enter the member\'s middle name: ")
last = input("Enter the member\'s last name: ")
phone = input("Enter the member\'s phone number: ")
address = input("Enter the member\'s mailing address: ")
print()
# print() creates a blank space
parta, partb, partc = address.split(',')
# split(',') splits the line into three parts because there is two commas.
number = (parta[0:3])
street = (parta[4:])
city = (partb[1:])
state = (partc[1:3])
zipcode = (partc[4:])
partd, parte = phone.split('.')
partf, partg = parte.split('-')
print("Member name:", first.capitalize(), middle.capitalize(), last.capitalize())
print(f"Phone number (International format): +1-{partd}-{parte}")
print(f"Phone number (North American format): ({partd}) {parte}")
print(f"Phone number (Local format): {partf}.{partg}")
# f allows me to do both a statement and a variable
print("Street number:", number)
print("Street name:", street.upper())
print("City:", city.upper())
print("State:", state.upper())
# .upper capitalizes the first letter of a word
print("Zip:", zipcode)
