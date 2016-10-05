import sys

[A, _, *ns] = list(sys.stdin)
A = set(A.strip().split(' '))
ns = [set(n.strip().split(' ')) for n in ns]
print(all(n & A == n and len(n) < len(A) for n in ns))
