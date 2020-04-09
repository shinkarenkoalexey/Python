# Нахождение максимального или минимального
def max_and_min(li: list, word: str):
    li.sort()
    ma = li[-1]
    mi = li[0]
    if word == "max":
        return ma
    elif word == "min":
        return mi

# Малькимальная цифра из числа
def max_figural(number: int):
    lis = []
    number = str(number)
    for i in range(len(number)):
        lis.append(number[i])
    lis.sort()
    return lis[-1]

# Число наоборот
def converse(number: int):
    s = ""
    number = str(number)
    for i in range(len(number)):
        i += 1
        s += number[-i]
    return s

# Среднее арифметическое
def average(li: list):
    n = len(li)
    s = 0
    while n > 0:
        n -= 1
        s += li[n-1]
    return s/len(li)

# Среднее геометрическое
def geo_average(li: list):
    n = len(li)
    s = 1
    while n > 0:
        n -= 1
        s *= li[n-1]**(1/len(li))
    return s
