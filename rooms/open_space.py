from dashboard_helpers import (mushroom_switch, mushroom_light, mushroom_climate, network_button)


def get_view():
    return {
        "title": "Open Space",
        "path": "tab_open_space",
        "icon": "mdi:sofa",
        "cards": [
            # Living Room
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 4,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:sofa",
                                "icon_color": "blue",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.dining_light", "mdi:ceiling-light"),
                            mushroom_switch("switch.ceiling_light_3", "mdi:ceiling-fan-light"),
                            mushroom_switch("light.ceiling_spots", "mdi:spotlight")
                        ]
                    },
                    mushroom_light("light.led_strip_window_2"),
                    mushroom_climate("climate.ac_living"),
                    {
                        "type": "grid",
                        "columns": 2,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-media-player-card",
                                "entity": "media_player.77_oled",
                                "icon": "mdi:television",
                                "use_media_info": False,
                                "show_volume_level": False,
                                "volume_controls": ["volume_buttons"],
                                "collapsible_controls": True,
                                "primary_info": "none",
                                "secondary_info": "none"
                            },
                            {
                                "type": "custom:mushroom-media-player-card",
                                "entity": "media_player.soundbar_q990b",
                                "icon": "mdi:speaker",
                                "use_media_info": False,
                                "show_volume_level": False,
                                "volume_controls": ["volume_buttons"],
                                "collapsible_controls": True,
                                "primary_info": "none",
                                "secondary_info": "none"
                            }
                        ]
                    },
                    {
                        "type": "grid",
                        "columns": 4,
                        "square": False,
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
                                "type": "custom:mushroom-entity-card",
                                "entity": "sensor.ap_living_uptime",
                                "icon": "mdi:clock-outline",
                                "primary_info": "none",
                                "secondary_info": "none"
                            },
                            network_button("button.ap_living_restart", "mdi:restart"),
                            network_button("button.switch_port_13_power_cycle", "mdi:power-plug-off")
                        ]
                    },
                    {
                        "type": "picture-entity",
                        "entity": "camera.camera_living_medium_resolution_channel",
                        "camera_image": "camera.camera_living_medium_resolution_channel",
                        "show_name": True,
                        "show_state": False,
                        "name": "📹 Living Room Camera"
                    }
                ]
            },
            # Kitchen
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 4,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:silverware-fork-knife",
                                "icon_color": "blue",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.led_strip_countertop", "mdi:led-strip"),
                            mushroom_switch("switch.rail_spots_2", "mdi:track-light"),
                            mushroom_switch("switch.ceiling_spots", "mdi:spotlight")
                        ]
                    },
                    mushroom_light("light.led_strip_window_3")
                ]
            },
            # Hallway
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 2,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:door",
                                "icon_color": "blue",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.ceiling_spots_4", "mdi:spotlight")
                        ]
                    },
                    {
                        "type": "grid",
                        "columns": 4,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "sensor.cloud_gateway_max_state",
                                "icon": "mdi:router-wireless",
                                "icon_color": "none",
                                "primary_info": "none",
                                "secondary_info": "none",
                                "card_mod": {
                                    "style": "ha-card { --card-mod-icon-color: {% if is_state('sensor.cloud_gateway_max_state', 'Connected') or is_state('sensor.cloud_gateway_max_state', 'connected') %}green{% else %}red{% endif %}; }"
                                }
                            },
                            mushroom_switch("switch.unifi_network_vpn", "mdi:vpn", "green"),
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "sensor.cloud_gateway_max_uptime",
                                "icon": "mdi:clock-outline",
                                "primary_info": "none",
                                "secondary_info": "none"
                            },
                            network_button("button.cloud_gateway_max_restart", "mdi:restart")
                        ]
                    },
                    {
                        "type": "grid",
                        "columns": 3,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "sensor.switch_state",
                                "icon": "mdi:switch",
                                "icon_color": "none",
                                "primary_info": "none",
                                "secondary_info": "none",
                                "card_mod": {
                                    "style": "ha-card { --card-mod-icon-color: {% if is_state('sensor.switch_state', 'Connected') or is_state('sensor.switch_state', 'connected') %}green{% else %}red{% endif %}; }"
                                }
                            },
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "sensor.switch_uptime",
                                "icon": "mdi:clock-outline",
                                "primary_info": "none",
                                "secondary_info": "none"
                            },
                            network_button("button.switch_restart", "mdi:restart")
                        ]
                    },
                    {
                        "type": "picture-entity",
                        "entity": "camera.camera_hallway_medium_resolution_channel",
                        "camera_image": "camera.camera_hallway_medium_resolution_channel",
                        "show_name": True,
                        "show_state": False,
                        "name": "📹 Hallway Camera"
                    }
                ]
            },
            # Staircase
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 2,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:stairs",
                                "icon_color": "blue",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.staircase_lights", "mdi:ceiling-light-multiple")
                        ]
                    }
                ]
            },
            # Terrace
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 2,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:flower",
                                "icon_color": "blue",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.terrace_lights", "mdi:outdoor-lamp")
                        ]
                    }
                ]
            }
        ]
    }
