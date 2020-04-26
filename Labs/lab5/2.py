def fi(n: int):
    if n in range(1, 3):
        return 1
    if n == 0:
        return 0
    else:
        return fi(n-1) + fi(n-2)


print(fi(3))
