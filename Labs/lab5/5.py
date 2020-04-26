bi = int(input("Введите число в двоичной системе счисления.."))
x = 0
dec = 0
for i in range(len(str(bi))):
    dec += (bi % 10)*2**x
    bi = bi // 10
    x += 1
print(dec)
