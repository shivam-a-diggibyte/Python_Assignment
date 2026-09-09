import numpy

from util import find_determinant

def main():
    n = int(input())

    matrix = []

    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)

    matrix = numpy.array(matrix)

    result = find_determinant(matrix)

    print(round(result, 2))

if __name__ == "__main__":
    main()