import sys

import numpy

array = numpy.array([numpy.array(line.split(), int) for line in list(sys.stdin)])
print(numpy.max(numpy.min(array, axis=1)))
