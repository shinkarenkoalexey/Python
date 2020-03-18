x = input("Введите число ")
lis = []
sum = 0
proz = 1
for i in range(len(str(x))):
    x = str(x)
    sum += int(x[i])
    proz *= int(x[i])
print("Сумма =",sum)
print("Произведение =",proz)
