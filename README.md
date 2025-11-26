# 🏠 Home Assistant Dashboard

> **Note:** This documentation is optimized for AI agent consumption. While human-readable, it's designed for full vibe coding workflows where an AI agent maintains and evolves the Home Assistant setup.

## 📋 Quick Context

**Home Assistant Instance:** http://tower.local:8123
**Dashboard URL:** http://tower.local:8123/clean-home
**Dashboard Title:** Home

**Structure:** 13 tabs total (Scenes + 11 rooms + Car/Garage)
**Features:** Lighting controls, 4 air conditioners, entertainment devices, smart appliances, Hyundai Tucson monitoring

---

## 📁 Files in This Directory

1. **`README.md`** - This file (quick start guide for AI agents)
2. **`HOME_ASSISTANT_STATE.md`** - Complete technical documentation (READ THIS FIRST)
3. **`generate_dashboard.py`** - Main dashboard generation script
4. **`generate_insights_dashboard.py`** - Insights dashboard generation script
5. **`configs/automations.yaml`** - All Home Assistant automations
6. **`configs/scenes.yaml`** - All Home Assistant scenes
7. **`configs/sensors.yaml`** - Climate history stats sensors
8. **`configs/scripts.yaml`** - Home Assistant scripts (lights off, everything off)
9. **`scripts/HyundaiFetchApiTokensSelenium.py`** - Hyundai EU refresh token extractor
10. **`scripts/delete_entities.sh`** - Delete entities from HA entity registry (run on NAS)

---

## 🚀 Working with the Dashboard

### Step 1: Read the Documentation
Open and read **`HOME_ASSISTANT_STATE.md`** completely. It contains:
- How to connect to HA (WebSocket API)
- Complete lighting inventory
- Current dashboard structure
- Entertainment devices and appliances

### Step 2: Query Entity Information
To find all dimmable lights:
```bash
source ~/.zshrc && curl -s -H "Authorization: Bearer $HA_TOKEN" \
  http://tower.local:8123/api/states | jq '[.[] | select(.attributes.supported_color_modes != null and (.attributes.supported_color_modes | contains(["brightness"])))] | .[] | {entity_id, friendly_name: .attributes.friendly_name, area: .attributes.area_id}'
```

To verify entity IDs exist:
```bash
source ~/.zshrc && curl -s -H "Authorization: Bearer $HA_TOKEN" \
  http://tower.local:8123/api/states | jq -r '.[].entity_id' | grep -E "^(switch\.|light\.)" | sort
```

### Step 3: Update the Dashboard
Modify `generate_dashboard.py` or `generate_insights_dashboard.py` as needed and **ALWAYS AUTOMATICALLY DEPLOY**:
```bash
# Main dashboard
source ~/.zshrc && source /tmp/ha_venv/bin/activate && python3 generate_dashboard.py
# Insights dashboard
source ~/.zshrc && source /tmp/ha_venv/bin/activate && python3 generate_insights_dashboard.py
```

**⚠️ IMPORTANT FOR AI AGENT: Automatically deploy dashboard updates after making changes, DO NOT ask user to run these commands.**

---

## 🔔 Working with Automations, Scenes, Sensors & Scripts

All automations are in `configs/automations.yaml` (23 total).
All scenes are in `configs/scenes.yaml` (8 total).
All sensors are in `configs/sensors.yaml`.
All scripts are in `configs/scripts.yaml` (2 total: lights_all_off, everything_off).

**⚠️ IMPORTANT: ALL config files in `configs/` directory CANNOT be copied automatically to HA. User must manually update them using vi.**

**To update automations, scenes, sensors, or scripts:**
1. Edit the respective file in `configs/` directory in this repo
2. Notify user that the file needs to be manually copied to HA
3. User will update via Unraid console:
   - Docker tab → homeassistant container → Console
   - Run: `vi /config/automations.yaml` (or `vi /config/scenes.yaml`, `vi /config/sensors.yaml`, `vi /config/scripts.yaml`)
   - Delete all content (in vi: `gg` then `dG`)
   - Paste new content
   - Save and exit (`:wq`)
4. **For scenes or scripts:** Use Developer Tools → YAML → Click "Scenes" or "Scripts" reload button
5. **For automations or sensors:** Restart Home Assistant container

**First-time sensor setup:**
1. Copy `configs/sensors.yaml` to `/config/sensors.yaml` on Unraid server (see above)
2. Edit `/config/configuration.yaml` and add: `sensor: !include sensors.yaml`
3. Restart Home Assistant container

**First-time scripts setup:**
1. Copy `configs/scripts.yaml` to `/config/scripts.yaml` on Unraid server (see above)
2. Edit `/config/configuration.yaml` and add: `script: !include scripts.yaml`
3. Use Developer Tools → YAML → Click "Scripts" reload button

**Automations included:**
- 1 Entertainment: Soundbar source selector
- 10 Critical notifications (bypass quiet hours 11pm-9am)
- 9 Important notifications (active hours 9am-11pm only)
- 3 Informational notifications (daily summaries at 9am)

**Quiet hours:** 11pm - 9am (Critical notifications bypass this)
**Notification service:** `notify.notify` (sends to all registered mobile devices)

### Automation Categories

Automations are organized into categories in the Home Assistant UI:

**Category Definitions** (stored in `configs/core.category_registry`):
- **Critical Alerts** (icon: `mdi:alert-circle`) - 10 automations
- **Important Notifications** (icon: `mdi:bell-alert`) - 9 automations
- **Daily Summaries** (icon: `mdi:calendar-today`) - 3 automations
- **Helpers** (icon: `mdi:cog`) - 1 automation

**Setting Up Categories:**

1. **Import category definitions:**
   - Copy contents of `configs/core.category_registry` from this repo
   - On Unraid server console: `vi /config/.storage/core.category_registry`
   - Replace content with the copied file
   - Restart Home Assistant

2. **Assign automations to categories:**
   - After importing automations, manually assign them to categories in the HA UI:
     - Go to Settings → Automations & Scenes
     - Click on an automation → Click the gear icon → Select category
   - Use the automation naming convention to identify categories:
     - `Critical - ...` → Critical Alerts category
     - `Important - ...` → Important Notifications category
     - `Informational - ...` → Daily Summaries category

---

## ⚠️ Critical Rules

### DO:
- ✅ Use WebSocket API for dashboard updates (documented in HOME_ASSISTANT_STATE.md)
- ✅ Use REST API for queries only
- ✅ Use `light` card type for dimmable lights (shows brightness slider)
- ✅ Use `entities` card type for on/off switches
- ✅ Use `media-control` card type for TVs and media players
- ✅ Use `thermostat` card type for air conditioners
- ✅ Use button cards with `tap_action` for scenes
- ✅ Check HOME_ASSISTANT_STATE.md for complete entity-to-room mappings
- ✅ Always add `"show_header_toggle": False` to ALL entities panels

### DON'T:
- ❌ Assume `light.*` entities are dimmable (check `supported_color_modes`)
- ❌ Automatically deploy config files (automations, scenes, sensors, scripts) - user applies them manually via vi

---

## 🔑 Quick Reference

**HA URL:** http://tower.local:8123  
**Dashboard:** http://tower.local:8123/clean-home  
**Token Location:** `~/.zshrc` environment variable `HA_TOKEN`  
**Load Token:** `source ~/.zshrc`

**WebSocket API:**
```python
HA_URL = "ws://tower.local:8123/api/websocket"
HA_TOKEN = os.environ.get("HA_TOKEN")
```

**REST API:**
```bash
curl -H "Authorization: Bearer $HA_TOKEN" http://tower.local:8123/api/states
```

---

## 📊 Dashboard Configuration

The dashboard includes:
- **4 air conditioners** with thermostat controls
- **6 dimmable lights** with brightness sliders
- **19 on/off switches** for ceiling lights, rail spots, and other fixtures
- **8 scenes** organized in 3 categories (defined in `configs/scenes.yaml`):
  - **Lighting Scenes:** Ambient 10%, Ambient 70%, Ambient 100%, All Off
  - **AC Scenes:** Living & Office (24°C), All On (24°C), All Off
  - **Leaving Home:** Everything Off (lights, ACs, TVs, cooktop, oven)
- **Entertainment devices:**
  - Living Room: 77" OLED TV with Soundbar Q990B
  - Bedroom: LG TV
- **Smart appliances** with conditional visibility:
  - Dishwasher, Oven, Cooktop, Washing Machine, Dryer
  - Controls appear only when relevant
  - NO global toggles on appliance panels
- **13 tabs total** (Scenes + 11 rooms + Car)

---

## 👤 User Preferences & Decisions (DO NOT CHANGE)

### Scenes

**Lighting Scenes:**
- **Ambient 10%**: Living Room + Kitchen window LED strips at 10% brightness (25/255)
- **Ambient 70%**: Living Room + Kitchen window LED strips at 70% brightness (178/255)
- **Ambient 100%**: Living Room + Kitchen window LED strips at 100% brightness (255/255)
- **All Off**: Turn off ALL lights and ventilators

**AC Scenes:**
- **Living & Office (24°C)**: Turn on ACs in Living Room + Office at 24°C in cool mode
- **All On (24°C)**: Turn on all 4 ACs at 24°C in cool mode
- **All Off**: Turn off all 4 ACs

**Leaving Home:**
- **Everything Off**: Turn off lights, ACs, TVs, cooktop power, oven power
  - **Excludes:** Washing machine, dryer, dishwasher (may want to leave running when away)

**Scene Implementation:**
- All scenes defined in `configs/scenes.yaml` (8 total scenes)
- Dashboard buttons call scene entities via `scene.turn_on` service
- Organized in 3 separate cards: Lighting Scenes, AC Scenes, Leaving Home
- After editing scenes.yaml, use scene reload (NOT container restart)

### Appliance Controls
- **Conditional visibility**: Show controls only when relevant
  - Finish time: Only when running
  - Pause/Resume: Only when running/paused
  - Door sensors: Only when open
- **NO global toggles** on ANY panels (`show_header_toggle: False`)

### Entertainment
- **Living Room**: Single entertainment card with TV and soundbar controls
  - Source selector: `input_select.soundbar_source` (HDMI/Bluetooth/Optical/WiFi/AUX)
- **Bedroom TV**: LG TV with media-control card

### Dashboard Structure
- **Title**: "Home"
- **Path**: `/clean-home`
- **Card Types**:
  - `light` card: For dimmable lights
  - `entities` card: For on/off switches and grouped controls
  - `media-control` card: For TVs and media players
  - Button cards with `tap_action`: For scenes

---

## 🗑️ Entity Management

### Deleting Entities from Registry

Use `scripts/delete_entities.sh` to remove entities from Home Assistant's entity registry.

**Run on Unraid NAS shell:**
```bash
./delete_entities.sh sensor.old_sensor switch.unused_switch light.removed_device
```

**What it does:**
1. Creates a timestamped backup of `core.entity_registry`
2. Removes specified entities from the registry JSON
3. Provides restore instructions if needed

**After running:**
- Restart Home Assistant container to apply changes
- If something goes wrong, restore from the backup file shown in output

**Note:** This script modifies `/mnt/cache/appdata/homeassistant/.storage/core.entity_registry` directly. Always verify entity IDs before deletion.

---

## 🆘 If You Get Stuck

1. Re-read `HOME_ASSISTANT_STATE.md` for complete technical documentation
2. Verify your WebSocket connection code matches the documented pattern
3. Check that `HA_TOKEN` is loaded: `echo $HA_TOKEN`
4. Test REST API queries work before trying WebSocket updates
5. Ask the user for clarification on specific issues

