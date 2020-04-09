A = int(input("A..."))
B = int(input("B..."))

s = [i for i in range(B, A+1)]
x = 1
while s[-1] % 2 == 1 and x > 0:
    for i in s[::-2]:
        print(i, end=" ")
    x = 0
while s[-1] % 2 == 0 and x > 0:
    s.remove(A)
    for i in s[::-2]:
        print(i, end=" ")
    x = 0
