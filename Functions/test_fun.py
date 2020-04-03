import fun
s = []
for i in range(0, 3):
    x = int(input("Введите число "))
    s.append(x)
print("Максимальное -", fun.max_and_min(s, "max"))
print("Минимальное -", fun.max_and_min(s, "min"))
conv = int(input("Введите число "))
print("Ваше число наоборот -", fun.converse(conv))
print("Наибольшая цифра в числе -", fun.max_figural(conv))




