#!/usr/bin/env python3

"""
Lesson 37. PROJECT 4 - Travis the Ridiculous Security System.
"""

KNOWN_USERS = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

print(len(KNOWN_USERS))

while True:
    print("Hi! My name is Travis.")
    NAME = input("What is your name?: ").strip().capitalize()

    if NAME in KNOWN_USERS:
        print("Hello {}!".format(NAME))
        REMOVE = input("Would you like to be removed from the system (y/n)? ").lower()

        if REMOVE == "y":
            print(KNOWN_USERS)
            KNOWN_USERS.remove(NAME)
            print(KNOWN_USERS)

    else:
        print("Hmmm I don't think I have net you yet {}".format(NAME))
        ADD_ME = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if ADD_ME == "y":
            KNOWN_USERS.append(NAME)
        elif ADD_ME == "n":
            print("No worries, see you around!")
