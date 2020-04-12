# My version of a task from the book by Michael Dawson
# A tic-tack-toe game (page 177).
# This version differs from the one presented in the book, but I just wanted to test how I would make it on my own
# if I weren't provided with the right answer.
# This approach helped me to understand better how functions work, so I think it was useful.
# I am only a beginner in Python, so please don't judge me too strictly. :)

# I need to add a check if the input was a number or did it contain letters
# Also some code can be transformed into functions.
# And I want to try if it is possible to use coordinates of a field like in chess

# Global constants

import random
xxx = "X"
ooo = "0"
TIE = "It's a tie"
EMPTY = " "

computer_piece = xxx
human_piece = ooo

continueGame = 1


def display_instruct():
    """Displays instructions"""
    print("---Please, enter number from 0 to 8.---\n")



board_fields = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def display_board(board_fields):
    """Draws a board"""
    print("________________")
    print("---3!", board_fields[0], "!", board_fields[1], "!", board_fields[2], "!")
    print("----------------")
    print("---2!", board_fields[3], "!", board_fields[4], "!", board_fields[5], "!")
    print("----------------")
    print("---1!", board_fields[6], "!", board_fields[7], "!", board_fields[8], "!")
    print("----------------")
    print("----! A ! B ! C !")
    print()


def myTry01(board_fields):
    if board_fields[0] == board_fields[1] == board_fields[2] and board_fields[0] != EMPTY:
        print("We have a winner")
        print("The winner is ", board_fields[0])
        print()
        exitGame = 3
        return exitGame
    elif board_fields[3] == board_fields[4] == board_fields[5] and board_fields[3] != EMPTY:
        print("We have a winner")
        print("The winner is ", board_fields[3], "! Congratulations.")
        print()
        exitGame = 3
        return exitGame
    elif board_fields[6] == board_fields[7] == board_fields[8] and board_fields[6] != EMPTY:
        print("We have a winner")
        print("The winner is ", board_fields[6], "! Congratulations.")
        print()
        exitGame = 3
        return exitGame
    elif board_fields[0] == board_fields[4] == board_fields[8] and board_fields[0] != EMPTY:
        print("We have a winner")
        print("The winner is ", board_fields[0], "! Congratulations.")
        print()
        exitGame = 3
        return exitGame
    elif board_fields[2] == board_fields[4] == board_fields[6] and board_fields[2] != EMPTY:
        print("We have a winner")
        print("The winner is ", board_fields[2],"! Congratulations.")

        print()
        exitGame = 3
        return exitGame
    else:
        exitGame = 2
        return exitGame


coordinatesToMoves = {"A3": 0,
                      "B3": 1,
                      "C3": 2,
                      "A2": 3,
                      "B2": 4,
                      "C2": 5,
                      "A1": 6,
                      "B1": 7,
                      "C1": 8}


def main():
    display_instruct()
    display_board(board_fields)
    # Cicle to check if someone has won
    myTry01(board_fields)
    # To decide that someone must go first. Let it be X
    player = "X"
    exitGame = myTry01(board_fields)

    while exitGame != 3:
        if EMPTY in board_fields:
            if player == "X":
                number_of_a_field = input("Enter number of a field HUMAN   ")
                # I should add a check if its a number or douse it contain letters
                number_of_a_field = int(number_of_a_field)
                if number_of_a_field < 9:
                    if board_fields[number_of_a_field] == EMPTY:
                        board_fields[number_of_a_field] = "X"
                        display_board(board_fields)
                        player = "0"
                        exitGame = myTry01(board_fields)
                    else:
                        print("\nThe number you've entered is unavailable. ")
                        #creates a list of available moves
                        moves = []
                        for number in range(9):
                            if board_fields[number] == EMPTY:
                                moves.append(number)
                        print(moves)
                        print("Please choose one of  those numbers.")
                        player = "X"
                        print()
                else:
                    print("Please enter a valid number from 0 to 8:")
                    player = "X"
            else:
                number_of_a_field = int(input("Enter number of a field Computer.   "))
                if number_of_a_field < 9:
                    if board_fields[number_of_a_field] == EMPTY:
                        board_fields[number_of_a_field] = "O"
                        display_board(board_fields)
                        player = "X"
                        exitGame = myTry01(board_fields)
                    else:
                        print("\nThe number you've entered is unavailable. ")
                        # creates a list of available moves
                        moves = []
                        for number in range(9):
                            if board_fields[number] == EMPTY:
                                moves.append(number)
                        print(moves)
                        print("Please choose one of  those numbers.")
                        player = "0"
                        print()
                else:
                    print("Please enter a valid number from 0 to 8:")
                    player = "0"
        else:
            print("Sorry, its a tie")
            print()
            input("Press enter to leave")


print()
print()
main()
input("press enter to leave. The code finished successfully :)")



