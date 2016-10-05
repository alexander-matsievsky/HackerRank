for i in range(1, int(input()) + 1):
    print(sum(map(lambda x: 10 ** x, range(0, i))) ** 2)
