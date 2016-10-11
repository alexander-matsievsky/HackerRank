import numpy

N = int(input())
A = numpy.array([numpy.array(input().split(), int) for _ in range(0, N)])
B = numpy.array([numpy.array(input().split(), int) for _ in range(0, N)])
print(numpy.dot(A, B))
