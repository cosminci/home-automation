# 🏠 Home Assistant Dashboard

> **Note:** This documentation is optimized for AI agent consumption. While human-readable, it's designed for full vibe coding workflows where an AI agent maintains and evolves the Home Assistant setup.

## 📋 Quick Context

**Home Assistant Instance:** http://tower.local:8123
**Main Dashboard:** http://tower.local:8123/clean-home
**Insights Dashboard:** http://tower.local:8123/home-insights
**Installation:** Docker container on Unraid NAS (`tower.local`)

**Structure:** 13 tabs (Overview + 11 rooms + Car)
**Features:** 4 ACs, 25 lights, 2 TVs, 5 appliances, Hyundai Tucson, UniFi network, 2 cameras, Zigbee ready

---

## 📁 Repository Structure

```
home-automation/
├── generate_dashboard.py              # Main dashboard orchestrator
├── generate_insights_dashboard.py     # Insights dashboard generator
├── dashboard_helpers.py               # Card creation helpers
├── templates/                         # Decluttering card templates (6 JSON files)
├── rooms/                             # Room view modules (13 Python files)
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
- **Room modules** (`rooms/*.py`) - Each room has a `get_view()` function
- **Helpers** (`dashboard_helpers.py`) - Shared card creation functions
- **Orchestrator** (`generate_dashboard.py`) - Loads and combines everything

### Making Changes
1. Edit room module in `rooms/` (e.g., `rooms/living_room.py`)
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
- **File:** `configs/scenes.yaml` (8 scenes)

### Sensors
- **File:** `configs/sensors.yaml`

### Scripts
- **File:** `configs/scripts.yaml` (2 scripts)

---

## 💡 Lighting

**6 Dimmable Lights** - Use Mushroom light cards
**19 On/Off Switches** - Use Mushroom entity cards

See room modules in `rooms/*.py` for entity IDs.

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

**HACS Frontend (15 cards installed):**
- Mushroom, button-card, Stack In Card, mini-graph-card, Multiple Entity Row
- Mini Media Player, Weather Radar Card, Horizon Card, Clock Weather Card
- Config Template Card, Plotly Graph Card
- *(Not using: Vertical Stack In Card, Decluttering Card, Power Flow Card Plus, Battery State Card, Vacuum Card)*

---

## 📊 Dashboard Features

**Main Dashboard** (`/clean-home`):
- 13 tabs (Overview + 11 rooms + Car)
- 4 ACs with Mushroom climate cards
- 6 dimmable lights with Mushroom light cards
- 19 switches with Mushroom entity cards
- 2 camera feeds
- Network monitoring (restart/power cycle buttons)
- 8 scenes with color-coded button-cards
- Entertainment (2 TVs, soundbar with source selector)
- 5 appliances with conditional visibility

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

**Completed (Nov 30 - Dec 1, 2024):**
- ✅ Mushroom climate cards (all 4 ACs with collapsible controls)
- ✅ Mushroom light cards (all 6 dimmable LED strips)
- ✅ button-card for scenes (color-coded: orange=lighting, blue=AC, red=off)
- ✅ Mushroom entity cards (network devices, appliances, switches)
- ✅ Fixed AC setpoint sensors (return `none` when AC off, preserves historical data in Plotly graphs)

**Remaining Work:**
1. **Weather Card** - Replace broken card (max temp = current temp issue)
   - Test: Weather Radar Card, Clock Weather Card, or Horizon Card
2. **Themes** - Apply modern HA theme (user researching)
3. **Stack In Card** - Remove borders for cleaner grouping
4. **Floor Plan** - Create visual floor plan navigation (low priority)
5. **Media Players** - Test Mini Media Player card (optional)

See `DASHBOARD_VISUAL_IMPROVEMENTS.md` for detailed implementation notes.

---

