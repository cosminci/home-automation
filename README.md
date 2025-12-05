# 🏠 Home Assistant Dashboard

> **Note:** This documentation is optimized for AI agent consumption. While human-readable, it's designed for full vibe coding workflows where an AI agent maintains and evolves the Home Assistant setup.

## 📋 Quick Context

**Home Assistant Instance:** http://tower.local:8123
**Main Dashboard:** http://tower.local:8123/clean-home
**Insights Dashboard:** http://tower.local:8123/home-insights
**Installation:** Docker container on Unraid NAS (`tower.local`)

**Structure:** 5 tabs (Overview, Open Space, Private Spaces, Utility Spaces, Floor Plan)
**Features:** 4 ACs, 25 lights, 2 TVs, 5 appliances, Hyundai Tucson, UniFi network, 2 cameras, Zigbee thermostats

---

## 📁 Repository Structure

```
home-automation/
├── generate_dashboard.py              # Main dashboard orchestrator
├── generate_insights_dashboard.py     # Insights dashboard generator
├── dashboard_helpers.py               # Card creation helpers
├── templates/                         # Decluttering card templates (8 JSON files)
├── rooms/                             # View modules (5 Python files)
│   ├── overview.py                   # Overview tab (weather, scenes, ACs, car)
│   ├── open_space.py                 # Open Space tab (Living, Kitchen, Hallway, Staircase, Terrace)
│   ├── private.py                    # Private Spaces tab (Bedroom, Bathrooms, Kid's Room, Office)
│   ├── utility.py                    # Utility Spaces tab (Dishwasher, Oven, Cooktop, Washer, Dryer)
│   └── floor_plan.py                 # Floor Plan tab (42 devices on 4K floor plan image)
├── configs/                           # HA configuration files (manual copy required)
│   ├── automations.yaml              # 18 automations (Critical, Important, Convenience)
│   ├── scenes.yaml                   # 8 scenes (3 ambient, 5 AC)
│   ├── scripts.yaml                  # 3 scripts (lights_all_off, everything_off, ambient_off)
│   ├── sensors.yaml                  # History stats sensors (sensor: !include)
│   ├── templates.yaml                # Template sensors (template: !include)
│   ├── customize.yaml                # Entity customizations (ZHA quirks workarounds)
│   └── core.category_registry        # Automation categories JSON
├── scripts/                           # Utility scripts
│   ├── HyundaiFetchApiTokensSelenium.py  # Hyundai EU token extractor
│   └── delete_entities.sh                # Entity registry cleanup
└── docs/
    └── UNRAID_INTEGRATION.md         # Unraid monitoring setup (in progress)
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

**⚠️ Config files in `configs/` CANNOT be deployed via API. User must manually copy via vi on Unraid console.**

### Update Process
1. Edit file in `configs/` directory
2. User updates via Unraid: Docker → homeassistant → Console
3. Run: `vi /config/automations.yaml` (or scenes.yaml, sensors.yaml, scripts.yaml)
4. Delete all (in vi: `gg` then `dG`), paste, save (`:wq`)
5. **Scenes/Scripts:** Developer Tools → YAML → Reload
6. **Automations/Sensors:** Restart HA container

### Automations (18 total)
- **Critical Alerts:** Car unlocked, doors/windows open, oven/cooktop left on, appliance errors, tire pressure, fuel, battery, device offline
- **Important Notifications:** Dishwasher/oven/washer/dryer complete, salt/rinse aid low, oven preheated
- **Convenience:** Late night lights off (1AM)
- **Helpers:** Soundbar source change

### Scenes (8 total)
- **Ambient:** 10%, 70%, 100% brightness for living room LED strips
- **AC:** Living+Office cool, All cool, Living+Office heat, All heat, All off

### Sensors
- **History Stats:** AC runtime (yesterday, 7 days), appliance runtime and cycle counts
- **Templates:** Total AC runtime, outdoor temp, AC setpoints (only when on - for Plotly graphs)

### Scripts (3 total)
- `lights_all_off` - Turn off all lights and switches
- `everything_off` - Lights + ACs + media players off
- `ambient_off` - Turn off living room LED strips only

---

## 🔌 Integrations

**Built-in:**
- UniFi Network (Gateway, Switch, 2 APs)
- UniFi Protect (2 cameras)
- ZHA (SLZB-06M Zigbee coordinator + 2 Tuya TRV thermostats)
- SmartThings (Samsung Q990B soundbar)

**HACS Integrations:**
- ConnectLife (4 Hisense ACs)
- Home Connect (5 Bosch appliances)
- LG ThinQ (2 TVs)
- Hyundai/Kia Connect (Tucson 2022 FHEV)

**HACS Frontend Cards:**
- Mushroom, button-card, Stack In Card, mini-graph-card
- Weather Radar Card, Clock Weather Card, Plotly Graph Card

### Known Integration Limitations

**Bosch Home Connect:**
- Child lock not exposed via API for washer/dryer
- Washer/dryer require power on before remote program selection
- Cooktop power cannot be turned on remotely (safety)

**Samsung SmartThings:**
- Soundbar source selection removed from API (Dec 2024) - soundbar auto-switches sources

**ZHA Quirks:**
- Tuya TRV `_TZE200_b6wax7g0` reports max_temp as 300°C - fixed via `customize.yaml`

---

## 📊 Dashboard Features

**Main Dashboard** (`/clean-home`) - 5 tabs:
- **Overview:** Weather radar, 8 scenes (ambient + AC), 4 AC cards, Hyundai Tucson status
- **Open Space:** Living (lights, AC, TV, soundbar, AP, camera), Kitchen (lights, LED strips), Hallway (lights, network devices, camera), Staircase, Terrace
- **Private Spaces:** Bedroom (lights, AC, TV), Shower Bathroom (lights, ventilator, floor heating), Kid's Room (lights, AC, AP), Office (lights, AC), Bathroom Tub
- **Utility Spaces:** Dishwasher, Oven, Cooktop, Washing Machine, Dryer (all with conditional program selectors and status)
- **Floor Plan:** 42 devices on 4K inverted floor plan image (`/local/floor_plan_4k_inverted.jpg`)

**Insights Dashboard** (`/home-insights`):
- Temperature history (24h Plotly graphs with setpoints only when AC running)
- AC runtime stats (yesterday + 7 days)
- Appliance usage stats (runtime + cycle counts)

---

## ⚠️ Critical Rules

**DO:**
- ✅ Deploy dashboards automatically after changes (never ask user to run commands)
- ✅ Use WebSocket API for dashboard updates, REST API for queries only
- ✅ Return `none` from template sensors when data shouldn't be plotted
- ✅ Research integrations thoroughly before implementing features
- ✅ Ask for feedback when encountering issues

**DON'T:**
- ❌ Deploy config files via API (user must manually copy via vi)
- ❌ Assume `light.*` entities are dimmable (check entity type)
- ❌ Remove or rollback features without confirmation

---

## 🛠️ Utility Scripts

**Delete Entities** (`scripts/delete_entities.sh`):
```bash
./delete_entities.sh sensor.old_sensor switch.unused_switch
```
Creates backup, removes entities from registry, requires HA restart.

**Hyundai Token Extractor** (`scripts/HyundaiFetchApiTokensSelenium.py`):
- Selenium script to extract EU refresh token (bypasses reCAPTCHA)
- Requires CLIENT_ID and CLIENT_SECRET to be filled in (search online for Hyundai Bluelink OAuth2 credentials)
- Token valid for 180 days

---

## 🖼️ Floor Plan

Device positions are configured in `rooms/floor_plan.py` using percentage-based coordinates:
- `left`: 0% = far left, 100% = far right
- `top`: 0% = top, 100% = bottom

To update positions: Edit `DEVICES` dict in `floor_plan.py`, regenerate dashboard.
