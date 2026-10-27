"""Python reference for the Commitment dialog in PlannerDialogs.jsx.

This models form behavior in memory. It does not draw or run the website.
"""

from copy import deepcopy
from uuid import uuid4
from .models import new_commitment
from .validation import valid_day, valid_time

CATEGORIES = ["School", "Practice", "Competition", "Meal", "Commute", "Other"]
WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
FIELDS = ["title", "category", "day", "start", "end"]


def open_window(day, existing=None):
    if existing is None:
        draft = new_commitment("", "Practice", day, "16:00", "17:00")
        draft["repeat_days"] = []
    else:
        draft = deepcopy(existing)
    return {
        "draft": draft,
        "editing_id": draft.get("id"),
        "is_open": True,
        "errors": [],
        "warnings": [],
    }


def change_field(window, field, value):
    if window["is_open"] and field in FIELDS:
        window["draft"][field] = value
        window["errors"] = []


def toggle_repeat_day(window, day):
    if not window["is_open"] or day not in WEEKDAYS:
        return
    days = window["draft"].setdefault("repeat_days", [])
    if day in days:
        days.remove(day)
    else:
        days.append(day)


def validate_fields(draft):
    errors = []
    if not draft["title"].strip():
        errors.append("Enter a title.")
    if len(draft["title"].strip()) > 100:
        errors.append("Keep the title under 101 characters.")
    if draft["category"] not in CATEGORIES:
        errors.append("Choose a commitment type.")
    if not valid_day(draft["day"]):
        errors.append("Choose a valid date.")
    if not valid_time(draft["start"]) or not valid_time(draft["end"]):
        errors.append("Use valid start and end times.")
    elif minutes(draft["end"]) <= minutes(draft["start"]):
        errors.append("End time must be after start time.")
    return errors


def minutes(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


def find_overlaps(draft, saved_items):
    warnings = []
    for item in saved_items:
        if draft.get("id") and item.get("id") == draft["id"]:
            continue
        if item.get("kind") != "commitment" or item["day"] != draft["day"]:
            continue
        if minutes(draft["start"]) < minutes(item["end"]):
            if minutes(item["start"]) < minutes(draft["end"]):
                warnings.append("Overlaps " + item["title"])
    return warnings


def save_window(window, saved_items):
    if not window["is_open"]:
        return False
    draft = window["draft"]
    window["errors"] = validate_fields(draft)
    if window["errors"]:
        return False
    window["warnings"] = find_overlaps(draft, saved_items)
    item = deepcopy(draft)
    item["title"] = item["title"].strip()
    if window["editing_id"] is None:
        item["id"] = str(uuid4())
        saved_items.append(item)
    else:
        for index, old in enumerate(saved_items):
            if old.get("id") == window["editing_id"]:
                saved_items[index] = item
                break
        else:
            window["errors"] = ["This commitment no longer exists."]
            return False
    window["is_open"] = False
    return True


def cancel_window(window):
    window["draft"] = None
    window["is_open"] = False


def delete_item(window, saved_items):
    if window["editing_id"] is None:
        return False
    for item in saved_items:
        if item.get("id") == window["editing_id"]:
            saved_items.remove(item)
            window["is_open"] = False
            return True
    return False
