# Conditional Statements and Loops


# Read the following before starting
# Automate The Boring Stuff With Python - Pages 31 to 58
# Python All in One For Dummies - Pages 125 to 144
# Python Crash Course - Pages 75 to 94, 117 to 131

# Do the Practice Questions in Automate The Boring Stuff With Python - Pages 59

# 1. Boolean operators
# Value is either True or False
x = 3 > 5
y = 5 > 3
print(f'The statement 3 > 5 is {x}')
print(f'The statement 5 > 3 is {y}')

# Greater than '>' VS Greater Than or Equal too '>='
z = 3
print(f'Is z > 3 (z greater than 3) True or False? {z > 3}') # False
print(f'Is z >= 3 (z greater than or equal to 3) True or False? {z >= 3}') # True

# Less than '<' VS Less Than or Equal too '<='
w = 7
print(f'Is w < 7 (z less than 3) True or False? {w < 7}') # False
print(f'Is w <= 7 (z less than or equal to 3) True or False? {w <= 7}') # True

# To directly compare a value using '=='. Note that '=' is to assign a value and '==' is for comparison
a = 1
print(f'a == 1 True or False? {a == 1}')
# What if the values compared are technically the same but of different types
b = '1'
print(f'would 1 == "1" return True or False? {a == b}')
# The above statement would return False. You would need to cast one of the values to the others data type
# for it to return True
print(f'would 1 == int("1") return True or False? {a == int(b)}')

# Does not equal to or '!='
print(f'a != 2? {a != 2}')

# You can use 'not' to also reverse the status of the boolean result
print(f'3 >= 4 should return {3 >= 4}. Then not(3 >= 4) should return {not(3 >= 4)}')
# This would be useful when working with 'flags' or statuses in the future

# One last tidbit, what do you think 1 == True would return?
print(f"1 == True? {1 == True}")
# What about 0 == False
print(f"0 == False? {0 == False}")
# In Python, 1 will be treated as True or 0 would be treated as False without the need of casting.
# If we tried the above with a different number it wouldn't work out the same
print(f"2 == True? {2 == True}")
# We could cast 2 to bool and attempt the same statement
print(f"bool(2) == True? {bool(2) == True}")
# As long as the number is 0 (could be negative or decimals) the bool cast will always return True


# 2. If Statements
# The if statement will execute the code block under it if its condition is True.
sad = True
if (sad):
    print("I am sad :(")

if (not sad):
    print("I am not sad :)")

# Sometimes you want to have another option if the condition in the if statement isn't True. In this case
# we would add a else right after. Let's use the above example:
if (sad):
    print("I am still sad :(")
else:
    print("I am not sad :)")

# You aren't limited to two branches in your logic statements. You can you an elif (short of else if) in your
# conditional statements to have three or more logical branches.
alone = True
if (sad and alone):
    print("Now I am sad and alone :(")
elif(sad and not alone):
    print("Now I am sad but at least im not alone :|")
elif(not sad and alone):
    print("Now I am no longer sad but now im alone :|")
else:
    print("I am not sad or alone. Yay! :)")

# Ternary operators allow easy variable assignment based on a condition.
concern = True if sad and alone else False
print(f"Should I be concerned? {concern}")

# 3. Loops

# 3.a) While loop
# A 'while' loop will execute a block of code in a loop as long as its condition is True.
# Be careful, if your condition does not evaluate to False at some point you may loop infinitely.
count = 0
while count < 10:
    print(count)
    count += 1

# The 'break' keyword allows us to exit a loop at any time.
while True:
    print("I'm inside a while loop.")
    break

# 3.b) For loop
# A 'for' loop will execute its block of code for a specified sequence in order.
for num in 1, 2, 3:
    print(num)
# Here, 'num' is a variable and '1, 2, 3' is the sequence we loop through.
# At the start of every cycle, Python binds the next value of the sequence to 'num'.

# The sequence does not have to be just numbers.
for item in "hello", True, 2.7:
    print(item)

# We can even provide a collection such as a list.
for list_item in ["a", "b", "c"]:
    print(list_item)

# 'Range' provides a way to loop until it reaches a specified number, starting from 0.
for number in range(6):  # Loops six times, from 0 to 5. Does not include 6.
    print(number)

# We can also specify two numbers as the starting and ending point.
for number in range(15, 21):
    print(number)

# The 'continue' keyword ignores the rest of the code block and jumps into the next loop cycle.
for number in range(10):
    if number % 2 == 0:
        continue
    else:
        print(number)

# What if we wanted to loop over a list, but also keep track of their indexes?
# 'Enumerate' lets us assign an index number as well as the element itself.
words = ["Alpha", "Bravo", "Charlie", "Delta"]
for index, element in enumerate(words):
    print("Index number:", index, "element:", element)

# It is not recommended to write something like this:
#   for i in range(len(words)): ...
# Enumerate is clearer and eliminates the necessity to track indexes yourself.
