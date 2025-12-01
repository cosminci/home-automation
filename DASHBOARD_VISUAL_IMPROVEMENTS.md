# Dashboard Visual Improvements Epic

**Status:** Planning Phase  
**Started:** 2025-11-30  
**Goal:** Improve visual appearance and ergonomics of Home Assistant dashboard

---

## Phase 1: Custom Cards Installation (User Action Required)

**Status:** ⏳ In Progress (User installing via HACS)

### Cards to Install
- [ ] **Mushroom Cards** - Modern, minimalist card designs
- [ ] **card-mod** - CSS customization for existing cards
- [ ] **fold-entity-row** - Collapsible rows within entity cards
- [ ] **Custom Theme** (User researching independently)

**Note:** Once installed, proceed to Phase 2 for implementation planning.

---

## Phase 2: Specific Card Improvements (Pending Analysis)

### 2.1 Overview Tab - Climate Card
**Current:** Standard `entities` card with weather attributes and AC climate entities  
**Analysis Needed:**
- Can Mushroom cards improve the weather display?
- Should AC entities remain as-is (they're already compact in overview)?
- Collapsible sections for "Outside Weather" vs "Indoor Temperature & AC"?

### 2.2 Overview Tab - Scenes Card
**Current:** Button entities within entities card (3 sections: Lighting, AC, Leaving Home)  
**Potential Improvement:**
- Mushroom button cards for better visual hierarchy
- Color coding: Blue for lighting, Orange for AC, Red for "Everything Off"
- Keep current grouping structure

### 2.3 Room Tabs - Light Controls
**Current:** Mix of `entities` cards (on/off switches) and `light` cards (dimmable)  
**Analysis Needed:**
- Can Mushroom light cards improve dimmable light controls?
- Should on/off switches use Mushroom entity cards?
- Verify Mushroom maintains brightness sliders for dimmable lights

### 2.4 Kitchen Tab - Appliance Cards
**Current:** Conditional entities showing status, programs, finish times  
**Potential Improvement:**
- Collapsible sections using fold-entity-row
- Primary info always visible: Status, Power
- Secondary info collapsible: Active program, finish time, warnings
- Reduces vertical space when appliances inactive

### 2.5 Living Room & Bedroom - Entertainment Cards
**Current:** Entities card with sections for TV and Soundbar  
**Analysis Needed:**
- Can Mushroom media cards improve this?
- Keep combined card structure or separate?

### 2.6 Network Cards (Living Room, Kid's Room, Hallway)
**Current:** Entities cards with status, uptime, restart buttons  
**Potential Improvement:**
- Collapsible: Hide uptime and restart buttons by default
- Always visible: Device status only
- Expand to show controls when needed

### 2.7 Car Tab - Conditional Visibility Cards
**Current:** Doors & Windows card with conditional rows (only show when open)  
**Status:** ✅ Already optimized - no changes needed

---

## Phase 3: Color Coding & Visual Hierarchy (Pending card-mod)

**Requires:** card-mod custom card installed

### 3.1 Card Header Colors
- **Climate/AC cards:** Blue theme
- **Lights cards:** Yellow/warm theme  
- **Appliances:** Green theme
- **Network:** Gray/neutral theme
- **Entertainment:** Purple theme
- **Scenes - Lighting:** Warm yellow
- **Scenes - AC:** Cool blue
- **Scenes - Everything Off:** Red/warning

### 3.2 State-Based Coloring
- AC cards: Change color when running (blue → orange when heating, blue when cooling)
- Light cards: Subtle glow when lights are on
- Appliance cards: Highlight when running

---

## Phase 4: Collapsible Sections Implementation

**Requires:** fold-entity-row installed

### Priority Cards for Collapsing:

1. **Kitchen - Dishwasher** (High Priority)
   - Always visible: Status, Power
   - Collapsible: Active program, finish time, salt/rinse aid warnings, stop button

2. **Kitchen - Oven** (High Priority)
   - Always visible: Status, Power
   - Collapsible: Active program, temperature, finish time, stop button, child lock

3. **Kitchen - Cooktop** (Low Priority - already minimal)
   - Keep as-is (only 3 entities)

4. **Washer Room - Washing Machine** (High Priority)
   - Always visible: Status, Power
   - Collapsible: Active program, finish time, stop/resume buttons, program selector

5. **Washer Room - Dryer** (High Priority)
   - Always visible: Status, Power
   - Collapsible: Active program, finish time, stop/resume buttons, program selector, child lock

6. **Network Cards** (Medium Priority)
   - Always visible: Device status
   - Collapsible: Uptime, restart/power cycle buttons

7. **Hallway - Network (Storage Room)** (Medium Priority)
   - Always visible: Gateway status, Switch status, VPN toggle
   - Collapsible: Uptime and restart buttons for each device

---

## Phase 5: Floor Plan View (Future - High Effort)

**Status:** 🔮 Future consideration  
**Requirements:**
- User has 2D apartment plan
- Need to create floor plan image
- Use `picture-elements` card type
- Map clickable zones to rooms/devices

**Feasibility:** High effort, high impact. Defer until Phases 1-4 complete.

---

## Questions for User (After HACS Installation)

1. Which Mushroom cards did you install?
2. Did you install card-mod?
3. Did you install fold-entity-row or similar collapsible card?
4. Which theme did you choose (if any)?
5. Do themes work on both mobile and web? (Answer: Yes, themes are server-side and apply to all clients)

---

## Implementation Order (After User Confirms Installations)

1. **Phase 2.4** - Implement collapsible appliance cards (Kitchen, Washer Room)
2. **Phase 2.6** - Implement collapsible network cards
3. **Phase 2.2** - Improve scene buttons with Mushroom cards
4. **Phase 2.3** - Evaluate Mushroom light cards for dimmable lights
5. **Phase 3** - Add color coding with card-mod (if installed)
6. **Phase 5** - Floor plan view (if user wants to proceed)

---

## Rejected Ideas

- ❌ Manual card size microtweaking - User confirmed this is a lost game
- ❌ Mobile vs desktop optimization - No native HA support for this
- ❌ Custom header minimization - Current header already minimal
- ❌ Auto-entities/filtered views - Complexity vs usefulness unclear for this setup
- ❌ Better thermostat card - Need to verify if better alternatives exist (don't make things up)

