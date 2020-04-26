import math
import fun
dec = int(input("Введите число в десятиричной системе счисления.."))
bi = ""
i = math.log(dec, 2)
if dec == 2 ** i:
    i += 1
while i > 0:
    x = dec % 2
    bi += str(x)
    dec //= 2
    i -= 1
print(fun.converse(bi))     # моя функция, находится в Function - fun.py (Число наоборот)


