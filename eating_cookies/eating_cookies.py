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

"""
U
-# of cookies to eat at a time: [0, 1, 2  3]
-# n = number of cookies in jar
output:
-# perms/ways to eat all of cookies in jar? Integer 

P
-most likely recursion as wants number of permutations
- base cases: 0 cookies: 0, -neg cookies: 0
# best thing to do to build out sequences until find pattern! may be long
cache pattern: {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13, 6:24, 7:44, 8:81}

E
-create function with 2 arguments:
-n (number of cookies in jar) & your cache 
-create base cases return 1 if n < =0 or n ==1 
- initialize cache for given base case
-check if n in cache, if so return cache[n]
-if n not in cache, 
    - then set cache[n] => 
    -recursive eating_cookies of n-1, n-2, n-3 (since there are only 3
    non zero ways to eat the cookie)
    -return cache[n]

R
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
    # print(cache)
    return cache[n]


# would not have worked if not seen test cases
#print("answer: ", eating_cookies(8))
# print(eating_cookies(50))

# cache pattern: {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13, 6:24, 7:44, 8:81 }


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
