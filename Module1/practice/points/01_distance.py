from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    distance = sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
    return(distance)


point1 = Point(5, 4)
point2 = Point(5, 10)

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
