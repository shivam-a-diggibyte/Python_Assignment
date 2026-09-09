from collections import namedtuple

def calculate_average(headers, students):
    Student = namedtuple("Student", headers)

    total_marks = 0

    for student in students:
        record = Student(*student)
        total_marks += int(record.MARKS)

    return total_marks / len(students)