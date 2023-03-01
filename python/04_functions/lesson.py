# 1. Functions

# A function is a block of code that is given a name.
# Giving a name to a block of code allows us to re-use that code.
# You have already seen functions being used. The 'def' keyword is used to define a function.
def my_function():
    print("Hello World")

# Using a function is known as 'invoking' or 'calling' a function.
# A function will not execute any code unless it is invoked.
my_function()

# A function can take input variables called 'parameters'. Any number of parameters are allowed.
def say_hello(name, age):
    print("Hello " + name + ", your age is: " + str(age))

# The values that we pass through to the function are called 'arguments'.
say_hello("Bob", 25)

# You can give a default value to a parameter.
# The default value will be used if you call a function without passing arguments.
def say_goodbye(name="nobody"):
    print("Goodbye " + name)

say_goodbye()

# A function can output a value using the 'return' statement.
def add_five(num):
    return num + 5

print(add_five(3))


# 2. Scope and Closure
# 'Scope' is the region of code containing names and variables that is able to be accessed.
# Local scope includes the variables and names that are defined locally (accessible only by code
# inside the same block level or deeper).
# Global scope includes the variables and names that are global (accessible by everything).
num1 = 5
num2 = 7
def change_vars():
    num1 = 10
    global num2  # The 'global' keyword tells Python that we are defining a variable name in the global scope.
    num2 = 20

# 2.a) What is the output of print(num1) and print(num2)? What about after calling change_vars()?

# Functions can be nested within one another. Closures are inner functions that are nested.
def outer_function(num):

    def inner_function():
        nonlocal num  # The 'nonlocal' keyword tells Python that we are defining a variable name in the scope of the outer function (neither local or global).
        num = "10"
        print("I'm the inner function and num is:", num)

    inner_function()
    print("I'm the outer function and num is:", num)

outer_function(8)

# 2.b) What happens when we remove the 'nonlocal num' line?
