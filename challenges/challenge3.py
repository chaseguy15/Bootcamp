# CHALLENGE 3

"""
Given: 2 obstacles

TODO: Generate 2 outer paths from one obstacle to another as the tuple of the
points the path start/end at.
"""

import math

class point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class obstacle:
    def __init__(self, radius: float, center: point):
        self.radius = radius
        self.center = center

class getPath:
    def __init__(self, obs1: obstacle, obs2: obstacle)
        self.r12_x = obs2.center.x - obs1.center.x
        self.r12_y = obs2.center.y - obs1.center.y

        self.r12_magnitude = math.sqrt((self.r12_x*self.r12_x) + (self.r12_y*self.r12_y))

        #imagine third circle inside of larger circle with r3 = r1 - r2
        self.radius_difference = 0

        if obs1.radius > obs2.radius:
            self.radius_difference = obs1.radius - obs2.radius
        elif obs2.radius > obs1.radius:
            self.radius_difference = obs2.radius - obs1.radius
        else:
            self.radius_difference = 0

        #find angle between the line connecting the center of the circles
        #and the line connecting the center of the circles to their tangent points

        self.theta = math.acos(self.radius_difference/self.r12_magnitude)

        self.r12_unit = 




path1 = #(point1, point2)
path2 = #(point3, point4)
