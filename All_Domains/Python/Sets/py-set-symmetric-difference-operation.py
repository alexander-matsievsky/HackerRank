import sys

[_, ns, _, bs] = list(sys.stdin)
ns = set(map(int, ns.strip().split(' ')))
bs = set(map(int, bs.strip().split(' ')))
print(len(ns ^ bs))
