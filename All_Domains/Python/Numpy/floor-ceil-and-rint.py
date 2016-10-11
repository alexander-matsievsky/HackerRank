import numpy

A = numpy.array(input().split(), float)
print(sep='\n', *(numpy.floor(A), numpy.ceil(A), numpy.rint(A)))
