import sys

import numpy

array = numpy.array([numpy.array(xs.split(), int) for xs in list(sys.stdin)[1:]])
print(numpy.transpose(array))
print(array.flatten())
