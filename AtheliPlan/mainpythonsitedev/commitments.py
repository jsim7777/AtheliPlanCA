"""Simple list operations for fixed commitments. Reference example only."""

from .models import new_commitment


def add_commitment(items, title, category, day, start, end):
    item = new_commitment(title, category, day, start, end)
    items.append(item)
    return item


def find_commitment(items, title):
    for item in items:
        if item["title"] == title:
            return item
    return None


def rename_commitment(items, old_title, new_title):
    item = find_commitment(items, old_title)
    if item is not None:
        item["title"] = new_title
    return item


def change_time(items, title, start, end):
    item = find_commitment(items, title)
    if item is not None:
        item["start"] = start
        item["end"] = end
    return item


def move_to_day(items, title, new_day):
    item = find_commitment(items, title)
    if item is not None:
        item["day"] = new_day
    return item


def remove_commitment(items, title):
    for item in items:
        if item["title"] == title:
            items.remove(item)
            return True
    return False


def commitments_on_day(items, day):
    matches = []
    for item in items:
        if item["day"] == day:
            matches.append(item)
    return matches


def commitments_in_category(items, category):
    matches = []
    for item in items:
        if item["category"] == category:
            matches.append(item)
    return matches


def overlaps(first, second):
    if first["day"] != second["day"]:
        return False
    return first["start"] < second["end"] and second["start"] < first["end"]


def conflicting_pairs(items):
    pairs = []
    for index in range(len(items)):
        for other_index in range(index + 1, len(items)):
            first = items[index]
            second = items[other_index]
            if overlaps(first, second):
                pairs.append((first, second))
    return pairs


def sort_by_start(items):
    return sorted(items, key=lambda item: (item["day"], item["start"]))
