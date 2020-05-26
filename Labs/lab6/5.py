import re


def kod1(k: str):    # a-i (1-9)
    k = re.findall(r"\d", k)
    for i in k:
        y = int(i) + 64
        print(chr(y), end="")


x = "8514"   # head
kod1(x)

print("\n")


def kod2(k: str):    # a-i (1-9)
    for i in list(k):
        if k.isdigit():
            print(chr(int(i)+96), end="")
        else:
            print("Вы ввели что-то не то")
            break


z = "8514"   # head
kod2(z)

print("\n")

z = "-8564"     # Специально неверный ввод
kod2(z)

