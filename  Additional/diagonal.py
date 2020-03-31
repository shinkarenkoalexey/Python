n = int(input("Размер..."))
x = 0
z = 1
y = n
e = 2
for i in range(1, n + 1):
    while y != 0:
        y -= 1
        z += x
        x += 1
        print(z, end="")
    y = n
    z = 0
    x = 2
    print(end="\n")
