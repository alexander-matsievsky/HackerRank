T = int(input())
for _ in range(0, T):
    try:
        [a, b] = list(map(int, input().split()))
        print(a // b)
    except Exception as e:
        print('Error Code: {}'.format(e))
