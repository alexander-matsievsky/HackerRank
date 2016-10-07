import itertools

A = map(int, input().strip().split(' '))
B = map(int, input().strip().split(' '))
print(sep=' ', *sorted(itertools.product(A, B)))
