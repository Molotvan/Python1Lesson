from array import array
from cmath import sqrt
from tokenize import Double
import math

print("Введите координаты:")

coordinates = input().split(",")


def distance_count(arr):
    x1 = float(arr[0])
    y1 = float(arr[1])
    x2 = float(arr[2])
    y2 = float(arr[3])
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance


print("расстояние между точками: " + str(distance_count(coordinates)))
