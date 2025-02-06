import math

# Write your functions for each part in the space below.

# Part 1
def first_element(lst:list[list[int]]) -> list[int]:
    full_list = [sublist for sublist in lst if sublist]
    return [sublist[0] for sublist in full_list]

# unit test 1
biglist = [[2,3],[5,7,6],[8,3,6],[5],[9,2,4,7,9,0]]
smalllist = first_element(biglist)
print(smalllist)

# unit test 2
mediumlist = [[], [4,5,6,7,8,9], [9], [8,7,6,5]]
small_list = first_element(mediumlist)
print(small_list)

#####################################################################################################
# Part 2
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def x_coordinates(lst:list[Point]) -> list[float]:
    return [point.x for point in lst]

# unit test 1
p1 = Point(2.3,4.5)
p2 = Point(6.7,8.9)
points_list = [p1, p2]
x_list = x_coordinates(points_list)
print(x_list)

# unit test 2
p3 = Point(8.2,9.1)
p4 = Point(3.6,7.4)
p5 = Point(6.2, 4.9)
points_list2 = [p3,p4,p5]
x_list2 = x_coordinates(points_list2)
print(x_list2)
#####################################################################################################
# Part 3
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def are_in_positive_quadrant(lst:list[Point]) -> list[float]:
    return[point.x for point in lst if point.x > 0]

# unit test 1
point1 = Point(4.5,8.9)
point2 = Point(-2.3,9.0)
point3 = Point(7.8,-3.5)
pointList = [point1, point2, point3]
positive = are_in_positive_quadrant(pointList)
print(positive)

# unit test 2
point4 = Point(-4.5,8.9)
point5 = Point(-2.3,9.0)
pointList2 = [point4, point5]
positives = are_in_positive_quadrant(pointList2)
print(positives)
#####################################################################################################
# Part 4
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def distance(x: int, y: int) -> float:
    return math.sqrt(x**2 + y**2)

# unit test1
distance1 = distance(9,2)
distance2 = distance(6.5,7.2)
print(distance1)
print(distance2)

# unit test2
distance3 = distance(-5,2)
distance4 = distance(4.5,-9)
print(distance3)
print(distance4)
#####################################################################################################
# Part 5
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def manhattan_distance(x1: int, x2: int, y1: int, y2: int) -> [float]:
    return abs(x2 - x1) + abs(y2 - y1)

# unit test 1
distance5 = manhattan_distance(1,2,3,4)
print(distance5)

# unit test 2
distance6 = manhattan_distance(5.5,7.2,4.8,9.1)
print(distance6)
#####################################################################################################
# Part 6
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def distance_all(lst:list[Point]) -> list[float]:
    return [distance(point.x, point.y) for point in lst]

# unit test 1
distance7 = [Point(8.8, 3.6), Point(3, 4)]
distances = distance_all(distance7)
print(distances)

# unit test 2
distance8 = [Point(6.3, 2.7), Point(7,4)]
distances2 = distance_all(distance8)
print(distances2)

