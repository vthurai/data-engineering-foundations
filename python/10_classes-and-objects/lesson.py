# Classes and Objects

# An object is an abstraction of a data structure.
# Objects in Python bundle data and functions together to form a cohesive unit.
# To create objects, we write a 'class', which defines how objects should be constructed.

# To create a class, use the class keyword. By convention, class names should start with a capital letter.

class MyClass:
    pass

# We have created our first class. To create an object, assign it to a variable like so:
x = MyClass()
print(x)            # We now see that we have an object of class: "MyClass".

# Classes can have their own functions. A function inside a class is called a "method" of that class.

class MyFunctionalClass:

    def myClassFunction(self):      # The "self" keyword is a required argument for every method of a class. This will be explained later.
        print("Hello world!")

# Now when we create our object, any methods that belong to the class are created for our object as well.
y = MyFunctionalClass()
y.myClassFunction()                 # Accessing an object's method is as simple as using function dot notation.

# The __init__ method is a special class function. It "initializes" or "constructs" the object when it is created.
# __init__ is executed whenever an object is created. __init__ may also take arguments.
# If arguments are specified, then the same number of arguments (minus 'self') must be provided during object creation.

class MyClass2:

    def __init__(self, name):
        print("Hello " + name)

z = MyClass2("Bob")

# The 'self' keyword
# Every time you create an object, you are making a new object "instance" of that class.
# Each instance has it's own methods and variables. The 'self' keyword is a reference to the current object instance.
# Consider the following class:

class Person:

    def __init__(self, name):
        self.name = name        # Store the string passed down by the 'name' argument into the property 'name' that belongs to the object instance.

    def say_my_name(self):
        return "Hi, my name is " + self.name        # Access the 'name' property that belongs to the object instance.

# Now lets create two instances of this class:
a = Person("Bobby")
b = Person("Charlie")

# Let's call the method of each object. Notice the difference in print statements because both objects have different properties.
print(a.say_my_name())
print(b.say_my_name())
