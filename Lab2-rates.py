# File: rates.py
# Author: Fatima Aguado Espinosa
# Date: 02/08/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for the number of days of a membership and gives the price for 14 weeks, 4 months,
# and quarterly memberships.
import math
# import math allows me to use math.ceil
print("Welcome to the Library Management App.")
print("Membership rates")
print()
# print() creates a blank line
user = input("Enter the membership number of days: ")
days = int(user)
# days = int(user) was used to get the number the user inserted and use it for the following equations
weekly = math.ceil(days / 7)
weeklyrate = 10 * weekly * .0825 + (10 * weekly)
monthly = math.ceil(days / 30)
# math.ceil rounds up
monthlyrate = 30 * monthly * .0825 + (30 * monthly)
# I changed the tax rate from a percentage to a decimal, so I wouldn't have to keep adding (8.25/100) everytime.
quarterly = math.ceil(days / 90)
quarterlyrate = 80 * quarterly * .0825 + (80 * quarterly)
print(f"Weekly membership: {weekly} weeks at ${weeklyrate}")
print(f"Monthly membership: {monthly} months at ${monthlyrate}")
print(f"Quarterly membership: {quarterly} quarters at ${quarterlyrate}")
