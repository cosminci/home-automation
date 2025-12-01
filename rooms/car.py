"""Car view configuration"""

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
                    {
                        "type": "entities",
                        "title": "🚗 Vehicle Status",
                        "show_header_toggle": False,
                        "entities": [
                            {"entity": "binary_sensor.tucson_engine", "name": "Engine", "icon": "mdi:engine"},
                            {"entity": "lock.tucson_door_lock", "name": "Door Lock", "icon": "mdi:car-door-lock"},
                            {"entity": "device_tracker.tucson_location", "name": "Location", "icon": "mdi:map-marker"},
                            {"entity": "sensor.tucson_last_updated_at", "name": "Last Updated", "icon": "mdi:clock-outline"}
                        ]
                    },
                    {
                        "type": "entities",
                        "title": "⛽ Fuel & Battery",
                        "show_header_toggle": False,
                        "entities": [
                            {"entity": "sensor.tucson_fuel_level", "name": "Fuel Level", "icon": "mdi:gas-station"},
                            {"entity": "sensor.tucson_fuel_driving_range", "name": "Driving Range", "icon": "mdi:map-marker-distance"},
                            {"entity": "sensor.tucson_car_battery_level", "name": "12V Battery", "icon": "mdi:car-battery"},
                            {"entity": "sensor.tucson_odometer", "name": "Odometer", "icon": "mdi:counter"}
                        ]
                    },
                    {
                        "type": "entities",
                        "title": "🚪 Doors & Windows",
                        "show_header_toggle": False,
                        "entities": [
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_front_left_door", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_front_left_door", "name": "Front Left Door", "icon": "mdi:car-door"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_front_right_door", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_front_right_door", "name": "Front Right Door", "icon": "mdi:car-door"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_back_left_door", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_back_left_door", "name": "Back Left Door", "icon": "mdi:car-door"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_back_right_door", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_back_right_door", "name": "Back Right Door", "icon": "mdi:car-door"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_trunk", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_trunk", "name": "Trunk", "icon": "mdi:car-back"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_hood", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_hood", "name": "Hood", "icon": "mdi:car-lifted-pickup"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_front_left_window", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_front_left_window", "name": "Front Left Window", "icon": "mdi:car-door"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_front_right_window", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_front_right_window", "name": "Front Right Window", "icon": "mdi:car-door"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_back_left_window", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_back_left_window", "name": "Back Left Window", "icon": "mdi:car-door"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_back_right_window", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_back_right_window", "name": "Back Right Window", "icon": "mdi:car-door"}
                            },
                            {
                                "type": "section",
                                "label": "All closed ✓"
                            }
                        ]
                    },
                    {
                        "type": "entities",
                        "title": "⚠️ Warnings & Alerts",
                        "show_header_toggle": False,
                        "entities": [
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_all", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_tire_pressure_all", "name": "Tire Pressure - All", "icon": "mdi:car-tire-alert"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_front_left", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_tire_pressure_front_left", "name": "Tire - Front Left", "icon": "mdi:car-tire-alert"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_front_right", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_tire_pressure_front_right", "name": "Tire - Front Right", "icon": "mdi:car-tire-alert"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_rear_left", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_tire_pressure_rear_left", "name": "Tire - Rear Left", "icon": "mdi:car-tire-alert"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_tire_pressure_rear_right", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_tire_pressure_rear_right", "name": "Tire - Rear Right", "icon": "mdi:car-tire-alert"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_fuel_low_level", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_fuel_low_level", "name": "Fuel Low", "icon": "mdi:gas-station-off"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_smart_key_battery_warning", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_smart_key_battery_warning", "name": "Smart Key Battery", "icon": "mdi:key-alert"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_washer_fluid_warning", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_washer_fluid_warning", "name": "Washer Fluid Low", "icon": "mdi:wiper-wash"}
                            },
                            {
                                "type": "conditional",
                                "conditions": [{"entity": "binary_sensor.tucson_brake_fluid_warning", "state": "on"}],
                                "row": {"entity": "binary_sensor.tucson_brake_fluid_warning", "name": "Brake Fluid Warning", "icon": "mdi:car-brake-alert"}
                            }
                        ]
                    }
                ]
            }
        ]
    }

