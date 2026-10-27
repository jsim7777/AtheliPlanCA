"""Small date helpers for explaining day, week, month, and year views."""

from calendar import monthrange
from datetime import date, timedelta


def next_day(day):
    return day + timedelta(days=1)


def previous_day(day):
    return day - timedelta(days=1)


def next_week(day):
    return day + timedelta(days=7)


def previous_week(day):
    return day - timedelta(days=7)


def sunday_of_week(day):
    days_since_sunday = (day.weekday() + 1) % 7
    return day - timedelta(days=days_since_sunday)


def days_in_week(day):
    days = []
    sunday = sunday_of_week(day)
    for offset in range(7):
        days.append(sunday + timedelta(days=offset))
    return days


def days_in_month(day):
    days = []
    count = monthrange(day.year, day.month)[1]
    for number in range(1, count + 1):
        days.append(date(day.year, day.month, number))
    return days


def months_in_year(day):
    months = []
    for number in range(1, 13):
        months.append(date(day.year, number, 1))
    return months


def dates_in_view(day, view):
    if view == "Day":
        return [day]
    if view == "Week":
        return days_in_week(day)
    if view == "Month":
        return days_in_month(day)
    if view == "Year":
        return months_in_year(day)
    return []


def format_heading(day, view):
    if view == "Day":
        return day.strftime("%A, %B %d")
    if view == "Year":
        return str(day.year)
    return day.strftime("%B %Y")


def is_today(day, today):
    return day == today
