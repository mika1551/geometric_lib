import math

def area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

def perimeter(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius
