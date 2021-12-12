from datetime import date
from datetime import datetime


def pixel_parse_to_date(value: str, reset_weekday=False):
    year, week, weekday = value.split("_")
    if reset_weekday:
        weekday = 1
    else:
        weekday = str(int(weekday) % 7)
    return datetime.strptime(f"{year}-{week}-{weekday}", "%Y-%W-%w").date()


def pixel_parse_to_identifier(value: date):
    return value.isocalendar()
