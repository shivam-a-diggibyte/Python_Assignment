from datetime import datetime

def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"

    time1 = datetime.strptime(t1, format_string)
    time2 = datetime.strptime(t2, format_string)

    difference = abs(time1 - time2)

    return str(int(difference.total_seconds()))