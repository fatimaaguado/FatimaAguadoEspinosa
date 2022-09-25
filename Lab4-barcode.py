# File: barcode.py
# Author: Fatima Aguado Espinosa
# Date: 03/03/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for the number of rows and columns for matrix A and B. It then uses that information
# to get matrix C by the Kronecker Product. Then it asks to find the transpose of matrix C and finally
# generate a barcode string made out of all the numbers that are the sum of the column numbers of C.
import random
# import random allows us to use random.randrange()
correct_matrix_a = False
correct_matrix_b = False
# this was needed in order to tell the while loop to stop
matrix_a_printed = list()
matrix_b_printed = list()
# empty list were needed to be able to append information into it
while correct_matrix_a is False:
    matrix_a = input("Enter matrix A rows and columns: ")
    matrix_a_split = matrix_a.split()
    first_a = int(matrix_a_split[0])
    second_a = int(matrix_a_split[1])
# the row and columns of a were changed from a string to an integer by using int()
    if 0 <= first_a > 10 or 0 <= second_a > 10:
        # 0 <= first_a > 10 or 0 <= second_a > 10 allowed us to check that the rows and columns
        # were greater than 0 but less than 10
        print("Invalid matrix size. Try again.")
    else:
        correct_matrix_a = True
# correct_matrix_a = True stops the loops since we stated at the top that correct_matrix_a = False
# so once it hit true, the loop would stop
        print()
        while correct_matrix_b is False:
            matrix_b = input("Enter matrix B rows and columns: ")
            matrix_b_split = matrix_b.split()
            # matrix b had to be split in order to get to the two numbers in the string
            first_b = int(matrix_b_split[0])
            second_b = int(matrix_b_split[1])
            # once the matrix is split, you can change it into an integer to manipulate it
            if 0 <= first_b > 10 or 0 <= second_b > 10:
                print("Invalid matrix size. Try again.")
            else:
                correct_matrix_b = True
        print()
# correct_matrix_b = True stops the loops since we stated at the top that correct_matrix_b = False
# so once it hit true, the loop would stop
print("Random matrix A:")
for row in range(first_a):
    line = [random.randrange(2, 99, 2) for n in range(second_a) if n >= 0]
    # random.randrange allows us to have a range and a stride
    matrix_a_printed.append(line)
for row in range(first_a):
    if row != 0:
        print()
    for columns in range(second_a):
        print(f"{matrix_a_printed[row][columns]:<6}", end="")
# :<6 allowed us to keep the spacing less than 6
print('\n')
print("Random matrix B:")
for row in range(first_b):
    line = [random.randrange(1, 100, 2) for n in range(second_b) if n >= 0]
    matrix_b_printed.append(line)
for row in range(first_b):
    if row != 0:
        print()
    for columns in range(second_b):
        print(f"{matrix_b_printed[row][columns]:<6}", end="")
print('\n')
print("Matrix C:")
matrix_c = []
# an empty list for matrix C was made inorder for information to be appended into it
for rows_in_a in range(first_a):
    for rows_in_b in range(first_b):
        line = []
        for columns_in_a in range(second_a):
            for columns_in_b in range(second_b):
                line.append(matrix_a_printed[rows_in_a][columns_in_a] * matrix_b_printed[rows_in_b][columns_in_b])
        matrix_c.append(line)
for row in range(first_a*first_b):
    for columns in range(second_a*second_b):
        print(f"{matrix_c[row][columns]:<6}", end="")
    print()
print('\n')
print("Transpose matrix T:")
matrix_t = []
# an empty list was made in order to append new stuff in it
for i in range(len(matrix_c[0])):
    # len is needed in order to get an integer to manipulate it into the code
    list2 = []
    for j in range(len(matrix_c)):
        list2.append(matrix_c[j][i])
        # append adds things into the list stated
    matrix_t.append(list2)
for row in range(len(matrix_t)):
    for columns in range(len(matrix_t[i])):
        # len changes it from a string to an integer
        print(f"{matrix_t[row][columns]:<6}", end="")
    print()
print('\n')
barcode = []
for row in range(len(matrix_t)):
    barcode.append(sum(matrix_t[row]))
# the code above appends the sum from each row to a list
    string = ' '.join(str(e) for e in barcode)
# .join changes a list into a string
print("Barcode string:")
print(string)
