# File: die_game.py
# Author: Fatima Aguado Espinosa
# Date: 04/14/2022
# Section: 589
# E-mail: fatima123@tamu.edu
# Description: This program asks for a program to play a die game with two players.
import random as die
# renaming random as die makes the code more readable


def roll_die():
    """ Simulate a 6-sided die roll """
    roll = die.randint(1, 6)
    return roll
# randint() returns an integer number selected element from the specified range


def player_turn(player_name, other_player, player_score):
    """ Implements what happens on player's turn. Returns player's score, which represents the player's total score."""
    option = 'r'
    print(f'\n*******{player_name}\'s turn********\n')
    while option == 'r':
        die_one = roll_die()
        die_two = roll_die()
        die_three = roll_die()
        # die_one, die_two, die_three all make up one turn since one turn is the roll of three dices
        player_score += die_one + die_two + die_three
        if 2 == die_one or 2 == die_two or 2 == die_three:
            # this if statement checks if at least one die is a 2
            player_score = 0
            print(f"Scores: {die_one}, {die_two}, {die_three}.")
            print(f"{player_name} got at least one 2.")
            print(f"{player_name}'s score: {player_score}")
            print()
            input(f"Press <enter> to continue ...")
            # adding input() allows the user to input whatever is stated and move on to the next line
            break
            # this breaks the loop, so it switches to the other player
        elif player_score <= 18:
            print(f"Scores: {die_one}, {die_two}, {die_three}.")
            print(f"{player_name}'s score: {player_score}")
            print()
            option = input("(p)ass or (r)oll? ").lower()
            # .lower() is needed just in case the user inputs a capital P
            print()
        else:
            print(f"Scores: {die_one}, {die_two}, {die_three}.")
            print(f"{player_name}'s score: {player_score}")
            break
    return player_score


def main():
    """ The main driver of the program. """
    player_name = input("Enter the first player name: ").title()
    # .title() capitalizes the first letter of every word
    other_player = input("Enter the second player name: ").title()
    score_one = 0
    score_two = 0
    while score_one <= 18 and score_two <= 18:
        score_one = player_turn(player_name, other_player, score_one)
        score_two = player_turn(other_player, player_name, score_two)
        # the order of the variables in the () matter because they state different information
    if score_one > score_two:
        # this statement checks if player one wins by checking if this score is higher than player two
        print()
        print(f"{player_name} wins with a score of {score_one}")
    if score_two > score_one:
        # this statement checks if player two wins by checking if this score is higher than player one
        print()
        print(f"{other_player} wins with a score of {score_two}")
    if score_one == score_two:
        # the if statements checks if they have the same score
        print()
        print("Both players got the same score")
        print(f"{player_name}: {score_one} scores")
        print(f"{other_player}: {score_two} scores")
    # three if statements were needed because there was three different outcome possibilities


main()
