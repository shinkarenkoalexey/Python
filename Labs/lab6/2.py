def say(word: str):
    print(word, end=" ")
    return say


say("Hello")("World")




