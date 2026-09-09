def find_average(marks):
    return sum(marks) / len(marks)


def get_student_average(records, student_name):
    marks = records[student_name]
    return find_average(marks)