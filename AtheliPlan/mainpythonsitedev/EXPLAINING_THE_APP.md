# Explaining the app with Python

Use these files as an explanation of the logic. A truthful introduction is:

> The website runs React and JavaScript. These Python reference examples help me explain its form and scheduling logic in a language I understand. Codex assisted with the implementation and these examples.

## Walk through a commitment

Open `commitment_window.py` and follow this sequence:

1. `open_window` creates a draft dictionary. When editing, it copies the saved item so typing cannot change saved data yet.
2. `change_field` stores what the student types. `toggle_repeat_day` adds or removes a weekday from a list.
3. `validate_fields` checks the title, date, and time range. `find_overlaps` compares the new time range with saved commitments.
4. `save_window` stops if the form is invalid. Otherwise it creates an ID and appends the item, or replaces an existing item with the same ID.
5. `cancel_window` discards the draft. Nothing was written to the saved list.

## Walk through an assignment

Open `assignment_window.py`. It follows the same flow, with a deadline and an estimate instead of start/end times. `read_minutes` converts text from the number input into an integer. `set_completed` models the completion checkbox. The Save function validates before updating the list.

## Connect the reference to the running site

| Python idea | Real JavaScript code | What to explain |
| --- | --- | --- |
| `open_window` and its draft | `PlannerDialogs.jsx`: `useState(initial)` | The form has temporary state. |
| `change_field` | `PlannerDialogs.jsx`: `update(field, value)` and input `onChange` | Typing updates the form. |
| `validate_fields` | `PlannerDialogs.jsx`: `submit`; `scheduleStore.js`: `normalizeItem` | Invalid values are rejected before saving. |
| `save_window` | `main.jsx`: `saveItem` and `commitItems` | Saved items are added or replaced by ID. The schedule recalculates. |
| `cancel_window` | Dialog `onClose` | Closing without Save discards the draft. |
| `rules_based_schedule.py` | `scheduleOptimizer.js`: `scheduleTasks` | Fixed events reserve time; unfinished work is placed by deadline. |
| `storage.py` | `scheduleStore.js` and `generatedScheduleStore.js` | Python uses in-memory lists; the website uses browser localStorage. |

The editable JavaScript source is in `../../AtheliPlan-private/src/`. The release at `../package.json` contains the compiled site.

From the AthletiPlan folder, run this short in-memory example:

```python
from python_experiment import assignment_window as form

items = []
window = form.open_window("2026-10-26")
form.change_field(window, "title", "Math review")
form.change_field(window, "minutes", "60")
print(items)                          # Still empty while typing
print(form.save_window(window, items)) # True when valid
print(items[0]["title"])              # Math review
```

Run `python -B -m unittest python_experiment.test_windows` to check the examples. They do not add any example records to the website.

These examples simplify the real app. The commitment overlap check only compares the given date; the website also expands recurring events. The Python scheduler is a one-day teaching example; the website handles multiple days and more edge cases. The Python files do not render HTML, call Ollama, or replace the actual source. Use them to explain logic you can demonstrate, and open the corresponding JavaScript file when discussing what actually runs.

Ask planner now fills missing details and saves valid changes with Undo, without asking follow-up questions. `ollama_context.py` demonstrates simple defaults; the real `requestDefaults.js` also finds a free event slot and reports assumptions. This is separate from manual form entry, which still validates the fields you type.
