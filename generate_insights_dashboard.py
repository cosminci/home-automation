#!/usr/bin/env python3

import asyncio
import websockets
import json
import os

HA_URL = "ws://192.168.1.3:8123/api/websocket"
HA_TOKEN = os.environ.get("HA_TOKEN")

async def create_insights_dashboard():
    async with websockets.connect(HA_URL) as websocket:
        await websocket.recv()
        await websocket.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
        await websocket.recv()

        dashboard_config = {
            "title": "Insights",
            "views": [
                {
                    "title": "Insights",
                    "path": "insights",
                    "icon": "mdi:chart-line",
                    "type": "sections",
                    "sections": [
                        {
                            "type": "grid",
                            "column_span": 4,
                            "cards": [
                                # Temperature History
                                {
                                    "type": "custom:plotly-graph",
                            "title": "🌡️ Temperature History",
                            "hours_to_show": 24,
                            "refresh_interval": 10,
                            "entities": [
                                {
                                    "entity": "climate.ac_living",
                                    "attribute": "current_temperature",
                                    "name": "Living Measured",
                                    "yaxis": "y1",
                                    "line": {
                                        "width": 2,
                                        "color": "#4CAF50",
                                        "shape": "spline"
                                    },
                                    "filters": [
                                        {"force_numeric": None}
                                    ]
                                },
                                {
                                    "entity": "sensor.ac_living_setpoint_when_on",
                                    "name": "Living Set Point",
                                    "yaxis": "y1",
                                    "line": {
                                        "dash": "dot",
                                        "width": 1,
                                        "color": "#4CAF50",
                                        "shape": "spline"
                                    }
                                },
                                {
                                    "entity": "climate.ac_bedroom",
                                    "attribute": "current_temperature",
                                    "name": "Bedroom Measured",
                                    "yaxis": "y1",
                                    "line": {
                                        "width": 2,
                                        "color": "#FF9800",
                                        "shape": "spline"
                                    },
                                    "filters": [
                                        {"force_numeric": None}
                                    ]
                                },
                                {
                                    "entity": "sensor.ac_bedroom_setpoint_when_on",
                                    "name": "Bedroom Set Point",
                                    "yaxis": "y1",
                                    "line": {
                                        "dash": "dot",
                                        "width": 1,
                                        "color": "#FF9800",
                                        "shape": "spline"
                                    }
                                },
                                {
                                    "entity": "climate.ac_office",
                                    "attribute": "current_temperature",
                                    "name": "Office Measured",
                                    "yaxis": "y1",
                                    "line": {
                                        "width": 2,
                                        "color": "#2196F3",
                                        "shape": "spline"
                                    },
                                    "filters": [
                                        {"force_numeric": None}
                                    ]
                                },
                                {
                                    "entity": "sensor.ac_office_setpoint_when_on",
                                    "name": "Office Set Point",
                                    "yaxis": "y1",
                                    "line": {
                                        "dash": "dot",
                                        "width": 1,
                                        "color": "#2196F3",
                                        "shape": "spline"
                                    }
                                },
                                {
                                    "entity": "climate.ac_iacopewee",
                                    "attribute": "current_temperature",
                                    "name": "Kid's Room Measured",
                                    "yaxis": "y1",
                                    "line": {
                                        "width": 2,
                                        "color": "#9C27B0",
                                        "shape": "spline"
                                    },
                                    "filters": [
                                        {"force_numeric": None}
                                    ]
                                },
                                {
                                    "entity": "sensor.ac_kid_setpoint_when_on",
                                    "name": "Kid's Room Set Point",
                                    "yaxis": "y1",
                                    "line": {
                                        "dash": "dot",
                                        "width": 1,
                                        "color": "#9C27B0",
                                        "shape": "spline"
                                    }
                                },
                                {
                                    "entity": "sensor.outdoor_temperature",
                                    "name": "Outdoor",
                                    "yaxis": "y1",
                                    "line": {
                                        "width": 4,
                                        "color": "#FFD700",
                                        "shape": "spline"
                                    },
                                    "filters": [
                                        {"force_numeric": None}
                                    ]
                                }
                            ],
                            "layout": {
                                "height": 400,
                                "margin": {
                                    "t": 30,
                                    "b": 40,
                                    "l": 50,
                                    "r": 20
                                },
                                "xaxis": {
                                    "showspikes": True,
                                    "spikemode": "across",
                                    "spikethickness": 1,
                                    "spikedash": "dot"
                                },
                                "yaxis": {
                                    "title": "Temperature (°C)"
                                },
                                "shapes": [
                                    {
                                        "type": "line",
                                        "x0": 0,
                                        "x1": 1,
                                        "xref": "paper",
                                        "y0": 30,
                                        "y1": 30,
                                        "line": {
                                            "color": "red",
                                            "width": 2,
                                            "dash": "dash"
                                        }
                                    }
                                ],
                                "annotations": [
                                    {
                                        "x": 0.98,
                                        "y": 30,
                                        "xref": "paper",
                                        "yref": "y",
                                        "text": "<b>⚠️ 30°C</b>",
                                        "showarrow": False,
                                        "xanchor": "right",
                                        "yanchor": "bottom",
                                        "font": {
                                            "color": "red",
                                            "size": 11,
                                            "family": "Arial"
                                        }
                                    }
                                ]
                            },
                            "config": {
                                "scrollZoom": True
                            },
                            "grid_options": {
                                "columns": "full"
                            }
                        },
                        # AC Runtime Section
                        {
                            "type": "custom:stack-in-card",
                            "title": "❄️ AC Runtime",
                            "cards": [
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Living Room",
                                    "secondary": "Yesterday: {{ states('sensor.ac_living_runtime_yesterday') | float(0) | round(1) }}h | 7 Days: {{ states('sensor.ac_living_runtime_7_days') | float(0) | round(1) }}h",
                                    "icon": "mdi:air-conditioner",
                                    "icon_color": "green",
                                    "tap_action": {"action": "none"}
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Bedroom",
                                    "secondary": "Yesterday: {{ states('sensor.ac_bedroom_runtime_yesterday') | float(0) | round(1) }}h | 7 Days: {{ states('sensor.ac_bedroom_runtime_7_days') | float(0) | round(1) }}h",
                                    "icon": "mdi:air-conditioner",
                                    "icon_color": "green",
                                    "tap_action": {"action": "none"}
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Office",
                                    "secondary": "Yesterday: {{ states('sensor.ac_office_runtime_yesterday') | float(0) | round(1) }}h | 7 Days: {{ states('sensor.ac_office_runtime_7_days') | float(0) | round(1) }}h",
                                    "icon": "mdi:air-conditioner",
                                    "icon_color": "green",
                                    "tap_action": {"action": "none"}
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Kid's Room",
                                    "secondary": "Yesterday: {{ states('sensor.ac_kid_runtime_yesterday') | float(0) | round(1) }}h | 7 Days: {{ states('sensor.ac_kid_runtime_7_days') | float(0) | round(1) }}h",
                                    "icon": "mdi:air-conditioner",
                                    "icon_color": "green",
                                    "tap_action": {"action": "none"}
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Total",
                                    "secondary": "Yesterday: {{ states('sensor.total_ac_runtime_yesterday') | float(0) | round(1) }}h | 7 Days: {{ states('sensor.total_ac_runtime_7days') | float(0) | round(1) }}h",
                                    "icon": "mdi:timer",
                                    "icon_color": "blue",
                                    "tap_action": {"action": "none"}
                                }
                            ],
                            "grid_options": {
                                "columns": 12,
                                "rows": "auto"
                            }
                        },
                        # Appliance Stats Section
                        {
                            "type": "custom:stack-in-card",
                            "title": "🏠 Appliance Stats",
                            "cards": [
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Dishwasher",
                                    "secondary": "Yesterday: {{ states('sensor.dishwasher_count_yesterday') | int(0) }} runs ({{ states('sensor.dishwasher_runtime_yesterday') | float(0) | round(1) }}h) | 7 Days: {{ states('sensor.dishwasher_count_7_days') | int(0) }} runs ({{ states('sensor.dishwasher_runtime_7_days') | float(0) | round(1) }}h)",
                                    "icon": "mdi:dishwasher",
                                    "icon_color": "blue",
                                    "tap_action": {"action": "none"}
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Oven",
                                    "secondary": "Yesterday: {{ states('sensor.oven_count_yesterday') | int(0) }} runs ({{ states('sensor.oven_runtime_yesterday') | float(0) | round(1) }}h) | 7 Days: {{ states('sensor.oven_count_7_days') | int(0) }} runs ({{ states('sensor.oven_runtime_7_days') | float(0) | round(1) }}h)",
                                    "icon": "mdi:stove",
                                    "icon_color": "orange",
                                    "tap_action": {"action": "none"}
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Cooktop",
                                    "secondary": "Yesterday: {{ states('sensor.cooktop_count_yesterday') | int(0) }} runs ({{ states('sensor.cooktop_runtime_yesterday') | float(0) | round(1) }}h) | 7 Days: {{ states('sensor.cooktop_count_7_days') | int(0) }} runs ({{ states('sensor.cooktop_runtime_7_days') | float(0) | round(1) }}h)",
                                    "icon": "mdi:pot-steam",
                                    "icon_color": "orange",
                                    "tap_action": {"action": "none"}
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Washing Machine",
                                    "secondary": "Yesterday: {{ states('sensor.washing_machine_count_yesterday') | int(0) }} runs ({{ states('sensor.washing_machine_runtime_yesterday') | float(0) | round(1) }}h) | 7 Days: {{ states('sensor.washing_machine_count_7_days') | int(0) }} runs ({{ states('sensor.washing_machine_runtime_7_days') | float(0) | round(1) }}h)",
                                    "icon": "mdi:washing-machine",
                                    "icon_color": "cyan",
                                    "tap_action": {"action": "none"}
                                },
                                {
                                    "type": "custom:mushroom-template-card",
                                    "primary": "Dryer",
                                    "secondary": "Yesterday: {{ states('sensor.dryer_count_yesterday') | int(0) }} runs ({{ states('sensor.dryer_runtime_yesterday') | float(0) | round(1) }}h) | 7 Days: {{ states('sensor.dryer_count_7_days') | int(0) }} runs ({{ states('sensor.dryer_runtime_7_days') | float(0) | round(1) }}h)",
                                    "icon": "mdi:tumble-dryer",
                                    "icon_color": "cyan",
                                    "tap_action": {"action": "none"}
                                }
                            ],
                            "grid_options": {
                                "columns": 12,
                                "rows": "auto"
                            }
                        }
                    ]
                }
            ]
        }
    ]
}

        await websocket.send(json.dumps({
            "id": 2,
            "type": "lovelace/config/save",
            "url_path": "home-insights",
            "config": dashboard_config
        }))

        response = await websocket.recv()
        result = json.loads(response)

        if not result.get("success"):
            await websocket.send(json.dumps({
                "id": 3,
                "type": "lovelace/dashboards/create",
                "url_path": "home-insights",
                "title": "Insights",
                "icon": "mdi:chart-line",
                "mode": "storage"
            }))

            response = await websocket.recv()
            result = json.loads(response)

            if result.get("success"):
                await websocket.send(json.dumps({
                    "id": 4,
                    "type": "lovelace/config/save",
                    "url_path": "home-insights",
                    "config": dashboard_config
                }))

                response = await websocket.recv()
                result = json.loads(response)

        if result.get("success"):
            print("✅ Insights dashboard created successfully!")
            print("📱 Access at: http://192.168.1.3:8123/home-insights")
        else:
            print(f"❌ Error: {result}")

if __name__ == "__main__":
    asyncio.run(create_insights_dashboard())


