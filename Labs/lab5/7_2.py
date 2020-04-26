import p7_1
import math
def disc(a: float, b: float, c: float):
    x1 = 0
    x2 = 0
    d = p7_1.subtraction(p7_1.multiplication(b, b), p7_1.multiplication(4, p7_1.multiplication(a, c)))
    if d < 0:
        print("Нет корней")
    elif d > 0:
        x1 = p7_1.division(p7_1.plus(-b, math.sqrt(d)), p7_1.multiplication(2, a))
        x2 = p7_1.division(p7_1.subtraction(-b, math.sqrt(d)), p7_1.multiplication(2, a))
        print(x1, x2)
    elif d == 0:
        x1 = p7_1.division(p7_1.plus(-b, math.sqrt(d)), p7_1.multiplication(2, a))
        print(x1)


disc(1, 6, 8)






