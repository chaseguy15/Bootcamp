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
    def __init__(self, x_velocity: float, z_velocity: float, height: float):
        self.xV = x_velocity
        self.zV = z_velocity
        self.height = height
        self.time = 0
        self.ACC_DUE_TO_GRAV = 9.81 #constant

    #I'm assuming the object starts at (0,h)
    def calcTime(self):
        # arbitrary test: time = 2.232
        time = math.sqrt(2*self.ACC_DUE_TO_GRAV*self.height + (self.zV**2))
        time = time - self.zV
        time = time/self.ACC_DUE_TO_GRAV
        return time

    def calcXval(self):
        xVal = self.calcTime()*self.xV
        return xVal

    def finalStringOutput(self):
        xCord = str(self.calcXval())
        output = "(" + xCord + ", 0)"
        return output
# TODO: Create methods


# TODO: Test results
getX = float (input("\n What's the X velocity: "))
getZ = float (input("\n What's the magnitude of the Z velocity: "))
getH = float (input("\n What's the height/z-value: "))
firstDropCalc = dropCalc (getX, getZ, getH)
print ("\nThe Final result is " + firstDropCalc.finalStringOutput())
# v_z =
# v_z =
# h =
