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

def my_function(x):
    _y = x + 2 # Good practice: internal variables should start with a _
    return _y
"""
A function, used often to do operation on many different inputs.
In python, a function is denoted by "def" and the output is given by "return".

A function may then be called at any time in order to complete operation.

An important thing to note is that a definition statement for a type must
precede any call to that type.
"""
my_input = 3
my_output = my_function(my_input) # A function call to operate on "my_input"

class myClass: #Good practice: name classes in lowerCamelCase
    def __init__(self, arg1, arg2):
        self.data1 = arg1
        self.data2 = arg2

"""
Classes are user-defined obects, allowing for code scalability.

While there is a lot to explore with classes, for now just know that they are a
sort of "container" of different data which can be called to create instances,
just like a function.
"""

class myOtherClass:
    def __init__(self, arg1, arg2, arg3):
        self.data1 = arg1
        self.data2 = arg2
        self.data3 = arg3
        self.data4 = arg2 + arg3 - self.data1

    def sum(self):
        return self.data1 + self.data2 + self.data3 + self.data4

    def product(self):
        return self.data1 * self.data2 * self.data3 * self.data4

    def difference_of_data2(self, x):
        return self.data2 - x
