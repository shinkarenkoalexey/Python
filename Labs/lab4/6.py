s = int(input("Номер символа..."))
h = int(input("Высота..."))
s = chr(s)
s1 = " "
d = h
x = 0
for j in range(0, h+1):
    if j != h:
        while j > 0:
            j -= 1
        if x != h:
            print('{}{}||{}{}'.format(s1*d, s*x, s*x, s1*d), end='')
            print(end='\n')
            x += 1
            d -= 1
    else: print('{}{}||{}{}'.format(s1*h, s*0, s*0, s1*h), end='')

