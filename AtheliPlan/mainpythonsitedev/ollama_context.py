"""Simple reference for the planner's single local model; no model call."""


# The working website chooses its model on the server, not in the interface.
FIXED_MODEL = "qwen3.5:2b-q4_K_M"


def connection_label(connected):
    if connected:
        return "Ollama connected"
    return "Ollama offline"


def planner_request(messages):
    return {"model": FIXED_MODEL, "messages": messages}


def test_study_defaults(subject, day):
    return {
        "title": subject + " test prep",
        "deadline": day + "T09:00",
        "minutes": 120,
    }



def commitments_for_day(commitments, day):
    selected = []
    for item in commitments:
        if item["day"] == day:
            selected.append(item)
    return selected


def unfinished_assignments(assignments):
    selected = []
    for item in assignments:
        if not item["completed"]:
            selected.append(item)
    return selected


def assignments_due_after(assignments, day):
    selected = []
    for item in unfinished_assignments(assignments):
        if item["deadline"][:10] >= day:
            selected.append(item)
    return selected


def titles_of(items):
    titles = []
    for item in items:
        titles.append(item["title"])
    return titles


def context_for_request(day, commitments, assignments):
    return {
        "selected_day": day,
        "commitment_titles": titles_of(commitments_for_day(commitments, day)),
        "assignment_titles": titles_of(assignments_due_after(assignments, day)),
    }


def fill_missing_practice_times(item):
    # Teaching example for an empty calendar; JavaScript also finds free time.
    result = item.copy()
    if not result.get("start"):
        result["start"] = "16:00"
    if not result.get("end"):
        hour, minute = result["start"].split(":")
        result["end"] = f"{int(hour) + 1:02d}:{minute}"
    return result



def explanation_fact(block):
    return block["title"] + " is planned on " + block["day"]


def divide_study_minutes(step_titles, total_minutes):
    # The model suggests titles; normal code keeps the total estimate exact.
    if not step_titles:
        return []
    each = total_minutes // len(step_titles)
    extra = total_minutes % len(step_titles)
    steps = []
    for index, title in enumerate(step_titles):
        minutes = each
        if index < extra:
            minutes += 1
        steps.append({"title": title, "minutes": minutes})
    return steps
