A = int(input("Первое целое"))
B = int(input("Второе целое"))
S = []
x = 0
if A < B:
    for i in range(A, B+1):
        S.append(i)
else:
    for i in range(B, A+1):
        S.insert(x, i)
print(S)