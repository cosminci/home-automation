# Smart Climate Control - Implementation Tracker

**Status:** 📋 Planning Phase
**Priority:** High (energy savings potential)
**Dependencies:** Weather integration (built-in), Ubiquiti integration (for presence)

---

## 🎯 Goals

1. **Daily Climate Monitoring:** Consolidated daily summary with climate, lighting, and energy insights
2. **Real-time Dashboard:** Main overview showing current outdoor/indoor temps and AC status
3. **Historical Insights:** Dedicated dashboard for previous day/night analysis
4. **Energy Savings:** Reduce AC runtime and electricity costs by 20-40%
5. **Weather-Aware Cooling:** Adjust AC behavior based on outdoor conditions (future)
6. **Presence-Aware:** Only cool when home (requires Ubiquiti presence detection - future)

---

## 🔧 Current Setup

### Air Conditioners (4 units)
- **Living Room:** `climate.ac_living`
- **Bedroom:** `climate.ac_bedroom`
- **Office:** `climate.ac_office`
- **Kid's Room:** `climate.ac_iacopewee`

**Hardware:** ConnectLife integration (Hisense ceiling duct units)  
**Capabilities:** Cool, Heat, Dry, Fan Only, Auto | Temp 16-32°C | Eco/AI presets

### Current Issues
- ✅ AC extreme temperature alert (>28°C or <18°C)
- ✅ AC running >8 hours alert (suggests inefficiency)
- ❌ No weather awareness
- ❌ No presence detection
- ❌ Manual control only

---

## 📚 Research Findings

### Weather Integration (Built-in)

#### Met.no Integration
**Status:** ✅ Available (Recommended)  
**Documentation:** https://www.home-assistant.io/integrations/met/

**Features:**
- [ ] Current outdoor temperature
- [ ] Humidity
- [ ] Weather condition (sunny, cloudy, rainy)
- [ ] Hourly forecast
- [ ] Daily forecast

**Requirements:**
- Location coordinates (latitude/longitude)
- No API key needed
- Free, unlimited calls

**Feasibility:** ✅ HIGH - Built-in, no dependencies

---

## 🚀 Implementation Plan

### Phase 1: Dashboard & Daily Summary (CURRENT FOCUS)

#### A. Main Home Overview Dashboard
**Goal:** Real-time climate monitoring + quick access to scenes

**Components:**
1. **Scenes Section** (moved from separate tab)
   - 🎬 Lighting Scenes (4 buttons)
   - ❄️ AC Scenes (3 buttons)
   - 🏠 Leaving Home (1 button)

2. **Climate Monitoring Card**
   - Outdoor temperature (current)
   - Indoor temperature per room (4 rooms from AC sensors)
   - AC status per room (on/off, setpoint when running)

**Layout:**
```
┌─────────────────────────────────────┐
│ 🎬 Lighting Scenes                  │
│ [Ambient 10%] [Ambient 70%] ...     │
├─────────────────────────────────────┤
│ ❄️ AC Scenes                        │
│ [Living & Office] [All On] ...      │
├─────────────────────────────────────┤
│ 🏠 Leaving Home                     │
│ [Everything Off]                    │
├─────────────────────────────────────┤
│ 🌡️ Climate Overview                 │
│ Outside: 28°C                       │
│ Living Room: 24°C (AC: 23°C)        │
│ Bedroom: 26°C (AC: Off)             │
│ Office: 23°C (AC: 22°C)             │
│ Kid's Room: 25°C (AC: Off)          │
└─────────────────────────────────────┘
```

**Tasks:**
- [ ] Add Met.no weather integration
- [ ] Create climate monitoring card
- [ ] Move scenes to main overview
- [ ] Test real-time temperature updates

---

#### B. Daily Insights Dashboard
**Goal:** Historical view of previous day/night data

**Components:**
1. **Climate Summary**
   - Outdoor temp range (yesterday's high/low)
   - Indoor temp trends (graph)
   - AC runtime by room (bar chart)
   - Estimated energy cost

2. **Lighting Summary**
   - Which lights ran overnight
   - Total runtime per light
   - Unusual patterns

3. **Energy Insights**
   - Total AC runtime
   - Cost estimates
   - Comparison to previous days

**Layout:**
```
┌─────────────────────────────────────┐
│ 📊 Yesterday's Climate              │
│ Outdoor: 18°C - 32°C                │
│                                     │
│ [Temperature Trend Graph]           │
│                                     │
│ AC Runtime:                         │
│ Living Room: ████████ 6.5h          │
│ Bedroom:     ██ 1.2h                │
│ Office:      █████ 4.8h             │
│ Kid's Room:  ███ 2.1h               │
│                                     │
│ Estimated Cost: €2.45               │
├─────────────────────────────────────┤
│ 💡 Lighting Summary                 │
│ Lights left on overnight: 2         │
│ - Kitchen LED Strip: 8.5h           │
│ - Living LED Strip: 8.5h            │
└─────────────────────────────────────┘
```

**Tasks:**
- [ ] Create new dashboard view (path: `/daily-insights`)
- [ ] Add temperature history graph
- [ ] Add AC runtime tracking sensors
- [ ] Add lighting runtime tracking
- [ ] Create cost estimation template

---

#### C. Consolidated Daily Notification
**Goal:** Single 9am notification with summary + link to insights

**Notification Structure:**
```
Title: "Daily Home Summary"
Message:
"Yesterday: 18-32°C outside
AC ran 14.6h total (€2.45)
2 lights left on overnight
Tap to view details"

Action: Open /daily-insights dashboard
```

**Tasks:**
- [ ] Replace existing 3 informational notifications with 1 consolidated
- [ ] Add clickable action to open Daily Insights dashboard
- [ ] Include climate, lighting, and energy summary
- [ ] Test notification delivery and action

---

### Phase 2: Smart Automations (FUTURE)

#### A. Weather-Based Suggestions (FUTURE)
**Concept:** Notify when outdoor conditions suggest AC adjustment

**Example Logic:**
```
IF outdoor_temp < 25°C AND any_ac_running:
  Notify: "It's cool outside (23°C). Consider turning off AC or increasing setpoint."

IF outdoor_temp > 35°C AND no_ac_running:
  Notify: "Extreme heat today (37°C). Consider pre-cooling home."
```

---

#### B. Night Cooling Optimization (FUTURE)
**Concept:** Adjust bedroom AC for sleep comfort

---

#### C. Presence-Based Control (FUTURE - Requires Ubiquiti Integration)
**Concept:** Turn off ACs when no one home

---

### Phase 3: Advanced Energy Monitoring (FUTURE)

#### Runtime Tracking (Included in Phase 1)
**Implementation:**
- Use `history_stats` sensors (built-in)
- Track time each AC is in "cool" state
- Calculate total runtime across all units

**Sensors to create:**
- `sensor.ac_living_runtime_yesterday`
- `sensor.ac_bedroom_runtime_yesterday`
- `sensor.ac_office_runtime_yesterday`
- `sensor.ac_kid_runtime_yesterday`
- `sensor.total_ac_runtime_yesterday`

---

#### Cost Estimation (Included in Phase 1)
**Formula:**
```
Cost = Runtime (hours) × Power (kW) × Rate (€/kWh)
```

**Assumptions:**
- Power consumption per AC unit: ~2.5kW (ceiling duct estimate)
- Electricity rate: TBD (user to provide)

**Template sensor:**
```yaml
sensor:
  - platform: template
    sensors:
      ac_cost_yesterday:
        friendly_name: "AC Cost Yesterday"
        unit_of_measurement: "€"
        value_template: >
          {{ (states('sensor.total_ac_runtime_yesterday') | float * 2.5 * 0.XX) | round(2) }}
```

---

## ⚠️ Information Needed

### For Phase 1 Implementation:

1. **Weather Integration:**
   - [ ] Location coordinates (latitude/longitude) for Met.no integration
   - [ ] City/country for reference

2. **Energy Cost Tracking:**
   - [ ] Electricity rate (€/kWh) for cost estimation
   - [ ] Confirm AC power consumption estimate (2.5kW per unit acceptable?)

3. **Dashboard Preferences:**
   - [ ] Confirm Main Home Overview layout (scenes + climate monitoring)
   - [ ] Confirm Daily Insights dashboard structure
   - [ ] Any additional metrics to include in daily summary?

4. **Notification Timing:**
   - [ ] Keep 9am for daily summary or prefer different time?
   - [ ] Confirm consolidating all 3 informational notifications into 1

### For Future Phases:

5. **Automation Preferences (Phase 2):**
   - Comfortable with automatic AC control or prefer notifications?
   - Want manual override capability?
   - Acceptable temperature ranges for auto-adjustment?

6. **Usage Patterns (Phase 2):**
   - Regular daily schedule or variable?
   - Which rooms are used most?
   - Typical bedtime/wake time?

---

## 🧪 Phase 1 Testing Plan

### Test 1: Weather Integration
- [ ] Install Met.no integration via HA UI
- [ ] Configure location coordinates
- [ ] Verify outdoor temperature sensor created
- [ ] Test temperature accuracy (compare to local weather)
- [ ] Verify sensor updates regularly

### Test 2: Main Home Overview Dashboard
- [ ] Deploy updated dashboard with scenes section
- [ ] Add climate monitoring card
- [ ] Verify real-time temperature updates
- [ ] Test scene buttons work correctly
- [ ] Verify AC status displays correctly (on/off, setpoint)

### Test 3: Runtime Tracking Sensors
- [ ] Create history_stats sensors in configuration.yaml
- [ ] Reload configuration
- [ ] Run AC for known duration (e.g., 1 hour)
- [ ] Verify runtime sensor accuracy
- [ ] Test yesterday's runtime calculation

### Test 4: Daily Insights Dashboard
- [ ] Create new dashboard view at /daily-insights
- [ ] Add temperature history graph (ApexCharts or built-in)
- [ ] Add AC runtime bar chart
- [ ] Add lighting summary
- [ ] Test navigation from main dashboard

### Test 5: Cost Estimation
- [ ] Create cost template sensor
- [ ] Verify calculation formula
- [ ] Test with known runtime values
- [ ] Display on Daily Insights dashboard

### Test 6: Consolidated Daily Notification
- [ ] Update automation to replace 3 informational notifications
- [ ] Test notification delivery at 9am
- [ ] Verify clickable action opens Daily Insights dashboard
- [ ] Test notification content accuracy

---

## 📝 Implementation Notes

### Weather Integration
- **Entity IDs to expect:**
  - `weather.home` (or `weather.met_no`)
  - `sensor.home_temperature` (outdoor temp)
  - `sensor.home_humidity`

### AC Temperature Sensors
- **Current temperature from AC units:**
  - `climate.ac_living` → `current_temperature` attribute
  - `climate.ac_bedroom` → `current_temperature` attribute
  - `climate.ac_office` → `current_temperature` attribute
  - `climate.ac_iacopewee` → `current_temperature` attribute

### History Stats Sensor Configuration
```yaml
# Add to configuration.yaml
sensor:
  - platform: history_stats
    name: AC Living Runtime Yesterday
    entity_id: climate.ac_living
    state: 'cool'
    type: time
    start: '{{ now().replace(hour=0, minute=0, second=0) - timedelta(days=1) }}'
    end: '{{ now().replace(hour=0, minute=0, second=0) }}'
```

---

## ✅ Phase 1 Completion Criteria

- [ ] Met.no weather integration installed and working
- [ ] Main Home Overview dashboard includes scenes + climate monitoring
- [ ] Daily Insights dashboard created with temperature graphs and runtime stats
- [ ] Runtime tracking sensors created for all 4 AC units
- [ ] Cost estimation template sensor working
- [ ] Consolidated daily notification (9am) with clickable action
- [ ] All existing 3 informational notifications replaced with 1
- [ ] Documentation updated with entity IDs and configuration

