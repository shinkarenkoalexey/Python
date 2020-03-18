s = int(input("Номер символа..."))
h = int(input("Высота..."))
s = chr(s)
s2 = "||"
x = 0
for j in range(0, h+1):
    if j != h:
        while j > 0:
            j -= 1
        if x != h:
            print('{:>25}||{}'.format(s*x, s*x), end='')
            print(end='\n')
            x += 1
    else: print('{:25}||{}'.format(s*0, s*0), end='')