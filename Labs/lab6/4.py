def maxnum(lis: list):
    result = sorted(lis, key=lambda x: lis.count(x))
    return result[-1]


numbers = [1, 4, 4, 5, 6, 7, 10, 10, 1, 11, 4]
print(maxnum(numbers))



