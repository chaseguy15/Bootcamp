# CHALLENGE 3

"""
Given: 2 obstacles

TODO: Generate 2 outer paths from one obstacle to another as the tuple of the
points the path start/end at.
"""
class point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class obstacle:
    def __init__(self, radius: float, center: point):
        self.radius = radius
        self.center = center

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

def findPaths(first_obstacle: obstacle, second_obstacle: obstacle):
    # Outer point on the first circle
    internal_radius = max(first_obstacle.radius, second_obstacle.radius) - \
                     min(first_obstacle.radius, second_obstacle.radius)
    larger = max(first_obstacle, second_obstacle)
    smaller = min(first_obstacle, second_obstacle)
    internal = obstacle(internal_radius, larger.center)

    middle_radius = (((first_obstacle.center.x - second_obstacle.center.x)**2 +
                    (first_obstacle.center.y - second_obstacle.center.y)**2) ** 0.5 ) / 2
    middle_center = point(first_obstacle.center.x - second_obstacle.center.x,
                          first_obstacle.center.y - second_obstacle.center.y)

    middle = obstacle(middle_radius, middle_center)

    intersections =  find_intersect(internal, middle)

    if intersections is not None:

        # first point
        first_projection = project_line(intersections[0], larger)
        first_path = find_path(first_projection, smaller, larger)

        second_projection = project_line(intersections[1], larger)
        second_path = find_path(second_projection, smaller, larger)

        return first_path, second_path
    return None




# uses triangles created by the intersection of both circles to find the points
def find_intersect(circle_one: obstacle, circle_two: obstacle):
    d = ((circle_two.center.x - circle_one.center.x)**2 -
         (circle_two.center.y - circle_one.center.y)**2) ** 0.5

    if circle_one.radius + circle_two.radius > d > abs(circle_one.radius - circle_two.radius):
        long_leg = (circle_one.radius**2 - circle_two.radius ** 2) / (2*d)
        intersecting_chord = (circle_one.radius**2 - long_leg**2) ** 0.5

        temp_point = point(circle_one.center.x + long_leg*(circle_two.center.x-circle_one.center.x)/d,
                          circle_one.center.y + long_leg*(circle_two.center.y-circle_one.center.y)/d)

        point_one = point(temp_point.x + intersecting_chord * (circle_two.center.y - circle_one.center.y) / d,
                          temp_point.y - intersecting_chord * (circle_two.center.x - circle_one.center.x) / d)
        point_two = point(temp_point.x - intersecting_chord * (circle_two.center.y - circle_one.center.y) / d,
                          temp_point.y + intersecting_chord * (circle_two.center.x - circle_one.center.x) / d)

        return point_one, point_two
    else:
        return None

# projects the line out to the larger circle to find the point the tangent meets
def project_line(first: point, second: obstacle):
    center = second.center
    slope = (center.y - first.x) / (center.x - first.x)
    first_intersect_x = center.x + ((second.radius ** 2) / (slope ** 2 + 1))

    first_intersect=  point(first_intersect_x, (second.radius**2 - (first_intersect_x - center.x)**2) ** 0.5 - center.y)

    second_intersect_x = center.x + ((second.radius ** 2) / (slope ** 2 + 1))

    second_intersect = point(second_intersect_x, (second.radius ** 2 - (second_intersect_x - center.x) ** 2) ** 0.5 - center.y)

    return slope, (first_intersect, second_intersect)

def find_path(projected, smaller: obstacle, larger: obstacle):
    first_point = projected[1][0]
    second_point = projected[1][1]
    slope = projected[0]
    closest = point()
    # finding distance between points
    first_dist = ((first_point.x - smaller.center.x) ** 2 + (first_point.y - smaller.center.y) ** 2) ** 0.5
    second_dist = ((second_point.x - smaller.center.x) ** 2 + (second_point.y - smaller.center.y) ** 2) ** 0.5

    if first_dist > second_dist:
        closest = second_point
    else:
        closest = first_point

    slope = - 1 / slope


    y_val = (slope * (smaller.center.x - closest.x + slope * smaller.center.y) + closest.y)/(slope**2 + 1)
    x_val = ((y_val - closest.y) / m) + closest.x

    found_point = point(x_val, y_val)

    return closest, found_point

obstacle1 = obstacle(3.0, point(1.0,1.0))
obstacle2 = obstacle(5, point(3.0,9.0))

paths = findPaths(obstacle1, obstacle2)

path1 = paths[0]
path2 = paths[1]
