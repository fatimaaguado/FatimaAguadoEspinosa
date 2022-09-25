# File: password.py
# Author: Fatima Aguado Espinosa
# Date: 02/08/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for the last name, phone number, and mailing address. It then it uses this information
# to generate a password.
print("Welcome to the Library Management App.")
print("Password generation")
last = input("Enter the member\'s last name: ")
phone = input("Enter the member\'s phone number: ")
address = input("Enter the member\'s mailing address: ")
print()
first = last.count('a') + last.count("e") + last.count('i') + last.count('o') + last.count('u') + last.count("A") \
    + last.count('E') + last.count("I") + last.count('O') + last.count('U')
# include all lowercase and upper case vowels
secondphone = phone[0]
# phone[0] finds the first letter which is index zero
secondphone_replace = phone.replace(secondphone, last[-1:].capitalize())
# ."replace" replaces the first thing in the parentheses with the second thing in the parentheses
second = secondphone_replace
zipcode = address[-4:]
reversed_zipcode = zipcode[3:] + zipcode[2:3] + zipcode[1:2] + zipcode[0:1]
third = reversed_zipcode
start = address[:3]
uno = int(start[:1])
dos = int(start[1:2])
tres = int(start[2:3])
fourth = int(uno % 2 == 1)
# % gets the remainder of the division
fifth = int(dos % 2 == 1)
sixth = int(tres % 2 == 1)
print(f"Generated password: {first}{second}{third}{fourth}{fifth}{sixth}")
# f allows me to mix both statements and variables
