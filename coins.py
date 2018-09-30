#!/usr/bin/env python3

"""
TODO: Pytest-ing.
"""

import random


class Coin:
    """
    Abstract base class for all other coins.
    """
    original_value = 0
    clean_colour = ""
    rusty_colour = ""
    diameter = 0
    thickness = 0
    num_edges = 0
    mass = 0
    # Initialization above is not necessary but feels like best practice.

    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def __str__(self):
        if self.original_value >= 1:
            representation = "£{} Coin".format(int(self.original_value))
        else:
            representation = "{}p Coin".format(int(self.original_value * 100))
        return representation

    def rust(self):
        """
        Change the colour to make it look old.
        """
        self.colour = self.rusty_colour

    def clean(self):
        """
        Change the colour to make it look new.
        """
        self.colour = self.clean_colour

    def flip(self):
        """
        Select either side at random.
        """
        heads_options = [True, False]
        self.heads = random.choice(heads_options)

    def __del__(self):
        print("Coin spent!")


class OnePence(Coin):
    """
    https://en.wikipedia.org/wiki/Penny_(British_decimal_coin)
    """

    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,  # mm
            "thickness": 1.52,  # mm
            "mass": 3.56  # g
        }
        super().__init__(**data)


class TwoPence(Coin):
    """
    https://en.wikipedia.org/wiki/Two_pence_(British_decimal_coin)
    """

    def __init__(self):
        data = {
            "original_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,  # mm
            "thickness": 1.85,  # mm
            "mass": 7.12  # g
        }
        super().__init__(**data)


class FivePence(Coin):
    """
    https://en.wikipedia.org/wiki/Five_pence_(British_coin)
    """

    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 18.0,  # mm
            "thickness": 1.77,  # mm
            "mass": 3.25  # g
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour  # Silver (and steel) coins do not rust!


class TenPence(Coin):
    """
    https://en.wikipedia.org/wiki/Ten_pence_(British_coin)
    """

    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.5,  # mm
            "thickness": 1.85,  # mm
            "mass": 6.50  # g
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour  # Silver (and steel) coins do not rust!


class TwentyPence(Coin):
    """
    https://en.wikipedia.org/wiki/Twenty_pence_(British_coin)
    """

    def __init__(self):
        data = {
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 21.4,  # mm
            "thickness": 1.7,  # mm
            "mass": 5.00  # g
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour  # Silver (and steel) coins do not rust!


class FiftyPence(Coin):
    """
    https://en.wikipedia.org/wiki/Fifty_pence_(British_coin)
    """

    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 27.3,  # mm
            "thickness": 1.78,  # mm
            "mass": 8.00  # g
        }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour  # Silver (and steel) coins do not rust!


class OnePound(Coin):
    """
    https://en.wikipedia.org/wiki/One_pound_(British_coin)
    """

    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,  # mm
            "thickness": 3.15,  # mm
            "mass": 9.5  # g
        }
        super().__init__(**data)


class TwoPound(Coin):
    """
    https://en.wikipedia.org/wiki/Two_pounds_(British_coin)
    """

    def __init__(self):
        data = {
            "original_value": 2.00,
            "clean_colour": "gold & silver",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 28.4,  # mm
            "thickness": 2.50,  # mm
            "mass": 12.00  # g
        }
        super().__init__(**data)


COINS = [
    OnePence(),
    TwoPence(),
    FivePence(),
    TenPence(),
    TwentyPence(),
    FiftyPence(),
    OnePound(),
    TwoPound()
]

for coin in COINS:
    arguments = [
        coin,
        coin.colour,
        coin.value,
        coin.diameter,
        coin.thickness,
        coin.num_edges,
        coin.mass
    ]
    string = """
{} -
Colour:{},
value(£):{},
diameter(mm):{},
thickness(mm):{},
NUMBER of edges:{}
mass(g):{}.
""".format(*arguments)
    print(string)
