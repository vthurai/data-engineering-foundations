# Modules and File Input/Output

# 1. Modules
# A module is a separate Python file that contains functions and code that you may wish to use.
# Python has many built-in modules. The import statement adds a module's functions to our file.
import math
print(math.sqrt(25))
print(math.pi)

# Instead of importing the entire module, we can select specific names that we want to import.
from math import sqrt, log
print(sqrt(49))         # Now, we can simply type sqrt() instead of math.sqrt().
print(log(64, 2))

# You can choose to use a different name for an imported module or module function.
import math as calc
print(calc.sqrt(9))
from math import sqrt as square_root
print(square_root(49))


# 2. External modules
# There are two methods to include external modules in our Python environment.
# The first way is to simply copy the module file manually into our directory, and then import it.
# This will work as long as you trust the file, and ensure there are no dependency issues.
# You may be required to do this if, say, you were collaborating on a project with a colleague.

# The second (and more ideal) method is to use a package installer.
# The default package installer included with Python3 is called 'pip'.
# Pip allows you to install Python packages submitted by other software distributors.
# If pip is not installed by default, visit https://pip.pypa.io/en/stable/getting-started/


# 3. File I/O
# Python has built-in functions for reading and writing to files.

# 3.a) Open
# > open(file_name, mode='r')
# Opens a file from the given file name. The 'mode' is a string that says to either read or write.
# To open a file for writing, use the mode 'w'. Then we can write to the file using write().
# If no file with the specified name exists, 'write' will create a new file.
# Note that Python opens the file path in the current working directory.
my_file = open('example.txt', 'w')
my_file.write('Hello world\n')
my_file.write('Goodbye world')
my_file.close()     # Always remember to close a file when you are finished with it.

# 'Write' will overwrite the file if any data already exists.
# If we want to append to the end of the file, use mode 'a':
my_file = open('example.txt', 'a')
my_file.write("\nHello again")
my_file.close()

# Opens a specified file for reading only (mode 'r', the default mode):
my_file = open('example.txt', 'r')
print(my_file.read())
my_file.close()

# To read every line in a sequence:
my_file = open('example.txt')
for line in my_file:
    print(line)
my_file.close()

# To read each line individually use readline(). Readline remembers its position in the file:
my_file = open('example.txt')
print("Line 1:", my_file.readline())
print("Line 2:", my_file.readline())
my_file.close()

# You *must* remember to close a file using close() when you are finished with a file.
# Failing to close a file properly may cause issues such as data loss.
# Alternatively (and more recommended), you can use the following syntax to open a file instead:
with open('example.txt') as my_file:
    print(my_file.read())
# This will close a file when finished even if an error occurs (you do not need to call close).


# 4. Storing Data as Files
# Strings can easily be written to text files. But what about other types (like list or dict)?

# 4.a) JSON
# https://www.json.org/json-en.html
# JSON is a data format. It is structurally similar looking to a Python dictionary.
import json

# Dictionaries and lists can be easily converted to JSON format.
animals = {
    "cows" : 2,
    "horses" : 3,
    "pigs" : 8,
    "chickens" : 10
}
converted_to_json = json.dumps(animals)
print(converted_to_json)

# Now we have a JSON string that we can save to a file. JSON files should use the '.json' extension.
with open('example.json', 'w') as f:
    f.write(converted_to_json)

# To read the file and get back our dictionary:
with open('example.json') as f:
    animals = json.load(f)
    print(animals)

# 4.b) Pickle 🥒
# Some types of data are difficult to convert to strings or JSON.
# Serialization is the process of converting data into a format that is suitable for saving.
# The json module serializes dictionaries and lists for us. For other things, 'pickle' might work.
import pickle

# Let's use pickle to write a function to a file.
def pickle_me(input_list):
    print("If all goes well, I should have been saved to a file.")
    total = 0
    for x in input_list:
        total += x
    return total

# We now use pickle to convert our function to bytes.
# The 'wb' mode opens our file in 'binary write mode' so that we can write the bytes.
with open('example', 'wb') as f:
    pickle.dump(pickle_me, f)

# Now to read back the file and de-serialize our function.
with open('example', 'rb') as f:
    unpickle_me = pickle.load(f)
    print(unpickle_me([2, 5, 7]))

# Pickle has its limitations and may not perfectly serialize every possible object you create.
# Also, since pickle loads object data into Python, you should only use pickle on files you trust.
# https://docs.python.org/3/library/pickle.html
