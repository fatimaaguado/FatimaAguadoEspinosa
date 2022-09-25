# File: textstats.py
# Author: Fatima Aguado Espinosa
# Date: 03/31/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for alphanumeric statistics about a block of text that the user inputs.
# Some examples are printing how many sentences, words, and punctuation is in the text.
# It also asks to print the number of occurrences of letter and palindromes in the text. 
import re
# this import allows us to specify a set of strings that matches it and be able to manipulate it


def main():
    """Driver function that calls all the functions"""
    text = input("Enter text: ")
    print()
    print(f"Number of sentences: {get_sentences(text)}")
    print(f"Number of words: {get_words(text)}")
    print(f"Number of punctuations: {get_punctuations(text)}")
    print_letters(text)
    print_palindromes(text)


def get_sentences(text):
    """Returns the number of sentences in the text"""
    period = text.count(".")
    point = text.count("!")
    question_mark = text.count("?")
    sentences = period + point + question_mark
    return sentences
# since this function isn't actually printing anything within it so, you have to do return


def get_words(text):
    """Returns the number of words in the text"""
    return len(re.findall(r'\w+', text))
# len finds the length


def get_punctuations(text):
    """Returns the number of punctuations in the text"""
    period = text.count(".")
    comma = text.count(",")
    question_mark = text.count("?")
    colon = text.count(":")
    semicolon = text.count(";")
    point = text.count("!")
# .count() counts everything named in the ()
    punctuations = period + comma + question_mark + colon + semicolon + point
    return punctuations


def print_letters(text):
    """Prints the number of occurrences of letters in the text"""
    letter_time = {}
    # this creates an empty dictionary named letter_time
    lowercase_text = text.lower()
    # .lower() makes the text lowercase
    new_text = re.sub(r'[^\w\s]', '', lowercase_text)
    print()
    print("Letter statistics:")
    split_text = new_text.split()
    # .split() splits the new_text by every space
    for word in split_text:
        if word.isalpha() is True:
            # .isalpha() returns a True or False statement
            for letter in word:
                if letter in letter_time:
                    letter_time[letter] += 1
                else:
                    count = 1
                    letter_time[letter] = count
    sorted_letter_time = sorted(letter_time.items(), key=lambda x: x[1], reverse=True)
    # code above sorts the values only
    max_letter = max([time for letter, time in sorted_letter_time])
    # this line finds the max letter
    for place in range(max_letter, 0, -1):
        # the -1 is the stride in the range
        count = 0
        for letter, time in sorted_letter_time:
            if time == place:
                count += 1
                # this adds one to the count
                if time == 1:
                    print(f"{letter} found {time} time.")
                else:
                    print(f"{letter} found {time} times.")
        if count > 0:
            print()


def print_palindromes(text):
    """Prints the number of occurrences of palindrome numbers and palindrome words and letters in the text"""
    lowercase_text = text.lower()
    new_text = re.sub(r'[^\w\s]', '', lowercase_text)
    # this line uses re to replace all the punctuations with an empty space
    correct_text = new_text.split()
    number = dict()
    word_letter = dict()
    # two empty dictionaries were created to be able to append the correct information
    for num in correct_text:
        if num.isnumeric():
            # .isnumeric() returns True if all the characters are numeric (0-9), otherwise False
            if num == num[::-1]:
                # this line checks in the num is a palindrome
                number[num] = correct_text.count(num)
    for word in correct_text:
        if not word.isdigit():
            if word == word[::-1]:
                # this line checks if the word is a palindrome
                word_letter[word] = correct_text.count(word)
    print("Palindrome numbers:")
    for num, count in sorted(number.items()):
        print(f"{num}: {count}")
    print()
    print("Palindrome words and letters:")
    for word, counts in sorted(word_letter.items()):
        print(f"{word}: {counts}")


main()
