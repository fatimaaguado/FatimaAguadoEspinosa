# File: sorting.py
# Author: Fatima Aguado Espinosa
# Date: 03/03/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for the number of books, their titles, publication year, and barcode string.
# It then uses this information to sort the books by ascending alphabetical order of title,
# by descending order of publication year, and ascending order of the maximum number in the barcode string.
number_of_books = input("Enter the number of book titles: ")
integer_number = int(number_of_books)
# the number of books needs to be an integer in order do the range which isn't allowed with a string
title = []
publication_year = []
barcode = []
correct_info = []
sorted_titles = []
sorted_publication_year = []
sorted_barcode = []
# empty list for title, publication year and barcode are needed in order to append stuff into the list in the for loop.
for number in range(0, integer_number):
    if number <= integer_number:
        print()
        title = input(f"Book title #{number + 1}: ")
        publication_year = int(input(f"Book ({title}) publication year: "))
        barcode = input(f"Book ({title}) barcode string: ")
        correct_info.append([title, publication_year, barcode])
        sorted_titles = sorted(correct_info)
        sorted_publication_year = sorted(correct_info, key=lambda x: x[1], reverse=True)
        sorted_barcode = sorted(correct_info, key=lambda item: max(int(num) for num in item[2].split()))
print()
# sorted() sorts the titles by alphabetical order by default
# reverse=True puts the list in descending order
# key=lambda item: max(int(num) for num in item[2].split())) sorts the list by
# ascending order of the maximum number in the barcode string
print("Sorted books by title:")
print()
for number in sorted_titles:
    print(number[0])
# [number] reminds the loop in which order it is in
    print(f"Published in: {number[1]}")
    print(f"Barcode string: {number[2]}")
    print()
print("Sorted books by publication year:")
print()
for number in sorted_publication_year:
# it was crucial that we changed the book number into an integer because if we hadn't,
# we wouldn't be able to do this operation
    print(number[0])
    print(f"Published in: {number[1]}")
    print(f"Barcode string: {number[2]}")
    print()
print("Sorted books by barcode string maximum number:")
print()
for number in sorted_barcode:
# a for loop was used because we know the number of times it needs to run and in this case it is integer number
    print(number[0])
    print(f"Published in: {number[1]}")
    print(f"Barcode string: {number[2]}")
    print()
