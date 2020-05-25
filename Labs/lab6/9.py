import random
from itertools import groupby
s = []
for i in range(1, random.randint(5, 20)):
    sec = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for j in range(random.randint(1, 5)))
    s.append(sec)
print(s)
result = [list(s1[1]) for s1 in groupby(sorted(s, key=len), len)]
print(result)
