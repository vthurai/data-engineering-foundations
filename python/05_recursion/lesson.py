# 1. Recursion

# A recursive function is a function that calls itself.
# Like a while loop, a recursive function will loop endlessly if there is no exit condition.

def recursive_func():
  print("hello")
  return             # Removing this will cause an infinite recursive loop.               
  recursive_func()
recursive_func()

# Lets write a function called factorial(n) that returns the factorial of a positive integer n.
# A factorial is the product of all integers from 1 to n. Eg. factorial(5) = 5*4*3*2*1 = 120.

# How to write a recursive function:
# Step 1: Define your base case.
# A base case is the point at which recursion should stop.
# (Sometimes it is possible to have multiple base cases.)
# In our factorial function, the base case is n==1. We don't go any further after that.

# Step 2: The recursive step.
# If we have not reached the base case, then we recurse deeper into the function.
# In our factorial function, we multiply n by the factorial of (n -1). This is where recursion starts.

def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)
 
print(factorial(5))

# 1.a) Write a recursive function sum_all(n) that returns the sum of all integers from 1 to n.
# 1.b) Can you re-write sum_all(n) without using recursion?
# 1.c) (Bonus) Can you re-write sum_all(n) without using any loops at all?
