"""
Python is a must-know language, used for a wide array of applications because
of how dynamic it is. The language is also user friendly so we will be starting
with it.
"""

### COMMENTS ###

# an single-line comment, can be used following statements

"""
A multi-line comment.
These are best used for important documentation.
"""

### BASIC TYPES ###

my_variable = 5 # Good practice: name variables with lower_snakecase
# Low level object given identity which can be operated on

MY_CONSTANT = 3 # Good practice: name constants in UPPER_SNAKECASE

# To see something in the command line when running, use a print statement
print(my_variable)

def my_function(x):
    _y = x + 2 # Good practice: internal variables should start with a _
    return _y
"""
A function, used often to do operation on many different inputs.
In python, a function is denoted by "def" and the output is given by "return".

A function may then be called at any time in order to complete operation.

Two important thing to note is that a definition statement for a type must
precede any call to that type, and any variable defined in a function stops
existing after that function ends. AKA it goes out of scope.
"""
my_input = 3
my_output = my_function(my_input) # A function call to operate on "my_input"

class myClass: #Good practice: name classes in lowerCamelCase
    def __init__(self, arg1, arg2):
        self.field1 = arg1
        self.field2 = arg2

"""
Classes are user-defined types, allowing for code scalability.

While there is a lot to explore with classes, for now just know that they define
a type which can then be used to generate objects.

Objects are a sort of "container" of different field which can be called to
create instances, just like a function.
"""

class myOtherClass:
    def __init__(self, arg1, arg2, arg3):
        self.field1 = arg1
        self.field2 = arg2
        self.field3 = arg3
        self.field4 = arg2 + arg3 - self.field1

    """
    Here we have a bunch of functions under the class. These functions are
    called methods, or associated functions. They are a special kind of function
    that can only operate on the associated object. Basically, we can now do
    "sum" or "product" on any object that is a "myOtherClass". This is probably
    confusing to read so I will explain a bit more in a bit.


    The main method used to define a class in python is __init__(), which sets
    parameters for how the object can be populated.
    """

    def sum(self):
        return self.field1 + self.field2 + self.field3 + self.field4

    def product(self):
        return self.field1 * self.field2 * self.field3 * self.field4

    def difference_of_field2(self, x):
        return self.field2 - x

"""
To then use the class to make an object, we have to assign it to a variable,
populating it with arguments as dictated by the initialize function.
"""
my_first_object = myOtherClass(1, True, 2 - 3j)
# Here we have created an object from myOtherClass with the needed arguments

# To reference an objects field, use Object.Field:
my_first_object.field3

"""
Because all definition is up to the user, a class can be as strict as you want.
Another thing to note is a class can be a field for another class.

A common example is one with animals.
"""

class Animal:
    def __init__(self, legs, warm_blooded, lays_eggs, sound):
        legs
        warm_blooded
        lays_eggs
        sound

duck = Animal(2, True, True, "quack")
snake = Animal(False, False, True, "hiss")

"""
You could even define each kind of animal as its own class which can then be
used for populating the animal class.
"""
