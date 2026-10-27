"""Plain dictionaries used by the Python experiment.

The running website has its own data model inside package.json.
"""


def new_commitment(title, category, day, start, end):
    return {
        "kind": "commitment",
        "title": title,
        "category": category,
        "day": day,
        "start": start,
        "end": end,
    }


def new_assignment(title, subject, deadline, minutes):
    return {
        "kind": "assignment",
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "minutes": minutes,
        "completed": False,
    }


def new_study_block(title, day, start, end):
    return {
        "kind": "study",
        "title": title,
        "day": day,
        "start": start,
        "end": end,
    }


def is_commitment(item):
    return item.get("kind") == "commitment"


def is_assignment(item):
    return item.get("kind") == "assignment"


def is_study_block(item):
    return item.get("kind") == "study"


def label(item):
    if is_commitment(item):
        return item["category"] + ": " + item["title"]
    if is_assignment(item):
        return item["subject"] + ": " + item["title"]
    return "Study: " + item["title"]
