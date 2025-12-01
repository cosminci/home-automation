"""Hallway view configuration (includes Storage/Network devices)"""

from dashboard_helpers import mushroom_switch, network_button, network_device_status

def get_view():
    """Return the Hallway view configuration"""
    return {
        "title": "Hallway",
        "path": "hallway",
        "icon": "mdi:door-open",
        "type": "sections",
        "sections": [
            # Lights section
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    {"type": "custom:stack-in-card", "cards": [mushroom_switch("switch.ceiling_spots_4", "mdi:spotlight")]}
                ]
            },
            # Network devices section
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    # Gateway
                    {
                        "type": "custom:stack-in-card",
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
                            {
                                "type": "grid",
                                "columns": 3,
                                "square": False,
                                "cards": [
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
                            }
                        ]
                    },
                    # Switch
                    {
                        "type": "custom:stack-in-card",
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
                                "type": "grid",
                                "columns": 2,
                                "square": False,
                                "cards": [
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "sensor.switch_uptime",
                                        "icon": "mdi:clock-outline",
                                        "primary_info": "none",
                                        "secondary_info": "none"
                                    },
                                    network_button("button.switch_restart", "mdi:restart")
                                ]
                            }
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
                        "entity": "camera.camera_hallway_medium_resolution_channel",
                        "camera_image": "camera.camera_hallway_medium_resolution_channel",
                        "show_name": True,
                        "show_state": False,
                        "name": "📹 Hallway Camera"
                    }
                ]
            }
        ]
    }

