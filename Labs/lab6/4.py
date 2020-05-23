def maxnum(lis: list):
    count = []

    for i in lis:
        count.append(i)
        count.append(lis.count(i))
        x = lis.count(i)
        for j in range(0, x-1):
            lis.remove(i)

    m = count.index(max(count[1::2])) - 1
    print("Число", count[m], "в вашем списке в количестве - ", max(count[1::2]), "шт.")


numbers = [1, 4, 4, 5, 6, 7, 10, 10, 1, 11, 4]
maxnum(numbers)



