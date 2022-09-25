# File: q3.py
# Author: Fatima Remedios Aguado Espinosa
# Date: 02/01/2022
# Section: 589
# E-mail: 123fatima@tamu.edu
# Description:
# e.g., This program asks for the distance between two points to be calculated.
print('**************************************************')
firstx = input('x amount of the first point: ')
firsty = input('y amount of the first point: ')
print()
secondx = input('x amount of the second point: ')
secondy = input('y amount of the second point: ')
number = ((float(firstx) - float(secondx))**2 + (float(firsty) - float(secondy))**2) ** (1 / 2)
print()
print(f'The distance between points ({firstx}, {firsty}) and ({secondx}, {secondy}) is {number}.')
# I used f in the beginning to allow to keep the code in one line instead of using end=''.
print('**************************************************')
