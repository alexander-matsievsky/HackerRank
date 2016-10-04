import sys

[_, ns, A, B] = list(sys.stdin)
ns = list(map(int, ns.strip().split(' ')))
A = set(map(int, A.strip().split(' ')))
B = set(map(int, B.strip().split(' ')))
print(sum(1 if n in A else (-1 if n in B else 0) for n in ns))
