n = int(input("n..."))
x = 0
y = 0
F = 1
for i in range(2, n+1):
    x = y
    y = F
    F = x + y
print(F)