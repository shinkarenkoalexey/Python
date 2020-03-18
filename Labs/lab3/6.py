import random
x = random.randint(1, 10)
xx = 0
y = int(input("Введите количество попыток - "))
f = "False"
while y > 0:
    y -= 1
    print("Попробуйте угадать: ")
    chislo = int(input())
    if chislo == x:
        print("Вы угадали")
        f = "True"
        break
    else:
        print("Не угадали")
        if chislo > x:
            print("Загаданное число меньше вашего")
        if chislo < x:
            print("Загаданное число больше вашего")

if f == "False":
    print("Рандомное число -", x)