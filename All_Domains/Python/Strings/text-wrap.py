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


[string, width] = list(sys.stdin)
width = int(width)
print(sep='\n', *[''.join(x) for x in window(string, width)])
