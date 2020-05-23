import re


def kod(k: str):
    k = re.findall(r"\d", k)
    for i in k:
        y = int(i) + 64
        print(chr(y), end="")


x = "8514"
kod(x)

