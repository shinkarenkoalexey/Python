for i in range(1, 10):
    for j in range(1,10):
        print('{} X {} = {:<5}'.format(j, i, i*j), end=" ")
    print(end="\n")