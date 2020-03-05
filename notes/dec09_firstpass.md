One strategy for approaching novel problems is to use Polya’s Problem Solving Techniques. Let’s break down each step a bit further and outline some things we can do to complete each step.

Understand
Read the problem. More than once if needed. A correct solution to the wrong problem won’t make your future boss too happy.
Don’t make assumptions. Clarify things. Ask questions. Reread the problem.
What type of data can we expect users to enter?
Do we need to handle invalid input?
What needs to be returned by this function?
Try explaining the problem to someone else or restating the problem to the asker.
Test your understanding by manually running through a test case with some easy-to-use sample data.
Plan
Think about the mental steps you followed when manually running through a test case. Write those out, then translate to operations and functions your program can run.
Look for steps that are repeating. These might be translated into a loop or helper function.
Use psuedocode to create an “outline” for your solution before writing the final version in the language of your choice.
Implement
Take the steps you outlined in your plan from step two and code it up!
Time permitting, write some test cases to ensure your solution works as intended.
Improve
This step will be the focus of the next module.

Hash table -just object in any lang (dict in python)

Constant O(1) -same # of ops to get job in, despite input (1 pick of lottery ball, despite number of balls, single operation to destroy stakc of card. Index method can directly access element of array, #1 op. )
Logarithmic O(log n) - (looking up words in dictionary, have general idea where to find our entry. Books in bookshelf that are sorted, )
Linear O(n) - #ops for given input, is in direct proportion to n.  ^incr input size = ^incr #op . Counting coins or
marbles,. search function  

Linearithmic O(n log n) - increase # of ops it performs as a log-linear function of the input size n
1/scan each element (n) 2) sort operation (mainly sorting algorithms)
(quicksort, mergesort, heapsort, timsort)
Polynomial O(n^c)
Exponential O(c^n)
Factorial O(n!)

# O(log n) 
def binary_search(sorted_arr, target):
  low= 0, high = len(sorted_arr)-1
  mid= (high-low) //2
  if target = sorted_arr[midpoint]: #if target = midpoint
  return midpoint
  elif target< sorted_arr[midpoint]:
  return binary_search(sorted_arr[:midpoint])  # recurse, with reavluating where to search using slice & midpoint, if target less than mid
  else:
  return binary_search(sorted_arr[midpoint:]) #if target more than mid

#O(n)
def foo(n):
  sq_root = int(math.sqrt(n))
  for i in range(0, sq_root): #O(n)
    print(i)

O(n^3)
def bar(x):
  sum = 0 #O(1)
  for i in range(0, 1463): #O(n)
    i += sum #O(1)
    for j in range(0, x): #O(n)
      for k in range(x, x + 15): #O(n)   
        sum += 1

#O(n^2)
def baz(array):
  print(array[1]) 
  midpoint = len(array) // 2 #O(logn)
  for i in range(0, midpoint):#O(n)
    print(array[i])
  for _ in range(1000): #O(n)
    print('hi')

#O(n)
def search(array, target):
  for el in array:
    if target == el:
      return True
  return False 