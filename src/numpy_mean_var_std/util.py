import numpy

def calculate_values(array):
    mean = numpy.mean(array, axis=1)
    var = numpy.var(array, axis=0)
    std = numpy.std(array)

    return mean, var, std