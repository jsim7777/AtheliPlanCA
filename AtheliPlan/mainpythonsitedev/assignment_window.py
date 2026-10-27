"""Python reference for the Assignment dialog in PlannerDialogs.jsx.

The draft is a separate dictionary until Save. No browser or model is called.
"""

from copy import deepcopy
from uuid import uuid4
from .models import new_assignment
from .validation import valid_deadline

FIELDS = ["title", "subject", "deadline", "minutes"]


def open_window(day, existing=None):
    if existing is None:
        draft = new_assignment("", "", day + "T23:00", 45)
    else:
        draft = deepcopy(existing)
    return {
        "draft": draft,
        "editing_id": draft.get("id"),
        "is_open": True,
        "errors": [],
    }


def change_field(window, field, value):
    if window["is_open"] and field in FIELDS:
        window["draft"][field] = value
        window["errors"] = []


def set_completed(window, completed):
    if window["is_open"]:
        window["draft"]["completed"] = bool(completed)


def read_minutes(value):
    text = str(value).strip()
    if not text.isdecimal():
        return None
    minutes = int(text)
    if minutes < 1 or minutes > 10000:
        return None
    return minutes


def validate_fields(draft):
    errors = []
    if not draft["title"].strip():
        errors.append("Enter a title.")
    if len(draft["title"].strip()) > 100:
        errors.append("Keep the title under 101 characters.")
    if len(draft["subject"]) > 50:
        errors.append("Keep the subject under 51 characters.")
    deadline = draft["deadline"]
    if len(deadline) != 16 or "T" not in deadline or not valid_deadline(deadline):
        errors.append("Choose a valid deadline date and time.")
    if read_minutes(draft["minutes"]) is None:
        errors.append("Enter a whole number of minutes from 1 to 10000.")
    return errors


def save_window(window, saved_items):
    if not window["is_open"]:
        return False
    draft = window["draft"]
    window["errors"] = validate_fields(draft)
    if window["errors"]:
        return False
    item = deepcopy(draft)
    item["title"] = item["title"].strip()
    item["subject"] = item["subject"].strip()
    item["minutes"] = read_minutes(item["minutes"])
    if window["editing_id"] is None:
        item["id"] = str(uuid4())
        saved_items.append(item)
    else:
        for index, old in enumerate(saved_items):
            if old.get("id") == window["editing_id"]:
                saved_items[index] = item
                break
        else:
            window["errors"] = ["This assignment no longer exists."]
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
