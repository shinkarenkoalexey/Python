A = int(input("A..."))
B = int(input("B..."))
s = []
s1 = []
k = 0
x = 0
for i in range(A, B+1):
    x = i
    while x != 0:
        if i % x == 0:
            k += 1
            s1.append(x)
            x -= 1
        else:
            x -= 1
    if k >= 3:
        s.append(i)
    else:
        s1.clear()
    if s:
        print(s, "Количество делителей -", k, s1)
        k = 0
        s.clear()
        s1.clear()
    else:
        k = 0