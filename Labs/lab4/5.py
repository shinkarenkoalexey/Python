A = int(input("A..."))
B = int(input("B..."))
s = []
k = 0
x = 0
for i in range(A, B+1):
    x = i
    while x != 0:
        if i % x == 0:
            k += 1
            x -= 1
        else:
            x -= 1
    if k >= 3:
        s.append(i)
    if s:
        print(s, "Количество делителей -", k)
        k = 0
        s.clear()
    else:
        k = 0