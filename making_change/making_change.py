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
"""
U
-list of possible denominations : [1, 5, 10, 25, 50]
-sequence pattern

0, 1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
1, 1, 1, 1, 1, 2, 2, 2, 2,  2, 4,  4    4   4   4, 6    6   6   6   6   9
-input: n (change to make) integer, (given denominations) list 
-output: result = integer (amount of possible ways to make "n" change)

P
E
R
"""

cache = {0: 1, 10: 4}

"""
def helper(denominations):
    global m
    m = len(denominations)
"""

denominations = [1, 5, 10, 25, 50]

lenDenom = len(denominations)


def making_change1(amount, denominations, lenDenom):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if (lenDenom <= 0 and amount >= 0):
        return 0
    t1 = lenDenom-1
    t2 = amount-denominations[lenDenom-1]

    #print("length Denom: ", t1, "change amount: ", t2)
    # n, list of currency,  # makes len denom shorter by 1 (len of currency list -1)   ( + add together)          #makes amount for change shorter by 1  n/amount -  list[length-1] (list at len-1)
    return making_change1(amount, denominations, lenDenom-1) + making_change1((amount-denominations[lenDenom-1]), denominations, lenDenom)

# https://codereview.stackexchange.com/questions/147505/iterative-counting-change-implementation-in-mit-scheme
# https://hackernoon.com/the-coin-change-problem-explained-ddd035a8f22f



#print(making_change(15, denominations, lenDenom))
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations, lenDenom), amount=amount))
    else:
        print("Usage: making_change.py [amount]")

# https://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/
