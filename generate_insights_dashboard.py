#!/usr/bin/env python3

import asyncio
import websockets
import json
import os

HA_URL = "ws://tower.local:8123/api/websocket"
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
                                {
                                    "type": "custom:plotly-graph",
                                    "title": "🌡️ Temperature History",
                                    "hours_to_show": 24,
                                    "refresh_interval": 10,
                                    "entities": [
                                        {
                                            "entity": "sensor.outdoor_temperature",
                                            "name": "Outdoor",
                                            "yaxis": "y1",
                                            "line": {
                                                "width": 4
                                            },
                                            "filters": [
                                                {"force_numeric": None}
                                            ]
                                        },
                                        {
                                            "entity": "climate.ac_living",
                                            "attribute": "current_temperature",
                                            "name": "Living Measured",
                                            "yaxis": "y1",
                                            "line": {
                                                "width": 2
                                            },
                                            "filters": [
                                                {"force_numeric": None}
                                            ]
                                        },
                                        {
                                            "entity": "climate.ac_living",
                                            "attribute": "temperature",
                                            "name": "Living Set Point",
                                            "yaxis": "y1",
                                            "line": {
                                                "dash": "dot",
                                                "width": 1
                                            },
                                            "filters": [
                                                {"force_numeric": None}
                                            ]
                                        },
                                        {
                                            "entity": "climate.ac_bedroom",
                                            "attribute": "current_temperature",
                                            "name": "Bedroom Measured",
                                            "yaxis": "y1",
                                            "line": {
                                                "width": 2
                                            },
                                            "filters": [
                                                {"force_numeric": None}
                                            ]
                                        },
                                        {
                                            "entity": "climate.ac_bedroom",
                                            "attribute": "temperature",
                                            "name": "Bedroom Set Point",
                                            "yaxis": "y1",
                                            "line": {
                                                "dash": "dot",
                                                "width": 1
                                            },
                                            "filters": [
                                                {"force_numeric": None}
                                            ]
                                        },
                                        {
                                            "entity": "climate.ac_office",
                                            "attribute": "current_temperature",
                                            "name": "Office Measured",
                                            "yaxis": "y1",
                                            "line": {
                                                "width": 2
                                            },
                                            "filters": [
                                                {"force_numeric": None}
                                            ]
                                        },
                                        {
                                            "entity": "climate.ac_office",
                                            "attribute": "temperature",
                                            "name": "Office Set Point",
                                            "yaxis": "y1",
                                            "line": {
                                                "dash": "dot",
                                                "width": 1
                                            },
                                            "filters": [
                                                {"force_numeric": None}
                                            ]
                                        },
                                        {
                                            "entity": "climate.ac_iacopewee",
                                            "attribute": "current_temperature",
                                            "name": "Iacob Measured",
                                            "yaxis": "y1",
                                            "line": {
                                                "width": 2
                                            },
                                            "filters": [
                                                {"force_numeric": None}
                                            ]
                                        },
                                        {
                                            "entity": "climate.ac_iacopewee",
                                            "attribute": "temperature",
                                            "name": "Iacob Set Point",
                                            "yaxis": "y1",
                                            "line": {
                                                "dash": "dot",
                                                "width": 1
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
                                        "columns": "full",
                                        "rows": "auto"
                                    }
                                },
                                {
                                    "type": "markdown",
                                    "title": "📊 AC Runtime",
                                    "content": "| Room | &nbsp; &nbsp; Last 24h &nbsp; &nbsp; | &nbsp; &nbsp; Last 7 Days &nbsp; &nbsp; |\n|------|:----------:|:-------------:|\n| 🛋️ &nbsp; &nbsp; Living | {% set h = states('sensor.ac_living_runtime_yesterday') | float(0) %}{{ h | int }}h{{((h - (h | int)) * 60) | int }}m | {% set h = states('sensor.ac_living_runtime_7days') | float(0) %}{{ h | int }}h{{((h - (h | int)) * 60) | int }}m |\n| 🛏️ &nbsp; &nbsp; Bedroom | {% set h = states('sensor.ac_bedroom_runtime_yesterday') | float(0) %}{{ h | int }}h{{((h - (h | int)) * 60) | int }}m | {% set h = states('sensor.ac_bedroom_runtime_7days') | float(0) %}{{ h | int }}h{{((h - (h | int)) * 60) | int }}m |\n| 🖥️ &nbsp; &nbsp; Office | {% set h = states('sensor.ac_office_runtime_yesterday') | float(0) %}{{ h | int }}h{{((h - (h | int)) * 60) | int }}m | {% set h = states('sensor.ac_office_runtime_7days') | float(0) %}{{ h | int }}h{{((h - (h | int)) * 60) | int }}m |\n| 🧸 &nbsp; &nbsp; Kid's Room | {% set h = states('sensor.ac_kid_runtime_yesterday') | float(0) %}{{ h | int }}h{{((h - (h | int)) * 60) | int }}m | {% set h = states('sensor.ac_kid_runtime_7days') | float(0) %}{{ h | int }}h{{((h - (h | int)) * 60) | int }}m |\n| **⏱️ &nbsp; &nbsp; Total** | {% set h = states('sensor.total_ac_runtime_yesterday') | float(0) %}**{{ h | int }}h{{((h - (h | int)) * 60) | int }}m** | {% set h = states('sensor.total_ac_runtime_7days') | float(0) %}**{{ h | int }}h{{((h - (h | int)) * 60) | int }}m** |",
                                    "grid_options": {
                                        "columns": 9,
                                        "rows": "auto"
                                    }
                                },
                                {
                                    "type": "markdown",
                                    "content": "# 🏠 Appliance Stats\n\n_Coming soon: Dishwasher, Oven, Washing Machine, Dryer run counts_",
                                    "grid_options": {
                                        "columns": 9,
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
            print("📱 Access at: http://tower.local:8123/home-insights")
        else:
            print(f"❌ Error: {result}")

if __name__ == "__main__":
    asyncio.run(create_insights_dashboard())

