#!/usr/bin/env python3

"""
TODO: include tests here.
"""
from enum import IntEnum

board = [" "] * 9
count = 0


class Player(IntEnum):
    """ Represents both players. """
    X = 1
    O = 2


def print_board():
    """ Displays the current state of the board in STDOUT. """
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(player):
    """ Updates the board with next (valid) move. """
    global count
    icon = player.name
    number = player.value

    print("Your turn player NUMBER {}.".format(number))

    choice = int(input("Enter your move [1-9]: ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
        count += 1
    else:
        print()
        print("That space is taken!")


def is_victory(player):
    """ Checks if 'player' just put 3 in line. """
    icon = player.name
    return (board[0] == icon and board[1] == icon and board[2] == icon) or \
           (board[3] == icon and board[4] == icon and board[5] == icon) or \
           (board[6] == icon and board[7] == icon and board[8] == icon) or \
           (board[0] == icon and board[3] == icon and board[6] == icon) or \
           (board[1] == icon and board[4] == icon and board[7] == icon) or \
           (board[2] == icon and board[5] == icon and board[8] == icon) or \
           (board[0] == icon and board[4] == icon and board[8] == icon) or \
           (board[6] == icon and board[4] == icon and board[2] == icon)


def main():
    """
    61. PROJECT 8 - Tic Tac Toe Game!
    """

    print_board()
    while count <= 8:
        if count % 2 == 0:
            player = Player.X
        else:
            player = Player.O
        player_move(player)
        print_board()
        if is_victory(player):
            print("{} Wins! Congratulations!".format(player.name))
            break

    if count == 9:
        print("It's a draw!")


main()
