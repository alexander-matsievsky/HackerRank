from collections import defaultdict

[n, m] = list(map(int, input().strip().split(' ')))
[A, B] = [[input().strip() for _ in range(0, n)], [input().strip() for _ in range(0, m)]]
d = defaultdict(list)
for a, i in zip(A, range(1, len(A) + 1)):
    d[a].append(i)
print(sep='\n', *[' '.join(map(str, d[b] or [-1])) for b in B])
