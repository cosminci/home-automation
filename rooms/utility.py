def get_view():
    return {
        "title": "Utility Spaces",
        "path": "tab_utility",
        "icon": "mdi:tools",
        "cards": [
            # Dishwasher
            {
                "type": "custom:stack-in-card",
                "cards": [
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
                                "tap_action": {"action": "more-info"},
                                "card_mod": {
                                    "style": "mushroom-state-item { margin: 0 auto !important; }"
                                }
                            }
                        ]
                    }
                ]
            },
            # Cooktop
            {
                "type": "custom:stack-in-card",
                "cards": [
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
            # Washing Machine
            {
                "type": "custom:stack-in-card",
                "cards": [
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

