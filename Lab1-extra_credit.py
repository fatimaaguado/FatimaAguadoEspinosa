# File: extra_credit.py
# Author: Fatima Remedios Aguado Espinosa
# Date: 01/01/2022
# Section: 589
# E-mail: 123fatima@tamu.edu
# Description: This program asks for the user to input a positive number and solves for the sum from 1 to that number.
print('**************************************************')
first = int(input("Enter a number: "))
print()
# Again, int limits the user's input to an integer.
total = int(first * (first + 1) / 2)
# This is a basic algebra equation that does the same thing as a loop without using an actual loop.
print(f"The sum from 1 to {first} is {total}.")
# I used f in the beginning to allow to keep the code in one line instead of using end=''. I find this to be easier.
print('**************************************************')
