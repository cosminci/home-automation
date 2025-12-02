"""Car view configuration"""

from dashboard_helpers import mushroom_readonly

def get_view():
    """Return the Car view configuration"""
    return {
        "title": "Car",
        "path": "car",
        "icon": "mdi:car",
        "type": "sections",
        "sections": [
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    # All car info grouped together
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            # Lock + Last Updated
                            {
                                "type": "grid",
                                "columns": 2,
                                "square": False,
                                "cards": [
                                    {
                                        "type": "custom:mushroom-entity-card",
                                        "entity": "lock.tucson_door_lock",
                                        "icon": "mdi:car-door-lock",
                                        "icon_color": "blue",
                                        "primary_info": "none",
                                        "secondary_info": "state",
                                        "tap_action": {"action": "toggle"}
                                    },
                                    mushroom_readonly("sensor.tucson_last_updated_at", "mdi:clock-outline", "blue")
                                ]
                            },
                            # Fuel & Battery
                            {
                                "type": "grid",
                                "columns": 2,
                                "square": False,
                                "cards": [
                                    mushroom_readonly("sensor.tucson_fuel_level", "mdi:gas-station", "orange"),
                                    mushroom_readonly("sensor.tucson_fuel_driving_range", "mdi:map-marker-distance", "orange")
                                ]
                            },
                            {
                                "type": "grid",
                                "columns": 2,
                                "square": False,
                                "cards": [
                                    mushroom_readonly("sensor.tucson_car_battery_level", "mdi:car-battery", "orange"),
                                    mushroom_readonly("sensor.tucson_odometer", "mdi:counter", "orange")
                                ]
                            },
                            # Doors & Windows (conditional - only show when open)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_front_left_door", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_front_left_door", "mdi:car-door", "red")
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_front_right_door", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_front_right_door", "mdi:car-door", "red")
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_back_left_door", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_back_left_door", "mdi:car-door", "red")
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_back_right_door", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_back_right_door", "mdi:car-door", "red")
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_trunk", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_trunk", "mdi:car-back", "red")
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_hood", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_hood", "mdi:car-lifted-pickup", "red")
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_front_left_window", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_front_left_window", "mdi:window-open", "red")
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_front_right_window", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_front_right_window", "mdi:window-open", "red")
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_back_left_window", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_back_left_window", "mdi:window-open", "red")
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_back_right_window", "state": "on"}],
                                "card": mushroom_readonly("binary_sensor.tucson_back_right_window", "mdi:window-open", "red")
                            },
                            # Warnings & Alerts (conditional - only show when active)
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_all", "state": "on"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 1,
                                    "square": False,
                                    "cards": [mushroom_readonly("binary_sensor.tucson_tire_pressure_all", "mdi:car-tire-alert", "red")]
                                }
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_front_left", "state": "on"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 1,
                                    "square": False,
                                    "cards": [mushroom_readonly("binary_sensor.tucson_tire_pressure_front_left", "mdi:car-tire-alert", "red")]
                                }
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_front_right", "state": "on"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 1,
                                    "square": False,
                                    "cards": [mushroom_readonly("binary_sensor.tucson_tire_pressure_front_right", "mdi:car-tire-alert", "red")]
                                }
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_rear_left", "state": "on"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 1,
                                    "square": False,
                                    "cards": [mushroom_readonly("binary_sensor.tucson_tire_pressure_rear_left", "mdi:car-tire-alert", "red")]
                                }
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_rear_right", "state": "on"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 1,
                                    "square": False,
                                    "cards": [mushroom_readonly("binary_sensor.tucson_tire_pressure_rear_right", "mdi:car-tire-alert", "red")]
                                }
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_fuel_low_level", "state": "on"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 1,
                                    "square": False,
                                    "cards": [mushroom_readonly("binary_sensor.tucson_fuel_low_level", "mdi:gas-station-off", "red")]
                                }
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_smart_key_battery_warning", "state": "on"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 1,
                                    "square": False,
                                    "cards": [mushroom_readonly("binary_sensor.tucson_smart_key_battery_warning", "mdi:key-alert", "red")]
                                }
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_washer_fluid_warning", "state": "on"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 1,
                                    "square": False,
                                    "cards": [mushroom_readonly("binary_sensor.tucson_washer_fluid_warning", "mdi:wiper-wash", "red")]
                                }
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_brake_fluid_warning", "state": "on"}],
                                "card": {
                                    "type": "grid",
                                    "columns": 1,
                                    "square": False,
                                    "cards": [mushroom_readonly("binary_sensor.tucson_brake_fluid_warning", "mdi:car-brake-alert", "red")]
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }

