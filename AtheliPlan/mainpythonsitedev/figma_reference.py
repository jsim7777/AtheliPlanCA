FIGMA_URL = (
    "https://www.figma.com/design/Abcoh9aPUQfLYu0oMYUr1N/"
    "AthletiPlan-%E2%80%94-Calendar-Replica?node-id=3-53"
    "&t=7IxQuU1gHlZSFmnT-0"
)


def figma_file_id():
    return "Abcoh9aPUQfLYu0oMYUr1N"


def figma_frame_id():
    return "3:53"


def reference_link():
    return FIGMA_URL


def local_component_map():
    """Names of pieces represented in the local planner examples."""
    return {
        "header": "brand and page title",
        "calendar": "day, week, month, and year views",
        "event_card": "fixed commitment on the timeline",
        "study_card": "generated study block",
        "assignment_list": "deadline and completion status",
    }


def reference_note():
    return "Figma link supplied for comparison; local design tokens remain separate."
