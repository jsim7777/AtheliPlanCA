"""Small form checks written as direct yes/no questions."""

from datetime import date, datetime


def has_title(title):
    return len(title.strip()) > 0


def title_is_short_enough(title):
    return len(title) <= 100


def valid_day(day):
    try:
        date.fromisoformat(day)
        return True
    except ValueError:
        return False


def valid_deadline(deadline):
    try:
        datetime.fromisoformat(deadline)
        return True
    except ValueError:
        return False


def valid_time(time):
    try:
        hour, minute = time.split(":")
        return 0 <= int(hour) <= 23 and 0 <= int(minute) <= 59
    except ValueError:
        return False


def end_follows_start(start, end):
    if not valid_time(start) or not valid_time(end):
        return False
    return end > start


def positive_estimate(minutes):
    return isinstance(minutes, int) and minutes > 0


def commitment_is_valid(item):
    if not has_title(item["title"]):
        return False
    if not title_is_short_enough(item["title"]):
        return False
    if not valid_day(item["day"]):
        return False
    return end_follows_start(item["start"], item["end"])


def assignment_is_valid(item):
    if not has_title(item["title"]):
        return False
    if not valid_deadline(item["deadline"]):
        return False
    return positive_estimate(item["minutes"])
