"""Kitchen view configuration"""

from dashboard_helpers import mushroom_switch, mushroom_light, mushroom_entity

def get_view():
    """Return the Kitchen view configuration"""
    return {
        "title": "Kitchen",
        "path": "kitchen",
        "icon": "mdi:silverware-fork-knife",
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
                                "columns": 3,
                                "square": False,
                                "cards": [
                                    mushroom_switch("switch.led_strip_countertop", "mdi:led-strip"),
                                    mushroom_switch("switch.rail_spots_2", "mdi:track-light"),
                                    mushroom_switch("switch.ceiling_spots", "mdi:spotlight")
                                ]
                            },
                            mushroom_light("light.led_strip_window_3", "Window")
                        ]
                    },
                    # Dishwasher
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            # Program selector (only when NOT running)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.dishwasher_operation_state", "state": "ready"}],
                                "card": {
                                    "type": "custom:mushroom-select-card",
                                    "entity": "select.dishwasher_active_program",
                                    "name": "Start Dishwasher Program",
                                    "icon": "mdi:dishwasher",
                                    "icon_color": "blue",
                                    "secondary_info": "none"
                                }
                            },
                            # Action buttons when running (Stop + Power Off)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.dishwasher_operation_state", "state_not": "inactive"}, {"entity": "sensor.dishwasher_operation_state", "state_not": "ready"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 2,
                                    "square": False,
                                    "cards": [
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "button.dishwasher_stop_program",
                                            "name": " ",
                                            "icon": "mdi:stop",
                                            "icon_color": "red",
                                            "primary_info": "none",
                                            "secondary_info": "none",
                                            "tap_action": {"action": "call-service", "service": "button.press", "service_data": {"entity_id": "button.dishwasher_stop_program"}}
                                        },
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "switch.dishwasher_power",
                                            "name": " ",
                                            "icon": "mdi:power",
                                            "icon_color": "orange",
                                            "primary_info": "none",
                                            "secondary_info": "none",
                                            "tap_action": {"action": "toggle"}
                                        }
                                    ]
                                }
                            },
                            # Program info (when running)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.dishwasher_operation_state", "state_not": "inactive"}, {"entity": "sensor.dishwasher_operation_state", "state_not": "ready"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 2,
                                    "square": False,
                                    "cards": [
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "select.dishwasher_active_program",
                                            "icon": "mdi:dishwasher",
                                            "icon_color": "blue",
                                            "primary_info": "none",
                                            "secondary_info": "state",
                                            "tap_action": {"action": "none"}
                                        },
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "sensor.dishwasher_program_finish_time",
                                            "icon": "mdi:clock-end",
                                            "icon_color": "blue",
                                            "primary_info": "none",
                                            "secondary_info": "state",
                                            "tap_action": {"action": "none"}
                                        }
                                    ]
                                }
                            },
                            # Salt & Rinse Aid warnings (always visible, at bottom)
                            {
                                "type": "grid",
                                "columns": 2,
                                "square": False,
                                "cards": [
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "sensor.dishwasher_salt_nearly_empty",
                                        "name": " ",
                                        "icon": "mdi:shaker",
                                        "primary_info": "none",
                                        "secondary_info": "none",
                                        "tap_action": {"action": "more-info"},
                                        "card_mod": {
                                            "style": "ha-card { --card-mod-icon-color: {% if is_state('sensor.dishwasher_salt_nearly_empty', 'on') %}red{% else %}green{% endif %}; }"
                                        }
                                    },
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "sensor.dishwasher_rinse_aid_nearly_empty",
                                        "name": " ",
                                        "icon": "mdi:spray-bottle",
                                        "primary_info": "none",
                                        "secondary_info": "none",
                                        "tap_action": {"action": "more-info"},
                                        "card_mod": {
                                            "style": "ha-card { --card-mod-icon-color: {% if is_state('sensor.dishwasher_rinse_aid_nearly_empty', 'on') %}red{% else %}green{% endif %}; }"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    # Oven
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            # Program selector (when inactive or ready)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.oven_operation_state", "state": "inactive"}],
                                "card": {
                                    "type": "custom:mushroom-select-card",
                                    "entity": "select.oven_active_program",
                                    "name": "Start Oven Program",
                                    "icon": "mdi:stove",
                                    "icon_color": "orange",
                                    "secondary_info": "none"
                                }
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.oven_operation_state", "state": "ready"}],
                                "card": {
                                    "type": "custom:mushroom-select-card",
                                    "entity": "select.oven_active_program",
                                    "name": "Start Oven Program",
                                    "icon": "mdi:stove",
                                    "icon_color": "orange",
                                    "secondary_info": "none"
                                }
                            },
                            # Action buttons when running (Stop + Power Off)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}, {"entity": "sensor.oven_operation_state", "state_not": "ready"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 2,
                                    "square": False,
                                    "cards": [
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "button.oven_stop_program",
                                            "name": " ",
                                            "icon": "mdi:stop",
                                            "icon_color": "red",
                                            "primary_info": "none",
                                            "secondary_info": "none",
                                            "tap_action": {"action": "call-service", "service": "button.press", "service_data": {"entity_id": "button.oven_stop_program"}}
                                        },
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "switch.oven_power",
                                            "name": " ",
                                            "icon": "mdi:power",
                                            "icon_color": "orange",
                                            "primary_info": "none",
                                            "secondary_info": "none",
                                            "tap_action": {"action": "toggle"}
                                        }
                                    ]
                                }
                            },
                            # Program info (when running)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}, {"entity": "sensor.oven_operation_state", "state_not": "ready"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 2,
                                    "square": False,
                                    "cards": [
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "select.oven_active_program",
                                            "icon": "mdi:stove",
                                            "icon_color": "orange",
                                            "primary_info": "none",
                                            "secondary_info": "state",
                                            "tap_action": {"action": "none"}
                                        },
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "sensor.oven_program_finish_time",
                                            "icon": "mdi:clock-end",
                                            "icon_color": "orange",
                                            "primary_info": "none",
                                            "secondary_info": "state",
                                            "tap_action": {"action": "none"}
                                        }
                                    ]
                                }
                            },
                            # Child lock + Temperature (always visible)
                            {
                                "type": "grid",
                                "columns": 2,
                                "square": False,
                                "cards": [
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "switch.oven_child_lock",
                                        "name": " ",
                                        "icon": "mdi:lock",
                                        "icon_color": "red",
                                        "primary_info": "none",
                                        "secondary_info": "none",
                                        "tap_action": {"action": "toggle"}
                                    },
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "sensor.oven_current_oven_cavity_temperature",
                                        "name": " ",
                                        "icon": "mdi:thermometer",
                                        "icon_color": "orange",
                                        "primary_info": "none",
                                        "secondary_info": "state",
                                        "tap_action": {"action": "more-info"}
                                    }
                                ]
                            }
                        ]
                    },
                    # Cooktop
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            # Power + Child Lock (always visible)
                            {
                                "type": "grid",
                                "columns": 2,
                                "square": False,
                                "cards": [
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "sensor.cooktop_operation_state",
                                        "name": " ",
                                        "icon": "mdi:pot-steam",
                                        "primary_info": "none",
                                        "secondary_info": "none",
                                        "tap_action": {"action": "more-info"},
                                        "card_mod": {
                                            "style": "ha-card { --card-mod-icon-color: {% if is_state('sensor.cooktop_operation_state', 'inactive') %}grey{% else %}orange{% endif %}; }"
                                        }
                                    },
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "switch.cooktop_child_lock",
                                        "name": " ",
                                        "icon": "mdi:lock",
                                        "icon_color": "red",
                                        "primary_info": "none",
                                        "secondary_info": "none",
                                        "tap_action": {"action": "toggle"}
                                    }
                                ]
                            }
                        ]
                    },

                ]
            }
        ]
    }

