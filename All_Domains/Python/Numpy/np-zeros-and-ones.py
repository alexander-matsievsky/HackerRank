import numpy

dimensions = numpy.array(input().split(), int)
print(numpy.zeros(tuple(dimensions), dtype=numpy.int))
print(numpy.ones(tuple(dimensions), dtype=numpy.int))
