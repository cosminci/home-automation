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
                                "entity": "media_player.hub_77_oled",
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
                        "type": "grid",
                        "columns": 3,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "binary_sensor.slzb_mr4u_ethernet",
                                "icon": "mdi:zigbee",
                                "icon_color": "none",
                                "primary_info": "none",
                                "secondary_info": "none",
                                "card_mod": {
                                    "style": "ha-card { --card-mod-icon-color: {% if is_state('binary_sensor.slzb_mr4u_ethernet', 'on') %}green{% else %}red{% endif %}; }"
                                }
                            },
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "button.slzb_mr4u_zigbee_restart",
                                "icon": "mdi:restart",
                                "icon_color": "red",
                                "primary_info": "none",
                                "secondary_info": "none",
                                "tap_action": {"action": "toggle"},
                                "card_mod": {
                                    "style": """
                                        ha-card::after {
                                            content: '';
                                            position: absolute;
                                            top: 6px;
                                            right: 6px;
                                            width: 14px;
                                            height: 14px;
                                            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23888888' d='M4.93,4.93C3.12,6.74 2,9.24 2,12C2,14.76 3.12,17.26 4.93,19.07L6.34,17.66C4.89,16.22 4,14.22 4,12C4,9.79 4.89,7.78 6.34,6.34L4.93,4.93M19.07,4.93L17.66,6.34C19.11,7.78 20,9.79 20,12C20,14.22 19.11,16.22 17.66,17.66L19.07,19.07C20.88,17.26 22,14.76 22,12C22,9.24 20.88,6.74 19.07,4.93M7.76,7.76C6.67,8.85 6,10.35 6,12C6,13.65 6.67,15.15 7.76,16.24L9.17,14.83C8.45,14.11 8,13.11 8,12C8,10.89 8.45,9.89 9.17,9.17L7.76,7.76M16.24,7.76L14.83,9.17C15.55,9.89 16,10.89 16,12C16,13.11 15.55,14.11 14.83,14.83L16.24,16.24C17.33,15.15 18,13.65 18,12C18,10.35 17.33,8.85 16.24,7.76M12,10A2,2 0 0,0 10,12A2,2 0 0,0 12,14A2,2 0 0,0 14,12A2,2 0 0,0 12,10Z'/%3E%3C/svg%3E");
                                            background-size: contain;
                                        }
                                    """
                                }
                            },
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "button.slzb_mr4u_core_restart",
                                "icon": "mdi:restart",
                                "icon_color": "red",
                                "primary_info": "none",
                                "secondary_info": "none",
                                "tap_action": {"action": "toggle"},
                                "card_mod": {
                                    "style": """
                                        ha-card::after {
                                            content: '';
                                            position: absolute;
                                            top: 6px;
                                            right: 6px;
                                            width: 14px;
                                            height: 14px;
                                            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23888888' d='M9,3V5H7A2,2 0 0,0 5,7V9H3V11H5V13H3V15H5V17A2,2 0 0,0 7,19H9V21H11V19H13V21H15V19H17A2,2 0 0,0 19,17V15H21V13H19V11H21V9H19V7A2,2 0 0,0 17,5H15V3H13V5H11V3H9M7,9H10V12H7V9M14,9H17V12H14V9M7,14H10V17H7V14M14,14H17V17H14V14Z'/%3E%3C/svg%3E");
                                            background-size: contain;
                                        }
                                    """
                                }
                            }
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
