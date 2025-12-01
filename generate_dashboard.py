#!/usr/bin/env python3
"""
Home Assistant Dashboard Generator
Loads templates and room configurations from separate files and generates the dashboard.
"""

import asyncio
import json
import os
import sys
import websockets
from pathlib import Path
from importlib import import_module

# Configuration
HA_URL = "ws://tower.local:8123/api/websocket"
HA_TOKEN = os.environ.get("HA_TOKEN")

# Room modules to load in order
ROOM_MODULES = [
    "overview",
    "living_room",
    "kitchen",
    "bedroom",
    "kids_room",
    "office",
    "hallway",
    "staircase",
    "bathroom_shower",
    "bathroom_tub",
    "washer_room",
    "terrace",
    "car"
]

def load_templates():
    """Load all decluttering templates from the templates/ directory."""
    templates = {}
    templates_dir = Path("templates")

    for template_file in templates_dir.glob("*.json"):
        template_name = template_file.stem
        with open(template_file, 'r') as f:
            template_data = json.load(f)
            # Keep the full structure including the "card" wrapper
            templates[template_name] = template_data

    return templates

def load_room_views():
    """Load all room view configurations from the rooms/ directory."""
    views = []

    for room_module_name in ROOM_MODULES:
        try:
            # Import the room module
            room_module = import_module(f"rooms.{room_module_name}")
            # Get the view configuration
            view = room_module.get_view()
            views.append(view)
            print(f"✓ Loaded {room_module_name}")
        except Exception as e:
            print(f"✗ Failed to load {room_module_name}: {e}")
            sys.exit(1)

    return views

def create_dashboard_config():
    """Create the complete dashboard configuration."""

    print("Loading templates...")
    decluttering_templates = load_templates()
    print(f"✓ Loaded {len(decluttering_templates)} templates")

    print("\nLoading room views...")
    views = load_room_views()
    print(f"✓ Loaded {len(views)} views")

    dashboard_config = {
        "decluttering_templates": decluttering_templates,
        "title": "Home",
        "views": views
    }

    return dashboard_config

async def deploy_dashboard(config):
    """Deploy the dashboard to Home Assistant via WebSocket API."""
    print("\nDeploying dashboard...")

    async with websockets.connect(HA_URL) as websocket:
        # Authenticate
        auth_response = json.loads(await websocket.recv())
        await websocket.send(json.dumps({
            "type": "auth",
            "access_token": HA_TOKEN
        }))
        auth_result = json.loads(await websocket.recv())

        # Update dashboard
        await websocket.send(json.dumps({
            "id": 2,
            "type": "lovelace/config/save",
            "url_path": "clean-home",
            "config": config
        }))

        response = await websocket.recv()
        print(f"Dashboard deployment response: {response}")

async def main():
    """Main entry point."""
    config = create_dashboard_config()
    await deploy_dashboard(config)

if __name__ == "__main__":
    asyncio.run(main())

