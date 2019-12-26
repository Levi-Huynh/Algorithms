#!/usr/bin/python
import itertools
from itertools import permutations

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

"""
try memoization
input: n
output: n (int) permutations of n
hints:
Since this question is asking you to generate a bunch of possible permutations, you'll probably want to use recursion for this.
Think about base cases that we would want our recursive function to stop recursing on. 
base:
How many ways are there to eat 0 cookies? 
What about a negative number of cookies?
Once we've established some base cases, 
recur:
how can we recursively call our function such that we move towards one or more of these base cases?
As far as performance optimizations go, caching/memoization might be one avenue we could go down? 
How should we make a cache available to our recursive function through multiple recursive calls?
"""

# cache = {}  # n=cookie(n)
res = []
res2 = []
perm1 = []
mlk = []
mylen = []

cache = {}


def eating_cookies(n, cache={0: 1, 1: 1, 2: 2, 3: 4}):
    if n <= 0 or n == 1:
        return 1
    if n in cache:
        return cache[n]
    if n not in cache:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    print(cache)
    return cache[n]


# would not have worked if not seen test cases
print("answer: ", eating_cookies(5))
# cache pattern: {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13}


"""
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
"""
