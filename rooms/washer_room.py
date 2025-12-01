"""Washer Room view configuration"""

from dashboard_helpers import mushroom_switch, mushroom_entity

def get_view():
    """Return the Washer Room view configuration"""
    return {
        "title": "Washer Room",
        "path": "washer_room",
        "icon": "mdi:washing-machine",
        "type": "sections",
        "sections": [
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    # Washing Machine
                    {
                        "type": "custom:stack-in-card",
                        "title": "👕 Washing Machine",
                        "cards": [
                            {
                                "type": "grid",
                                "columns": 2,
                                "square": False,
                                "cards": [
                                    mushroom_entity("sensor.washing_machine_operation_state", "Status", "mdi:washing-machine", "blue"),
                                    mushroom_switch("switch.washing_machine_power", "mdi:power", "green")
                                ]
                            },
                            {
                                "type": "entities",
                                "show_header_toggle": False,
                                "entities": [
                                    {"type": "conditional", "conditions": [{"entity": "sensor.washing_machine_operation_state", "state_not": "inactive"}], "row": {"entity": "select.washing_machine_active_program", "name": "Active Program", "icon": "mdi:play"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.washing_machine_operation_state", "state_not": "inactive"}], "row": {"entity": "sensor.washing_machine_program_finish_time", "name": "Finish Time", "icon": "mdi:clock-outline"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.washing_machine_operation_state", "state_not": "inactive"}], "row": {"entity": "button.washing_machine_stop_program", "name": "Stop", "icon": "mdi:stop"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.washing_machine_operation_state", "state": "paused"}], "row": {"entity": "button.washing_machine_resume_program", "name": "Resume", "icon": "mdi:play"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.washing_machine_operation_state", "state": "inactive"}], "row": {"entity": "select.washing_machine_selected_program", "name": "Select Program", "icon": "mdi:playlist-play"}}
                                ]
                            }
                        ]
                    },
                    # Dryer
                    {
                        "type": "custom:stack-in-card",
                        "title": "🧺 Dryer",
                        "cards": [
                            {
                                "type": "grid",
                                "columns": 3,
                                "square": False,
                                "cards": [
                                    mushroom_entity("sensor.dryer_operation_state", "Status", "mdi:tumble-dryer", "blue"),
                                    mushroom_switch("switch.dryer_power", "mdi:power", "green"),
                                    mushroom_switch("switch.dryer_child_lock", "mdi:lock", "red")
                                ]
                            },
                            {
                                "type": "entities",
                                "show_header_toggle": False,
                                "entities": [
                                    {"type": "conditional", "conditions": [{"entity": "sensor.dryer_operation_state", "state_not": "inactive"}], "row": {"entity": "select.dryer_active_program", "name": "Active Program", "icon": "mdi:play"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.dryer_operation_state", "state_not": "inactive"}], "row": {"entity": "sensor.dryer_program_finish_time", "name": "Finish Time", "icon": "mdi:clock-outline"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.dryer_operation_state", "state_not": "inactive"}], "row": {"entity": "button.dryer_stop_program", "name": "Stop", "icon": "mdi:stop"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.dryer_operation_state", "state": "paused"}], "row": {"entity": "button.dryer_resume_program", "name": "Resume", "icon": "mdi:play"}},
                                    {"type": "conditional", "conditions": [{"entity": "sensor.dryer_operation_state", "state": "inactive"}], "row": {"entity": "select.dryer_selected_program", "name": "Select Program", "icon": "mdi:playlist-play"}}
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

