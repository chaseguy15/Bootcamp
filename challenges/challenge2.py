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
    def __init__(self,
                 x_vel: float,
                 z_vel: float,
                 ht: float,
                 ):
        self.x_velocity = x_vel # dropCalc's x_velocity is = the x_vel parameter
        self.z_vel = z_vel
        self.height = ht
        self.g = -9.81

        self.l_x = 0
        self.l_z = -ht
        self.t = 0

# TODO: Create methods
    def solve_time(self):
        t = (-z_velocity + math.sqrt(z_velocity*z_velocity + 2*self.g*self.l_z))/self.g
        self.t = t

    def solve_x_length(self)
        self.l_x = self.x_velocity*self.t

    def run(selfself):
        self.solve_time()
        self.solve_x_length()
        print(self.l_x)

# TODO: Test results

# v_z =
# v_z =
# h =

drop = dropCalc(v_x, v_z, h)
drop.run()