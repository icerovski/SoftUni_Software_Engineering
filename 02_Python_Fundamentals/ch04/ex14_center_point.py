'''
You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines.
Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
If the points are at the same distance from the center, print only the first one. The resulting coordinates must be formatted to the lower integer.
'''

from math import sqrt
def distance_to_center(x, y):
    return sqrt(abs(x)**2 + abs(y)**2)

def format(num):
    return num * 100 // 100


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point_one = distance_to_center(x1, y1)
point_two = distance_to_center(x2, y2)

# points = []
if point_one <= point_two:
    print(f'({format(x1):.0f}, {format(y1):.0f})')
else:
    print(f'({format(x2):.0f}, {format(y2):.0f})')
