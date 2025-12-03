# 🏠 Home Assistant Dashboard

> **Note:** This documentation is optimized for AI agent consumption. While human-readable, it's designed for full vibe coding workflows where an AI agent maintains and evolves the Home Assistant setup.

## 📋 Quick Context

**Home Assistant Instance:** http://tower.local:8123
**Main Dashboard:** http://tower.local:8123/clean-home
**Insights Dashboard:** http://tower.local:8123/home-insights
**Installation:** Docker container on Unraid NAS (`tower.local`)

**Structure:** 5 tabs (Overview, Open Space, Private Spaces, Utility Spaces, Floor Plan)
**Features:** 4 ACs, 25 lights, 2 TVs, 5 appliances, Hyundai Tucson, UniFi network, 2 cameras, Zigbee ready

---

## 📁 Repository Structure

```
home-automation/
├── generate_dashboard.py              # Main dashboard orchestrator
├── generate_insights_dashboard.py     # Insights dashboard generator
├── dashboard_helpers.py               # Card creation helpers
├── templates/                         # Decluttering card templates (6 JSON files)
├── rooms/                             # View modules (5 Python files)
│   ├── overview.py                   # Overview tab
│   ├── open_space.py                 # Open Space tab (Living, Kitchen, Hallway, Staircase, Terrace)
│   ├── private.py                    # Private Spaces tab (Bedroom, Bathrooms, Kid's Room, Office)
│   ├── utility.py                    # Utility Spaces tab (Appliances, Washer Room)
│   └── floor_plan.py                 # Floor Plan tab (Interactive floor plan with 42 devices)
├── configs/                           # HA configuration files
│   ├── automations.yaml              # 23 automations
│   ├── scenes.yaml                   # 8 scenes
│   ├── sensors.yaml                  # Climate & appliance sensors
│   ├── scripts.yaml                  # 2 scripts
│   └── core.category_registry        # Automation categories
├── scripts/                           # Utility scripts
│   ├── HyundaiFetchApiTokensSelenium.py
│   └── delete_entities.sh
└── docs/                              # Additional documentation
    └── UNRAID_INTEGRATION.md
```

---

## 🔑 Authentication & API Access

**Token Location:** `~/.zshrc` environment variable `HA_TOKEN`
**Load Token:** `source ~/.zshrc`

**WebSocket API (for dashboard updates):**
```python
import asyncio, websockets, json, os

HA_URL = "ws://tower.local:8123/api/websocket"
HA_TOKEN = os.environ.get("HA_TOKEN")

async with websockets.connect(HA_URL) as websocket:
    await websocket.recv()  # auth_required
    await websocket.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
    await websocket.recv()  # auth_ok

    # Update dashboard
    await websocket.send(json.dumps({
        "id": 1,
        "type": "lovelace/config/save",
        "url_path": "clean-home",
        "config": dashboard_config
    }))
```

**REST API (for queries only):**
```bash
source ~/.zshrc && curl -s -H "Authorization: Bearer $HA_TOKEN" \
  http://tower.local:8123/api/states | jq '...'
```

---

## 🚀 Working with the Dashboard

### Modular Structure
- **Templates** (`templates/*.json`) - Decluttering card templates
- **View modules** (`rooms/*.py`) - Each tab has a `get_view()` function
- **Helpers** (`dashboard_helpers.py`) - Shared card creation functions
- **Orchestrator** (`generate_dashboard.py`) - Loads and combines everything

### Making Changes
1. Edit view module in `rooms/` (e.g., `rooms/overview.py`, `rooms/open_space.py`)
2. Or edit templates in `templates/`
3. Or edit helpers in `dashboard_helpers.py`
4. **Deploy automatically:**

```bash
# Main dashboard
source ~/.zshrc && source /tmp/ha_venv/bin/activate && python3 generate_dashboard.py

# Insights dashboard
source ~/.zshrc && source /tmp/ha_venv/bin/activate && python3 generate_insights_dashboard.py
```

**⚠️ CRITICAL: AI agents must deploy dashboard updates automatically. Never ask user to run these commands.**

---

## 🔔 Automations, Scenes, Sensors & Scripts

**⚠️ IMPORTANT: Config files in `configs/` CANNOT be deployed via API. User must manually copy them using vi on Unraid console.**

### Update Process
1. Edit file in `configs/` directory
2. Notify user to manually copy to HA
3. User updates via Unraid: Docker → homeassistant → Console
4. Run: `vi /config/automations.yaml` (or scenes.yaml, sensors.yaml, scripts.yaml)
5. Delete all (in vi: `gg` then `dG`), paste, save (`:wq`)
6. **Scenes/Scripts:** Developer Tools → YAML → Reload
7. **Automations/Sensors:** Restart HA container

### Automations
- **File:** `configs/automations.yaml` (23 automations)
- **Categories:** Critical Alerts, Important Notifications, Daily Summaries, Helpers
- **Setup:** Import `configs/core.category_registry` to `/config/.storage/core.category_registry`, restart HA

### Scenes
- **File:** `configs/scenes.yaml` (7 scenes: 3 ambient lighting, 4 AC control)
- **Note:** `ambient_70` uses brightness 177 (not 178) - value 178 doesn't work when lights already on

### Sensors
- **File:** `configs/sensors.yaml`

### Scripts
- **File:** `configs/scripts.yaml` (3 scripts: lights_all_off, everything_off, ambient_off)
- **Why scripts vs scenes:** Scripts use dynamic templates to target all entities of a type (e.g., all lights), which scenes cannot do

---

## 💡 Lighting

**6 Dimmable Lights** - Use Mushroom light cards
**19 On/Off Switches** - Use Mushroom entity cards

See view modules in `rooms/*.py` for entity IDs.

---

## 🔌 Integrations

**Built-in:**
- UniFi Network (Gateway, Switch, 2 APs)
- UniFi Protect (2 cameras)
- ZHA (SLZB-06M Zigbee coordinator)

**HACS Custom:**
- ConnectLife (4 Hisense ACs)
- Home Connect (5 Bosch appliances: dishwasher, oven, cooktop, washing machine, dryer)
- LG ThinQ (2 TVs)
- Hyundai/Kia Connect (Tucson 2022 FHEV)

### Bosch Home Connect API Limitations

**Child Lock:** Available in Bosch Home & Connect app but not exposed via API for washing machine and dryer (returns `SDK.Error.UnsupportedSetting`)

**RemoteStart:** Washing machine and dryer require power to be turned on before programs can be selected remotely

**Cooktop Safety:** Cooktop power cannot be turned on remotely (safety feature), only status display available

### Samsung SmartThings API Limitations

**Soundbar Source Selection (Q990B):** Samsung removed the `mediaInputSource` capability for soundbars in December 2024. Direct `media_player.select_source` service calls no longer work. Soundbar automatically switches sources, so manual source selection is not needed in dashboard. See: [SmartThings Community Issue](https://community.smartthings.com/t/mediainputsource-capability-has-disappeared-for-some-samsung-soundbars/292356)

**HACS Frontend (15 cards installed):**
- Mushroom, button-card, Stack In Card, mini-graph-card, Multiple Entity Row
- Mini Media Player, Weather Radar Card, Horizon Card, Clock Weather Card
- Config Template Card, Plotly Graph Card
- *(Not using: Vertical Stack In Card, Decluttering Card, Power Flow Card Plus, Battery State Card, Vacuum Card)*

---

## 📊 Dashboard Features

**Main Dashboard** (`/clean-home`):
- 5 tabs:
  - **Overview** - Weather, AC controls, scenes, car
  - **Open Space** - Living Room, Kitchen, Hallway, Staircase, Terrace
  - **Private Spaces** - Bedroom, Shower Bathroom, Kid's Room, Office, Bathroom Tub
  - **Utility Spaces** - Kitchen Appliances (Dishwasher, Oven, Cooktop), Washer Room
  - **Floor Plan** - Interactive floor plan with 42 devices (4 ACs, 25 lights, 2 TVs, soundbar, 5 appliances, 4 UniFi devices, 2 cameras)
- 4 ACs with Mushroom climate cards
- 6 dimmable lights with Mushroom light cards
- 19 switches with Mushroom entity cards (icon-only display)
- 2 camera feeds
- Network monitoring (UniFi devices with restart/power cycle buttons)
- 8 scenes with color-coded button-cards
- Entertainment (2 TVs, soundbar)
- 5 appliances with conditional visibility (program selectors, stop buttons, status displays)
- Floor plan using picture-elements card with state-icon elements on 4K inverted floor plan image

**Insights Dashboard** (`/home-insights`):
- Temperature history (24h) with Plotly graphs
- AC setpoint tracking (only when running)
- AC runtime stats
- Appliance usage stats

---

## ⚠️ Critical Rules

**DO:**
- ✅ Use WebSocket API for dashboard updates
- ✅ Use REST API for queries only
- ✅ Use Mushroom cards for modern UI
- ✅ Deploy dashboards automatically after changes
- ✅ Return `none` from template sensors when data shouldn't be plotted
- ✅ Always do thorough library, add-on and integration research before implementing features
- ✅ Stop and ask for feedback when encountering issues - user makes decisions, not AI

**DON'T:**
- ❌ Deploy config files via API (user must manually copy via vi)
- ❌ Assume `light.*` entities are dimmable
- ❌ Create new test files unless requested
- ❌ Remove or rollback features without asking for confirmation first
- ❌ Make assumptions about how integrations work without researching documentation

---

## 🛠️ Utility Scripts

**Delete Entities** (`scripts/delete_entities.sh`):
```bash
./delete_entities.sh sensor.old_sensor switch.unused_switch
```
- Creates backup of `core.entity_registry`
- Removes entities from registry JSON
- Restart HA container to apply

**Hyundai Token Extractor** (`scripts/HyundaiFetchApiTokensSelenium.py`):
- Automated Selenium script to extract EU refresh token
- Required for Hyundai/Kia Connect integration (EU region has reCAPTCHA)
- Token valid for 180 days

---

## 📝 Dashboard Visual Improvements

**Completed (Nov 30 - Dec 3, 2024):**
- ✅ Mushroom climate cards (all 4 ACs with collapsible controls)
- ✅ Mushroom light cards (all 6 dimmable LED strips)
- ✅ button-card for scenes (color-coded: orange=lighting, blue=AC, red=off)
- ✅ Mushroom entity cards (network devices, appliances, switches)
- ✅ Fixed AC setpoint sensors (return `none` when AC off, preserves historical data in Plotly graphs)
- ✅ Interactive floor plan with 42 devices using picture-elements card

**Floor Plan Implementation:**
- Uses Home Assistant's built-in `picture-elements` card (no HACS addons)
- 4K inverted floor plan image (`/local/floor_plan_4k_inverted.jpg`)
- 42 devices positioned using percentage-based coordinates
- Device positions stored in `floor_plan_placement.txt` for version control
- State-based icon coloring (lights work correctly, appliances/ACs show colored when on)
- Workflow: Position icons in HA UI → Export YAML → Update Python → Regenerate dashboard

See `DASHBOARD_VISUAL_IMPROVEMENTS.md` for detailed implementation notes.

---

