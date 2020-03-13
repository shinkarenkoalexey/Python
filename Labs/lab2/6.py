x = int(input("Введите x..."))
y = int(input("Введите y..."))
if x > 0:
    if y > 0: cht = 1
    else: cht = 4
else:
    if y > 0: cht = 2
    else: cht = 3
print("Координаты принадлежат", cht, "четверти")

