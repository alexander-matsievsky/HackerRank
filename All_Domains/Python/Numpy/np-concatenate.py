import numpy

[N, M, P] = list(map(int, input().split()))
ns = [numpy.array(input().split(), int) for _ in range(0, N)]
ms = [numpy.array(input().split(), int) for _ in range(0, M)]
print(numpy.concatenate((ns, ms)))
