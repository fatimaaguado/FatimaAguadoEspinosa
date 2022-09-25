# File: q2.py
# Author: Fatima Remedios Aguado Espinosa
# Date: 02/01/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for the amount of money ,in dollars,
# to be calculated into the numbers of halves, quarters, or ten cents that equals that same amount of money.
print('**************************************************')
dollars = float(input("Please enter your amount: $"))
half = int(dollars // .50)
# At first I was dividing by 2 but .50 makes more sense since half a dollar is 50 cents. Same thing for quarters and cents.
quarter = int(dollars // .25)
cents = int(dollars *100 / 10)
print()
# print() adds a blank line between your output.
print('For $', end='')
# Adding end='' usually makes my code more complicated but for this question, it made sense to do it this way sense there
# was alot of mixing between the statement and the variables.
print(dollars, end='')
print(', you can get ', end='')
print(half, 'half, ', end='')
print(quarter, 'quarter, ', end='')
print('or', cents, 'ten cents.')
print('**************************************************')
