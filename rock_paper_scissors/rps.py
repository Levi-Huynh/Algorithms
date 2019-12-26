#!/usr/bin/python

import sys

"""
-generate all the possible plays that can be made in the game rps
-input =n (number of plays per round)
-n = 2:
[['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'],
    ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
output = list of lists (with strings) each inner list should have length equal to input n

hints:
You'll want to define a list with all of the possible Rock Paper Scissors plays.
Another problem that asks you to generate a bunch of permutations, so we're probably going to want to opt for using recursion again.
[PERMUTATIONS=> RECURSION]

Since we're building up a list of results, we'll have to pass the list we're constructing around to multiple recursive calls so that each
recursive call can add to the overall result.
[PASS LISTS TO HELPER FUNCTION/RECURSE HELPER FUNCTION. KEEP N FOR MAIN FUNCTION ]

^ However, the tests only give our function n as input. To get around this, we could define an inner recursive
helper function that will perform the recursion for us, while allowing us to preserve the outer function's function signature.

In Python, you can concatenate two lists with the + operator. However, you'll want to make sure that both operands are lists!
If you opt to define an inner recursive helper function, don't forget to make an initial call to the recursive helper function to kick off the recursion.
[LIST + LIST]

"""
"""
def helper([]):
rps = ["rock", "paper", "scissors"]

cache = {}
def rock_paper_scissors(n):
  if n =0:
    return 0
  if n in cache:
    return cache[n]
  if n not in cache:
    cache[n] = helper(3^n)
    """


"""
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')



print("perms:", str(res))
"""


def recurse(prev, n, all_results):
    # add r, or p, or s to prev
    if n == 0:
        all_results.append(prev)  #ENTIRE RECURSION FUNCTION IS YOUR LOOP, BASE IS WHERE YOU BREAK LOOP
        return prev #prev is list # RETURN ONLY OCCURS WHEN N==0 
    # adds 3 arrays that start with rock
    recurse(prev + ['rock'], n - 1, all_results) #rhis is logic youre doing on each loop, with the prev=[] first, 
                                                  # and n = n-1 in recurse, & results = [] (from main function)
                                                  # recurse([], n, results) (ORDER OF ARGS SET IN HELPER FUNCTION )
    # add 3 arrays that start with paper
    recurse(prev + ['paper'], n - 1, all_results)
    # add 3 arrays that start with scissors
    recurse(prev + ['scissors'], n - 1, all_results)


def rock_paper_scissors(n):
    results = []
    recurse([], n, results)

    return results



print(rock_paper_scissors(2))


