# File: checkout.py
# Author: Fatima Aguado Espinosa
# Date: 03/22/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for the user to input their selection of the menu options displayed. The code should
# exactly what the menu option says. It allows the user to add new book titles, authors,
# and how many days they will have the book.  It is case-sensitive and has special output when
# the book title is duplicated. The user can ask for the titles to be in ascending or descending alphabetical order.
# Once the user chooses option 5, the loop stops running.
correct = True
# correct = True is necessary, so we can tell the while loop when to stop.
information = {}
# an empty dictionary was made to be able to add the following information
while correct is True:
    print("1. Add a book to the cart")
    print("2. Remove book(s) from the cart")
    print("3. View cart")
    print("4. Sort cart")
    print("5. Quit")
    print()
    option = input("Select from the menu: ")
    if option == '1':
        title = input("Book title: ")
        title_capitalized = title.title()
        # .title() capitalizes the first letter of every word, even if it is two words
        if title_capitalized in information:
            print("This book is in your cart.")
        else:
            name = input("Book author's name: ")
            name_capitalized = name.title()
            # .title() was used so if the user inputs a title without capitalizing, the code automatically capitalizes.
            # This was made so the code can read all titles without being case-sensitive since it
            # capitalizes the first word or every title, they will all be in the same format.
            days = int(input("How many days: "))
            # int was used to limit the user to only input an integer
            information[title_capitalized] = [name_capitalized, days]
            # this adds all the information into the dictionary in this specific order
            # the titles_capitalized is the key and name_capitalized and days are the variables
    if option == '2':
        delete = input("Remove all or an item? (Enter 'all' or 'book title'): ").title()
        if delete == 'All':
            information.clear()
            print()
            # .clear() deletes the entire dictionary
        elif delete not in information:
            print(f"{delete} is not in your cart.")
        else:
            information.pop(delete)
            # .pop() removes the item with that key
    if option == '3':
        if information == {}:
            # {} means empty dictionary
            print("Cart is empty.")
        else:
            print(f"{'Title':<20}{'Author':<20}{'Period':<20}")
            # :<20 makes the spacing exactly 20 spaces
            for title in information.keys():
                # .keys() returns all the keys in that said dictionary
                print(f"{title:<20}", end='')
                print(f"{information[title][0]:<20}", end='')
                print(f"{information[title][1]:<20}", end='')
                print()
    if option == '4':
        if information == {}:
            print("Cart is empty.")
        else:
            order = input("Enter 'A' for Ascending and 'D' for Descending: ").upper()
            # .upper() capitalizes the entire word but in this case letter
            if order == 'A':
                # by using .upper(), we do not have to worry if the user
                # input an uppercase or lower case letter
                sorted_titles = sorted(information.keys())
                # sorted() sorts the titles ascending alphabetical order
                print(f"{'Title':<20}{'Author':<20}{'Period':<20}")
                for title in sorted_titles:
                    print(f"{title:<20}", end='')
                    print(f"{information[title][0]:<20}", end='')
                    print(f"{information[title][1]:<20}", end='')
                    print()
            if order == 'D':
                sorted_titles = sorted(information.keys(), reverse=True)
                # reverse=True sorts the titles in descending alphabetical order
                print(f"{'Title':<20}{'Author':<20}{'Period':<20}")
                for title in sorted_titles:
                    print(f"{title:<20}", end='')
                    print(f"{information[title][0]:<20}", end='')
                    # title was used to keep track of what title the for loop was on
                    print(f"{information[title][1]:<20}", end='')
                    print()
    print()
    if option == '5':
        correct = False
        # correct = False stops the loop because we stated on the top that correct = True
