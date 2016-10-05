import sys


def window(iterable, n):
    window = []
    for x in iterable:
        if len(window) >= n:
            yield window
            window = []
        window.append(x)
    if len(window) > 0:
        yield window


[_, A, _, *operations] = list(sys.stdin)
A = set(map(int, A.strip().split(' ')))
operations = [(op.strip().split(' ')[0], set(map(int, B.strip().split(' ')))) for [op, B] in window(operations, 2)]
for (operation, B) in operations:
    if operation == 'update':
        A |= B
    elif operation == 'intersection_update':
        A &= B
    elif operation == 'difference_update':
        A -= B
    elif operation == 'symmetric_difference_update':
        A ^= B
print(sum(A))
