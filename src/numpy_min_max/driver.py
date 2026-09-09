import numpy

from src.numpy_min_max.util import find_max_after_min

def main():
    n, m = map(int, input().split())

    array = []

    for _ in range(n):
        row = list(map(int, input().split()))
        array.append(row)

    array = numpy.array(array)

    result = find_max_after_min(array)

    print(result)

if __name__ == "__main__":
    main()