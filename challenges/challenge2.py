"""
Challenge Two:
- Create a class that calculates the a dropping objects location!

You will be given: x_velocity, z_velocity, height

Note: The object is dropping in the -z direction.
Once you have completed the challenge, please push this to your remote branch.
"""

# TODO: Create dropCalc class
class dropCalc:
    def __init__(self, x_v, z_v, h):
        self.x_v = x_v
        self.z_v = z_v
        self.height = h



    # TODO: Create methods
    def calc_location(self):
        # s = (v+u)*t/2
        # s = h, u = 0
        time = self.calc_time()
        x_dist = time * self.x_v
        return (x_dist, self.height)

    def calc_time(self):
            return 2 * abs(self.height/self.z_v)

# TODO: Test results

v_z = -3
v_x = 2
h = 5

test = dropCalc(v_x, v_z, h)
print(test.calc_location())