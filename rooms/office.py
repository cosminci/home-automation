"""Office view configuration"""

from dashboard_helpers import mushroom_switch, mushroom_light, mushroom_climate

def get_view():
    """Return the Office view configuration"""
    return {
        "title": "Office",
        "path": "office",
        "icon": "mdi:desk",
        "type": "sections",
        "sections": [
            # Lights section
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            mushroom_switch("switch.ceiling_light_4", "mdi:ceiling-light"),
                            mushroom_light("light.led_strip_window", "Window")
                        ]
                    }
                ]
            },
            # AC section
            {
                "type": "grid",
                "column_span": 4,
                "cards": [mushroom_climate("climate.ac_office")]
            }
        ]
    }

