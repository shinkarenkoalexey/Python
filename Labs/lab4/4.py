A = int(input("A..."))
B = int(input("B..."))
s = []
x = 0
for i in range(B, A + 1):
    if i % 2 == 1:
        s.insert(x, i)
        i += 1
print(s)