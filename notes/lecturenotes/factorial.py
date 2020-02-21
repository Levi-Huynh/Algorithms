
# factorial ex:
# 4! = 4x3x2x1

# input type
# output type
# constraints,
# size

"""
ex: 
4! = 4*3*2*1
5! =5* 4!
6! =6* 5!

constraints:
1/ O<n<10000 int

2/ n! = n* (n-1) * (n-2) ...1
    -recursive
    -bsae case:
        - if n<=1 return 1
    -recursive case:
        -return n*f(n-1)

3/ notice max memory for python is 998 storage space per call => max recursion depth error at n=998 

#function will run until it hits its base case then will return , waits until base case returned, then recursive calls will return 
(running out of mem before the base function has chance to execute a return) recursive may not allow us to cover cases

    
"""


def factorial(n):
    if n <= 1:
        return 1
    # O(n) rt # space: O(n) (memory O(c) created n times function is called)
    return n*factorial(n-1)


# print(factorial(10))

# 4*3*2*1
# O(n)


def it_factorial(n):

    tracker = 1
    for i in range(1, n+1):  # range starts 1, 2, 3, ends 4+1 #runs n times
                                # i =1, 2, 3, 4, 5
        tracker *= i
        return tracker


"""
rule:
xn= x(n-1) +x(n-2)
nth term = (n-1) term  + (n-2) term 

value of arr(n) = arr(n-1) + arr(n-2)
result = 1
create list 
for i in range(2, n+1)
    result += ((i-1) + (i-2)) 
    return result 
#mem cache used when repetition may cause a lot slowing /db work/not able to store this much for each user(doesnt have to be recursion)

"""
# memoization memcache dynamic programming
# O(n)
cache = {}  # dictionary [n=fib(n)]


def fib(n):
    # use cache now don't have to repeat f(n) in various parts of tree
    if n in cache.keys():
        return cache[n]
    if n == 1:
        return 1
    if n == 0:
        return 0
    # def of recursive calling this recursive case until base case is reached
    fib_res = fib(n-1) + fib(n-2)
    # store result of f(n) in cache
    cache[n] = fib_res
    return fib_res


print("res:", fib(6))

# functools import lru_cache - built on memoization
"""
@lru_cache(maxsize=500)
def lru_fib(n):
    if n==0:
        return 0
    if n ==1:
        return 1
    return fibonnaci(n-1) + fibonnaci(n-2)
"""

# given array, find the integer that appears an odd number of times
# pos & neg, always only 1 int that appears an odd number of times

"""
plan
2/ given array 
    freq_dict for each n, store its count
    loop thru array, 
    freq_dict[n] +=1
    loop thru k,values in freq_dict:
    if v %2! =0
    return k

    optimize: check rt, space, 
    -comments
    -name of variables 
    -be ready for are we done questions
    -who are we solving this for? what is the purpose? worth spending to optimize?
    
    """
# rt 2n (same scope add) => O(n)
# space n O(n)


def find_it(seq):
    freq_dict = {}
    for num in seq:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1
    for k, v in freq_dict.items():
        if v % 2 != 0:
            return k
