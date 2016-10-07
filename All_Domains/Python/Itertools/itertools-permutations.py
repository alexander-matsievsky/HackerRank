import itertools

[S, k] = input().strip().split(' ')
[S, k] = [sorted(S), int(k)]
print(sep='\n', *(''.join(p) for p in itertools.permutations(S, k)))
