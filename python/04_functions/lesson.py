# 4.a) Functions

# Functions are a block of code that is given a name.
# Giving a name to a block of code allows us to re-use that code.
# You have already seen functions being used. The "def" keyword is used to define a function.

def myFunction():
  print("Hello World")
  
# Using a function is known as "invoking" or "calling" a function.
# A function will not execute any code unless it is invoked.

myFunction()

# A function can take inputs called "arguments". Any number of arguments are allowed.

def say_hello(name, age):
  print("Hello " + name + ", your age is: " + str(age))
  
say_hello("Bob", 25)

# You can give a default value to an argument. The default value will be used if you call a function without passing arguments.

def say_goodbye(name="nobody"):
  print("Goodbye " + name)
  
say_goodbye()

# A function can output a value using the "return" statement.

def add_five(num):
  return num + 5

print(add_five(3))


# 4.b) Scope and Closure
# "Scope" is the region of code that can be accessed.
# Local scope is the block of code that is accessible only by the same level.
# Global scope is code that is accessible by everything.

num1 = 5
num2 = 7
def change_vars():
	num1 = 10
	global num2       # The "global" keyword tells Python that we are defining a variable name in the global scope.
	num2 = 20

# What is the output of print(num1) and print(num2) currently? What about after calling change_vars()?

# Functions can be nested within one another. Closures are inner functions that are nested.
 
def outer_function(num):
  def inner_function():
    print("I'm the inner function")
    nonlocal num    # The "nonlocal" keyword tells Python that we are defining a variable name in the scope of the outer function.
    num = "10"
    print(num)
  inner_function()
  print("I'm the outer function")
  print(num)
 
outer_function(8)
# What happens when we remove the "nonlocal num" line? 
