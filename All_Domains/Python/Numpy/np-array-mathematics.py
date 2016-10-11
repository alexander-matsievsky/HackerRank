import numpy

[N, M] = numpy.array(input().split(), int)
A = numpy.array([numpy.array(input().split(), int) for _ in range(0, N)])
B = numpy.array([numpy.array(input().split(), int) for _ in range(0, N)])
print(sep='\n', *(A + B, A - B, A * B, A // B, A % B, A ** B))
