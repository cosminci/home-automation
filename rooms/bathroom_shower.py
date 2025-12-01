"""Bathroom - Shower view configuration"""

from dashboard_helpers import mushroom_switch

def get_view():
    """Return the Bathroom - Shower view configuration"""
    return {
        "title": "Bathroom - Shower",
        "path": "bathroom_shower",
        "icon": "mdi:shower-head",
        "type": "sections",
        "sections": [
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            {
                                "type": "grid",
                                "columns": 3,
                                "square": False,
                                "cards": [
                                    mushroom_switch("switch.led_strip_2", "mdi:led-strip"),
                                    mushroom_switch("switch.ceiling_spots_3", "mdi:spotlight"),
                                    mushroom_switch("switch.ventilator", "mdi:fan", "blue")
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

