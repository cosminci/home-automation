#!/usr/bin/env python3
"""
Generate Home Assistant dashboard
"""

import asyncio
import websockets
import json
import os

HA_URL = "ws://tower.local:8123/api/websocket"
HA_TOKEN = os.environ.get("HA_TOKEN")

async def create_corrected_dashboard():
    """Create the dashboard"""
    
    async with websockets.connect(HA_URL) as websocket:
        # Auth
        await websocket.recv()
        await websocket.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        await websocket.recv()

        # Dashboard configuration
        dashboard_config = {
            "title": "Home",
            "views": [
                # Main Home Overview
                {
                    "title": "Overview",
                    "path": "overview",
                    "icon": "mdi:home",
                    "cards": [
                        {
                            "type": "entities",
                            "title": "🌡️ Climate",
                            "show_header_toggle": False,
                            "entities": [
                                {
                                    "entity": "weather.weather_home",
                                    "name": "Outside",
                                    "icon": "mdi:weather-partly-cloudy"
                                },
                                {
                                    "type": "section",
                                    "label": "Indoor Temperature & AC"
                                },
                                {
                                    "entity": "climate.ac_living",
                                    "name": "Living Room",
                                    "icon": "mdi:sofa"
                                },
                                {
                                    "entity": "climate.ac_bedroom",
                                    "name": "Bedroom",
                                    "icon": "mdi:bed"
                                },
                                {
                                    "entity": "climate.ac_office",
                                    "name": "Office",
                                    "icon": "mdi:desk"
                                },
                                {
                                    "entity": "climate.ac_iacopewee",
                                    "name": "Kid's Room",
                                    "icon": "mdi:teddy-bear"
                                },
                                {
                                    "type": "section",
                                    "label": "AC Scenes"
                                },
                                {"type": "button", "name": "Living & Office (24°C)", "icon": "mdi:air-conditioner", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ac_living_office"}}},
                                {"type": "button", "name": "All On (24°C)", "icon": "mdi:air-conditioner", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ac_all_on"}}},
                                {"type": "button", "name": "All Off", "icon": "mdi:snowflake-off", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ac_all_off"}}}
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "🎬 Lighting Scenes",
                            "show_header_toggle": False,
                            "entities": [
                                {"type": "button", "name": "Ambient 10%", "icon": "mdi:movie-open", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ambient_10"}}},
                                {"type": "button", "name": "Ambient 70%", "icon": "mdi:brightness-6", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ambient_70"}}},
                                {"type": "button", "name": "Ambient 100%", "icon": "mdi:lightbulb-on", "tap_action": {"action": "call-service", "service": "scene.turn_on", "service_data": {"entity_id": "scene.ambient_100"}}},
                                {"type": "button", "name": "All Off", "icon": "mdi:lightbulb-off", "tap_action": {"action": "call-service", "service": "script.turn_on", "service_data": {"entity_id": "script.lights_all_off"}}}
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "🏠 Leaving Home",
                            "show_header_toggle": False,
                            "entities": [
                                {"type": "button", "name": "Everything Off", "icon": "mdi:home-export-outline", "tap_action": {"action": "call-service", "service": "script.turn_on", "service_data": {"entity_id": "script.everything_off"}}}
                            ]
                        }
                    ]
                },

                # Living Room
                {
                    "title": "Living Room",
                    "path": "living_room",
                    "icon": "mdi:sofa",
                    "cards": [
                        {
                            "type": "thermostat",
                            "entity": "climate.ac_living",
                            "name": "Air Conditioner",
                            "features": [
                                {
                                    "type": "climate-hvac-modes",
                                    "hvac_modes": ["off", "cool", "heat", "dry", "fan_only", "auto"]
                                },
                                {
                                    "type": "climate-preset-modes",
                                    "style": "dropdown",
                                    "preset_modes": ["none", "eco", "ai"]
                                }
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "💡 Lights",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.dining_light", "name": "Dining Light", "icon": "mdi:ceiling-light"},
                                {"entity": "switch.ceiling_light_3", "name": "Ceiling Fan Light", "icon": "mdi:ceiling-fan-light"},
                                {"entity": "light.ceiling_spots", "name": "Ceiling Spots", "icon": "mdi:lightbulb-group"}
                            ]
                        },
                        {
                            "type": "light",
                            "entity": "light.led_strip_window_2",
                            "name": "LED Strip Window",
                            "icon": "mdi:led-strip-variant"
                        },
                        {
                            "type": "entities",
                            "title": "📺 Entertainment",
                            "show_header_toggle": False,
                            "entities": [
                                {
                                    "type": "section",
                                    "label": "TV"
                                },
                                {"entity": "media_player.77_oled", "name": "77\" OLED"},
                                {
                                    "type": "section",
                                    "label": "Soundbar"
                                },
                                {"entity": "media_player.soundbar_q990b", "name": "Power & Volume"},
                                {"entity": "input_select.soundbar_source", "name": "Source"}
                            ]
                        }
                    ]
                },

                # Kitchen
                {
                    "title": "Kitchen",
                    "path": "kitchen",
                    "icon": "mdi:silverware-fork-knife",
                    "cards": [
                        {
                            "type": "entities",
                            "title": "💡 Lights",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.led_strip_countertop", "name": "Countertop LED", "icon": "mdi:led-strip"},
                                {"entity": "switch.rail_spots_2", "name": "Rail Spots", "icon": "mdi:track-light"},
                                {"entity": "switch.ceiling_spots", "name": "Ceiling Spots", "icon": "mdi:ceiling-light"}
                            ]
                        },
                        {
                            "type": "light",
                            "entity": "light.led_strip_window_3",
                            "name": "LED Strip Window",
                            "icon": "mdi:led-strip-variant"
                        },
                        {
                            "type": "entities",
                            "title": "🍽️ Dishwasher",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "sensor.dishwasher_operation_state", "name": "Status", "icon": "mdi:dishwasher"},
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.dishwasher_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "select.dishwasher_active_program", "name": "Active Program", "icon": "mdi:play"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.dishwasher_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "sensor.dishwasher_program_finish_time", "name": "Finish Time", "icon": "mdi:clock-outline"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.dishwasher_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "button.dishwasher_stop_program", "name": "Stop Program", "icon": "mdi:stop"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.dishwasher_operation_state", "state": "inactive"}],
                                    "row": {"entity": "select.dishwasher_selected_program", "name": "Select Program", "icon": "mdi:playlist-play"}
                                },
                                {"entity": "switch.dishwasher_power", "name": "Power", "icon": "mdi:power"},
                                {"entity": "sensor.dishwasher_salt_nearly_empty", "name": "Salt Warning", "icon": "mdi:shaker"},
                                {"entity": "sensor.dishwasher_rinse_aid_nearly_empty", "name": "Rinse Aid Warning", "icon": "mdi:spray-bottle"}
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "🔥 Oven",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "sensor.oven_operation_state", "name": "Status", "icon": "mdi:stove"},
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "select.oven_active_program", "name": "Active Program", "icon": "mdi:play"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "sensor.oven_current_oven_cavity_temperature", "name": "Temperature", "icon": "mdi:thermometer"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "sensor.oven_program_finish_time", "name": "Finish Time", "icon": "mdi:clock-outline"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.oven_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "button.oven_stop_program", "name": "Stop", "icon": "mdi:stop"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.oven_operation_state", "state": "inactive"}],
                                    "row": {"entity": "select.oven_selected_program", "name": "Select Program", "icon": "mdi:playlist-play"}
                                },
                                {"entity": "switch.oven_power", "name": "Power", "icon": "mdi:power"},
                                {"entity": "switch.oven_child_lock", "name": "Child Lock", "icon": "mdi:lock"}
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "🍳 Cooktop",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "sensor.cooktop_operation_state", "name": "Status", "icon": "mdi:stove"},
                                {"entity": "switch.cooktop_power", "name": "Power", "icon": "mdi:power"},
                                {"entity": "switch.cooktop_child_lock", "name": "Child Lock", "icon": "mdi:lock"}
                            ]
                        }
                    ]
                },

                # Bedroom
                {
                    "title": "Bedroom",
                    "path": "bedroom",
                    "icon": "mdi:bed",
                    "cards": [
                        {
                            "type": "thermostat",
                            "entity": "climate.ac_bedroom",
                            "name": "Air Conditioner",
                            "features": [
                                {
                                    "type": "climate-hvac-modes",
                                    "hvac_modes": ["off", "cool", "heat", "dry", "fan_only", "auto"]
                                },
                                {
                                    "type": "climate-preset-modes",
                                    "style": "dropdown",
                                    "preset_modes": ["none", "eco", "ai"]
                                }
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "💡 Lights",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.rail_spots", "name": "Rail Spots", "icon": "mdi:track-light"},
                                {"entity": "switch.ceiling_light", "name": "Ceiling Light", "icon": "mdi:ceiling-light"}
                            ]
                        },
                        {
                            "type": "light",
                            "entity": "light.led_strip",
                            "name": "LED Strip Window",
                            "icon": "mdi:led-strip-variant"
                        },
                        {
                            "type": "media-control",
                            "entity": "media_player.lg_webos_tv_oled48c22lb"
                        }
                    ]
                },

                # Kid's Room
                {
                    "title": "Kid's Room",
                    "path": "kid_room",
                    "icon": "mdi:teddy-bear",
                    "cards": [
                        {
                            "type": "thermostat",
                            "entity": "climate.ac_iacopewee",
                            "name": "Air Conditioner",
                            "features": [
                                {
                                    "type": "climate-hvac-modes",
                                    "hvac_modes": ["off", "cool", "heat", "dry", "fan_only", "auto"]
                                },
                                {
                                    "type": "climate-preset-modes",
                                    "style": "dropdown",
                                    "preset_modes": ["none", "eco", "ai"]
                                }
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "💡 Lights",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.rail_spots_3", "name": "Rail Spots", "icon": "mdi:track-light"},
                                {"entity": "switch.ceiling_light_2", "name": "Ceiling Light", "icon": "mdi:ceiling-light"},
                                {"entity": "switch.light_2", "name": "Wall Light", "icon": "mdi:wall-sconce"}
                            ]
                        },
                        {
                            "type": "light",
                            "entity": "light.led_strip_window_4",
                            "name": "LED Strip Window",
                            "icon": "mdi:led-strip-variant"
                        },
                        {
                            "type": "light",
                            "entity": "light.led_strip_bed",
                            "name": "LED Strip Bed",
                            "icon": "mdi:led-strip-variant"
                        }
                    ]
                },

                # Office
                {
                    "title": "Office",
                    "path": "office",
                    "icon": "mdi:desk",
                    "cards": [
                        {
                            "type": "thermostat",
                            "entity": "climate.ac_office",
                            "name": "Air Conditioner",
                            "features": [
                                {
                                    "type": "climate-hvac-modes",
                                    "hvac_modes": ["off", "cool", "heat", "dry", "fan_only", "auto"]
                                },
                                {
                                    "type": "climate-preset-modes",
                                    "style": "dropdown",
                                    "preset_modes": ["none", "eco", "ai"]
                                }
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "💡 Lights",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.ceiling_light_4", "name": "Ceiling Light", "icon": "mdi:ceiling-light"}
                            ]
                        },
                        {
                            "type": "light",
                            "entity": "light.led_strip_window",
                            "name": "LED Strip Window",
                            "icon": "mdi:led-strip-variant"
                        }
                    ]
                },

                # Hallway
                {
                    "title": "Hallway",
                    "path": "hallway",
                    "icon": "mdi:door-open",
                    "cards": [
                        {
                            "type": "entities",
                            "title": "💡 Lights",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.ceiling_spots_4", "name": "Ceiling Spots", "icon": "mdi:ceiling-light"}
                            ]
                        }
                    ]
                },

                # Staircase
                {
                    "title": "Staircase",
                    "path": "staircase",
                    "icon": "mdi:stairs",
                    "cards": [
                        {
                            "type": "entities",
                            "title": "💡 Lights",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.staircase_lights", "name": "Hanging Lights (4)", "icon": "mdi:ceiling-light-multiple"}
                            ]
                        }
                    ]
                },

                # Bathroom - Shower
                {
                    "title": "Bathroom - Shower",
                    "path": "bathroom_shower",
                    "icon": "mdi:shower-head",
                    "cards": [
                        {
                            "type": "entities",
                            "title": "💡 Lights & Ventilation",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.ceiling_spots_3", "name": "Ceiling Spots", "icon": "mdi:ceiling-light"},
                                {"entity": "switch.led_strip_2", "name": "LED Strip", "icon": "mdi:led-strip"},
                                {"entity": "switch.ventilator", "name": "Ventilator", "icon": "mdi:fan"}
                            ]
                        }
                    ]
                },

                # Bathroom - Tub
                {
                    "title": "Bathroom - Tub",
                    "path": "bathroom_tub",
                    "icon": "mdi:bathtub",
                    "cards": [
                        {
                            "type": "entities",
                            "title": "💡 Lights & Ventilation",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.ceiling_spots_2", "name": "Ceiling Spots", "icon": "mdi:ceiling-light"},
                                {"entity": "switch.led_strip", "name": "LED Strip", "icon": "mdi:led-strip"},
                                {"entity": "switch.ventilator_2", "name": "Ventilator", "icon": "mdi:fan"}
                            ]
                        }
                    ]
                },

                # Washer Room
                {
                    "title": "Washer Room",
                    "path": "washer_room",
                    "icon": "mdi:washing-machine",
                    "cards": [
                        {
                            "type": "entities",
                            "title": "👕 Washing Machine",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "sensor.washing_machine_operation_state", "name": "Status", "icon": "mdi:washing-machine"},
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.washing_machine_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "select.washing_machine_active_program", "name": "Active Program", "icon": "mdi:play"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.washing_machine_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "sensor.washing_machine_program_finish_time", "name": "Finish Time", "icon": "mdi:clock-outline"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.washing_machine_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "button.washing_machine_stop_program", "name": "Stop", "icon": "mdi:stop"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.washing_machine_operation_state", "state": "paused"}],
                                    "row": {"entity": "button.washing_machine_resume_program", "name": "Resume", "icon": "mdi:play"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.washing_machine_operation_state", "state": "inactive"}],
                                    "row": {"entity": "select.washing_machine_selected_program", "name": "Select Program", "icon": "mdi:playlist-play"}
                                },
                                {"entity": "switch.washing_machine_power", "name": "Power", "icon": "mdi:power"}
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "🧺 Dryer",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "sensor.dryer_operation_state", "name": "Status", "icon": "mdi:tumble-dryer"},
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.dryer_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "select.dryer_active_program", "name": "Active Program", "icon": "mdi:play"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.dryer_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "sensor.dryer_program_finish_time", "name": "Finish Time", "icon": "mdi:clock-outline"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.dryer_operation_state", "state_not": "inactive"}],
                                    "row": {"entity": "button.dryer_stop_program", "name": "Stop", "icon": "mdi:stop"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.dryer_operation_state", "state": "paused"}],
                                    "row": {"entity": "button.dryer_resume_program", "name": "Resume", "icon": "mdi:play"}
                                },
                                {
                                    "type": "conditional",
                                    "conditions": [{"entity": "sensor.dryer_operation_state", "state": "inactive"}],
                                    "row": {"entity": "select.dryer_selected_program", "name": "Select Program", "icon": "mdi:playlist-play"}
                                },
                                {"entity": "switch.dryer_power", "name": "Power", "icon": "mdi:power"},
                                {"entity": "switch.dryer_child_lock", "name": "Child Lock", "icon": "mdi:lock"}
                            ]
                        }
                    ]
                },

                # Terrace
                {
                    "title": "Terrace",
                    "path": "terrace",
                    "icon": "mdi:balcony",
                    "cards": [
                        {
                            "type": "entities",
                            "title": "💡 Lights",
                            "show_header_toggle": False,
                            "entities": [
                                {"entity": "switch.terrace_lights", "name": "Terrace Lights", "icon": "mdi:outdoor-lamp"}
                            ]
                        }
                    ]
                },

                # Car - Hyundai Tucson
                {
                    "title": "Car",
                    "path": "car",
                    "icon": "mdi:car",
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

        # Update dashboard
        await websocket.send(json.dumps({
            "id": 1,
            "type": "lovelace/config/save",
            "url_path": "clean-home",
            "config": dashboard_config
        }))

        response = await websocket.recv()
        result = json.loads(response)

        if result.get("success"):
            print("✅ Dashboard updated successfully!")
            print(f"📱 Access at: http://tower.local:8123/clean-home")
        else:
            print(f"❌ Error: {result}")

if __name__ == "__main__":
    asyncio.run(create_corrected_dashboard())

