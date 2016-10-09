from collections import deque

d = deque()
for _ in range(0, int(input())):
    [operation, *args] = input().split()
    args = list(map(int, args))
    {
        'append': lambda: d.append(args[0]),
        'appendleft': lambda: d.appendleft(args[0]),
        'pop': lambda: d.pop(),
        'popleft': lambda: d.popleft()
    }.get(operation)()
print(sep=' ', *d)
