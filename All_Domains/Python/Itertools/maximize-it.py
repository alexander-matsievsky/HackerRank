import itertools
import sys


def f(x):
    return x ** 2


def s(xs, m):
    return sum(map(f, xs)) % m


[K, M] = list(map(int, sys.stdin.readline().strip().split(' ')))
ns = [[int(x) for x in n.strip().split(' ')[1:]] for n in sys.stdin]
print(max(s(xs, M) for xs in itertools.product(*ns)))
