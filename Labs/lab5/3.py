from math import pi
from math import sin
from math import sqrt

def rectangle(a: int, b: int):      # Площадь прямоугольника
    s = a * b
    return s

def circle(r: int):     # Площадь круга
    s = round(pi * r**2, 2)
    return s

def triangle_ah(a: int, h: int):        # Площадь треугольника (основание и высота)
    s = (a * h) / 2
    return s

def triangle_aba(a: int, b: int, angle: int):       # Площадь треугольника (две стороны и угол между ними)
    s = round((a * b * sin(angle*pi/180)) / 2, 2)
    return s

def triangle_abc(a: int, b: int, c: int):       # Площадь треугольника (три стороны)
    p = (a + b + c) / 2
    s = round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)
    return s

def triangle_ab90(a: int, b: int):      # Площадь прямоугольного треугольника
    s = (a * b) / 2
    return s


print(rectangle(5, 6))
print(circle(5))
print(triangle_ah(5, 6))
print(triangle_aba(5, 6, 30))
print(triangle_abc(5, 6, 7))
print(triangle_ab90(5, 6))
