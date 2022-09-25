# File: collections.py
# Author: Fatima Aguado Espinosa
# Date: 03/31/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for a menu selection that can add books to the library, print the available books
# create and sort book collections, and lastly delete collections.
from math import *
# this import will allow us to do math.ciel


def print_menu():
    """Prints a menu of option"""
    print("*******************Main Menu*******************")
    print("1. Add books to the library")
    print("2. Print available books in the library")
    print("3. Create book collections")
    print("4. Sort books in the collections")
    print("5. Delete a collection")
    print("6. Quit")
    print("***********************************************")


def add_books(library):
    """Adds unique books to the library."""
    entries = int(input("How many books would you like to enter: "))
    # int restricts the user to only input integers
    print()
    for entry in range(1, entries + 1):
        # you had to add one to the range so, it includes entries
        while True:
            book_record = input(f"Book {entry}: ")
            ISBN = book_record.split()[-1]
            title = book_record[:-11].strip()
            # the two codes above allows you to split the input into two sections known as ISBN and title
            if check_ISBN(ISBN) and ISBN not in library:
                library[ISBN] = [title, -1]
                # -1 is used as a place-holder for later code
                break
                # this ends the while loop
            else:
                print("Invalid entry")
    print()


def check_ISBN(ISBN):
    """Checks the format of an ISBN. The return value of this function is true or false!"""
    return len(ISBN) == 10 and ISBN.isnumeric()
# this checks if the length of the isbn is to and that it is number


def print_books(library):
    """Prints available books in the library"""
    available_books = [library[isbn][0] for isbn in library.keys() if library[isbn][1] == -1]
    # available books counts all the -1's in library
    if library == {} or len(available_books) == 0:
        print("Invalid entry")
        print()
    else:
        print()
        print("Books available in the library:")
        for isbn, book in library.items():
            print(f"{book[0]:<20}{isbn:<20}")
        print()


def create_collections(library):
    """Creates book collections"""
    available_books = [library[isbn][0] for isbn in library.keys() if library[isbn][1] == -1]
    # available_books was copied and pasted because global variables are considered bad coding
    collection_size = int(input("What is the size of the collection? "))
    # int restricts the user to only input integers
    number_of_collections = ceil(len(available_books) / collection_size)
    total = 0
    for book in range(1, number_of_collections + 1):
        # range is not inclusive for the last digit so adding +1 allows number_of_collections to be included
        print()
        print(f"Enter the book ISBNs for collection {book}:")
        count_each = 0
        while True:
            isbn = input()
            if isbn in library.keys():
                library[isbn][1] = book
                # the code above changed the -1 to whatever the collection number is
                total += 1
                count_each += 1
            else:
                print("Invalid entry")
            if total == len(available_books):
                break
            if count_each == collection_size:
                # this stops the code when there is enough isbn in the collection
                break
    print()
    print("Current book collections:")
    for collection in range(1, number_of_collections + 1):
        print(f"Collection {collection}:")
        for key, values in library.items():
            # .items() allows there to be two variables
            if library[key][1] == collection:
                print(f"{values[0]:<20}{key:<20}")
        print()


def sort_collections(library):
    """Prints the books sorted in each collection"""
    sort_option = input("Sort books in ascending or descending order of ISBN: ").lower()
    collection_num = max([library[isbn][1] for isbn in library])
    # this find the max collection number so, we can use it as a range
    print()
    print("Current book collections:")
    for num in range(1, collection_num+1):
        print(f"Collection {num}")
        for keys in sorted(library, reverse=(sort_option == 'descending')):
            # this allows the code to be reverse=True or False, depending on what the user inputs
            if library[keys][1] == num:
                print(f'{library[keys][0]:<20}{keys:<20}')
        print()


def delete_collections(library):
    """Deletes a collection from the list of collections and adds it back to the library"""
    collection_num = max([library[isbn][1] for isbn in library])
    # this code was copied again to be used in this for loop since global variables are not good
    delete_option = int(input("Which collection would you like to delete? "))
    if delete_option > collection_num:
        # if the number entered is higher than the max number of collection then the following statement is printed
        print("Invalid entry")
        print()
    if delete_option <= collection_num:
        # this checks if the number entered is less than or equal to the max number of collections
        print("Current book collections:")
        for collection in range(1, collection_num + 1):
            print(f"Collection {collection}:")
            for key, values in library.items():
                if library[key][1] == collection:
                    print(f"{values[0]:<20}{key:<20}")
            print()


def main():
    """Driver function that calls all the functions above."""
    library = {}
    # this creates an empty dictionary named library
    while True:
        print_menu()
        print()
        entry = int(input("Choose a menu option: "))
        # int restricts the user to only entering integers
        if entry == 1:
            add_books(library)
        elif entry == 2:
            print_books(library)
        elif entry == 3:
            create_collections(library)
        elif entry == 4:
            sort_collections(library)
        elif entry == 5:
            delete_collections(library)
        elif entry == 6:
            print("End")
            break
            # this break statements ends the loop


main()
