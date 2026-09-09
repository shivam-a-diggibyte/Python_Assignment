import numpy

numpy.set_printoptions(legacy='1.13')

def calculate_values(arr):
    floor_value = numpy.floor(arr)
    ceil_value = numpy.ceil(arr)
    rint_value = numpy.rint(arr)

    return floor_value, ceil_value, rint_value