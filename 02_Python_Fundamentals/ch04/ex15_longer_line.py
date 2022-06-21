'''
You will be given the coordinates of four points. The first and the second pair of points form two different lines.
Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point which is closer to the center of the coordinate system (0, 0).
You can reuse the method that you wrote for the previous problem. If the lines are of equal length, print only the first one.
The resulting coordinates must be formatted to the lower integer.
'''

from math import sqrt
def distance_to_center(x):
    return sqrt(abs(x[0])**2 + abs(x[1])**2)

def distance_btw_points(x, y):
    x_axis = abs(x[0] - y[0])
    y_axis = abs(x[1] - y[1])
    return sqrt(x_axis**2 + y_axis**2)

def format(num):
    return num * 100 // 100

points_dict = {}
for i in range(1, 2 + 1):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    points_dict[i] = (x1, y1), (x2, y2)

lines_dict = {}
for i in range(1, 2 + 1):
    lines_dict[i] = distance_btw_points(points_dict[i][0], points_dict[i][1])
longest_line = max(lines_dict, key=lines_dict.get)

key = points_dict[longest_line]
distance_one = distance_to_center(key[0])
distance_two = distance_to_center(key[1])
if distance_one <= distance_two:
    print(f'({format(key[0][0]):.0f}, {format(key[0][1]):.0f})', end='')
    print(f'({format(key[1][0]):.0f}, {format(key[1][1]):.0f})')
else:
    print(f'({format(key[1][0]):.0f}, {format(key[1][1]):.0f})', end='')
    print(f'({format(key[0][0]):.0f}, {format(key[0][1]):.0f})')
