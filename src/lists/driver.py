from util import process_command


def main():
    numbers = []
    count = int(input())

    for _ in range(count):
        result = process_command(numbers, input())

        if result is not None:
            print(result)


if __name__ == "__main__":
    main()