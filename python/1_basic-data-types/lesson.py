### Read the following before starting
### Automate The Boring Stuff With Python - Pages 14 to 28
### Python All in One For Dummies - Pages 85 to 123
### Python Crash Course - Pages 19 to 36



## 1. Basic Data Types
## 1.a) Number Types
x = 34 # Integer Type
y1 = 4 # Integer Type
y2 = 4.0 # Float Type

# What are the difference between both divisions statements? Why is that?
# Bonus: Run the below using Python2 and Python 3
print(x / y1)
print(x / y2)

# What are the difference between both multiplication statements? Why is that?
# Bonus: Run the below using Python2 and Python 3
print(x * y1)
print(x * y2)

## 1.b) String Type
# Create a string variable 'name' that will be used in the print statement below
print(f'Welcome to {name} python code')

# 2. Data type conversion



## 3. String Manipulation
a = "hello there"
b = "goodbye now"

# String concatenation
print("a + b")

# Some useful built-in functions that can be used on strings:
print(a.upper())                # Converts to uppercase
print(a.lower())                # Converts to lowercase
print(a.replace("ello", "5"))   # Replaces a specified phrase with another specified phrase
print(len(a))                   # Gets the length (number of characters) in the string.
# There are many others. Google is your friend here.

# Strings in Python are *immutable*. They can't be changed once assigned.
a.replace("there", "friend")
print(a)                        # Does not change the original string

# You must assign a new string if you want to change the value of the variable.
a = a.replace("there", "friend")
print(a)                        # "a" now has new string.
a += b                          # This is the same as "a = a + b". A useful shorthand form.
print(a)

## 4. Date Time and Time zone Offset
import datetime

## 4.a) Print the current time using the datetime library

## 4.b) Print the time in the above answer in the full date format (e.g. Sunday Febuary 12 2023)

## 4.c) Using the above time, create the following statement using the current time variable
## 'Right now its HH:MM (AM/PM) on [Weekday], [Month] [Day], [Year]'
## E.g. 'Right now its 8:23 PM on Sunday, February 12, 2023'

## 4.d) Using the logic above, create the same statement but convert to the approriate time zone in:
## - Vancouver
## - Paris
## - Tokyo
## E.g. 'Right now in Tokyo its 10:23 AM on Sunday, February 13, 2023'

## 4.e) Write a python statement that will print the current amount of days till Christmas
