import fun
s = []
for i in range(0, 3):
    x = int(input())
    s.append(x)
print("Максимальное -", fun.max_and_min(s, "max"))
print("Минимальное -", fun.max_and_min(s, "min"))




