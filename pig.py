#!/usr/bin/env python3

"""
52. PROJECT 7 - Pig Latin Translator
"""

VOWELS = "aeiou"


def main():
    """
    Requests for a sentence to be typed, then prints
    its "pig-latin" equivalent to standard output.
    """
    #  get sentence from user

    original = input("Please enter a sentence: ").strip().lower()

    # split sentence into words

    words = original.split()

    # loop through words adn convert to pig latin

    new_words = []

    for word in words:
        if word[0] in VOWELS:
            word = word + "y"
        else:
            pos = 1
            while (len(word) > pos) and (not word[pos] in VOWELS):
                pos += 1
            word = word[pos:] + word[0:pos]
        word = word + "ay"
        print(word)

        new_words.append(word)
    # if starts with a voewl, just add "yay"

    # Otherwise, move the first consonant cluster to end and add ay

    # stick words back together
    output = " ".join(new_words)

    # output the final string

    print(output)


main()
