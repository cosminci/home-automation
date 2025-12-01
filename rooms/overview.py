"""Overview view configuration"""

from dashboard_helpers import button_scene

def button_scene_custom(name, icon, entity, color):
    """Custom button scene with specific color"""
    return {
        "type": "custom:button-card",
        "entity": entity,
        "name": name,
        "icon": icon,
        "tap_action": {
            "action": "call-service",
            "service": "scene.turn_on" if entity.startswith("scene.") else "script.turn_on",
            "service_data": {"entity_id": entity}
        },
        "styles": {
            "card": [{"background-color": color, "height": "50px"}],
            "name": [{"font-size": "14px"}]
        }
    }

def get_view():
    """Return the Overview view configuration"""
    return {
        "title": "Overview",
        "path": "overview",
        "icon": "mdi:home",
        "type": "sections",
        "sections": [
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    # Presence card
                    {
                        "type": "entities",
                        "title": "👥 Presence",
                        "show_header_toggle": False,
                        "entities": [
                            {"entity": "person.sepph", "icon": "mdi:account"},
                            {"entity": "person.mara", "icon": "mdi:account"},
                            {"entity": "device_tracker.tucson_location", "name": "Car", "icon": "mdi:car"}
                        ],
                        "grid_options": {"columns": 12}
                    },
                    # Climate card
                    {
                        "type": "entities",
                        "title": "🌡️ Climate",
                        "show_header_toggle": False,
                        "entities": [
                            {"type": "section", "label": "Outside Weather"},
                            {"entity": "weather.weather_home", "name": "Conditions", "icon": "mdi:weather-partly-cloudy"},
                            {"type": "attribute", "entity": "weather.weather_home", "attribute": "temperature", "name": "Temperature", "icon": "mdi:thermometer", "suffix": "°C"},
                            {"type": "attribute", "entity": "weather.weather_home", "attribute": "humidity", "name": "Humidity", "icon": "mdi:water-percent", "suffix": "%"},
                            {"type": "attribute", "entity": "weather.weather_home", "attribute": "wind_speed", "name": "Wind Speed", "icon": "mdi:weather-windy", "suffix": " km/h"},
                            {"type": "attribute", "entity": "weather.weather_home", "attribute": "pressure", "name": "Pressure", "icon": "mdi:gauge", "suffix": " hPa"},
                            {"type": "section", "label": "Indoor Temperature & AC"},
                            {"entity": "climate.ac_living", "name": "Living Room", "icon": "mdi:sofa"},
                            {"entity": "climate.ac_bedroom", "name": "Bedroom", "icon": "mdi:bed"},
                            {"entity": "climate.ac_office", "name": "Office", "icon": "mdi:desk"},
                            {"entity": "climate.ac_iacopewee", "name": "Kid's Room", "icon": "mdi:teddy-bear"}
                        ],
                        "grid_options": {"columns": 12}
                    },
                    # Scenes card
                    {
                        "type": "entities",
                        "title": "🎬 Scenes",
                        "show_header_toggle": False,
                        "entities": [
                            {"type": "section", "label": "Lighting"},
                            {
                                "type": "custom:multiple-entity-row",
                                "entity": "scene.ambient_10",
                                "name": "Open Space Ambient",
                                "icon": "mdi:lightbulb-group",
                                "show_state": False,
                                "entities": [
                                    {"icon": "mdi:brightness-4", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ambient_10"}}},
                                    {"icon": "mdi:brightness-6", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ambient_70"}}},
                                    {"icon": "mdi:brightness-7", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ambient_100"}}}
                                ]
                            },
                            button_scene_custom("All Lights Off", "mdi:lightbulb-off", "script.lights_all_off", "rgb(255, 152, 0)"),
                            {"type": "section", "label": "Air Conditioning"},
                            button_scene_custom("Living & Office (24°C)", "mdi:air-conditioner", "scene.ac_living_office", "rgb(33, 150, 243)"),
                            button_scene_custom("All On (24°C)", "mdi:air-conditioner", "scene.ac_all_on", "rgb(33, 150, 243)"),
                            button_scene_custom("All Off", "mdi:snowflake-off", "scene.ac_all_off", "rgb(33, 150, 243)"),
                            {"type": "section", "label": "Leaving Home"},
                            button_scene_custom("Everything Off", "mdi:home-export-outline", "script.everything_off", "rgb(244, 67, 54)")
                        ],
                        "grid_options": {"columns": 12}
                    }
                ]
            }
        ]
    }

