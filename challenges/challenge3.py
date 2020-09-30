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
        #r12 is the line connecting the centers of the two obstacles
        self.r12_x = obs2.center.x - obs1.center.x
        self.r12_y = obs2.center.y - obs1.center.y
        self.obs1 = obs1
        self.obs2 = obs2

        #values that need to be calculated
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0

        #find the angle between r12 and the line connecting the circles' centers
        # and their tangent points
        def get_angle(r12_x, r12_y, obs1: obstacle, obs2: obstacle):
            r12_magnitude = math.sqrt((r12_x*r12_x) + (r12_y*r12_y))

            radius_difference = 0

            if obs1.radius > obs2.radius:
                radius_difference = obs1.radius - obs2.radius
            elif obs2.radius > obs1.radius:
                radius_difference = obs2.radius - obs1.radius
            else:
                self.radius_difference = 0

            alpha = math.acos(radius_difference/r12_magnitude)
            beta = 90 + (90 - alpha)
            theta = (alpha,beta)

            #theta[0] is the angle that the radius of circle one will rotate
            #theta[1] is the angle that the radius of circle two will rotate
            return theta



        #Takes an angle, a radius, and a vector (r12) and finds the point where
        # a tangent line from another circle will touch
        def tangent_point(r12_x, r12_y, theta, radius, center: point):

            #Find unit vector of r12
             r12_magnitude = math.sqrt((r12_x*r12_x) + (r12_y*r12_y))
             unit_x = r12_x/r12_magnitude
             unit_y = r12_y/r12_magnitude

            #Rotation matrix
             rotated_x = radius*unit_x*math.cos(theta) - radius*unit_y*math.sin(theta)
             rotated_y - radius*unit_x*math.sin(theta) + radius*unit_y*math.cos(theta)

             return rotated_x, rotated_y


        self.theta = get_angle(self.r12_x, self.r12_y, self.obs1, self.obs2)
        self.tangent_point1 = tangent_point(self.r12_x, self.r12_y, self.theta[0], self.obs1.radius, self.obs1.center)
        self.tangent_point2 = tangent_point(self.r12_x, self.r12_y, -1*self.theta[1], self.obs2.radius, self.obs2.center)

        self.start_x = self.tangent_point1[0] + self.obs1.center.x
        self.start_y = self.tangent_point1[1] + self.obs1.center.y
        self.end_x = self.tangent_point2[0] + self.obs2.center.x
        self.end_y = self.tangent_point2[1] + self.obs2.center.y







path1 = #(point1, point2)
path2 = #(point3, point4)
