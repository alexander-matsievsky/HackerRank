from itertools import groupby, combinations

[_, ns, K] = [input(), input().strip().split(' '), int(input())]
groups = [(with_a, len(list(g))) for with_a, g in groupby(combinations(ns, K), lambda c: 'a' in c)]
print(
    sum(count for (with_a, count) in groups if with_a) /
    sum(count for (_, count) in groups)
)
