from util import find_day

def main():
    mm,dd,yyyy = map(int, input().split())

    result = find_day(mm,dd,yyyy)

    print(result)

if __name__ == "__main__":
    main()