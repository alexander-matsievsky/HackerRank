import itertools

[S, k] = input().strip().split(' ')
[S, k] = [sorted(S), int(k)]
print(sep='\n', *(''.join(c) for c in itertools.combinations_with_replacement(S, k)))
