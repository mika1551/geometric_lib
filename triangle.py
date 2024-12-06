import math

def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Side lengths cannot be negative.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    
    # Геронова формула для площади треугольника
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Side lengths cannot be negative.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    
    return a + b + c
