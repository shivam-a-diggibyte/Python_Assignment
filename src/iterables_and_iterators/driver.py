from src.iterables_and_iterators.util import calculate_probability

def main():
    n = int(input())
    letters = input().split()
    k = int(input())

    result = calculate_probability(letters, k)

    print(f"{result:.3f}")


if __name__ == "__main__":
    main()