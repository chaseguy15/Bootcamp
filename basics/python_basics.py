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

"""
---------------------------------VARIABLES--------------------------------------
"""

### BASIC TYPES ###

my_variable = 5 # Good practice: name variables with lower_snakecase
# Low level object given identity which can be operated on

logic_variable = True # Variables can take on any type
string_variable = "characters"

new_variable = 13

newer_variable = new_variable

MY_CONSTANT = 3 # Good practice: name constants in UPPER_SNAKECASE

"""
------------------------------LOOPS/CONDITIONS----------------------------------
"""

"""
Loops are used to iterate through values to do operations. For example, if you
wanted to create a program that printed out a every number from 0 to 4 you would
run:
"""

for x in range(5):
    #print(x)

    """
    This is a "for loop". It simply uses range() to create a vector [0,1,2,3,4]
    and runs what is inside the loop for each value. For loops are useful when
    you know exactly how many times you want to iterate.

    There are also "while loops" which run until your condition is no longer
    met, or more precisely that the stated condition is no longer True. While
    loops are useful when you don't know how long you want to iterate yet.
    """

x = 10
while x > 0:
    #print(x)
    x = x - 1

    """
    If statements are also very useful. You can use an if statement to check
    whether a condition is true and then perform a given operation if it is.

    if, else if, and else are the common calls for these statements.
    """
#x = 1

#_y = 1
'''
if x == 0:
    _y = (x + 2) ** 2
    print("x is zero")
    print(_y)
elif x == 4:
    print("x is four")
else:
    print("x is neither zero nor four")
'''


#print(_y)

"""
Notice how each one of these operations creates an indent. This shows what is
happening within the scope of the if statement
"""

"""
---------------------------------FUNCTIONS--------------------------------------
"""

def my_function(my_input):
    _y = x + 2 # Good practice: internal variables should start with a _
    my_input = 5

    #print("during function", my_input)
    return _y

def strings_only(input: str) -> str:
    return "Good job, that was a string"
"""
A function, used often to do operation on many different inputs.
In python, a function is denoted by "def" and the output is given by "return".

A function may then be called at any time in order to complete operation.

An important thing to note is that a definition statement for a type must
precede any call to that type.
"""

my_input = 3
#print("before function:", my_input)
my_output = my_function(my_input) # A function call to operate on "my_input"


"""
Notice how my_input goes back to its original value despite it changing in the
function. That's because that change to the value is only "in the scope" of the
function. Once the function ends, that version of my_input is erased. Scopes are
very important.
"""


"""
----------------------------------CLASSES---------------------------------------
"""

class myClass: #Good practice: name classes in lowerCamelCase
    def __init__(self, arg1, arg2):
        self.data1 = arg1
        self.data2 = arg2



"""
Classes are user-defined objects, allowing for code scalability.

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

class1 = myOtherClass(4, 5, 8)
x = class1.difference_of_data2(3)
print(x)
