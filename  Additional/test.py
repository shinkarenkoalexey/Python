import random
b = [str(i**random.randint(1, 5)) for i in range(random.randint(10, 20))]
res = sorted(b, key=len)
res1 = res.split(key=len)
print(res)