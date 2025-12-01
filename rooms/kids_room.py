"""Kid's Room view configuration"""

from dashboard_helpers import mushroom_switch, mushroom_light, mushroom_climate, network_button

def get_view():
    """Return the Kid's Room view configuration"""
    return {
        "title": "Kid's Room",
        "path": "kid_room",
        "icon": "mdi:teddy-bear",
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
                            {
                                "type": "grid",
                                "columns": 3,
                                "square": False,
                                "cards": [
                                    mushroom_switch("switch.rail_spots_3", "mdi:track-light"),
                                    mushroom_switch("switch.ceiling_light_2", "mdi:ceiling-light"),
                                    mushroom_switch("switch.light_2", "mdi:wall-sconce")
                                ]
                            },
                            mushroom_light("light.led_strip_window_4", "Window"),
                            mushroom_light("light.led_strip_bed", "Bed")
                        ]
                    }
                ]
            },
            # Network section
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "sensor.ap_iacopewee_state",
                                "icon": "mdi:access-point",
                                "icon_color": "none",
                                "primary_info": "none",
                                "secondary_info": "none",
                                "card_mod": {
                                    "style": "ha-card { --card-mod-icon-color: {% if is_state('sensor.ap_iacopewee_state', 'Connected') or is_state('sensor.ap_iacopewee_state', 'connected') %}green{% else %}red{% endif %}; }"
                                }
                            },
                            {
                                "type": "grid",
                                "columns": 3,
                                "square": False,
                                "cards": [
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "sensor.ap_iacopewee_uptime",
                                        "icon": "mdi:clock-outline",
                                        "primary_info": "none",
                                        "secondary_info": "none"
                                    },
                                    network_button("button.ap_iacopewee_restart", "mdi:restart"),
                                    network_button("button.switch_port_14_power_cycle", "mdi:power-plug-off")
                                ]
                            }
                        ]
                    }
                ]
            },
            # AC section
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    {"type": "custom:stack-in-card", "cards": [mushroom_climate("climate.ac_iacopewee")]}
                ]
            }
        ]
    }

