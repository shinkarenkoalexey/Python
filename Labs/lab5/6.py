import random


def tree(f: int, h: int):
    s = "\\"
    s1 = "/"
    for i in range(0, h):
        if f == 0:
            print(" "*(i+1) + s + " "*(2*(h-i)-1) + s1)
        if f == 1:
            x = random.randint(1, 4)
            if x <= 3:
                print(" " * (i + 1) + s + " " * (2 * (h - i) - 1) + s1)
            else:
                y = random.randint(0, 1)
                if y == 0:
                    print(" " * (i + 1) + s + s1 + " " * (2 * (h - i) - 2) + s1)
                if y == 1:
                    print(" " * (i + 1) + s + " " * (2 * (h - i) - 2) + s + s1)
        if f == 2:
            x = random.randint(1, 4)
            if x <= 2:
                print(" "*(i+1) + s + " "*(2*(h-i)-1) + s1)
            else:
                y = random.randint(0, 1)
                if y == 0:
                    print(" "*(i+1) + s + s1 + " "*(2*(h-i)-2) + s1)
                if y == 1:
                    print(" "*(i+1) + s + " "*(2*(h-i)-2) + s + s1)
        if f == 3:
            x = random.randint(1, 4)
            if x == 1:
                print(" " * (i + 1) + s + " " * (2 * (h - i) - 1) + s1)
            else:
                y = random.randint(0, 1)
                if y == 0:
                    print(" " * (i + 1) + s + s1 + " " * (2 * (h - i) - 2) + s1)
                if y == 1:
                    print(" " * (i + 1) + s + " " * (2 * (h - i) - 2) + s + s1)
    print(" "*(h+1) + "|")


"""
f = Ветвистость (0, 1, 2, 3)
h = Высота
tree(f,h)
"""

tree(2, 10)
