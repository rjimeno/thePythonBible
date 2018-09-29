#!/usr/bin/env python3

from enum import IntEnum


class Field(IntEnum):
    AGE = 0
    SEATS = 1


films = {
    "Finding Dory": [3,5],
    "Bourne":[18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
}

while True:
    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())

        if age >= films[choice][Field.AGE]:
            if films[choice][Field.SEATS] > 0:
                print("Enjoy the film!")
                films[choice][Field.SEATS] -= 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film.")

    else:
        print("We don't have that film.")
