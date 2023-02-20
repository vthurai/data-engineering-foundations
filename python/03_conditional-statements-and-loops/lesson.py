# Conditional Statements and Loops


# Read the following before starting
# Automate The Boring Stuff With Python - Pages 31 to 58
# Python All in One For Dummies - Pages 125 to 144
# Python Crash Course - Pages 75 to 94, 117 to 131

# Do the Practice Questions in Automate The Boring Stuff With Python - Pages 59

# Bool Type
# Value is either True or False
x = 3 > 5
y = 5 > 3
print(f'The statement 3 > 5 is {x}')
print(f'The statement 5 > 3 is {y}')

# Greater than '>' VS Greater Than or Equal too '>='
z = 3
print(f'Is z > 3 (z greater than 3) True or False? {z > 3}') # False
print(f'Is z >= 3 (z greather than or equal to 3) True or False? {z >= 3}') # True

# Less than '<' VS Less Than or Equal too '<='
w = 7
print(f'Is w < 7 (z less than 3) True or False? {w < 7}') # False
print(f'Is w <= 7 (z less than or equal to 3) True or False? {w <= 7}') # True

#To directly compare a value using '=='. Note that '=' is to assign a value and '==' is for comparison
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
# If we tried the above with a different number it wouldnt work out the same
print(f"2 == True? {2 == True}")
# We could cast 2 to bool and attempt the same statement
print(f"bool(2) == True? {bool(2) == True}")
# As long as the number is 0 (could be negative or decimals) the bool cast will always return True


# If Statements
# The code will enter you if statement if the condition inside is True
sad = True
if (sad):
    print("I am sad :(")

if (not sad):
    print("I am not sad :)")

# Sometimes you want to have another option if the condition in the if statement isnt true. In this case
# we would add a else right after. Lets use the above example:
if (sad):
    print("I am still sad :(")
else:
    print("I am not sad :)")

# You aren't limited to two branches in your logic statements. You can you an elif (short of else if) in your
# conditional statements to have three or more logical branches
alone = True
if (sad and alone):
    print("Now I am sad and alone :(")
elif(sad and not alone):
    print("Now I am sad but atleast im not alone :|")
elif(not sad and alone):
    print("Now I am no longer sad but now im alone :|")
else:
    print("I am not sad or alone. Yay! :)")

# A need trick is a shortcut conditional expression where you can assign a value to a new variable based on
# conditional statements
concern = True if sad and alone else False
print(f"Should I be concerned? {concern}")

# for range
# for each
# while
# break
# continue

