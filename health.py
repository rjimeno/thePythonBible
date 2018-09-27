#!/usr/bin/env python3

import random

health = 50

difficulty = 2  # Easy: 1, Medium: 2, Hard: 3.

potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health

print(health)
