import sys

import numpy

A = numpy.array([numpy.array(line.split(), float) for line in list(sys.stdin)[1:]])
print(numpy.linalg.det(A))
