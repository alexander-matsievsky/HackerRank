import sys

import numpy

array = numpy.array([numpy.array(line.split(), float) for line in list(sys.stdin)[1:]])
print(sep='\n', *(numpy.mean(array, axis=1), numpy.var(array, axis=0), numpy.std(array)))
