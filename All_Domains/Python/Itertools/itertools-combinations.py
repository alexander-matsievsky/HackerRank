import itertools

[S, k] = input().strip().split(' ')
[S, k] = [sorted(S), int(k)]
print(sep='\n', *(''.join(c) for i in range(1, k + 1) for c in itertools.combinations(S, i)))
