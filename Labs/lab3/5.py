x = int(input("Введите целое число"))
lis = []
for i in range(len(str(x))):
    x = str(x)
    lis.append(x[i])
lis.sort()
print(lis[-1])

