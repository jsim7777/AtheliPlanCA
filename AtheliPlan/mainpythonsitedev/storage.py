"""In-memory list helpers. No JSON, file access, or browser storage."""


def empty_planner():
    return {"commitments": [], "assignments": [], "study_blocks": []}


def add_to_planner(planner, item):
    if item["kind"] == "commitment":
        planner["commitments"].append(item)
    elif item["kind"] == "assignment":
        planner["assignments"].append(item)
    elif item["kind"] == "study":
        planner["study_blocks"].append(item)
    return planner


def clear_study_blocks(planner):
    planner["study_blocks"] = []
    return planner


def count_commitments(planner):
    return len(planner["commitments"])


def count_assignments(planner):
    return len(planner["assignments"])


def count_study_blocks(planner):
    return len(planner["study_blocks"])


def all_items(planner):
    items = []
    for item in planner["commitments"]:
        items.append(item)
    for item in planner["assignments"]:
        items.append(item)
    for item in planner["study_blocks"]:
        items.append(item)
    return items


def titles(planner):
    names = []
    for item in all_items(planner):
        names.append(item["title"])
    return names
