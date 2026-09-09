from util import find_runner_up

def main():
    count = int(input())
    scores = list(map(int, input().split()))

    runner_up = find_runner_up(scores)

    print(runner_up)


if __name__ == "__main__":
    main()