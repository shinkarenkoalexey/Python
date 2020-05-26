def say(word1):
    x = (lambda z: word1)(word1)
    print(x, end=" ")
    return say


say("Hello")("World")

