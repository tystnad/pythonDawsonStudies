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


#Its a list that holds
board_fields = [" ", " ", " ", " ", " ", " ", " ", " ", " "]



# То есть функция берет данные из board_fields, да?
# все-таки с этой функцией удобнее
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

    # print("boards grafic\n")


# не забыть добавить в скобочки аргументы
def human_move(board_fields, human_piece):
    """Asks players input"""
    move = int(input("Please enter the number of a field: "))
    # добавить проверку на занятые поля
    return move


def computer_move(board_fields, human_piece):
    """Asks computers input"""
    move = int(input("Computer, Please enter the number of a field: "))
    return move




def congrat_winner(the_final_winner, computer_piece, human_piece):
    if the_final_winner != TIE:
        print("We have a winner")
    else:
        print(TIE)
    if the_final_winner == computer_piece:
        print("Congratulations player 2")
    elif the_final_winner == human_piece:
        print("Congratulations human")
    elif the_final_winner == TIE:
        print("Sory, we dont have a winner, lets try again.")
    print("Congrats\n")


def myTry01(board_fields):
    if board_fields[0] == board_fields[1] and board_fields != EMPTY:
        print("We have a winner")
        continueGame = 3
        return continueGame
    else:
        continueGame = 2
        return continueGame



def main():
    display_instruct()
    display_board(board_fields)
    #Cicle to check if someone has won
    myTry01(board_fields)
    #To decide that someone must go first. Let it be X
    player = "X"
    exitGame = 1
    winner = "noOne"
    while EMPTY in board_fields:
        while exitGame != 3:
            if player == "X":
                number_of_a_field = int(input("Enter number of a field HUMAN   "))
                board_fields[number_of_a_field] = "X"
                display_board(board_fields)
                player = "O"
                exitGame = myTry01(board_fields)
            else:
                number_of_a_field = int(input("Enter number of a field Computer.   "))
                board_fields[number_of_a_field] = "O"
                display_board(board_fields)
                player = "X"
                exitGame = myTry01(board_fields)
    if winner != "noOne":
        print("Congrats")
    else:
        print("Sorry, its a tie")
    input("press enter to leave")


print()
print()
main()
input("press enter to leave")

