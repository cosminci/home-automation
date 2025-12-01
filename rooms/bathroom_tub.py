"""Bathroom - Tub view configuration"""

from dashboard_helpers import mushroom_switch

def get_view():
    """Return the Bathroom - Tub view configuration"""
    return {
        "title": "Bathroom - Tub",
        "path": "bathroom_tub",
        "icon": "mdi:bathtub",
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
                                    mushroom_switch("switch.led_strip", "mdi:led-strip"),
                                    mushroom_switch("switch.ceiling_spots_2", "mdi:spotlight"),
                                    mushroom_switch("switch.ventilator_2", "mdi:fan", "blue")
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

