"""Kitchen view configuration"""

from dashboard_helpers import mushroom_switch, mushroom_light

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
                    # Dishwasher (compact appliance card)
                    {
                        "type": "grid",
                        "title": "🍽️ Dishwasher",
                        "columns": 1,
                        "cards": [
                            mushroom_switch("sensor.dishwasher_operation_state", "mdi:dishwasher", "blue"),
                            mushroom_switch("switch.dishwasher_power", "mdi:power", "green"),
                            mushroom_switch("sensor.dishwasher_salt_nearly_empty", "mdi:shaker", "orange"),
                            mushroom_switch("sensor.dishwasher_rinse_aid_nearly_empty", "mdi:spray-bottle", "orange"),
                            {
                                "type": "entities",
                                "show_header_toggle": False,
                                "entities": [
                                    {"type": "conditional", "conditions": [{"entity": "sensor.dishwasher_operation_state", "state_not": "inactive"}], "row": {"entity": "select.dishwasher_active_program", "name": "Active Program", "icon": "mdi:play"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.dishwasher_operation_state", "state_not": "inactive"}], "row": {"entity": "sensor.dishwasher_program_finish_time", "name": "Finish Time", "icon": "mdi:clock-outline"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.dishwasher_operation_state", "state_not": "inactive"}], "row": {"entity": "button.dishwasher_stop_program", "name": "Stop Program", "icon": "mdi:stop"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.dishwasher_operation_state", "state": "inactive"}], "row": {"entity": "select.dishwasher_selected_program", "name": "Select Program", "icon": "mdi:playlist-play"}}
                                ]
                            }
                        ],
                        "grid_options": {"columns": 12}
                    },
                    # Oven (compact appliance card)
                    {
                        "type": "grid",
                        "title": "🔥 Oven",
                        "columns": 1,
                        "cards": [
                            mushroom_switch("sensor.oven_operation_state", "mdi:stove", "orange"),
                            mushroom_switch("switch.oven_power", "mdi:power", "green"),
                            mushroom_switch("switch.oven_child_lock", "mdi:lock", "red"),
                            {
                                "type": "entities",
                                "show_header_toggle": False,
                                "entities": [
                                    {"type": "conditional", "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}], "row": {"entity": "select.oven_active_program", "name": "Active Program", "icon": "mdi:play"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}], "row": {"entity": "sensor.oven_current_oven_cavity_temperature", "name": "Temperature", "icon": "mdi:thermometer"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}], "row": {"entity": "sensor.oven_program_finish_time", "name": "Finish Time", "icon": "mdi:clock-outline"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}], "row": {"entity": "button.oven_stop_program", "name": "Stop", "icon": "mdi:stop"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.oven_operation_state", "state": "inactive"}], "row": {"entity": "select.oven_selected_program", "name": "Select Program", "icon": "mdi:playlist-play"}}
                                ]
                            }
                        ],
                        "grid_options": {"columns": 12}
                    },
                    # Cooktop
                    {
                        "type": "grid",
                        "title": "🍳 Cooktop",
                        "columns": 1,
                        "cards": [
                            mushroom_switch("sensor.cooktop_operation_state", "mdi:stove", "orange"),
                            mushroom_switch("switch.cooktop_power", "mdi:power", "green"),
                            mushroom_switch("switch.cooktop_child_lock", "mdi:lock", "red")
                        ],
                        "grid_options": {"columns": 12}
                    }
                ]
            }
        ]
    }

