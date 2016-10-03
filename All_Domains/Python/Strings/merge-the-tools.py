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


def ordered_set(iterable):
    data_set = set()
    ordered_set = []
    for x in iterable:
        if x not in data_set:
            data_set.add(x)
            ordered_set.append(x)
    return ordered_set


[S, K] = list(sys.stdin)
S = S.strip()
K = int(K)
print(sep='\n', *[''.join(ordered_set(chunk)) for chunk in window(S, K)])
