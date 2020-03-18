n = int(input())
s = []
x = 1
if 9 >= n > 0:
    for i in range(1, n+1):
        while i > 0:
            s.append(x)
            i -= 1
        print(s)
        s.clear()
else: print("Введите другое число")