#!/usr/bin/python

import sys

"""
input: n (money in cents), list [] of coin dnominations, 
output: n (total ways change can be made for the input )
For example, making_change(10) should return 4, since there are 4 ways to make change for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:

We can make change for 10 cents using 10 pennies
We can use 5 pennies and a nickel
We can use 2 nickels
We can use a single dime


"""


cache = {0: 1, 10: 4}

"""
def helper(denominations):
    global m
    m = len(denominations)
"""


def making_change(amount, denominations, lenDenom):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if (lenDenom <= 0 and amount >= 0):
        return 0

    return making_change(amount, denominations, lenDenom-1) + making_change((amount-denominations[lenDenom-1]), denominations, lenDenom)


denominations = [1, 5, 10, 25, 50]
lenDenom = len(denominations)

print(making_change(10, denominations, lenDenom))

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
