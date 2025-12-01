"""Living Room view configuration"""

from dashboard_helpers import mushroom_switch, mushroom_light, mushroom_climate, network_button

def get_view():
    """Return the Living Room view configuration"""
    return {
        "title": "Living Room",
        "path": "living_room",
        "icon": "mdi:sofa",
        "type": "sections",
        "sections": [
            # Lights & Network section
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
                                "columns": 3,
                                "square": False,
                                "cards": [
                                    mushroom_switch("switch.dining_light", "mdi:ceiling-light"),
                                    mushroom_switch("switch.ceiling_light_3", "mdi:ceiling-fan-light"),
                                    mushroom_switch("light.ceiling_spots", "mdi:spotlight")
                                ]
                            },
                            mushroom_light("light.led_strip_window_2", "Window")
                        ]
                    },
                    # Network card (AP Living)
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "sensor.ap_living_state",
                                "icon": "mdi:access-point",
                                "icon_color": "none",
                                "primary_info": "none",
                                "secondary_info": "none",
                                "card_mod": {
                                    "style": "ha-card { --card-mod-icon-color: {% if is_state('sensor.ap_living_state', 'Connected') or is_state('sensor.ap_living_state', 'connected') %}green{% else %}red{% endif %}; }"
                                }
                            },
                            {
                                "type": "grid",
                                "columns": 3,
                                "square": False,
                                "cards": [
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "sensor.ap_living_uptime",
                                        "icon": "mdi:clock-outline",
                                        "primary_info": "none",
                                        "secondary_info": "none"
                                    },
                                    network_button("button.ap_living_restart", "mdi:restart"),
                                    network_button("button.switch_port_13_power_cycle", "mdi:power-plug-off")
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
                "cards": [mushroom_climate("climate.ac_living")]
            },
            # Entertainment section
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    {
                        "type": "entities",
                        "title": "📺 Entertainment",
                        "show_header_toggle": False,
                        "entities": [
                            {"type": "section", "label": "TV"},
                            {"entity": "media_player.77_oled", "name": "77\" OLED"},
                            {"type": "section", "label": "Soundbar"},
                            {"entity": "media_player.soundbar_q990b", "name": "Power & Volume"},
                            {"entity": "input_select.soundbar_source", "name": "Source"}
                        ]
                    }
                ]
            },
            # Camera section
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    {
                        "type": "picture-entity",
                        "entity": "camera.camera_living_medium_resolution_channel",
                        "camera_image": "camera.camera_living_medium_resolution_channel",
                        "show_name": True,
                        "show_state": False,
                        "name": "📹 Living Room Camera"
                    }
                ]
            }
        ]
    }

