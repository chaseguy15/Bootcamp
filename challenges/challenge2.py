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
        self.zVu = z_velocity #intial z_velocity
        self.zVf = 0 #final velocity
        self.height = height
        self.time = 0
        self.ACC_DUE_TO_GRAV = 9.81 #constant
        self.x = 0
        self.y = 0
        self.z = 0

    #I'm assuming the object starts at (0,h)
    def calcTime(self):
        # arbitrary test: time = 2.232
        self.zVf = -math.sqrt(2*self.ACC_DUE_TO_GRAV*self.height + (self.zVu**2))
        print("\nFinal Velocity is " + str(self.zVf))
        time = abs(self.zVf - self.zVu)
        time = time/self.ACC_DUE_TO_GRAV
        return time

    def calcXval(self):
        xVal = self.calcTime()*self.xV
        self.x = xVal
        return xVal

    def finalStringOutput(self):
        xCord = str(self.calcXval())
        output = "(" + str(self.x) + ", " + str(self.y) + ", " +str(self.z) + ")"
        return output
# TODO: Create methods


# TODO: Test results
getX = float (input("\n What's the X velocity: "))
getZ = float (input("\n What's the Z velocity: "))
getH = float (input("\n What's the height/z-value: "))
firstDropCalc = dropCalc (getX, getZ, getH)
print ("\nThe Final result is " + firstDropCalc.finalStringOutput())
# v_z =
# v_z =
# h =
