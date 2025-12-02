"""Overview view configuration"""

from dashboard_helpers import button_scene, mushroom_readonly, mushroom_climate

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
                    # Weather - compact display
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
                            # Collapsible radar with temperature, UV, humidity
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
                    # AC cards - grouped together
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            mushroom_climate("climate.ac_living", " ", "mdi:sofa"),
                            mushroom_climate("climate.ac_bedroom", " ", "mdi:bed"),
                            mushroom_climate("climate.ac_office", " ", "mdi:desk"),
                            mushroom_climate("climate.ac_iacopewee", " ", "mdi:teddy-bear")
                        ]
                    },
                    # Scenes card - hierarchical grouping
                    {
                        "type": "custom:stack-in-card",
                        "cards": [
                            # 1. LIGHT SCENES
                            # 1a. Cinema lights (open space ambient)
                            {
                                "type": "custom:multiple-entity-row",
                                "entity": "scene.ambient_10",
                                "name": " ",
                                "icon": "mdi:movie-open",
                                "show_state": False,
                                "entities": [
                                    {"icon": "mdi:brightness-4", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ambient_10"}}},
                                    {"icon": "mdi:brightness-6", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ambient_70"}}},
                                    {"icon": "mdi:brightness-7", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ambient_100"}}},
                                    {"icon": "mdi:lightbulb-off", "tap_action": {"action": "call-service", "service": "script.turn_on", "service_data": {"entity_id": "script.ambient_off"}}}
                                ]
                            },
                            # 2. AC SCENES - COOL MODE
                            {
                                "type": "custom:multiple-entity-row",
                                "entity": "scene.ac_living_office",
                                "name": " ",
                                "icon": "mdi:snowflake",
                                "icon_color": "blue",
                                "show_state": False,
                                "entities": [
                                    {"icon": "mdi:sofa", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ac_living_office"}}},
                                    {"icon": "mdi:home", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ac_all_on"}}}
                                ]
                            },
                            # 2b. AC SCENES - WARM MODE
                            {
                                "type": "custom:multiple-entity-row",
                                "entity": "scene.ac_living_office_warm",
                                "name": " ",
                                "icon": "mdi:fire",
                                "icon_color": "orange",
                                "show_state": False,
                                "entities": [
                                    {"icon": "mdi:sofa", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ac_living_office_warm"}}},
                                    {"icon": "mdi:home", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ac_all_warm"}}}
                                ]
                            },
                            # 3. OFF SCENES
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
                                        "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ac_all_off"}}
                                    },
                                    {
                                        "type": "custom:mushroom-template-card",
                                        "icon": "mdi:lightbulb-off",
                                        "icon_color": "orange",
                                        "primary": " ",
                                        "tap_action": {"action": "call-service", "service": "script.turn_on", "service_data": {"entity_id": "script.lights_all_off"}}
                                    },
                                    {
                                        "type": "custom:mushroom-template-card",
                                        "icon": "mdi:home-export-outline",
                                        "icon_color": "red",
                                        "primary": " ",
                                        "tap_action": {"action": "call-service", "service": "script.turn_on", "service_data": {"entity_id": "script.everything_off"}}
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

