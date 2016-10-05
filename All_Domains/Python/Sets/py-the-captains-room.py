import sys

[K, rooms] = list(sys.stdin)
K = int(K.strip())
rooms = list(map(int, rooms.strip().split(' ')))
print((sum(set(rooms)) * K - sum(rooms)) // (K - 1))
