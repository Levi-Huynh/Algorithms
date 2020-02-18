Once a working first-pass solution has been implemented, we can iterate upon it and improve it. We’re going to describe a few strategies for doing that here.

Overview
Ok, so we got an initial working solution. That’s great! But can we improve it? Most of the time, yes, we can.

The first step to improving upon something is to first figure out what it’s issues are. Does our implementation use nested loops when it doesn’t need to? Perhaps our solution is performing work that we don’t actually need to be doing? Or maybe there’s a data structure we could use to store our data more efficiently while our solution is working with it?

With our initial solution to Nth Fibonacci, a lot of unneeded, redundant work is being performed. One avenue we could take in order to improve our implementation then is to cut down on all the redundant work. How might we do that?

FIRST PASS
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

CACHING/MEMOIZATION
def fib(n, cache):
    if n < 2:
        return n
    elif cache[n] > 0:
        return cache[n]
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]

All we’d have to do now is to initialize our cache before calling our function for the first time:
    n = 35
cache = {i: 0 for i in range(n + 1)}
print(fib(n, cache))


We can clean this up so that the function doesn’t break if no cache is passed into it:
def fib(n, cache=None):
  if n < 2:
    return n
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache = {i: 0 for i in range(n+1)}
    cache[n] = fib(n-1, cache) + fib(n-2, cache)
    return cache[n]

    The fact is that recursion is rarely the most efficient approach to solving a problem, and iteration is almost always more efficient. This is because there is usually more overhead associated with making recursive calls due to the fact that the call stack is so heavily used during recursion.Mar 12, 2013

    ITERATIVE VERSION OF NTH fib:
    def iter_fib(n):
    answer = 0
    prev = 1
    prevPrev = 0
    for i in range(n - 1):
        answer = prev + prevPrev
        prevPrev = prev
        prev = answer
    return answer