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
                        "cards": [
                            # Power button
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "switch.washing_machine_power",
                                "name": " ",
                                "icon": "mdi:washing-machine",
                                "icon_color": "blue",
                                "primary_info": "none",
                                "secondary_info": "none",
                                "tap_action": {"action": "toggle"}
                            },
                            # Program Selector (when powered on)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "switch.washing_machine_power", "state": "on"}],
                                "card": {
                                    "type": "custom:mushroom-select-card",
                                    "entity": "select.washing_machine_active_program",
                                    "name": "Start Washing Machine Program",
                                    "icon": "mdi:play-circle-outline",
                                    "icon_color": "blue",
                                    "secondary_info": "none"
                                }
                            },
                            # Stop button when running
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.washing_machine_operation_state", "state_not": "inactive"}, {"entity": "sensor.washing_machine_operation_state", "state_not": "ready"}],
                                "card": {
                                    "type": "custom:mushroom-entity-card",
                                    "entity": "button.washing_machine_stop_program",
                                    "name": "Stop Program",
                                    "icon": "mdi:stop",
                                    "icon_color": "red",
                                    "primary_info": "name",
                                    "secondary_info": "none",
                                    "tap_action": {"action": "call-service", "service": "button.press", "service_data": {"entity_id": "button.washing_machine_stop_program"}}
                                }
                            },
                            # Program info (when running)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.washing_machine_operation_state", "state_not": "inactive"}, {"entity": "sensor.washing_machine_operation_state", "state_not": "ready"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 2,
                                    "square": False,
                                    "cards": [
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "select.washing_machine_active_program",
                                            "icon": "mdi:washing-machine",
                                            "icon_color": "blue",
                                            "primary_info": "none",
                                            "secondary_info": "state",
                                            "tap_action": {"action": "none"}
                                        },
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "sensor.washing_machine_program_finish_time",
                                            "icon": "mdi:clock-end",
                                            "icon_color": "blue",
                                            "primary_info": "none",
                                            "secondary_info": "state",
                                            "tap_action": {"action": "none"}
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    # Dryer
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            # Power button
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "switch.dryer_power",
                                "name": " ",
                                "icon": "mdi:tumble-dryer",
                                "icon_color": "blue",
                                "primary_info": "none",
                                "secondary_info": "none",
                                "tap_action": {"action": "toggle"}
                            },
                            # Drying Target (when powered on)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "switch.dryer_power", "state": "on"}],
                                "card": {
                                    "type": "custom:mushroom-chips-card",
                                    "alignment": "center",
                                    "chips": [
                                        {
                                            "type": "template",
                                            "icon": "mdi:water",
                                            "icon_color": "{% if is_state('select.dryer_drying_target', 'laundry_care_dryer_enum_type_drying_target_iron_dry') %}blue{% else %}grey{% endif %}",
                                            "tap_action": {
                                                "action": "call-service",
                                                "service": "select.select_option",
                                                "service_data": {
                                                    "entity_id": "select.dryer_drying_target",
                                                    "option": "laundry_care_dryer_enum_type_drying_target_iron_dry"
                                                }
                                            }
                                        },
                                        {
                                            "type": "template",
                                            "icon": "mdi:water-outline",
                                            "icon_color": "{% if is_state('select.dryer_drying_target', 'laundry_care_dryer_enum_type_drying_target_cupboard_dry') %}blue{% else %}grey{% endif %}",
                                            "tap_action": {
                                                "action": "call-service",
                                                "service": "select.select_option",
                                                "service_data": {
                                                    "entity_id": "select.dryer_drying_target",
                                                    "option": "laundry_care_dryer_enum_type_drying_target_cupboard_dry"
                                                }
                                            }
                                        },
                                        {
                                            "type": "template",
                                            "icon": "mdi:water-off",
                                            "icon_color": "{% if is_state('select.dryer_drying_target', 'laundry_care_dryer_enum_type_drying_target_cupboard_dry_plus') %}blue{% else %}grey{% endif %}",
                                            "tap_action": {
                                                "action": "call-service",
                                                "service": "select.select_option",
                                                "service_data": {
                                                    "entity_id": "select.dryer_drying_target",
                                                    "option": "laundry_care_dryer_enum_type_drying_target_cupboard_dry_plus"
                                                }
                                            }
                                        }
                                    ]
                                }
                            },
                            # Program Selector (when powered on)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "switch.dryer_power", "state": "on"}],
                                "card": {
                                    "type": "custom:mushroom-select-card",
                                    "entity": "select.dryer_active_program",
                                    "name": "Start Dryer Program",
                                    "icon": "mdi:play-circle-outline",
                                    "icon_color": "blue",
                                    "secondary_info": "none"
                                }
                            },
                            # Stop button when running
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.dryer_operation_state", "state_not": "inactive"}, {"entity": "sensor.dryer_operation_state", "state_not": "ready"}],
                                "card": {
                                    "type": "custom:mushroom-entity-card",
                                    "entity": "button.dryer_stop_program",
                                    "name": "Stop Program",
                                    "icon": "mdi:stop",
                                    "icon_color": "red",
                                    "primary_info": "name",
                                    "secondary_info": "none",
                                    "tap_action": {"action": "call-service", "service": "button.press", "service_data": {"entity_id": "button.dryer_stop_program"}}
                                }
                            },
                            # Program info (when running)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "sensor.dryer_operation_state", "state_not": "inactive"}, {"entity": "sensor.dryer_operation_state", "state_not": "ready"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 2,
                                    "square": False,
                                    "cards": [
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "select.dryer_active_program",
                                            "icon": "mdi:tumble-dryer",
                                            "icon_color": "blue",
                                            "primary_info": "none",
                                            "secondary_info": "state",
                                            "tap_action": {"action": "none"}
                                        },
                                        {
                                            "type": "custom:mushroom-entity-card",
                                            "entity": "sensor.dryer_program_finish_time",
                                            "icon": "mdi:clock-end",
                                            "icon_color": "blue",
                                            "primary_info": "none",
                                            "secondary_info": "state",
                                            "tap_action": {"action": "none"}
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }

