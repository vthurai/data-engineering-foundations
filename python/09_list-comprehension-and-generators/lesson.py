# 1. List Comprehension

# We can create a list using the following shorthand syntax:
digits = [i for i in range(10)]
print(digits)

# We can even add in a conditional statement.
only_even = [i for i in range(10) if i%2 == 0]
print(only_even)

# This works for the starting expression as well.
names = ["Steven", "Alex", "Chris", "Bob", "David"]
everyone_hates_chris = [x if x != "Chris" else "Raymond" for x in names]
print(everyone_hates_chris)

# This type of syntax is called list comprehension. It is somewhat similar to how set notation is written in mathematics.
# Using list comprehension allows us to easily define lists without the need of a loop.

# 2. Generators
# A generator is a function that behaves like an iterator, i.e. it can be used in a for loop.
# The yield keyword is used to "generate" a value instead of return.
# When a generator is called by a loop, it executes code until it reaches a yield statment and then pauses.
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
for j in count:      # This does not output any more values. You will need a new generator object.
    print(j)

# Generators will only generate values when they are needed (called lazy evaluation). This is useful for when performance is a concern.

def get_integers(n):
    count = 0
    while count < n:
        yield count
        count += 1

print(list(get_integers(15)))       # We can simple cast to a list instead of using a loop.

# In fact, there is a shorthand form for writing generators as well.
# Take the following list created using list comprehension:
odd_numbers = [i for i in range(10) if i%2 == 1]
# If we replace the square brackets [] with parentheses (), we obtain a generator!
odd_num_gen = (i for i in range(10) if i%2 == 1)
print(odd_num_gen)
print(list(odd_num_gen))