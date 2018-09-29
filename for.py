#!/usr/bin/env python3

"""
48. PROJECT 6: Baby Conversation Simulator
"""

def main():
    """
    Asks for some input and  prints the number of vowels and consonants in it.
    """
    vowels = 0
    consonants = 0

    text = input("Which line of text would you like to analyze?\n")
    for letter in text:
        if letter.lower() in "aeiou":
            vowels += 1
        elif letter == " ":
            pass
        else:
            consonants += 1

    print("There are {} vowels and {} consonants".format(vowels, consonants))

main()
