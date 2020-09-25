"""
Challenge Two:
- Create a class that calculates the a dropping objects location!

You will be given: x_velocity, z_velocity, height

Note: The object is dropping in the -z direction.
Once you have completed the challenge, please push this to your remote branch.
"""
import math

# TODO: Create dropCalc class
class dropCalc:
    def __init__(self, v_x, v_z, h):
        self.v_x = v_x
        self.v_z = v_z
        self.h = h
        self.g = -9.81

        self.l_x = 0
        self.l_z = 0
        self.t = 0
# TODO: Create methods

# function to solve for time
    def solve_t(self):
        a = self.g
        b = self.v_z
        c = self.h
        self.t = -b - ((b**2 - 4*a*c)**.5)/(2*a)
        print 'time check... time solved!'

# function to solve for length in x direction
    def solve_x_len(self):
        self.l_x = self.v_x * self.t
        length = int(self.l_x)
        print 'drop distance solved! it\'s', length,'... whatever units, from where the object dropped'

# function to run everything
    def run_all(self):
        self.solve_t()
        self.solve_x_len()

# TODO: Test results
# place values into the three variables, these are just
# placeholders so I could test the code
v_x = 12
v_z = 0
h = 100
example = dropCalc(v_x, v_z, h)
example.run_all()
