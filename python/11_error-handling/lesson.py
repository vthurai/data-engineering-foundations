# Exceptions and Error Handling

# Whenever an error occurs, Python gives some valuable information about the error.
# A SyntaxError usually happens when some part of your code is mistyped.
# Many errors, however, happen during code execution.
# Let's look at an example error message:
#
#   Traceback (most recent call last):
#       File "<stdin>", line 1, in <module>
#   TypeError: can only concatenate str (not "int") to str
#
# The error message Python prints out is called a traceback, because Python works back
# through your code to locate the error.
# Python then shows which files and modules were involved in the error, as well as line numbers.
# The name of the error is given, and finally a message that tries to define the error.
# In our example, Python tells us that we can't concatenate an integer to a string.
# We can deduce that the error was likely a mistake using the '+' operator.


# 1. Exceptions
# An error that occurs during runtime is called an 'exception'.
# You can probably guess what most exceptions mean just from their names.
# Example: TypeError means an invalid type was used. FileNotFoundError means no file exists.
# There are many built-in exceptions: https://docs.python.org/3/library/exceptions.html


# 2. Assert
# The assert keyword evaluates an expression. If the expression returns False, AssertError is given.
# Uncomment the lines below to see the error messages they produce.
#assert 1 > 5
#assert False, "I'm an error message."


# 3. Raise
# Because exceptions are objects themselves, we can make Python throw an exception by using 'raise'.
#raise Exception
#raise TypeError("This is my custom error message.")


# 4. Try-Except
# If an exception occurs under a 'try' block, immediately jump to the 'except' block.
try:
    print(1 + "2")
    print("Success")
except:
    print("An error occurred!")

# However, the example above will jump to the except block if *any* exception occurs.
# This is bad, as it may be difficult to tell exactly which exception caused the jump.
# Instead, we should specify exactly which exceptions we want to check for.
try:
    print(1 + "2")
except TypeError:
    print("An error occurred!")

# To check for multiple exceptions, either use another except block or a tuple.
values = ["2", 0]
for i in range(3):
    try:
        print(1 / values[i])
    except IndexError:
        print("IndexError occurred!")
    except (TypeError, ZeroDivisionError):
        print("TypeError or ZeroDivisionError occurred!")

# You may specify a variable name to bind the exception that is caught.
try:
    print(1 + "2")
except TypeError as e:
    print("Error:", e)

# The 'finally' block executes after the try-except block finishes, even if an exception occurred.
for x in "1", 2:
    try:
        print(1 + x)
    except TypeError:
        print("TypeError occurred!")
    finally:
        print("Used item:", x)

# Python's built-in exceptions have their own class inheritance hierarchy.
# All non-system-exiting exceptions inherit from the 'Exception' class.
# Some exceptions are subclasses of others. A parent class will catch all subclass exceptions.
# To view the full hierarchy, refer to the Python docs.
try:
    print(1 / 0)
except ArithmeticError as e:    # ZeroDivisionError is a subclass of ArithmeticError.
    print("Error:", e)

# Writing Your Own Exceptions
