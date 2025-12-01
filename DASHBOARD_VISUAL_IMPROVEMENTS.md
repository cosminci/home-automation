# Dashboard Visual Improvements Epic

**Status:** Analysis Complete - Ready for Implementation
**Started:** 2025-11-30
**Goal:** Improve visual appearance and ergonomics of Home Assistant dashboard

---

## Quick Start Context (For New Chat Sessions)

### Current Setup
- **Dashboard:** Generated via modular Python structure using WebSocket API
- **Location:** `http://tower.local:8123/clean-home`
- **Structure:** 13 tabs (Overview + 11 rooms + Car) using sections view layout
- **Key files:**
  - `generate_dashboard.py` - Main orchestrator script
  - `dashboard_helpers.py` - Helper functions for card creation
  - `templates/` - 6 decluttering card templates (JSON)
  - `rooms/` - 13 room view modules (Python)
  - `HOME_ASSISTANT_STATE.md`, `README.md` - Documentation

### Known Issues
- ❌ **Weather card is broken** - Max temp always shows current temp, very little info displayed
- ✅ **Car tab conditional visibility** - Already well optimized
- ✅ **Appliance conditional entities** - Already working well

### Cards Installed via HACS (15 total)
**High Value:** Mushroom, button-card, Stack In Card, mini-graph-card
**Test Needed:** Mini Media Player, Multiple Entity Row, Weather Radar Card, Horizon Card, Clock Weather Card
**Available:** Config Template Card (use only when needed)
**Skip:** Vertical Stack In Card (duplicate), Decluttering Card (not needed), Power Flow Card Plus, Battery State Card, Vacuum Card

### Implementation Priority
1. ✅ **Mushroom Climate Cards** - COMPLETED (individual room tabs)
2. ✅ **Mushroom Light Cards** - COMPLETED (all 6 dimmable lights)
3. ✅ **button-card for Scenes** - COMPLETED (Color coding + compact layout)
4. ✅ **Mushroom Entity Cards** - COMPLETED (Network devices + Appliances)
5. **Stack In Card** - Remove borders
6. **Fix Weather Display** - Replace broken weather card
7. **Test Mini Media Player** - Optional

### User Preferences
- ❌ No manual card size microtweaking
- ❌ No mobile vs desktop optimization (not natively supported)
- ✅ Python-generated dashboard (not YAML)
- ✅ Collapsible controls preferred
- ✅ Color coding for visual hierarchy

---

## Installed Cards Analysis

**Status:** ✅ User has installed the following cards via HACS

### Cards Installed & Analyzed:

1. ✅ **mini-graph-card** - Minimalistic graph card (210K downloads)
2. ✅ **Mushroom** - Modern card collection (199K downloads)
3. ✅ **Config Template Card** - Templatable configurations (175K downloads)
4. ✅ **Stack In Card** - Group cards without borders (167K downloads)
5. ✅ **Power Flow Card Plus** - Energy distribution visualization (101K downloads)
6. ✅ **Battery State Card** - Battery monitoring (98K downloads)
7. ✅ **button-card** - Highly customizable buttons (95K downloads)
8. ✅ **Vertical Stack In Card** - Vertical card grouping (94K downloads)
9. ✅ **Multiple Entity Row** - Multiple entities per row (85K downloads)
10. ✅ **Vacuum Card** - Vacuum cleaner controls (82K downloads)
11. ✅ **Weather Radar Card** - Rain viewer integration (81K downloads)
12. ✅ **Mini Media Player** - Compact media controls (78K downloads)
13. ✅ **Horizon Card** - Sun position visualization (70K downloads)
14. ✅ **Clock Weather Card** - Date/time with weather (69K downloads)
15. ✅ **Decluttering Card** - Template reuse tool (61K downloads)

---

## Card Applicability Assessment

### 🟢 HIGH VALUE - Adopt Immediately

#### 1. **Mushroom Cards** (Priority 1)
**What it does:** Complete card collection with modern, minimalist design
**Applicable to:**
- ✅ **Overview - Scenes buttons** → Mushroom button cards with color coding
- ✅ **All room tabs - Light controls** → Mushroom light cards (maintains brightness sliders)
- ✅ **All room tabs - AC controls** → Mushroom climate cards (collapsible controls!)
- ✅ **Living Room/Bedroom - Entertainment** → Mushroom media player cards
- ✅ **Network cards** → Mushroom entity cards for cleaner look
- ✅ **Appliance cards** → Mushroom entity cards as base

**Why adopt:**
- Native collapsible controls for climate cards (solves AC clutter)
- Better visual hierarchy with icons and colors
- Maintains all functionality (brightness sliders, dropdowns, etc.)
- Consistent modern look across entire dashboard

**Implementation order:** Start with climate cards (biggest visual impact)

---

#### 2. **button-card** (Priority 2)
**What it does:** Highly customizable button with templates, state-based styling, JavaScript support
**Applicable to:**
- ✅ **Overview - Scene buttons** → Replace current button entities
- ✅ **Network restart buttons** → Better visual feedback
- ✅ **Appliance stop/start buttons** → State-based colors

**Why adopt:**
- State-based color coding (green when running, red when off, etc.)
- Templates reduce code duplication
- JavaScript templates for complex logic
- Better than standard button entities

**Synergy:** Works great with Mushroom cards for consistent styling

---

#### 3. **mini-graph-card** (Priority 3)
**What it does:** Minimalistic sensor history graphs
**Applicable to:**
- ✅ **Insights Dashboard** → Already uses plotly, but mini-graph-card is lighter
- ⚠️ **Main Dashboard** → Could add temperature trend graphs to climate cards
- ❌ **Not needed** if current plotly graphs work well

**Why consider:**
- Lighter weight than plotly
- Better integration with Lovelace
- Customizable colors, fills, animations

**Decision needed:** Compare with existing plotly implementation in insights dashboard

---

#### 4. **Stack In Card** (Priority 4)
**What it does:** Groups multiple cards without visible borders
**Applicable to:**
- ✅ **All tabs** → Cleaner visual grouping
- ✅ **Appliance cards** → Group status + controls without card borders
- ✅ **Network cards** → Group device info + buttons seamlessly

**Why adopt:**
- Reduces visual clutter from card borders
- Makes grouped controls look like single cohesive unit
- Works with any card type

**Synergy:** Combine with Mushroom cards for cleanest look

---

### 🟡 MEDIUM VALUE - Consider Selectively

#### 5. **Multiple Entity Row** (Priority 5)
**What it does:** Shows multiple entity states/attributes in a single row
**Applicable to:**
- ⚠️ **Climate overview** → Show temp + humidity in one row
- ⚠️ **Network cards** → Status + uptime in one row
- ❌ **Most other cards** → Current layout is already good

**Why consider:**
- Saves vertical space
- Good for read-only status displays

**Concern:** May reduce touch target size on mobile

---

#### 6. **Mini Media Player** (Priority 6)
**What it does:** Compact media player with artwork, shortcuts, grouping
**Applicable to:**
- ⚠️ **Living Room - TV & Soundbar** → More compact than current
- ⚠️ **Bedroom - LG TV** → Cleaner media controls

**Why consider:**
- More compact than standard media-control card
- Better artwork display
- Shortcuts for common actions

**Decision needed:** Test if it works with LG WebOS TV and Samsung Soundbar integrations

---

#### 7. **Config Template Card** (Priority 7)
**What it does:** Allows Jinja2 templates in any card configuration
**Status:** ✅ Installed and available if needed
**Applicable to:**
- ⚠️ **Conditional visibility** → More complex conditions than standard conditional cards
- ⚠️ **Dynamic content** → Template-based card generation
- ⚠️ **Complex state logic** → When standard card options insufficient

**Why keep available:**
- More powerful than standard conditional cards
- Can reduce code duplication for complex scenarios
- Good to have in toolkit for edge cases

**When to use:** Only when standard card features and conditionals are insufficient

---

### 🔴 LOW VALUE / NOT APPLICABLE

#### 8. **Vertical Stack In Card** ❌ DUPLICATE
**What it does:** Same as "Stack In Card" but vertical only
**Why skip:** Stack In Card does the same thing and more

---

#### 9. **Decluttering Card** ❌ NOT NEEDED
**What it does:** Template reuse for card configurations
**Why skip:**
- You generate dashboard via Python script
- Templates better handled in Python than YAML
- button-card already has template support

---

#### 10. **Power Flow Card Plus** ❌ NOT APPLICABLE
**What it does:** Energy distribution visualization (solar, grid, battery, home)
**Why skip:** You don't have solar panels or home battery system

---

#### 11. **Battery State Card** ❌ NOT APPLICABLE
**What it does:** Monitors battery levels across multiple devices
**Why skip:**
- You don't have battery-powered Zigbee devices yet
- Car battery already shown in car tab
- Revisit when you add Zigbee sensors

---

#### 12. **Vacuum Card** ❌ NOT APPLICABLE
**What it does:** Robot vacuum controls
**Why skip:** You don't have a robot vacuum

---

#### 13. **Weather Radar Card** ⚠️ CONSIDER
**What it does:** Animated rain radar from RainViewer
**Why consider:** Current weather card has issues (max temp always shows current temp, broken plugin)
**Applicable to:**
- ✅ **Overview tab** → Replace broken weather card
- ✅ **Could add weather info** → To other relevant tabs

**Decision needed:** Test if this provides better weather display than current broken card

---

#### 14. **Horizon Card** ⚠️ CONSIDER
**What it does:** Visualizes sun position over horizon
**Why consider:** Could replace/supplement broken weather card
**Applicable to:**
- ⚠️ **Overview tab** → Sun position visualization
- ⚠️ **Insights dashboard** → Daily sun patterns

**Decision needed:** Test if this adds value given current weather card is broken

---

#### 15. **Clock Weather Card** ⚠️ CONSIDER
**What it does:** Clock with date/time and weather info
**Why consider:** Current weather card is broken (max temp = current temp)
**Applicable to:**
- ✅ **Overview tab** → Replace broken weather card with clock + weather combo

**Decision needed:** Test if this provides better weather display than current implementation

---

## Implementation Roadmap

### Phase 1: Mushroom Climate Cards ✅ COMPLETED
**Goal:** Replace individual room thermostat cards with Mushroom climate cards
**Impact:** Immediate visual improvement + collapsible controls
**Effort:** Low (straightforward replacement)
**Completed:** 2025-11-30

**Cards replaced:**
1. ✅ Living Room tab - AC thermostat → Mushroom climate card
2. ✅ Bedroom tab - AC thermostat → Mushroom climate card
3. ✅ Kid's Room tab - AC thermostat → Mushroom climate card
4. ✅ Office tab - AC thermostat → Mushroom climate card
5. ⏭️ Overview tab - Climate section - LEFT UNCHANGED (will be addressed separately)

**Final Configuration:**
```python
{
    "type": "custom:mushroom-climate-card",
    "entity": "climate.ac_living",  # or bedroom, iacopewee, office
    "name": "Air Conditioner",
    "icon": "mdi:air-conditioner",
    "show_temperature_control": True,
    "hvac_modes": ["off", "cool", "heat", "dry", "fan_only", "auto"],
    "collapsible_controls": True,
    "grid_options": {
        "columns": 12
    }
}
```

**Results:**
- ✅ Modern, clean Mushroom design
- ✅ Current temperature displayed by default (no need for `secondary_info`)
- ✅ Collapsible controls reduce clutter when AC is off
- ✅ All HVAC modes available
- ⚠️ Preset modes (eco/ai/none) removed - acceptable tradeoff for modern design

**Key Learnings:**
- Mushroom climate cards show current temperature by default
- `secondary_info: "state"` shows HVAC state (off/cool/heat), not temperature
- Preset modes are not supported by Mushroom climate cards
- No need for separate temperature display cards

---

### Phase 2: Mushroom Light Cards ✅ COMPLETED
**Goal:** Replace all light cards with Mushroom equivalents
**Impact:** Consistent modern look, better color representation
**Effort:** Low
**Completed:** 2025-11-30

**Cards replaced:**
1. ✅ Living Room - LED Strip Window (`light.led_strip_window_2`)
2. ✅ Kitchen - LED Strip Window (`light.led_strip_window_3`)
3. ✅ Bedroom - LED Strip Window (`light.led_strip`)
4. ✅ Kid's Room - LED Strip Window (`light.led_strip_window_4`)
5. ✅ Kid's Room - LED Strip Bed (`light.led_strip_bed`)
6. ✅ Office - LED Strip Window (`light.led_strip_window`)

**Final Configuration:**
```python
{
    "type": "custom:mushroom-light-card",
    "entity": "light.led_strip_window_2",  # or other light entities
    "name": "LED Strip Window",
    "icon": "mdi:led-strip-variant",
    "show_brightness_control": True,
    "collapsible_controls": True,
    "grid_options": {
        "columns": 12
    }
}
```

**Results:**
- ✅ Modern Mushroom design consistent with climate cards
- ✅ Brightness slider available via collapsible controls
- ✅ Cleaner, more compact design
- ✅ All 6 dimmable lights successfully migrated

**Key Learnings:**
- `show_brightness_control: True` enables brightness slider
- `collapsible_controls: True` keeps controls hidden when light is off
- `use_light_color` NOT used - LED strips are fixed 2700K warm white (brightness only, no color temperature or RGB)
- On/off switches kept in entities cards (will be addressed in Phase 4)

---

### Phase 3: button-card for Scenes ✅ COMPLETED
**Goal:** Replace scene buttons with button-card for color coding + compact layout
**Impact:** Better visual hierarchy, space efficiency
**Effort:** Medium
**Completed:** 2025-11-30

**Implementation:**
1. ✅ **Compact Ambient Lighting** - Used `multiple-entity-row` to combine 3 ambient scenes (10%, 70%, 100%) into one row with icon buttons
2. ✅ **Color-coded button-card scenes:**
   - **Lighting scenes** → Warm orange/amber (`rgb(255, 152, 0)`)
   - **AC scenes** → Cool blue (`rgb(33, 150, 243)`)
   - **Everything Off** → Red/warning (`rgb(244, 67, 54)`)

**Final Configuration:**

**Compact Ambient Row (multiple-entity-row):**
```python
{
    "type": "custom:multiple-entity-row",
    "entity": "scene.ambient_10",
    "name": "Open Space Ambient",
    "icon": "mdi:lightbulb-group",
    "show_state": False,
    "entities": [
        {
            "icon": "mdi:brightness-4",
            "tap_action": {
                "action": "call-service",
                "service": "scene.turn_on",
                "service_data": {"entity_id": "scene.ambient_10"}
            }
        },
        {
            "icon": "mdi:brightness-6",
            "tap_action": {
                "action": "call-service",
                "service": "scene.turn_on",
                "service_data": {"entity_id": "scene.ambient_70"}
            }
        },
        {
            "icon": "mdi:brightness-7",
            "tap_action": {
                "action": "call-service",
                "service": "scene.turn_on",
                "service_data": {"entity_id": "scene.ambient_100"}
            }
        }
    ]
}
```

**Color-coded button-card (example - AC scene):**
```python
{
    "type": "custom:button-card",
    "name": "Living & Office (24°C)",
    "icon": "mdi:air-conditioner",
    "tap_action": {
        "action": "call-service",
        "service": "scene.turn_on",
        "service_data": {"entity_id": "scene.ac_living_office"}
    },
    "color": "rgb(33, 150, 243)",  # Blue for AC
    "styles": {
        "card": [
            {"background-color": "rgba(33, 150, 243, 0.1)"},
            {"border": "1px solid rgba(33, 150, 243, 0.3)"}
        ]
    }
}
```

**Results:**
- ✅ Compact ambient lighting row - 3 scenes in one row instead of 3 separate buttons
- ✅ Clear visual hierarchy with color coding:
  - Orange/amber for lighting scenes
  - Blue for AC scenes
  - Red for "Everything Off"
- ✅ Subtle background colors and borders for better visual feedback
- ✅ Space savings - reduced from 7 buttons to 5 rows (1 compact + 4 buttons)

**Key Learnings:**
- `multiple-entity-row` perfect for grouping related scenes with different intensities
- `button-card` provides excellent color customization with `color` and `styles.card`
- Subtle background colors (`rgba` with 0.1 opacity) + borders provide visual hierarchy without being overwhelming
- Icon-only buttons in `multiple-entity-row` work well for intensity variations (brightness-4, brightness-6, brightness-7)

---

### Phase 4: Mushroom Entity Cards ✅ COMPLETED
**Goal:** Replace standard entities cards with Mushroom equivalents
**Impact:** Consistent look across dashboard
**Effort:** Low-Medium

**Cards replaced:**
1. ✅ All light switch cards (on/off switches) - Converted to Mushroom entity cards with icon-only display
2. ✅ Network device cards - Converted to Mushroom entity cards with button-card for restart/power cycle buttons
3. ✅ Appliance cards - Converted to Mushroom entity cards for status/power/warnings, kept conditional entities for programs

**Implementation Details:**

**Network Devices:**
- Living Room AP: Mushroom entity cards for status/uptime + button-card for restart/power cycle
- Kid's Room AP: Mushroom entity cards for status/uptime + button-card for restart/power cycle
- Hallway (Storage Room): Mushroom entity cards for Gateway/Switch status/uptime + button-card for restart buttons + Mushroom entity card for VPN toggle
- Used `icon_color: "blue"` for status sensors, `icon_color: "green"` for VPN
- Used button-card with orange styling (`rgba(255, 152, 0, 0.1)` background) for restart/power cycle buttons

**Appliances:**
- Dishwasher: Mushroom entity card for status + conditional entities for programs + Mushroom entity cards for power/warnings
- Oven: Mushroom entity card for status + conditional entities for programs/temperature + Mushroom entity cards for power/child lock
- Cooktop: Mushroom entity cards for status/power/child lock (no conditional entities needed)
- Washing Machine: Mushroom entity card for status + conditional entities for programs + Mushroom entity card for power
- Dryer: Mushroom entity card for status + conditional entities for programs + Mushroom entity cards for power/child lock
- Used `icon_color: "blue"` for status, `icon_color: "orange"` for oven/cooktop, `icon_color: "green"` for power, `icon_color: "red"` for child lock

**Benefits Achieved:**
- Consistent Mushroom design language across all entity cards
- Better icon and color support for visual hierarchy
- Cleaner typography and spacing
- Maintained all functionality (conditional visibility, dropdowns, buttons)

---

### Phase 5: Stack In Card (Medium Impact)
**Goal:** Remove card borders for cleaner grouping
**Impact:** Reduced visual clutter
**Effort:** Low (wrap existing cards)

**Where to apply:**
- Appliance cards (group status + controls)
- Network cards (group device info + buttons)
- Entertainment cards (group TV + soundbar)

**Benefits:**
- Cards look like cohesive units
- Less visual noise from borders
- Cleaner, more professional look

---

### Phase 6: Fix Weather Display (Medium Priority)
**Goal:** Replace broken weather card with better alternative
**Impact:** Actually useful weather information
**Effort:** Low-Medium (test 3 weather card options)

**Current problem:**
- Weather card shows very little info
- Max temp always equals current temp (broken plugin)

**Options to test:**
1. **Weather Radar Card** - Animated rain radar + weather info
2. **Clock Weather Card** - Clock + date + weather combo
3. **Horizon Card** - Sun position + weather data

**Decision criteria:**
- Shows accurate max/min temps
- Displays useful weather info (precipitation, forecast)
- Fits well in Overview tab layout

---

### Phase 7: Evaluate Mini Media Player (Low Priority)
**Goal:** Test if mini-media-player improves entertainment cards
**Impact:** Potentially more compact media controls
**Effort:** Medium (requires testing with LG WebOS and Samsung integrations)

**Test with:**
- Living Room: 77" OLED + Soundbar Q990B
- Bedroom: LG TV

**Decision criteria:**
- Must work with existing integrations
- Must be more compact than current media-control cards
- Must support source selection for soundbar

---

### Phase 8: Consider Multiple Entity Row (Optional)
**Goal:** Compress some status displays
**Impact:** Space savings in specific cards
**Effort:** Low

**Potential uses:**
- Climate overview: Temp + humidity in one row
- Network cards: Status + uptime in one row

**Concern:** May reduce touch target size - test on mobile first

---

## Detailed Implementation Plans

### Phase 2: Specific Card Improvements

### 2.1 Overview Tab - Climate Card
**Current:** Standard `entities` card with broken weather + 4 AC climate entities
**Recommendation:**
- **REPLACE broken weather card** with Weather Radar Card, Clock Weather Card, or Horizon Card
- Replace 4 AC climate entities with Mushroom climate cards
- Use `collapsible_controls: true` to hide temp controls by default

**Weather card problem:**
- Current weather shows very little info
- Max temp always equals current temp (broken plugin)
- Need to test alternative weather cards

**Implementation:**
```yaml
# Replace current climate entities with:
- type: custom:mushroom-climate-card
  entity: climate.ac_living
  name: Living Room
  icon: mdi:sofa
  collapsible_controls: true
  hvac_modes: [off, cool, heat, dry, fan_only, auto]
  show_temperature_control: true
```

---

### 2.2 Overview Tab - Scenes Card
**Current:** Button entities within entities card (3 sections)
**Recommendation:** Replace with button-card for color coding

**Implementation:**
```yaml
# Lighting Scenes - Warm colors
- type: custom:button-card
  name: Ambient 10%
  icon: mdi:movie-open
  tap_action:
    action: call-service
    service: scene.turn_on
    service_data:
      entity_id: scene.ambient_10
  styles:
    card:
      - background-color: 'rgba(255, 193, 7, 0.2)'
    icon:
      - color: '#FFC107'

# AC Scenes - Cool colors
- type: custom:button-card
  name: Living & Office (24°C)
  icon: mdi:air-conditioner
  tap_action:
    action: call-service
    service: scene.turn_on
    service_data:
      entity_id: scene.ac_living_office
  styles:
    card:
      - background-color: 'rgba(33, 150, 243, 0.2)'
    icon:
      - color: '#2196F3'

# Everything Off - Warning color
- type: custom:button-card
  name: Everything Off
  icon: mdi:home-export-outline
  tap_action:
    action: call-service
    service: script.turn_on
    service_data:
      entity_id: script.everything_off
  styles:
    card:
      - background-color: 'rgba(244, 67, 54, 0.2)'
    icon:
      - color: '#F44336'
```

---

### 2.3 Room Tabs - Light Controls
**Current:** Mix of `entities` cards (switches) and `light` cards (dimmable)
**Recommendation:**
- Dimmable lights → Mushroom light cards with `use_light_color: true`
- On/off switches → Mushroom entity cards

**Implementation:**
```yaml
# Dimmable lights
- type: custom:mushroom-light-card
  entity: light.led_strip_window_2
  name: LED Strip Window
  icon: mdi:led-strip-variant
  use_light_color: true
  show_brightness_control: true
  collapsible_controls: true

# On/off switches
- type: custom:mushroom-entity-card
  entity: switch.dining_light
  name: Dining Light
  icon: mdi:ceiling-light
  tap_action:
    action: toggle
```

---

### 2.4 Kitchen Tab - Appliance Cards
**Current:** Conditional entities showing status, programs, finish times
**Recommendation:**
- Use Mushroom entity cards as base
- Keep conditional visibility (already works well)
- Wrap in Stack In Card to remove borders

**Implementation:**
```yaml
- type: custom:stack-in-card
  cards:
    - type: custom:mushroom-entity-card
      entity: sensor.dishwasher_operation_state
      name: Dishwasher
      icon: mdi:dishwasher

    - type: entities
      show_header_toggle: false
      entities:
        - type: conditional
          conditions:
            - entity: sensor.dishwasher_operation_state
              state_not: inactive
          row:
            entity: sensor.dishwasher_program_finish_time
            name: Finish Time
            icon: mdi:clock-outline
        # ... other conditional entities
```

**Note:** Mushroom doesn't have built-in collapsible entity rows - would need fold-entity-row card (not installed)

---

### 2.5 Living Room & Bedroom - Entertainment Cards
**Current:** Entities card with sections for TV and Soundbar
**Recommendation:** Test mini-media-player, but may not improve much

**Current structure works well:**
- Combined TV + Soundbar in one card
- Source selector for soundbar
- Sections provide clear separation

**Decision:** Keep current structure unless mini-media-player testing shows clear benefit

---

### 2.6 Network Cards (Living Room, Kid's Room, Hallway)
**Current:** Entities cards with status, uptime, restart buttons
**Recommendation:**
- Use Mushroom entity cards for cleaner look
- Keep all info visible (uptime is useful)
- Use button-card for restart buttons with visual feedback

**Implementation:**
```yaml
- type: custom:mushroom-entity-card
  entity: sensor.ap_living_state
  name: Access Point
  icon: mdi:access-point

- type: custom:mushroom-entity-card
  entity: sensor.ap_living_uptime
  name: Uptime
  icon: mdi:clock-outline

- type: custom:button-card
  name: Restart AP
  icon: mdi:restart
  tap_action:
    action: call-service
    service: button.press
    service_data:
      entity_id: button.ap_living_restart
  styles:
    card:
      - background-color: 'rgba(255, 152, 0, 0.2)'
    icon:
      - color: '#FF9800'
```

---

### 2.7 Car Tab - Conditional Visibility Cards
**Current:** Doors & Windows card with conditional rows (only show when open)
**Status:** ✅ Already optimized - no changes needed

---

## Summary: Cards to Adopt

### ✅ ADOPT - High Value
1. **Mushroom Cards** - Complete replacement for climate, light, entity cards
2. **button-card** - Scene buttons, restart buttons, state-based styling
3. **Stack In Card** - Remove borders for cleaner grouping
4. **mini-graph-card** - Consider for insights dashboard (compare with plotly)

### ⚠️ TEST - Medium Value
5. **Mini Media Player** - Test with LG WebOS and Samsung Soundbar
6. **Multiple Entity Row** - Test for space savings (check mobile usability)
7. **Weather Radar Card** - Test as replacement for broken weather card
8. **Horizon Card** - Test for sun position visualization
9. **Clock Weather Card** - Test as replacement for broken weather card

### ✅ AVAILABLE IF NEEDED
10. **Config Template Card** - Installed, use for complex templating scenarios

### ❌ SKIP - Not Applicable
11. **Vertical Stack In Card** - Duplicate of Stack In Card
12. **Decluttering Card** - Not needed (Python generates dashboard)
13. **Power Flow Card Plus** - No solar/battery system
14. **Battery State Card** - No battery devices yet
15. **Vacuum Card** - No vacuum

---

## Implementation Order (Logical Sequence)

### Step 1: Foundation - Mushroom Climate Cards
**Why first:** Biggest visual impact, enables collapsible controls
**Effort:** Low
**Risk:** Low (straightforward replacement)

### Step 2: Mushroom Light Cards
**Why second:** Builds on Mushroom design language
**Effort:** Low
**Risk:** Low (verify brightness sliders work)

### Step 3: button-card for Scenes
**Why third:** Requires template setup, builds on visual improvements
**Effort:** Medium
**Risk:** Low (just buttons)

### Step 4: Mushroom Entity Cards
**Why fourth:** Complete the Mushroom migration
**Effort:** Medium
**Risk:** Low

### Step 5: Stack In Card Grouping
**Why fifth:** Wraps existing cards, should be done after card types finalized
**Effort:** Low
**Risk:** Low

### Step 6: Fix Weather Display
**Why sixth:** Current weather card is broken, need working alternative
**Effort:** Low-Medium (test 3 options)
**Risk:** Low

### Step 7: Test Mini Media Player (Optional)
**Why last:** Requires integration testing, may not adopt
**Effort:** Medium
**Risk:** Medium (integration compatibility)

---

## Notes on Missing Cards

### fold-entity-row - NOT INSTALLED
**What it does:** Collapsible rows within entity cards
**Why we don't need it:**
- Mushroom climate cards have built-in `collapsible_controls`
- Appliance conditional visibility already works well
- Would add complexity without clear benefit

### card-mod - NOT INSTALLED
**What it does:** CSS customization for any card
**Why we don't need it (yet):**
- button-card has built-in styling
- Mushroom cards have good default styling
- Can add later if specific customization needed

### Config Template Card - INSTALLED
**What it does:** Allows Jinja2 templates in any card configuration
**Status:** ✅ Installed and available
**When to use:**
- Complex conditional logic beyond standard conditional cards
- Dynamic content generation based on templates
- Edge cases where standard card features insufficient
**Note:** Keep in toolkit, use only when needed

---

## Floor Plan View (Future Consideration)

**Status:** 🔮 Deferred until main dashboard improvements complete
**Requirements:**
- User has 2D apartment plan
- Create floor plan image with transparent background
- Use `picture-elements` card type
- Map clickable zones to rooms/devices

**Effort:** High (image creation, zone mapping, testing)
**Impact:** High (very cool visual navigation)
**Decision:** Revisit after Phases 1-5 complete

---

## Questions Answered

1. ✅ **Which Mushroom cards did you install?** - Full Mushroom collection
2. ❌ **Did you install card-mod?** - No (not needed yet)
3. ❌ **Did you install fold-entity-row?** - No (Mushroom has collapsible controls)
4. ⏳ **Which theme did you choose?** - User researching independently
5. ✅ **Do themes work on both mobile and web?** - Yes, themes are server-side

---

## Rejected Ideas (From Previous Analysis)

- ❌ Manual card size microtweaking - User confirmed this is a lost game
- ❌ Mobile vs desktop optimization - No native HA support for this
- ❌ Custom header minimization - Current header already minimal
- ❌ Auto-entities/filtered views - Complexity vs usefulness unclear
- ❌ Better thermostat card - Mushroom climate card IS the better alternative

