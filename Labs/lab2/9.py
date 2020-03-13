from math import sqrt
x = int(input("Введите x..."))
y = int(input("Введите y..."))
r = int(input("Введите радиус..."))
dis = round(sqrt(x**2+y**2), 2)
if dis > r:
    print("Точка (", x, ",", y, ") не принадлежит кругу")
elif dis < r:
    print("Точка (", x, ",", y, ") принадлежит кругу")
else:
    print("Точка (", x, ",", y, ") лежит на границе круга")
