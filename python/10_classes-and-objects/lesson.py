# Classes and Objects
# TODO Encapsulation

# An object is an abstraction of a data structure.
# Objects in Python bundle data and functions together to form a cohesive unit.
# To create objects, we write a 'class', which defines how objects should be constructed.

# To create a class, use the class keyword. Class names should start with a capital letter.
class MyClass:
    pass

# To create an object, use the class name and assign it to a variable like so:
x = MyClass()
print(x)            # We now see that we have an object of class 'MyClass'.

# Classes may have their own functions. A function inside a class is called a 'method' of that class.
class MyFunctionalClass:

    def myClassFunction(self):  # 'Self' is a required parameter for every method of a class. This will be explained later.
        print("Hello world!")

# Now when we create our object, any methods that belong to the class are created for our object as well.
y = MyFunctionalClass()
y.myClassFunction()             # Accessing an object's method by using function dot notation.

# The __init__ method is a special class method.
# It tells the class how to 'construct' or 'initialize' the object.
# __init__ is automatically executed whenever an object is created.
# __init__ may also take parameters.
# If parameters are specified, the same number of arguments must be passed during object creation.
class MyClass2:

    def __init__(self, name):
        print("Hello " + name)

z = MyClass2("Bob")

# 'Self'
# Every time you create an object, you are making a new object 'instance' of that class.
# Each instance stores its own methods and variables.
# 'Self' is a reference to the current object instance, allowing access to the instance properties.
# Consider the following class:
class Person:

    def __init__(self, name):
        self.name = name  # Store the string passed down by 'name' into the property 'name' that belongs to the object instance.

    def say_my_name(self):
        return "Hi, my name is " + self.name  # Access the 'name' property that belongs to the object instance.

# Now lets create two instances of this class:
a = Person("Bobby")
b = Person("Charlie")

# Notice the difference in print statements because both objects have different properties.
print(a.say_my_name())
print(b.say_my_name())
