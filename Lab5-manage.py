# File: manage.py
# Author: Fatima Aguado Espinosa
# Date: 03/22/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for ...
loop = True
# loop = True allows us to control when the loop starts and when it stops
information = {}
# creating an empty dictionary outside is necessary so everything in the loop can be added to the dictionary
while loop is True:
    # while loop is True starts the loop
    genre = input("Enter book type: ").title()
    # .title() capitalizes the first letter of every word
    if genre != 'Done':
        # != means it is not equal to
        title = input("Enter book's title: ").title()
        year = int(input("Enter book's publication year: "))
        # int() limits the user to only enter integers
        author = input("Enter book's first author's name: ").title()
        publisher = input("Enter book's publisher name: ").title()
        if genre not in information:
            information[genre] = {}
            # this makes a new empty list
        if year in information[genre]:
            # this if statement is the first check point
            information[genre][year].append([title, author, publisher])
        if year not in information[genre]:
            # this is the second check point
            # this tells the information how to be appending according to the check points
            information[genre][year] = [[title, author, publisher]]
        print()
    else:
        loop = False
        # this ends the while loop
print()
for genre in information.keys():
    # .keys() checks all the genre in just the keys of the dictionary named information
    print(f"===={genre}")
    # this prints all the genres in the keys
    for year in information[genre].keys():
        print(f"Published in {year}:")
        print(f"{'Title':<15}|{'Author':<15}|{'Publisher':<15}|")
        # :<15 makes the spacing 15 spaces
        for place in information[genre][year]:
            print(f"{place[0]:<15}|{place[1]:<15}|{place[2]:<15}|")
            # place keeps track on the spot the for loop is on every time it loops
        print()
