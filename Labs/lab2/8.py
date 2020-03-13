t = str(input("Введите температуру в формате (Градусы C/F)..."))
if t[-1] == "C" or t[-1] == "С":
    tt = round(int(t[:-1])*1.8+32, 2)
    print(t[:-1], "C =", tt, "F")
elif t[-1] == "F":
    tt = round((int(t[:-1])-32)/1.8, 2)
    print(t[:-1], "F =", tt, "C")
else:
    print("Вы ввели что-то не то")

