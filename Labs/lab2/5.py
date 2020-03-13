first = int(input("Делимое..."))
second = int(input("Делитель..."))
if second != 0:
    if first % second == 0:
        print("Делится без остатка")
        print("Частное -", int(first / second))
    else:
        print("Делится с остатком")
        print("Частное -", int(first / second))
        print("Остаток - ", first % second)
else:
    print("На ноль делить нельзя, ты что не знал?")
    print("Ответьте этой тупой машине:")
    input()
    print("ERROR")

