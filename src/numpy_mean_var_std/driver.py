import numpy

from src.numpy_mean_var_std.util import calculate_values

def main():
    n, m = map(int, input().split())

    array = []

    for _ in range(n):
        row = list(map(int, input().split()))
        array.append(row)

    array = numpy.array(array)

    mean, var, std = calculate_values(array)

    print(mean)
    print(var)
    print(std)

if __name__ == "__main__":
    main()