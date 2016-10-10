[N, M] = list(map(int, input().split()))
ms = [input().split() for _ in range(0, N)]
K = int(input())
print(sep='\n', *[' '.join(m) for m in sorted(ms, key=lambda m: int(m[K]))])
