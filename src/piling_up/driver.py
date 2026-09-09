from src.piling_up.util import can_stack

def main():
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        blocks = list(map(int, input().split()))

        print(can_stack(blocks))

if __name__ == "__main__":
    main()