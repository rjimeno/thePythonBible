#!/usr/bin/env python3

"""
44. PROJECT 5 - Cinema Simulator!
"""

from enum import IntEnum


class Field(IntEnum):
    """ Simple helper enumeration. """
    AGE = 0
    SEATS = 1


FILMS = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}

while True:
    CHOICE = input("What film would you like to watch?: ").strip().title()
    if CHOICE in FILMS:
        AGE = int(input("How old are you?: ").strip())

        if AGE >= FILMS[CHOICE][Field.AGE]:
            if FILMS[CHOICE][Field.SEATS] > 0:
                print("Enjoy the film!")
                FILMS[CHOICE][Field.SEATS] -= 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film.")

    else:
        print("We don't have that film.")
