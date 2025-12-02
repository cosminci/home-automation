"""Bedroom view configuration"""

from dashboard_helpers import mushroom_switch, mushroom_light, mushroom_climate, mushroom_media_player

def get_view():
    """Return the Bedroom view configuration"""
    return {
        "title": "Bedroom",
        "path": "bedroom",
        "icon": "mdi:bed",
        "type": "sections",
        "sections": [
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    # Lights card
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            {
                                "type": "grid",
                                "columns": 2,
                                "square": False,
                                "cards": [
                                    mushroom_switch("switch.rail_spots", "mdi:track-light"),
                                    mushroom_switch("switch.ceiling_light", "mdi:ceiling-light")
                                ]
                            },
                            mushroom_light("light.led_strip", "Window")
                        ]
                    },
                    # TV
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            mushroom_media_player("media_player.lg_webos_tv_oled48c22lb", "mdi:television")
                        ]
                    }
                ]
            },
            # AC section
            {
                "type": "grid",
                "column_span": 4,
                "cards": [mushroom_climate("climate.ac_bedroom")]
            }
        ]
    }

