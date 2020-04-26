def converse(number: str):
    s = ""
    for i in range(len(number)):
        i += 1
        s += number[-i]
    return s
