def degree(y, lam):
    return lam(y)


z = lambda x: x ** x
print(degree(3, z))



