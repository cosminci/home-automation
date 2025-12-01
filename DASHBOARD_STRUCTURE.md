# Home Assistant Dashboard Structure

## Overview

The dashboard has been refactored from a single 863-line monolithic file into a modular structure with:
- **6 decluttering card templates** (JSON files)
- **13 room view modules** (Python files)
- **1 helper module** with card creation functions
- **1 orchestrator script** that loads and combines everything

## Directory Structure

```
home-automation/
├── generate_dashboard.py          # Original monolithic version (BACKUP)
├── generate_dashboard_v2.py       # New modular orchestrator (~113 lines)
├── dashboard_helpers.py           # Helper functions for creating cards
├── templates/                     # Decluttering card templates (JSON)
│   ├── mushroom_switch.json
│   ├── mushroom_light.json
│   ├── mushroom_climate.json
│   ├── button_scene.json
│   ├── network_button.json
│   └── network_status.json
└── rooms/                         # Room configurations (Python modules)
    ├── __init__.py
    ├── overview.py                (~105 lines)
    ├── living_room.py             (~111 lines)
    ├── kitchen.py                 (~105 lines)
    ├── bedroom.py                 (~43 lines)
    ├── kids_room.py               (~92 lines)
    ├── office.py                  (~35 lines)
    ├── hallway.py                 (~79 lines)
    ├── staircase.py               (~22 lines)
    ├── bathroom_shower.py         (~36 lines)
    ├── bathroom_tub.py            (~36 lines)
    ├── washer_room.py             (~72 lines)
    ├── terrace.py                 (~21 lines)
    └── car.py                     (~48 lines)
```

## Usage

### Deploy Dashboard

```bash
python3 generate_dashboard_v2.py
```

### Add a New Room

1. Create a new file in `rooms/` (e.g., `rooms/garage.py`)
2. Define a `get_view()` function that returns the view configuration
3. Add the module name to `ROOM_MODULES` list in `generate_dashboard_v2.py`

Example:
```python
"""Garage view configuration"""

from dashboard_helpers import mushroom_switch

def get_view():
    return {
        "title": "Garage",
        "path": "garage",
        "icon": "mdi:garage",
        "type": "sections",
        "sections": [
            {
                "type": "grid",
                "column_span": 4,
                "cards": [
                    mushroom_switch("switch.garage_light", "mdi:lightbulb")
                ]
            }
        ]
    }
```

### Add a New Template

1. Create a new JSON file in `templates/` (e.g., `templates/my_card.json`)
2. Define the card structure with `[[variable]]` placeholders
3. Add a helper function in `dashboard_helpers.py`

Example template (`templates/my_card.json`):
```json
{
    "card": {
        "type": "custom:my-card",
        "entity": "[[entity]]",
        "name": "[[name]]"
    }
}
```

Example helper (`dashboard_helpers.py`):
```python
def my_card(entity, name):
    return {
        "type": "custom:decluttering-card",
        "template": "my_card",
        "variables": [{"entity": entity}, {"name": name}]
    }
```

## Benefits

✅ **Modularity**: Each room is ~20-110 lines instead of part of an 800-line function
✅ **Maintainability**: Easy to modify individual rooms without touching others
✅ **Reusability**: Templates are defined once and reused throughout
✅ **Clarity**: Clear separation between templates, helpers, rooms, and orchestration
✅ **Extensibility**: Easy to add new rooms or templates
✅ **Version Control**: Smaller, focused files are easier to track in git

## Migration Notes

- The original `generate_dashboard.py` is kept as a backup
- All functionality from the original script is preserved
- The new structure generates the exact same dashboard configuration
- Templates use the decluttering-card format with `[[variable]]` syntax

