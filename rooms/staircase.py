"""Staircase view configuration"""

from dashboard_helpers import mushroom_switch

def get_view():
    """Return the Staircase view configuration"""
    return {
        "title": "Staircase",
        "path": "staircase",
        "icon": "mdi:stairs",
        "type": "sections",
        "sections": [
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    {"type": "custom:stack-in-card", "cards": [mushroom_switch("switch.staircase_lights", "mdi:ceiling-light-multiple")]}
                ]
            }
        ]
    }

