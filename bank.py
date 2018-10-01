#!/usr/bin/env python3

"""
This would make a good library file for Chequeings and Savings bank accounts.
"""


class Account:
    """
    Abstract base class for other types of accounts like
    Current (i.e. Chequeing) and Savings.
    """

    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        """ Add the provided amount to balance. """
        self.balance += amount

    def withdraw(self, amount):
        """ Substract the requested ammount from balance. """
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds.")

    def statement(self):
        """ Report how much money is left in the account. """
        print("Account Balance: ${}:".format(self.balance))


class Current(Account):
    """
    Chequeing accounts (aka Current) have a minimum_balance requirement.
    """

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}'s Current Account: Balance ${}".format(self.name, self.balance)


class Savings(Account):
    """
    Savings have zero minumum balance requirement.
    """

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Savings Account: Balance ${}".format(self.name, self.balance)


CHEQUEING = Current("Ziyad", 500)
