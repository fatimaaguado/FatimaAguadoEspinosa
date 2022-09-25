# File: q1.py
# Author: Fatima Remedios Aguado Espinosa
# Date: 01/27/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for the first and last names as well as their title and then uses the year they were
# born to determine their age in 5 years.
print('**************************************************************************')
first = input("What is your first name? ")
last = input("What is your last name? ")
prefix = input("Which title do you prefer? Mr., Mrs., Miss, Ms., Dr.: ")
year = int(input("In what year were you born? "))
# I have added int to the beginning to limit the number to an integer only. This makes less space for error.
age = 2022 - year + 5
# A simple equation to figure out someone's age is to subtract the year it currently is and the year they were born.
# I added five to get the age they would be in five years.
print()
# I have added print() to create a blank line.
print(f'Welcome, {prefix} {first} {last}.')
# I have added "f" to the beginning to be able to add variables inside my sentences.
print('You will be', age, "years old in five years.")
# The previous sentence is another way to add a variable into a sentence.
print('**************************************************************************')
