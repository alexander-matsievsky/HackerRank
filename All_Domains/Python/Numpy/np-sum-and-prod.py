import sys

import numpy

array = numpy.array([numpy.array(line.split(), float) for line in list(sys.stdin)[1:]])
print(numpy.product(numpy.sum(array, axis=0), dtype=int))
