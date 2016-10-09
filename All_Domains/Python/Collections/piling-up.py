from collections import deque

for _ in range(0, int(input())):
    [_, cubes] = [input(), deque(map(int, input().split()))]
    lengths = [(cubes.popleft() if cubes[0] > cubes[-1] else cubes.pop()) for i in range(0, len(cubes))]
    stackable = all(lengths[i] >= lengths[i + 1] for i in range(0, len(lengths) - 1))
    print('Yes' if stackable else 'No')
