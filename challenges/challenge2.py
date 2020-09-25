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
    def __init__(self,v_x,v_z,h):
        self.v_x = v_x
        self.v_z = v_z
        self.h = h

        self.x = 0
        self.g = -9.81
        self.t = 0

        def final_time(h,v_z,g):
            t_f1 = (-1*v_z + math.sqrt(v_z ** 2 -4*(g/2)*h))/g
            t_f2 = (-1*v_z - math.sqrt((v_z) ** 2 -2*g*h))/g

            if t_f1>0:
                return t_f1
            else:
                return t_f2

        def x_f(v_x,t_f):
            x_f = v_x*t_f
            return x_f

        self.t = final_time(self.h, self.v_z, self.g)
        self.x = x_f(self.v_x, self.t)

# TODO: Create methods


# TODO: Test results

v_x = 4
v_z = 3
h = 10

drop = dropCalc(v_x, v_z, h)
print(f"The final x position of the object is {drop.x}")
