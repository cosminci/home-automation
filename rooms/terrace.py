"""Terrace view configuration"""

from dashboard_helpers import mushroom_switch

def get_view():
    """Return the Terrace view configuration"""
    return {
        "title": "Terrace",
        "path": "terrace",
        "icon": "mdi:balcony",
        "type": "sections",
        "sections": [
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    {"type": "custom:stack-in-card", "cards": [mushroom_switch("switch.terrace_lights", "mdi:outdoor-lamp")]}
                ]
            }
        ]
    }

