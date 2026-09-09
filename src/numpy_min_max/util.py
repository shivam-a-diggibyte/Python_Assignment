import numpy

def find_max_after_min(array):
    min_values = numpy.min(array, axis=1)
    result = numpy.max(min_values)

    return result