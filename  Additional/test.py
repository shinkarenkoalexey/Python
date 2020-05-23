import random
def zzz(h):
    left = ["\\", ""]
    right = ["/", ""]
    for i in range(0, h-1):
        x = random.choice(left)
        y = random.choice(right)
        if x == "" and y == "":
            print(" "*(i+1) + "\\" + " "*(2*(h-i)-1) + "/")
        elif x == "\\" and y == "":
            print(" " * (i + 1) + "\\" + " " * (2 * (h - i) - 2) + x + "/")
        elif x == "" and y == "/":
            print(" " * (i+1) + "\\" + y + " " * (2 * (h - i) - 2) + "/")
        elif x == "\\" and y == "/":
            print(" " * (i + 1) + "\\" + y + " " * (2 * (h - i) - 3) + x + "/")
    print(" " * h + "\\ /")
    print(" " * (h+1) + "|")


zzz(10)

