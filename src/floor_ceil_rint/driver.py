import numpy

from util import calculate_values


def main():
    arr = numpy.array([float(x) for x in input().split(' ')])

    floor_value, ceil_value, rint_value = calculate_values(arr)

    print(floor_value)
    print(ceil_value)
    print(rint_value)


if __name__ == "__main__":
    main()