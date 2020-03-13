first = int(input("Первое число..."))
second = str(input("Операция..."))
third = int(input("Второе число..."))
if third != 0 and second != "/":
    if second == "+": print(first, second, third, "=", first + third)
    elif second == "-": print(first, second, third, "=", first - third)
    elif second == "*": print(first, second, third, "=", first * third)
    elif second == "/": print(first, second, third, "=", first / third)
    else: print("Неизвестная операция")
else:
    print("Делить на ноль нельзя")


