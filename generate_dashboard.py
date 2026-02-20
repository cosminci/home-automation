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

# Ensure imports work from any working directory
sys.path.insert(0, str(Path(__file__).parent))

# Configuration
HA_URL = "ws://192.168.1.3:8123/api/websocket"
HA_TOKEN = os.environ.get("HA_TOKEN")

# Room modules to load in order
ROOM_MODULES = [
    "overview",
    "open_space",
    "private",
    "utility",
    "floor_plan"
]

def load_templates():
    """Load all decluttering templates from the templates/ directory."""
    templates = {}
    templates_dir = Path(__file__).parent / "templates"

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
    if not HA_TOKEN:
        print("Error: HA_TOKEN environment variable is not set.")
        print("Set it in ~/.zshrc or run: export HA_TOKEN='your_token'")
        sys.exit(1)

    print("\nDeploying dashboard...")

    async with websockets.connect(HA_URL) as websocket:
        # Authenticate
        await websocket.recv()  # auth_required
        await websocket.send(json.dumps({
            "type": "auth",
            "access_token": HA_TOKEN
        }))
        auth_result = json.loads(await websocket.recv())
        if auth_result.get("type") != "auth_ok":
            print(f"Error: Authentication failed: {auth_result}")
            sys.exit(1)

        # Update dashboard
        await websocket.send(json.dumps({
            "id": 2,
            "type": "lovelace/config/save",
            "url_path": "clean-home",
            "config": config
        }))

        response = json.loads(await websocket.recv())
        if response.get("success"):
            print("Dashboard deployed successfully!")
        else:
            print(f"Error: Deployment failed: {response}")
            sys.exit(1)

async def main():
    """Main entry point."""
    config = create_dashboard_config()
    await deploy_dashboard(config)

if __name__ == "__main__":
    asyncio.run(main())

