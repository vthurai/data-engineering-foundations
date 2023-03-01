# List Comprehension, Iterables, Iterators, and Generators


# 1. List Comprehension
# We can create a list of values using the following shorthand syntax:
digits = [i for i in range(10)]
print(digits)

# We can even add in a conditional statement.
only_even = [i for i in range(10) if i%2 == 0]
print(only_even)

# This works for the starting expression as well.
names = ["Steven", "Alex", "Chris", "Bob", "David"]
everyone_hates_chris = [x if x != "Chris" else "Raymond" for x in names]
print(everyone_hates_chris)

# This type of syntax is called list comprehension.
# It is somewhat similar to how set notation is written in mathematics.
# Using list comprehension allows us to easily define lists without the need of a loop.
# Nested list comprehension is also possible:
print([[(j,i) for i in range(3)] for j in range(3)])


# 2. Iterables and Iterators
# An 'iterable' is an object that can return its members one at a time.
# Lists, tuples, sets, dictionaries, and strings are examples of iterables.
# An 'iterator' is an object that allows iterating over its members using next().
my_iterator = iter(["a", "b", "c"])  # iter() converts an iterable (here, a list) into an iterator.
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# 2.a) Zip
# > zip(*iterables)
# Zip is a built in function. Zip takes two or more iterables, and produces a list of tuples.
# Each tuple produced will contain an element from each one supplied.
# By default, zip will stop when the shortest iterable has exhausted all elements.
zip_me = zip([1, 2, 3], ['sugar', 'spice', 'everything nice'])
print(list(zip_me))
zip_me_again = zip(range(3), ['fee', 'fi', 'fo', 'fum'], "ABCDEFG")
print(list(zip_me_again))

# Itertools is a built-in module which contains many useful functions for iterators.
import itertools

# 2.b) Repeat
# > itertools.repeat(object, times=None)
# Makes an iterator that returns the object a specified number of times.
# If no number is specified, will run indefinitely.
repeat_hello = itertools.repeat("hello")
print([next(repeat_hello) for _ in range(5)])

# 2.c) Cycle
# > itertools.cycle(iterable)
# Makes an iterator that indefinitely returns elements from the specified iterable in a cycle.
cycle = itertools.cycle("ABCD")
print([next(cycle) for _ in range(10)])

# 2.d) Takewhile and dropwhile
# > itertools.takewhile(bool_func, iterable)
# > itertools.dropwhile(bool_func, iterable)
# The first argument must be a function that takes an element and returns a boolean.
# Takewhile makes an iterator that returns items from the iterable until the function returns False.
# Dropwhile drops items until the function returns True, then returns every remaining element.
some_numbers = [-13, 4, -6, 0, 1, 5, -9, 9, 11, 27]
print(list(itertools.dropwhile(lambda x: x < 5, some_numbers)))
print(list(itertools.takewhile(lambda x: x < 5, some_numbers)))

# 2.e) Combinations
# > itertools.combinations(iterable, r)
# Makes an iterator that returns tuples containing element combinations of r-length.
# A combination is a unique selection of elements where order does not matter.
print(list(itertools.combinations('ABCD', 3)))


# 3. Generators
# A generator is a function that behaves like an iterator.
# The yield keyword is used to 'generate' a value instead of return.
# When a generator is called by a loop, it will run until it reaches a yield statement, then pause.
# When it is called again, the generator resumes from the previously paused yield statement.
def my_generator():
    yield 1
    yield 2
    yield 3

# This will create a generator object.
count = my_generator()
print(count)

# We can access the yielded values with a loop:
for i in count:
    print(i)

# The yield statement executes only *once*.
for j in count:  # This does not output any more values. You will need a new generator object.
    print(j)

# We can also access generator values using next().
count2 = my_generator()
print(next(count2) + 10)
print(next(count2) + 10)
print(next(count2) + 10)

# Generators will only generate values when they are needed (called lazy evaluation).
# This is useful for when performance is a concern.
def get_integers(n):
    count = 0
    while count < n:
        yield count
        count += 1

print(list(get_integers(15)))

# In fact, there is a shorthand form for writing generators as well.
# Take the following list created using list comprehension:
odd_numbers = [i for i in range(10) if i%2 == 1]
# If we replace the square brackets [] with parentheses (), we obtain a generator!
odd_num_gen = (i for i in range(10) if i%2 == 1)
print(odd_num_gen)
print(list(odd_num_gen))
