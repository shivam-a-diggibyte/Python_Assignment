from util import calculate_happiness

def main():
    n, m = map(int, input().split())

    array = list(map(int, input().split()))
    liked = set(map(int, input().split()))
    disliked = set(map(int, input().split()))

    result = calculate_happiness(array, liked, disliked)

    print(result)


if __name__ == "__main__":
    main()
