#!/usr/bin/env python3
"""
Home Assistant Dashboard Generator
Loads templates and room configurations from separate files and generates the dashboard.
"""

import asyncio
import json
import sys
from pathlib import Path
from importlib import import_module

# Ensure imports work from any working directory
sys.path.insert(0, str(Path(__file__).parent))

from ha_deploy import deploy_dashboard

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

async def main():
    """Main entry point."""
    config = create_dashboard_config()
    await deploy_dashboard("clean-home", config)

if __name__ == "__main__":
    asyncio.run(main())
