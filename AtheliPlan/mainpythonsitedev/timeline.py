"""Easy-to-read display helpers for a single day's timeline."""


def rows_for_day(day, commitments, study_blocks):
    rows = []
    for item in commitments:
        if item["day"] == day:
            rows.append(item)
    for block in study_blocks:
        if block["day"] == day:
            rows.append(block)
    rows.sort(key=lambda item: item["start"])
    return rows


def first_item(rows):
    if len(rows) == 0:
        return None
    return rows[0]


def last_item(rows):
    if len(rows) == 0:
        return None
    return rows[-1]


def titles_on_timeline(rows):
    titles = []
    for row in rows:
        titles.append(row["title"])
    return titles


def has_practice(rows):
    for row in rows:
        if row.get("category") == "Practice":
            return True
    return False


def count_study_blocks(rows):
    count = 0
    for row in rows:
        if row["kind"] == "study":
            count += 1
    return count


def timeline_is_empty(rows):
    return len(rows) == 0
