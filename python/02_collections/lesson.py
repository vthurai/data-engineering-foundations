# Collections: Lists, Set, Tuples, Dictionaries

# Read the following before starting
# Automate The Boring Stuff With Python - Pages 80 to 120
# Python All in One For Dummies - Pages 147 to 192
# Python Crash Course - Pages 37 to 74, 95 - 115

# Do the Practice Questions in Automate The Boring Stuff With Python - Pages 102 - 103, 119 - 121


# 1. Lists
# Lists are:
# Ordered - every element in a list has a unique index, and their order is preserved.
# Mutable - unlike strings, a list item can be changed to something else.
# Lists can have duplicate elements.
# List items can be any type. Mixing types is allowed.

# 1.a)
myList = [1, 3, 6, 11, 20, 31]
print(myList[2])
print(myList[1:3])
print(myList[0:5:2])
print(myList[1:-1])
print(myList[3:])
print(myList[:])
# What does each of these print statements output?


# 2. Sets
# Sets are:
# Unordered - items in a set do not have an index and their order is not preserved.
# Immutable - items in a set cannot be changed once a set is created. However, you may delete or add new elements.
# Set items are unique. They cannot contain duplicate elements.
# Set items can be any type. Mixing types is allowed.

# 2.a)
myList2 = [1, 4, 4, 8, 8, 8, 16, 21]
# Change myList2's type into a set. Print the new set, what does it look like?


# 3. Tuples
# Tuples are:
# Ordered - every element in a tuple has a unique index, and their order is preserved.
# Immutable - items in a tuple cannot be changed once created. You must create a new tuple if you want to add or remove elements.
# Tuples can contain duplicate elements.
# Tuple items can be any type. Mixing types is allowed.

#3.a)
myTuple1 = (16, "Bob", 3.14, "Charlie")
myTuple2 = (0, [14, 8], 16)
# Combine both tuples into one. What does it look like after printing?


# 4. Dictionaries
# Dictionaries are a collection of key-value pairs.
# Dictionaries are:
# Ordered? - they are ordered after Python version 3.7. However if order is important, you probably want to be using a list instead. Access dictionary elements by their key, not their index.
# Mutable - dictionary items may be changed after creation.
#
# Dictionary keys are:
# Unique - no duplicate keys are allowed.
# Immutable - you must use an immutable type. Integer, float, string and booleans can be used as keys. Lists and other dictionaries cannot be used as keys. You may still remove or add new keys.
#
# Dictionary values are:
# Non-unique - you may have duplicate values.
# Mutable - you may change a value after a dictionary is created.
# Dictionary values can be of any type. Mixing types is allowed.

# 4.a)
myDict = {"First name": "Bob",
          "Last name": "Simmons",
          "Age": 21,
          "Birthday": "11/08/1992",
          "ID": 12221}

# Change the value contained in the key "Age" to 30.
# Remove the "Last name" key.
# Add a new key-value pair: {"Gender": "Male"}
