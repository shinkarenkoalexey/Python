s = ""
x = input("Число = ")
for i in range(len(str(x))):
    i += 1
    s += x[-i]
print(s)
