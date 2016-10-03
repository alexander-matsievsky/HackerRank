[N, M] = map(int, input().split(' '))
upper = [('.|.' * (2 * n - 1)).center(M, '-') for n in range(1, N // 2 + 1)]
print('{upper}\n{welcome}\n{lower}'.format(upper='\n'.join(upper), welcome='WELCOME'.center(M, '-'),
                                           lower='\n'.join(reversed(upper))))
