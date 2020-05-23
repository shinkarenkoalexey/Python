import re


def match(letter: str, word: str):
    word = re.findall(r"\D", word)
    letter = letter.split(", ")
    c = 0
    for i in letter:
        if i in word:
            c += word.count(i)
    if c == len(word):
        print("Возможно")
    else:
        print("Невозможно")


ll = "е, т, ш, о, д, и, ч, к, а, н, г, м"
w = "методичка"
match(ll, w)

ll = "е, т, ш, о, д, и, ч, к, а, н, г, м"
w = "Программирование"
match(ll, w)
