import calendar


def find_day(mm,dd,yyyy):
    return calendar.day_name[calendar.weekday(yyyy, mm, dd)].upper()