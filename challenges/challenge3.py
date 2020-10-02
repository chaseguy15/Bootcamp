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

    def __str__(self):
        return ("\n(" + str(self.x) + ", " + str(self.y) + ")")

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
        self.o2X = obst2.getCenter().getX()
        self.o2Y = obst2.getCenter().getY()
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
        #debugging stuff
        print("\n The radius of the larger circle is: " + str(self.megaCircleRadius))
        if (self.megaCircleRadius==0):
            print("\nSomething's wrong since radius is 0")

    def calcCenterPoint(self):
        spotX = (self.o2X - self.o1X)/2.0 + self.o1X
        spotY = (self.o2Y - self.o1Y)/2.0 +self.o1Y
        self.megaCircleCenter = point(spotX, spotY)
        print("centerP: " + str(self.megaCircleCenter))

    def calcIntersectionWithObstOne(self):
        self.calcMegaRadius()
        self.calcCenterPoint()
        dBtwn = (self.megaCircleCenter.getX() - self.o1X)**2
        print ("xdbtw: " + str(dBtwn))
        dBtwn = dBtwn + (self.megaCircleCenter.getY() - self.o1Y)**2
        dBtwn = math.sqrt(dBtwn)
        print("Distance betweenis" + str(dBtwn))
        t1a = (self.o1R**2 - self.megaCircleRadius**2 + dBtwn**2)/(2*dBtwn)
        hTP = (self.o1R**2) - (t1a**2)
        print("htp is: " + str(hTP))
        hTP = math.sqrt(hTP)
        tempProp = t1a/dBtwn
        deltaX1 = (self.megaCircleCenter.getX() - self.o1X)*tempProp
        deltaY1 = (self.megaCircleCenter.getY() - self.o1Y)*tempProp
        basePoint = (self.o1X+deltaX1, self.o1Y+deltaY1)
        reciprocalSlope = -deltaX1/deltaY1
        xStep = htp/reciprocalSlope
        yStep = sqrt(xStep**2+htP**2)
        upStepPoint = point(basePoint.getX()+xStep, basePoint.getY()+yStep)
        downStepPoint = point(basePoint.getY()-xStep, basePoint.getY()-yStep)
        self.o1point1 = upStepPoint
        self.o1point2 = downStepPoint

    def calcIntersectionWithObstTwo(self):
        self.calcMegaRadius()
        self.calcCenterPoint()
        dBtwn = (self.megaCircleCenter.getX() - self.o2X)**2 + (self.megaCircleCenter.getY() - self.o2Y)**2
        dBtwn = math.sqrt(dBtwn)
        t1a = (self.o2R**2 - self.megaCircleRadius**2 + dBtwn**2)/(2*dBtwn)
        hTP = (self.o2R**2) - (t1a**2)
        hTP = math.sqrt(hTP)
        tempProp = t1a/dBtwn
        deltaX1 = (self.megaCircleCenter.getX() - self.o2X)*tempProp
        deltaY1 = (self.megaCircleCenter.getY() - self.o2Y)*tempProp
        basePoint = (self.o2X+deltaX1, self.o2Y+deltaY1)
        reciprocalSlope = -deltaX1/deltaY1
        xStep = htp/reciprocalSlope
        yStep = sqrt(xStep**2+htP**2)
        upStepPoint = point(basePoint.getX()+xStep, basePoint.getY()+yStep)
        downStepPoint = point(basePoint.getY()-xStep, basePoint.getY()-yStep)
        self.o2point1 = upStepPoint
        self.o2point2 = downStepPoint

    def returnPoint (self, obstacleNumber: int, desiredPoint: int):
        self.calcIntersectionWithObstOne()
        self.calcIntersectionWithObstTwo()
        if  (obstacleNumber == 1):
            if (desiredPoint == 1):
                status = True
                return self.o1point1
            elif (desiredPoint == 2):
                status = True
                return self.o1point2
        if  (obstacleNumber == 2):
            if (desiredPoint == 1):
                status = True
                return self.o2point1
            elif (desiredPoint == 2):
                status = True
                return self.o2point2



"""
Testing UI

"""
print("\nThis program solves for the tangential between two circles (denoting obstacles).")
input("\nPress Enter to continue\n")
print("\nFirst, the properties of the two circles need to be determined.")
input("\nPress Enter to continue\n")
print("\nInputs are of type float. This UI does not catch wrong inputs")
input("\nPress Enter to continue\n")
print("\nIn other words, you'll have to start over if you don't enter floats")
input("\nPress Enter to continue\n")
circle1Rad = float(input("\n Please enter the radius of circle 1: "))
circle1xCord = float(input("\n Please enter the X cordinate of circle 1:  "))
circle1yCord = float(input("\n Please enter the Y cordinate of circle 1:  "))
pointC1 = point (circle1xCord,circle1yCord)
obstacle1 = obstacle (circle1Rad, pointC1)
circle2Rad = float(input("\n Please enter the radius of circle 2: "))
circle2xCord = float(input("\n Please enter the X cordinate of circle 2:  "))
circle2yCord = float(input("\n Please enter the Y cordinate of circle 2:  "))
pointC2 = point (circle2xCord,circle2yCord)
obstacle2 = obstacle (circle2Rad, pointC2)
pathSolver = solvePath(obstacle1, obstacle2)
closeUI = False
while (closeUI != True):
    print("\nNow there are options. Type STOP when the point prompt is open to stop")
    input("\nPress Enter to continue \n")
    print("\nEnter the the obstacle number and point you would like")
    input("\nPress Enter to continue\n")
    print("\nFor example, if you wanted Obstacle 2's first point:")
    print("\nYou would type '21' without the quotes")
    print("\nIf you want all four points type '00' wihtout the quotes")
    input("\nPress Enter to continue\n")
    userInput = input("Please type the points you want or STOP: ")
    if (userInput == "STOP"):
        closeUI = True
        break
    elif (userInput == "11"):
        print("\nThe point loaded is for Obstacle 1 and the FIRST point")
        print(pathSolver.returnPoint(1,1))
    elif (userInput == "12"):
        print("\nThe point loaded is for Obstacle 1 and the SECOND point")
        print(pathSolver.returnPoint(1,2))
    elif (userInput == "21"):
        print("\nThe point loaded is for Obstacle 2 and the FIRST point")
        print(pathSolver.returnPoint(2,1))
    elif (userInput == "22"):
        print("\nThe point loaded is for Obstacle 2 and the SECOND point")
        print(pathSolver.returnPoint(2,2))
    elif(userInput == "00"):
        print("\nAll points will be loaded")
        print(pathSolver.returnPoint(1,1))
        print(pathSolver.returnPoint(2,2))
        print(pathSolver.returnPoint(2,1))
        print(pathSolver.returnPoint(2,2))
    else:
        print("Hmm. The input could not be processed. Let's try this again")

print("\nYou have reached the end of this program")







#path1 = #(point1, point2)
#path2 = #(point3, point4)
