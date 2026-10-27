"""Straightforward assignment actions. Reference example only."""

from datetime import datetime
from .models import new_assignment


def add_assignment(items, title, subject, deadline, minutes):
    item = new_assignment(title, subject, deadline, minutes)
    items.append(item)
    return item


def find_assignment(items, title):
    for item in items:
        if item["title"] == title:
            return item
    return None


def rename_assignment(items, old_title, new_title):
    item = find_assignment(items, old_title)
    if item is not None:
        item["title"] = new_title
    return item


def change_deadline(items, title, new_deadline):
    item = find_assignment(items, title)
    if item is not None:
        item["deadline"] = new_deadline
    return item


def change_estimate(items, title, new_minutes):
    item = find_assignment(items, title)
    if item is not None:
        item["minutes"] = new_minutes
    return item


def mark_complete(items, title):
    item = find_assignment(items, title)
    if item is not None:
        item["completed"] = True
    return item


def mark_unfinished(items, title):
    item = find_assignment(items, title)
    if item is not None:
        item["completed"] = False
    return item


def remove_assignment(items, title):
    item = find_assignment(items, title)
    if item is None:
        return False
    items.remove(item)
    return True


def status(item, now):
    if item["completed"]:
        return "Completed"
    if datetime.fromisoformat(item["deadline"]) < now:
        return "Overdue"
    return "Upcoming"


def unfinished_by_deadline(items):
    unfinished = []
    for item in items:
        if not item["completed"]:
            unfinished.append(item)
    return sorted(unfinished, key=lambda item: item["deadline"])


def assignments_for_subject(items, subject):
    matches = []
    for item in items:
        if item["subject"] == subject:
            matches.append(item)
    return matches


def minutes_left(items):
    total = 0
    for item in items:
        if not item["completed"]:
            total += item["minutes"]
    return total
