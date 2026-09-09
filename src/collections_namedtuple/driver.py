from util import calculate_average

def main():
    n = int(input())
    headers = input().split()

    students = []

    for _ in range(n):
        students.append(input().split())

    average = calculate_average(headers, students)

    print(f"{average:.2f}")

if __name__ == "__main__":
    main()