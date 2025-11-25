# Home Assistant Dashboard - Current State & Context

**HA Instance:** http://tower.local:8123
**Dashboard URL:** http://tower.local:8123/clean-home
**Dashboard Title:** Home

**Installation:**
- Docker container on Unraid NAS
- Container name: `homeassistant`
- Volume mapping: `/mnt/user/appdata/homeassistant` (host) → `/config` (container)
- Auto-updates: Watchtower (custom integrations in `/config` persist across updates)

**Automations:**
- File: `/config/automations.yaml` (23 automations total)
- Local copy: `configs/automations.yaml` in this directory
- Quiet hours: 11pm - 9am (Critical notifications bypass this)

---

## 🔑 Authentication & Connection

### Access Token
- **Location:** `~/.zshrc` environment variable `HA_TOKEN`
- **Usage:** `source ~/.zshrc` to load the token in any terminal session

### API Connection Methods

**✅ WORKING METHOD - WebSocket API (USE THIS):**
```python
import asyncio
import websockets
import json
import os

HA_URL = "ws://tower.local:8123/api/websocket"
HA_TOKEN = os.environ.get("HA_TOKEN")

async with websockets.connect(HA_URL) as websocket:
    # Auth
    await websocket.recv()  # Receive auth_required
    await websocket.send(json.dumps({"type": "auth", "access_token": HA_TOKEN}))
    await websocket.recv()  # Receive auth_ok
    
    # Update dashboard
    await websocket.send(json.dumps({
        "id": 1,
        "type": "lovelace/config/save",
        "url_path": "clean-home",
        "config": dashboard_config  # Your dashboard JSON
    }))
```

**✅ WORKING METHOD - REST API (for queries only):**
```bash
source ~/.zshrc && curl -s -H "Authorization: Bearer $HA_TOKEN" \
  http://tower.local:8123/api/states | jq '...'
```

---

## 🏠 Home Layout & Rooms

1. **Living Room**
2. **Kitchen**
3. **Bedroom**
4. **Kid's Room**
5. **Office**
6. **Hallway**
7. **Staircase**
8. **Bathroom - Shower**
9. **Bathroom - Tub**
10. **Washer Room**
11. **Terrace**
12. **Garage**

---

## 💡 Lighting Inventory

### Dimmable Lights (6 total - ALL use `light` card type for sliders)

| Entity ID | Friendly Name | Room |
|-----------|---------------|------|
| `light.led_strip_window` | LED Strip Window | Office |
| `light.led_strip_window_2` | LED Strip Window | Living Room |
| `light.led_strip_window_3` | LED Strip Window | Kitchen |
| `light.led_strip` | LED Strip Window | Bedroom |
| `light.led_strip_window_4` | LED Strip Window | Kid's Room |
| `light.led_strip_bed` | LED Strip Bed | Kid's Room |

### On/Off Switches (19 total - ALL use `entities` card type)

| Entity ID | Friendly Name | Room |
|-----------|---------------|------|
| `switch.rail_spots` | Rail Spots | Bedroom |
| `switch.rail_spots_2` | Rail Spots | Kitchen |
| `switch.rail_spots_3` | Rail Spots | Kid's Room |
| `switch.ceiling_spots` | Ceiling Spots | Kitchen |
| `switch.ceiling_spots_2` | Ceiling Spots | Bathroom - Tub |
| `switch.ceiling_spots_3` | Ceiling Spots | Bathroom - Shower |
| `switch.ceiling_spots_4` | Ceiling Spots | Hallway |
| `switch.ceiling_light` | Ceiling Light | Bedroom |
| `switch.ceiling_light_2` | Ceiling Light | Kid's Room |
| `switch.ceiling_light_3` | Ceiling Fan Light | Living Room |
| `switch.ceiling_light_4` | Ceiling Light | Office |
| `switch.light_2` | Wall Light | Kid's Room |
| `switch.led_strip` | LED Strip | Bathroom - Tub |
| `switch.led_strip_2` | LED Strip | Bathroom - Shower |
| `switch.ventilator` | Ventilator | Bathroom - Shower |
| `switch.ventilator_2` | Ventilator | Bathroom - Tub |
| `switch.dining_light` | Dining Light | Living Room |
| `switch.led_strip_countertop` | LED Strip Countertop | Kitchen |
| `switch.staircase_lights` | Staircase Lights | Staircase |
| `switch.terrace_lights` | Terrace Lights | Terrace |
| `light.ceiling_spots` | Ceiling Spots | Living Room |

---

## 📺 Entertainment Devices

| Entity ID | Friendly Name | Room |
|-----------|---------------|------|
| `media_player.77_oled` | 77" OLED TV | Living Room |
| `media_player.soundbar_q990b` | Soundbar Q990B | Living Room |
| `input_select.soundbar_source` | Soundbar Source | Living Room |
| `media_player.lg_webos_tv_oled48c22lb` | LG TV | Bedroom |

**Soundbar Details:**
- **Model:** Samsung Q990B
- **Integration:** SmartThings (built-in)
- **Supported Features:**
  - Power control
  - Volume control
  - Source selection (HDMI, Bluetooth, Optical, WiFi, AUX)
- **Source Selection:** Uses `input_select.soundbar_source` helper with automation
- **Dashboard:** Combined entertainment card with TV and soundbar controls

---

## ❄️ Air Conditioners (ConnectLife Integration)

| Entity ID | Friendly Name | Room |
|-----------|---------------|------|
| `climate.ac_living` | AC - Living | Living Room |
| `climate.ac_bedroom` | AC - Bedroom | Bedroom |
| `climate.ac_office` | AC - Office | Office |
| `climate.ac_iacopewee` | AC - Iacopewee | Kid's Room |

**Hardware:**
- WiFi Module: AEH-W4A1
- Control App: ConnectLife
- Device Type: 009 (Air conditioner)
- Installation Type: Ceiling duct units (no swing controls)

**Features:**
- HVAC Modes: Off, Cool, Heat, Dry, Fan Only, Auto
- Temperature Range: 16-32°C
- Preset Modes: None, Eco, AI
- Fan Modes: Auto, Low, Middle Low, Medium, Middle High, High
- Current temperature sensor

**Integration Details:**
- Custom Integration: `oyvindwe/connectlife-ha` (installed via HACS)
- Installed to: `/config/custom_components/connectlife/`
- Persists across Watchtower container updates
- Account: ConnectLife username/password

---

## 🍽️ Appliances (Home Connect Integration)

### Kitchen
- **Dishwasher:** `sensor.dishwasher_operation_state`, `sensor.dishwasher_program_finish_time`, `sensor.dishwasher_program_progress`, `button.dishwasher_stop_program`
- **Oven:** `sensor.oven_operation_state`, `sensor.oven_current_oven_cavity_temperature`, `sensor.oven_program_finish_time`, `button.oven_pause_program`, `button.oven_stop_program`
- **Cooktop:** `sensor.cooktop_operation_state`

### Washer Room
- **Washing Machine:** `select.washing_machine_active_program`, `sensor.washing_machine_program_finish_time`, `sensor.washing_machine_program_progress`, `select.washing_machine_selected_program`, `button.washing_machine_stop_program`
- **Dryer:** `sensor.dryer_operation_state`, `sensor.dryer_program_finish_time`, `sensor.dryer_program_progress`, `button.dryer_stop_program`

---

## 🎨 Dashboard Structure

### Current Dashboard: `clean-home`
- **Title:** Home
- **Path:** `/clean-home`
- **Views (Tabs):** 13 total
  1. **Scenes** - 8 scenes total
  2. **Living Room** - AC + Lights + Entertainment
  3. **Kitchen** - Lights + Appliances
  4. **Bedroom** - AC + Lights + LG TV
  5. **Kid's Room** - AC + Lights
  6. **Office** - AC + Lights
  7. **Hallway** - Lights
  8. **Staircase** - Lights
  9. **Bathroom - Shower** - Lights + Ventilation
  10. **Bathroom - Tub** - Lights + Ventilation
  11. **Washer Room** - Washing Machine + Dryer
  12. **Terrace** - Lights
  13. **Car** - Hyundai Tucson monitoring

### Card Types Used

**For Dimmable Lights (brightness sliders):**
```json
{
    "type": "light",
    "entity": "light.led_strip_window_2",
    "name": "LED Strip Window",
    "icon": "mdi:led-strip-variant"
}
```

**For On/Off Switches:**
```json
{
    "type": "entities",
    "title": "💡 Lights",
    "entities": [
        {"entity": "switch.dining_light", "name": "Dining Light", "icon": "mdi:ceiling-light"}
    ]
}
```

**For Scene Buttons (NO scripts - direct service calls):**
```json
{
    "type": "button",
    "name": "Cinema Mode (10%)",
    "icon": "mdi:movie-open",
    "tap_action": {
        "action": "call-service",
        "service": "light.turn_on",
        "service_data": {
            "entity_id": ["light.led_strip_window_2", "light.led_strip_window_3"],
            "brightness": 25
        }
    }
}
```

**For Media Players (TVs with volume control):**
```json
{
    "type": "media-control",
    "entity": "media_player.77_oled"
}
```

**For Air Conditioners (thermostat cards):**
```json
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
}
```

**For Conditional Appliance Controls:**
```json
{
    "type": "entities",
    "title": "🍽️ Dishwasher",
    "show_header_toggle": false,
    "entities": [
        {
            "type": "conditional",
            "conditions": [{"entity": "sensor.dishwasher_operation_state", "state_not": "inactive"}],
            "row": {"entity": "sensor.dishwasher_finish_time", "name": "Finish Time"}
        }
    ]
}
```

---

## 🎬 Lighting Scenes

All scenes are defined in `configs/scenes.yaml`. See that file for complete entity lists.

---



---

## 🚀 Working with the Dashboard

1. **Query all dimmable lights:**
   ```bash
   source ~/.zshrc && curl -s -H "Authorization: Bearer $HA_TOKEN" \
     http://tower.local:8123/api/states | jq '[.[] | select(.attributes.supported_color_modes != null and (.attributes.supported_color_modes | contains(["brightness"])))] | .[] | {entity_id, friendly_name: .attributes.friendly_name}'
   ```

2. **Verify entity IDs exist:**
   ```bash
   source ~/.zshrc && curl -s -H "Authorization: Bearer $HA_TOKEN" \
     http://tower.local:8123/api/states | jq -r '.[].entity_id' | grep -E "^(switch\.|light\.)" | sort
   ```

3. **Update the dashboard:**
   ```bash
   source ~/.zshrc && source /tmp/ha_venv/bin/activate && python3 generate_dashboard.py
   ```

4. **Access the dashboard** at http://tower.local:8123/clean-home

---

## 🔌 Custom Integrations

### HACS (Home Assistant Community Store)
- **Installed:** Yes
- **Location:** `/config/custom_components/hacs/`
- **Persistence:** Survives Watchtower container updates
- **Authorization:** GitHub account required

### ConnectLife Integration (Hisense ACs)
- **Repository:** `oyvindwe/connectlife-ha`
- **Installed via:** HACS custom repository
- **Location:** `/config/custom_components/connectlife/`
- **Persistence:** Survives Watchtower container updates
- **Account:** ConnectLife username/password

### Hyundai / Kia Connect Integration
- **Repository:** `Hyundai-Kia-Connect/kia_uvo`
- **Installed via:** HACS
- **Location:** `/config/custom_components/kia_uvo/`
- **Persistence:** Survives Watchtower container updates
- **Vehicle:** Hyundai Tucson 2022 FHEV
- **Region:** EU
- **Authentication:** Refresh token (required for EU region due to reCAPTCHA)
- **Token Validity:** 180 days (must regenerate after expiration)

**Dashboard Integration:**
- **Tab:** Car (13th tab)
- **Cards:**
  1. **Vehicle Status** - Engine, door lock, location, last updated
  2. **Fuel & Battery** - Fuel level, range, 12V battery, odometer
  3. **Doors & Windows** - Conditional visibility (only shows when open)
  4. **Warnings & Alerts** - Tire pressure warnings, fluid warnings (conditional)

**Obtaining Refresh Token:**
```bash
# Run the automated token extraction script
cd /tmp/kia
python3 -m venv .venv
source .venv/bin/activate
pip install selenium requests webdriver-manager

# Run the script
python3 /Users/ciobanu/personal/home-automation/scripts/HyundaiFetchApiTokensSelenium.py
```

**Integration Setup:**
1. Settings → Devices & Services → Add Integration
2. Search for "Hyundai / Kia Connect"
3. Select Region: EU, Brand: Hyundai
4. Enter:
   - Username: Hyundai BlueLink email
   - Token/Password: Refresh token from script
   - Pin: Vehicle PIN

### Installing New Custom Integrations
1. Access Unraid terminal: `docker exec -it homeassistant bash`
2. Install via HACS (integrations auto-install to `/config/custom_components/`)
3. Restart Home Assistant
4. All custom integrations persist across Watchtower updates

---

## 🔔 Automations

**File:** `automations.yaml` (23 automations total)

### Automation List

**Entertainment (1):**
1. Soundbar - Change Source (syncs `input_select.soundbar_source` with soundbar)

**Critical Notifications (10) - Bypass quiet hours:**
1. Car Unlocked (5+ min)
2. Car Door/Window/Trunk/Hood Open (10+ min)
3. Kitchen Oven Left On >2 Hours
4. Kitchen Cooktop Left On >30 Minutes
5. Appliances Error State
6. Car Low Tire Pressure (<30 PSI)
7. Car Fuel Level Critical (<10%)
8. Car Washer Fluid Low
9. Car Battery Warning (<20%)
10. System Device Offline (integrations failing)

**Important Notifications (9) - Active hours 9am-11pm only:**
1. Kitchen Dishwasher Complete
2. Kitchen Dishwasher Salt Low
3. Kitchen Dishwasher Rinse Aid Low
4. Kitchen Oven Preheating Complete
5. Kitchen Oven Cooking Complete
6. Laundry Washing Machine Complete
7. Laundry Dryer Complete
8. Climate AC Extreme Temperature (>28C or <18C)
9. Climate AC Running >8 Hours

**Informational Notifications (3) - Daily summaries at 9am:**
1. Home Lights Left On Overnight
2. Entertainment TV Left On Overnight
3. Daily Summary (lights on, ACs running)

### Notification Settings
- **Quiet hours:** 11pm - 9am
- **Active hours:** 9am - 11pm
- **Service:** `notify.notify` (sends to all registered mobile devices)

### Updating Automations
1. Edit `automations.yaml` in this directory
2. Copy entire file contents
3. On Unraid: Docker → homeassistant → Console
4. Run: `vi /config/automations.yaml`
5. Replace all content (in vi: `gg` then `dG` to delete, paste, `:wq` to save)
6. Restart Home Assistant container

---

## ⚠️ Critical Reminders

- **DO NOT** create YAML script files - they cannot be installed via API
- **DO NOT** use REST API for dashboard updates - use WebSocket API
- **DO NOT** manually edit automations in HA UI - edit `automations.yaml` and replace entire file
- **ALWAYS** use `light` card type for dimmable lights
- **ALWAYS** use `entities` card type for on/off switches
- **NEVER** assume `light.*` entities are dimmable - check `supported_color_modes`

