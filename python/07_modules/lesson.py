# Modules

# A module is a seperate Python file that contains functions and code
# that you may wish to use in the current environment.
# Python has many built-in modules. The import statement adds a module's functions to our file.

import math
print(math.sqrt(25))
print(math.pi)

# Instead of importing the entire module, we can select specific names from the module that we want to import.

from math import sqrt, log
print(sqrt(49))         # Now, we can simply type sqrt() instead of math.sqrt().
print(log(64, 2))

# You can choose to use a different name for an imported module or module function.

import math as calc
print(calc.sqrt(9))
from math import sqrt as squareroot
print(squareroot(49))


# External modules

# There are two main ways to include external modules in our Python environment.
# The first way is to simply copy the module file manually into our directory, and then import it.
# This will work as long as you trust the file, and ensure there are no dependency issues.
# You may be required to do this if, say, you were collaborating on a project with a colleague.

# The second (and more ideal) way is to use a "package installer".
# The default package installer included with Python3 is called "pip".
# Pip allows you to install Python packages from a repository submitted by various other software distributors.
# (If pip is not installed by default, visit https://pip.pypa.io/en/stable/getting-started/ for instructions on setting up.)


