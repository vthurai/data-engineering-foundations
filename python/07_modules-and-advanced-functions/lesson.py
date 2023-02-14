
# Advanced function topics

def my_function():
  return 15

a = my_function()
b = my_function

# What is the difference between a and b? What happens when you print them?

# Lambda functions
# A lambda function is an *anonymous function* (a function without a name).
# Named after lambda calculus - a system for expressing functions using mathematical logic.
# They are useful when we want to create a simple function but don't require a named function.

c = lambda: 15
print(c)
print(c())

# Lambda functions can take arguments as well.

product = lambda x, y: x*y
print(product(3, 6))

# Map
# Map is a built-in function. Map takes a *function* as it's first parameter, and a list as it's second parameter.
# > map(function, list)
# Map then applies the function to every element in the list.

times_two = map(lambda x: x*2, [3, 5, 7])      # Lambda functions are useful here!

# Map returns a reference to a map object.
print(times_two)
# To see the results, change it's type to a list
print(list(times_two))


# Filter
# Filter is a built-in function.
# Filter takes a function as it's first parameter. This function *must* return a boolean. Filter takes a list as it's second parameter.
# > filter(bool_function, list)
# Filter then creates a new list for which the function returns true when applied to every element in the specified list.

less_than_five = filter(lambda x: x < 5, [2, 3, 4, 5, 7, 9, 11])
print(list(less_than_five))


# Reduce
# Reduce takes a function as it's first parameter. This function *must* take two arguments. Reduce takes a list as it's second parameter.
# > reduce(function, list)
# Reduce then applies the function to the first two items in the list. Then, it will apply the same function using the result and the next item in the list.
# This continues for every item in the list.

from functools import reduce
add_all = reduce((lambda x, y: x + y), [1, 2, 3, 4, 5])
print(add_all)

