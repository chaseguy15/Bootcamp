# CHALLENGE 3

import math

"""
Given: 2 obstacles

TODO: Generate 2 outer paths from one obstacle to another as the tuple of the
points the path start/end at.
"""
class point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class obstacle:
    def __init__(self, radius: float, center: point):
        self.radius = radius
        self.center = center

    def getRadius(self):
        return self.radius

    def getCenter(self):
        return self.center

class solvePath:
    def __init__(self, obst1: obstacle, obst2: obstacle):
        #naming convention first letter: obstacle, second letter: number of obstacle, third: specific property
        self.o1R = obst1.getRadius()
        self.o2R= obst2.getRadius()
        self.o1X = obst1.getCenter().getX()
        self.o1Y = obst1.getCenter().getY()
        self.o2Y = obst1.getCenter().getX()
        self.o2Y = obst1.getCenter().getY()
        #not assigned a value at the start
        self.o1point1 = point(0,0)
        self.o1point2 = point(0,0)
        self.o2point1 = point(0,0)
        self.o2point2 = point(0,0)
        #mC stands for megaCircle
        self.megaCircleCenter = point(0,0)
        self.megaCircleRadius = 0

    def calcMegaRadius(self):
        distX = self.o2X - self.o1X
        distY = self.o2Y - self.o1Y
        self.megaCircleRadius = distX**2 + distY**2
        self.megaCircleRadius = math.sqrt(self.megaCircleRadius)
        print("\n The radius of the larger circle is: " + str(self.megaCircleRadius))
        if (self.megaCircleRadius==0):
            print("\nSomething's wrong since radius is 0")

    def calcCenterPoint(self):
        spotX = (self.o2X - self.o1X)/2.0 + self.o1X
        spotY = (self.o2Y - self.o1Y)/2.0 +self.o1Y
        megaCircleCenter = (spotX, spotY)

    def calcIntersectionWithObstOne(self):
        self.calcMegaRadius()
        self.calcCenterPoint()
        dBtwn = self.megaCircleRadius + self.o1R
        t1a = (self.o1R**2 - self.megaCircleRadius**2 + dBtwn**2)/(2*dBtwn)
        hTP = (self.o1R**2) - (tla**2)
        hTP = math.sqrt(hTP)





#path1 = #(point1, point2)
#path2 = #(point3, point4)
