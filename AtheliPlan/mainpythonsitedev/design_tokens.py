"""A readable sketch of the planner's colors and spacing.

These values were written locally; no Figma import is claimed.
"""

INK = "#202622"
MUTED = "#5e6860"
GREEN = "#28644b"
LIME = "#e5f0e9"
BORDER = "#dfe4df"
WHITE = "#ffffff"
BACKGROUND = "#fafbf9"


def page_background():
    return BACKGROUND


def main_text_color():
    return INK


def quiet_text_color():
    return MUTED


def action_color():
    return GREEN


def highlight_color():
    return LIME


def border_color():
    return BORDER


def category_color(category):
    if category == "Practice":
        return "#6e9680"
    if category == "Competition":
        return "#6e9680"
    if category == "Meal":
        return "#9fac9f"
    if category == "Commute":
        return "#aeb7a5"
    return GREEN


def assignment_color(status):
    if status == "Overdue":
        return "#b86645"
    if status == "Completed":
        return "#79936e"
    return "#8f773f"


def study_block_color():
    return "#6686ae"


def spacing_size(name):
    if name == "tiny":
        return 4
    if name == "small":
        return 8
    if name == "medium":
        return 16
    if name == "large":
        return 24
    return 32


def card_radius():
    return 6


def font_stack():
    return "Arial, system-ui, sans-serif"
