# 🏠 Home Assistant Dashboard - Start Here

## 📋 Quick Context

You are working with a Home Assistant dashboard at **http://tower.local:8123/clean-home** (title: "Home")

The dashboard includes 13 tabs: Scenes + 11 rooms + Car. Features lighting controls, air conditioners (4 rooms), entertainment devices (TVs & soundbar), smart appliances with conditional controls, and Hyundai Tucson vehicle monitoring.

---

## 📁 Files in This Directory

### ✅ Keep These Files
1. **`HOME_ASSISTANT_STATE.md`** - Complete technical documentation (READ THIS FIRST)
2. **`START_HERE.md`** - This file (quick start guide)
3. **`generate_dashboard.py`** - Dashboard generation script ✅ WORKING
4. **`automations.yaml`** - All Home Assistant automations (soundbar + notifications) ✅ WORKING
5. **`scripts/HyundaiFetchApiTokensSelenium.py`** - Hyundai EU refresh token extractor
6. **`create_soundbar_helpers.md`** - Instructions for creating soundbar dropdown helpers (reference only)

### ❌ All Other Files Are Obsolete
If you see any other `.py`, `.yaml`, or `.md` files, they are junk from previous attempts.

---

## 🚀 Working with the Dashboard

### Step 1: Read the Documentation
Open and read **`HOME_ASSISTANT_STATE.md`** completely. It contains:
- How to connect to HA (WebSocket API - the ONLY method that works)
- Complete lighting inventory with all 6 dimmable lights
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
Modify `generate_dashboard.py` as needed and deploy:
```bash
source ~/.zshrc && source /tmp/ha_venv/bin/activate && python3 generate_dashboard.py
```

---

## 🔔 Working with Automations

All automations are in `automations.yaml` (23 total).

**To update automations:**
1. Edit `configs/automations.yaml` directly
2. Copy the entire file contents
3. On Unraid server:
   - Docker tab → homeassistant container → Console
   - Run: `vi /config/automations.yaml`
   - Delete all content (in vi: `gg` then `dG`)
   - Paste new content
   - Save and exit (`:wq`)
4. Restart Home Assistant container

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

**Setting Up Categories (After Fresh Install):**

1. **Import category definitions:**
   - Copy contents of `configs/core.category_registry` from this repo
   - On Unraid server console: `vi /config/.storage/core.category_registry`
   - Replace content with the copied file
   - Restart Home Assistant

2. **Assign automations to categories:**
   - Category assignments are stored in `core.entity_registry` (NOT in git - auto-managed by HA)
   - After importing automations, manually assign them to categories in the HA UI:
     - Go to Settings → Automations & Scenes
     - Click on an automation → Click the gear icon → Select category
   - Use the automation naming convention to identify categories:
     - `Critical - ...` → Critical Alerts category
     - `Important - ...` → Important Notifications category
     - `Informational - ...` → Daily Summaries category

**Note:** Category-to-automation mappings cannot be automated because they're stored in `core.entity_registry`, which contains ALL entities in your HA instance and is auto-managed by Home Assistant.

---

## ⚠️ Critical Rules

### DO:
- ✅ Use WebSocket API for dashboard updates (documented in HOME_ASSISTANT_STATE.md)
- ✅ Use REST API for queries only
- ✅ Use `light` card type for dimmable lights (shows brightness slider)
- ✅ Use `entities` card type for on/off switches
- ✅ Use `media-control` card type for TVs and media players (shows volume slider + mute)
- ✅ Use `thermostat` card type for air conditioners (shows temp dial + mode controls)
- ✅ Use button cards with `tap_action` for scenes (NO script files)
- ✅ Check HOME_ASSISTANT_STATE.md for complete entity-to-room mappings
- ✅ Always add `"show_header_toggle": False` to ALL entities panels (prevents dangerous global toggles)

### DON'T:
- ❌ Create YAML script files (cannot be installed via API)
- ❌ Try alternative connection methods (the documented method WORKS)
- ❌ Assume `light.*` entities are dimmable (check `supported_color_modes`)
- ❌ Use `light` card for `light.ceiling_spots` in Living Room (it's NOT dimmable)

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
- **4 air conditioners** with thermostat controls:
  - Living Room: AC - Living (`climate.ac_living`)
  - Bedroom: AC - Bedroom (`climate.ac_bedroom`)
  - Office: AC - Office (`climate.ac_office`)
  - Kid's Room: AC - Iacopewee (`climate.ac_iacopewee`)
- **6 dimmable lights** with brightness sliders:
  - Office: LED Strip Window (`light.led_strip_window`)
  - Living Room: LED Strip Window (`light.led_strip_window_2`)
  - Kitchen: LED Strip Window (`light.led_strip_window_3`)
  - Bedroom: LED Strip Window (`light.led_strip`)
  - Kid's Room: LED Strip Window (`light.led_strip_window_4`)
  - Kid's Room: LED Strip Bed (`light.led_strip_bed`)
- **19 on/off switches** for ceiling lights, rail spots, and other fixtures
- **8 scenes** organized in 3 categories:
  - **Lighting Scenes:** Cinema 10%, Ambient 80%, All Off
  - **AC Scenes:** Living & Office (24°C), All On (24°C), All Off
  - **Leaving Home:** Everything Off (lights, ACs, TVs, cooktop, oven)
- **Entertainment devices:**
  - Living Room: 77" OLED TV (`media_player.77_oled`) - controls Soundbar Q990B via ARC
  - Bedroom: LG TV (`media_player.lg_webos_tv_oled48c22lb`) - ⚠️ Cannot turn on remotely (use ThinQ app first)
- **Smart appliances** with conditional visibility:
  - Dishwasher, Oven, Cooktop, Washing Machine, Dryer
  - Controls appear only when relevant (e.g., finish time only when running)
  - NO global toggles on appliance panels (safety feature)
- **13 tabs total** (Scenes + 11 rooms + Car)

---

## 👤 User Preferences & Decisions (DO NOT CHANGE)

### Scenes

**Lighting Scenes:**
- **Cinema (10%)**: Living Room + Kitchen window LED strips at 10% brightness
- **Ambient (80%)**: Living Room + Kitchen window LED strips at 80% brightness
- **All Off**: Turn off ALL lights and ventilators (6 dimmable LED strips + 20 light switches + 2 ventilators = 28 total)
  - Uses `homeassistant.turn_off` service (works with both light.* and switch.* entities)
  - Includes: 6 dimmable LED strips, 15 ceiling/rail/wall lights, 3 LED strip switches, 2 ventilators
  - Note: `light.ceiling_spots` (Living Room) is NOT dimmable - same model as hallway spots
  - Netatmo integration has no "turn off all" command - must list all entities explicitly

**AC Scenes:**
- **Living & Office (24°C)**: Turn on ACs in Living Room + Office at 24°C in cool mode
  - Living Room and Office are connected (open space)
  - Excludes bedroom ACs (separate climate zones)
- **All On (24°C)**: Turn on all 4 ACs at 24°C in cool mode (Living, Bedroom, Office, Kid's Room)
- **All Off**: Turn off all 4 ACs (Living, Bedroom, Office, Kid's Room)

**Leaving Home:**
- **Everything Off**: Turn off lights, ACs, TVs, cooktop power, oven power
  - **Includes:** 4 ACs, 6 dimmable LED strips, 19 light switches, 2 ventilators, 2 TVs, cooktop power, oven power
  - **Excludes:** Washing machine, dryer, dishwasher (may want to leave running when away)
  - Uses `homeassistant.turn_off` service (works with climate.*, light.*, switch.*, media_player.* entities)

**Scene Implementation:**
- ✅ Use button cards with direct service calls (NO script files)
- ✅ Compact format (NOT giant buttons filling the screen)
- ✅ Organized in 3 separate cards: Lighting Scenes, AC Scenes, Leaving Home

### Room Icons
- **Kid's Room**: `mdi:teddy-bear` (NOT `mdi:account`)

### Appliance Controls
- **Show finish time only** (not separate progress row)
- **Conditional visibility**: Show controls only when relevant
  - Finish time: Only when running
  - Pause/Resume: Only when running/paused
  - Door sensors: Only when open
- **NO global toggles** on ANY panels - lights or appliances (`show_header_toggle: False`)
- **Dishwasher naming**:
  - "Salt Warning" (not "Salt Level") - makes on/off sensible
  - "Rinse Aid Warning" (not "Rinse Aid") - makes on/off sensible
- **Removed entities**:
  - Oven pause/resume buttons (don't work - throw errors)
  - Washing machine child lock (shows unavailable)
  - Oven pre-heat sensor (not useful)

### Entertainment
- **Living Room**: Single entertainment card with TV and soundbar controls
  - **TV**: `media_player.77_oled` (LG OLED)
  - **Soundbar**: `media_player.soundbar_q990b` (Samsung Q990B)
    - Power & Volume control
    - Source selector: `input_select.soundbar_source` (HDMI/Bluetooth/Optical/WiFi/AUX)
    - **Note**: Sound mode control NOT supported by SmartThings integration (use SmartThings app)
- **Bedroom TV**: Use `media-control` card for `media_player.lg_webos_tv_oled48c22lb`
  - ⚠️ Cannot turn on remotely - must use ThinQ app first, then HA works
- **Volume & Mute**: Both TVs have volume sliders and mute buttons

### Dashboard Structure
- **Title**: "Home" (not "Clean Home")
- **Path**: `/clean-home` (URL path stays the same)
- **Card Types**:
  - `light` card: For dimmable lights (shows brightness slider)
  - `entities` card: For on/off switches and grouped controls
  - `media-control` card: For TVs and media players
  - Button cards with `tap_action`: For scenes

---

## 🆘 If You Get Stuck

1. Re-read `HOME_ASSISTANT_STATE.md` - the answer is probably there (includes complete entity-to-room mappings)
2. Verify your WebSocket connection code matches the documented pattern
3. Check that `HA_TOKEN` is loaded: `echo $HA_TOKEN`
4. Test REST API queries work before trying WebSocket updates
5. Ask the user for clarification on specific issues

**Remember:** The connection methods documented in `HOME_ASSISTANT_STATE.md` WORK. If you get errors, debug your code, don't try alternative methods.

---

Good luck! 🚀

