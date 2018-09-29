#!/usr/bin/env python3

"""
48. PROJECT 6: Baby Conversation Simulator.
"""

import random

QUESTIONS = (
    "What's that?: ",
    "Is this yours?: ",
    "Why is the sky blue?: "
)

QUESTION = random.choice(QUESTIONS)

ANSWER = input(QUESTION).strip().lower()

while ANSWER != "just because!":
    ANSWER = input("Why?: ").strip().lower()

print("OKeeey")
