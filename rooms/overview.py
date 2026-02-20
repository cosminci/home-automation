from dashboard_helpers import mushroom_readonly, mushroom_climate, conditional_alert


def get_view():
    return {
        "title": "Overview",
        "path": "tab_overview",
        "icon": "mdi:home",
        "cards": [
            # Weather
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
                                "entity": "weather.weather_home",
                                "icon_color": "blue",
                                "primary_info": "none",
                                "secondary_info": "state",
                                "tap_action": {"action": "more-info"}
                            },
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:weather-windy",
                                "icon_color": "cyan",
                                "primary": " ",
                                "secondary": "{{ state_attr('weather.weather_home', 'wind_speed') }} km/h"
                            }
                        ]
                    },
                    {
                        "type": "custom:expander-card",
                        "clear": True,
                        "padding": "0",
                        "child-padding": "0.6em",
                        "title-card-button-overlay": True,
                        "title-card": {
                            "type": "grid",
                            "columns": 3,
                            "square": False,
                            "cards": [
                                {
                                    "type": "custom:mushroom-template-card",
                                    "icon": "mdi:thermometer",
                                    "icon_color": "orange",
                                    "primary": " ",
                                    "secondary": "{{ state_attr('weather.weather_home', 'temperature') }}°C"
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "icon": "mdi:weather-sunny-alert",
                                    "icon_color": "yellow",
                                    "primary": " ",
                                    "secondary": "{{ state_attr('weather.weather_home', 'uv_index') }}"
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "icon": "mdi:water-percent",
                                    "icon_color": "cyan",
                                    "primary": " ",
                                    "secondary": "{{ state_attr('weather.weather_home', 'humidity') }}%"
                                }
                            ]
                        },
                        "cards": [
                            {
                                "type": "custom:weather-radar-card",
                                "frame_count": 20,
                                "frame_delay": 300,
                                "restart_delay": 1000,
                                "show_marker": True,
                                "show_range": True,
                                "show_zoom": True,
                                "show_recenter": True,
                                "show_playback": True,
                                "show_scale": True,
                                "zoom_level": 8,
                                "map_style": "dark",
                                "data_source": "RainViewer-Original"
                            }
                        ]
                    }
                ]
            },
            # Scenes
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "custom:multiple-entity-row",
                        "entity": "scene.ambient_10",
                        "name": " ",
                        "icon": "mdi:movie-open",
                        "show_state": False,
                        "entities": [
                            {"icon": "mdi:brightness-4",
                             "tap_action": {"action": "call-service", "service": "scene.turn_on",
                                            "service_data": {"entity_id": "scene.ambient_10"}}},
                            {"icon": "mdi:brightness-6",
                             "tap_action": {"action": "call-service", "service": "scene.turn_on",
                                            "service_data": {"entity_id": "scene.ambient_70"}}},
                            {"icon": "mdi:brightness-7",
                             "tap_action": {"action": "call-service", "service": "scene.turn_on",
                                            "service_data": {"entity_id": "scene.ambient_100"}}},
                            {"icon": "mdi:lightbulb-off",
                             "tap_action": {"action": "call-service", "service": "script.turn_on",
                                            "service_data": {"entity_id": "script.ambient_off"}}}
                        ]
                    },
                    {
                        "type": "custom:multiple-entity-row",
                        "entity": "scene.ac_living_office",
                        "name": " ",
                        "icon": "mdi:snowflake",
                        "icon_color": "blue",
                        "show_state": False,
                        "entities": [
                            {"icon": "mdi:sofa", "tap_action": {"action": "call-service", "service": "scene.turn_on",
                                                                "service_data": {
                                                                    "entity_id": "scene.ac_living_office"}}},
                            {"icon": "mdi:home", "tap_action": {"action": "call-service", "service": "scene.turn_on",
                                                                "service_data": {"entity_id": "scene.ac_all_on"}}}
                        ]
                    },
                    {
                        "type": "custom:multiple-entity-row",
                        "entity": "scene.ac_living_office_warm",
                        "name": " ",
                        "icon": "mdi:fire",
                        "icon_color": "orange",
                        "show_state": False,
                        "entities": [
                            {"icon": "mdi:sofa", "tap_action": {"action": "call-service", "service": "scene.turn_on",
                                                                "service_data": {
                                                                    "entity_id": "scene.ac_living_office_warm"}}},
                            {"icon": "mdi:home", "tap_action": {"action": "call-service", "service": "scene.turn_on",
                                                                "service_data": {"entity_id": "scene.ac_all_warm"}}}
                        ]
                    },
                    {
                        "type": "grid",
                        "columns": 3,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:snowflake-off",
                                "icon_color": "blue",
                                "primary": " ",
                                "tap_action": {"action": "call-service", "service": "scene.turn_on",
                                               "service_data": {"entity_id": "scene.ac_all_off"}}
                            },
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:lightbulb-off",
                                "icon_color": "orange",
                                "primary": " ",
                                "tap_action": {"action": "call-service", "service": "script.turn_on",
                                               "service_data": {"entity_id": "script.lights_all_off"}}
                            },
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:home-export-outline",
                                "icon_color": "red",
                                "primary": " ",
                                "tap_action": {"action": "call-service", "service": "script.turn_on",
                                               "service_data": {"entity_id": "script.everything_off"}}
                            }
                        ]
                    }
                ]
            },
            # Air Conditioners
            {
                "type": "custom:stack-in-card",
                "cards": [
                    mushroom_climate("climate.ac_living", " ", "mdi:sofa"),
                    mushroom_climate("climate.ac_bedroom", " ", "mdi:bed"),
                    mushroom_climate("climate.ac_office", " ", "mdi:desk"),
                    mushroom_climate("climate.ac_iacopewee", " ", "mdi:teddy-bear")
                ]
            },
            # Car
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
                    # Car openings (doors, trunk, hood, windows) - show only when open
                    *[conditional_alert(f"binary_sensor.tucson_{d}", "mdi:car-door")
                      for d in ("front_left_door", "front_right_door", "back_left_door", "back_right_door")],
                    conditional_alert("binary_sensor.tucson_trunk", "mdi:car-back"),
                    conditional_alert("binary_sensor.tucson_hood", "mdi:car-lifted-pickup"),
                    *[conditional_alert(f"binary_sensor.tucson_{w}", "mdi:window-open")
                      for w in ("front_left_window", "front_right_window", "back_left_window", "back_right_window")],
                    # Car warnings (tires, fuel, key, fluids) - show only when active
                    *[conditional_alert(f"binary_sensor.tucson_tire_pressure_{t}", "mdi:car-tire-alert", wrap_grid=True)
                      for t in ("all", "front_left", "front_right", "rear_left", "rear_right")],
                    conditional_alert("binary_sensor.tucson_fuel_low_level", "mdi:gas-station-off", wrap_grid=True),
                    conditional_alert("binary_sensor.tucson_smart_key_battery_warning", "mdi:key-alert", wrap_grid=True),
                    conditional_alert("binary_sensor.tucson_washer_fluid_warning", "mdi:wiper-wash", wrap_grid=True),
                    conditional_alert("binary_sensor.tucson_brake_fluid_warning", "mdi:car-brake-alert", wrap_grid=True),
                ]
            }
        ]
    }
