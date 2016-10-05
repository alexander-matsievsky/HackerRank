for i in range(1, int(input())):
    print(sum(map(lambda x: 10 ** x, range(0, i))) * i)
