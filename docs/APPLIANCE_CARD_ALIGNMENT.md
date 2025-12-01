# Appliance Card Alignment Progress

## Goal
Align all Bosch Home Connect appliance cards to follow the dishwasher card structure for consistency.

## Reference: Dishwasher Card Structure

The dishwasher card serves as the reference implementation:

```
Stack-in-card (no title):
  
  Row 1 - Program Selector (conditional: when state = "ready"):
    - mushroom-select-card
    - entity: select.dishwasher_active_program
    - name: "Start Dishwasher Program"
    - icon: mdi:dishwasher
    - icon_color: blue
    - secondary_info: none
  
  Row 2 - Action Buttons (conditional: when state NOT "inactive" AND NOT "ready"):
    - 2-column grid
    - Column 1: Stop button (red icon, icon-only)
    - Column 2: Power Off button (orange icon, icon-only)
  
  Row 3 - Program Info (conditional: when state NOT "inactive" AND NOT "ready"):
    - 2-column grid
    - Column 1: Active program (icon + state as secondary_info)
    - Column 2: Finish time (icon + state as secondary_info)
  
  Row 4 - Maintenance Warnings (always visible):
    - 2-column grid
    - Column 1: Salt level (icon-only, red/green via card_mod)
    - Column 2: Rinse aid level (icon-only, red/green via card_mod)
```

## Completed Appliances

### ✅ Oven (rooms/kitchen.py)

**Structure:**
- Row 1: Program selector (shows when state = "inactive" OR "ready")
- Row 2: Stop + Power Off buttons (shows when running)
- Row 3: Active program + Finish time (shows when running)
- Row 4: Child lock + Cavity temperature (always visible)

**Key Differences from Dishwasher:**
- Program selector shows for BOTH "inactive" and "ready" states (two separate conditionals)
- Row 4 has child lock switch + temperature sensor instead of maintenance warnings
- Uses orange color theme instead of blue

### ✅ Cooktop (rooms/kitchen.py)

**Structure:**
- Row 1: Operation state indicator + Child lock (always visible)

**Key Differences from Dishwasher:**
- No programs (cooktop has no programmable cycles)
- Operation state is read-only icon-only display (grey when inactive, orange when active)
- Uses card_mod to change icon color based on state
- Child lock is the only interactive control
- Much simpler than other appliances

## Pending Appliances

### ⏳ Washing Machine (rooms/washer_room.py)

**Expected Structure:**
- Row 1: Program selector (when inactive/ready)
- Row 2: Stop + Power Off buttons (when running)
- Row 3: Active program + Finish time (when running)
- Row 4: i-DOS 1 + i-DOS 2 fill levels (always visible, like dishwasher maintenance)

**Available Entities:**
- `select.washing_machine_active_program`
- `button.washing_machine_stop_program`
- `switch.washing_machine_power`
- `sensor.washing_machine_operation_state`
- `sensor.washing_machine_program_finish_time`
- `sensor.washing_machine_poor_i_dos_1_fill_level`
- `sensor.washing_machine_poor_i_dos_2_fill_level`

### ⏳ Dryer (rooms/washer_room.py)

**Expected Structure:**
- Row 1: Program selector (when inactive/ready)
- Row 2: Stop + Power Off buttons (when running)
- Row 3: Active program + Finish time (when running)
- Row 4: No maintenance sensors available

**Available Entities:**
- `select.dryer_active_program`
- `button.dryer_stop_program`
- `switch.dryer_power`
- `sensor.dryer_operation_state`
- `sensor.dryer_program_finish_time`

**Note:** No maintenance sensors found for dryer (no lint filter sensor available)

## Key Learnings

1. **Conditional Logic:** Dishwasher uses `state: "ready"` for program selector, but other appliances may be in `state: "inactive"` when idle
2. **Icon-Only Display:** All buttons use `primary_info: "none"` and `secondary_info: "none"`
3. **Color Coding:** Red for stop, orange for power, appliance-specific color for program info
4. **No Titles:** All appliance cards have no title for cleaner look
5. **Maintenance Row:** Always visible at bottom, uses card_mod for red/green indicators
6. **Cooktop Exception:** Cooktops are much simpler with no programs, just status + child lock
7. **Safety Limitations:** Cooktop power cannot be turned on remotely (safety feature), only status display

## Next Steps

1. Align washing machine card
2. Align dryer card
3. Test all appliances in various states (inactive, ready, running, finished)
4. Update this document with final implementation details

