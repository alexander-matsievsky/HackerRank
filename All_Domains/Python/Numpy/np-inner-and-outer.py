import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(sep='\n', *(numpy.inner(A, B), numpy.outer(A, B)))
