from util import get_student_average


def main():
    records = {}

    student_count = int(input())

    for _ in range(student_count):
        data = input().split()

        name = data[0]
        marks = list(map(float, data[1:]))
        records[name] = marks

    student_name = input().strip()
    average = get_student_average(records, student_name)
    print(f"{average:.2f}")


if __name__ == "__main__":
    main()