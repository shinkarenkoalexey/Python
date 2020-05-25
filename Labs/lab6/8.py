def find(lis1: list, lis2: list):
    result = list(set(lis1) & set(lis2))
    result.sort()
    return result


a = [11, 9, 4, 3, 6, 5]
b = [4, 9, 5, 1, 2, 10]
print(find(a, b))
