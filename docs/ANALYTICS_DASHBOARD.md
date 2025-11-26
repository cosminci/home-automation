# Analytics Dashboard - Implementation Tracker

**Status:** 🔍 Research Phase  
**Priority:** Medium (depends on other integrations)  
**Dependencies:** Smart Climate (for AC data), Ubiquiti (for network data), Unraid (for system data)

---

## 🎯 Goals

1. **Energy Insights:** Track AC runtime, lighting usage, appliance cycles
2. **Usage Patterns:** Identify most-used devices, peak usage times
3. **System Health:** Monitor integration status, device connectivity
4. **Cost Tracking:** Estimate energy costs and identify savings opportunities
5. **Trend Analysis:** Historical data to optimize automations

---

## 🔧 Current Data Sources

### Available Now
- **4 Air Conditioners:** On/off state, temperature, mode
- **6 Dimmable Lights:** On/off state, brightness level
- **19 On/Off Switches:** On/off state
- **5 Appliances:** Operation state, program progress, finish time
- **2 TVs + Soundbar:** On/off state, source, volume
- **Car (Hyundai Tucson):** Fuel level, odometer, location, door status

### Coming Soon (Pending Integration)
- **Weather:** Outdoor temperature, humidity, forecast
- **Ubiquiti Network:** Device presence, network uptime, bandwidth
- **Ubiquiti Cameras:** Motion events, recording status
- **Unraid NAS:** Array health, disk usage, container status

---

## 📚 Research Findings

### Analytics Approach

#### Recommended: History Stats (Built-in)
**Status:** ✅ Available  
**Type:** HA built-in integration

**Capabilities:**
- Track time entity is in specific state
- Count state changes
- Calculate statistics over time periods
- No additional services needed

**Example Use Cases:**
```yaml
# AC runtime today
sensor:
  - platform: history_stats
    name: AC Living Runtime Today
    entity_id: climate.ac_living
    state: 'cool'
    type: time
    start: '{{ now().replace(hour=0, minute=0, second=0) }}'
    end: '{{ now() }}'
```

**Feasibility:** ✅ HIGH - Built-in, no dependencies

---

#### Optional: InfluxDB + Grafana (Advanced)
**Status:** 🔍 Optional for future  
**Type:** External time-series database + visualization

**When to Consider:**
- Need long-term data retention (years)
- Want professional-looking dashboards
- Need complex queries and aggregations

**Complexity:** High - Additional services to maintain

**Recommendation:** Start with History Stats, upgrade later if needed

---

## 🚀 Proposed Features

### Phase 1: Basic Statistics (Feasibility: ✅ HIGH)

#### A. AC Runtime Tracking
**Sensors to Create:**
- AC runtime per room (today, this week, this month)
- Total AC runtime (all units combined)
- Most-used AC
- Average daily runtime

**Dashboard Display:**
- Bar chart: AC runtime by room
- Gauge: Total runtime today
- Trend: Runtime this week vs. last week

---

#### B. Lighting Usage
**Sensors to Create:**
- Total lights currently on (count)
- Lights left on overnight (from existing automation)
- Most-used light (by runtime)

**Dashboard Display:**
- Number: Currently on lights
- List: Which lights are on
- History: Lights on over time

---

#### C. Appliance Cycles
**Sensors to Create:**
- Dishwasher cycles per week/month
- Washing machine cycles per week/month
- Dryer cycles per week/month
- Oven usage hours per week

**Dashboard Display:**
- Counter: Cycles this month
- Comparison: This month vs. last month
- Most-used appliance

---

#### D. Cost Estimation
**Sensors to Create:**
- Estimated AC cost per day/week/month
- Estimated lighting cost per day/week/month
- Total estimated energy cost

**Requirements:**
- Electricity rate (€/kWh)
- Estimated power consumption per device type

**Example Calculation:**
```
AC Cost = Runtime (hours) × 2.5kW × €0.15/kWh
```

**Dashboard Display:**
- Gauge: Estimated cost today
- Trend: Cost this month vs. last month
- Breakdown: Cost by category

---

### Phase 2: Dashboard Integration (Feasibility: ✅ HIGH)

**New Tab: "Insights"**

**Section 1: Energy Overview**
- Total estimated cost today/this week/this month
- Breakdown by category (AC, lights, appliances)
- Comparison to previous periods

**Section 2: Climate**
- AC runtime by room (bar chart)
- Total AC runtime trend (line graph)
- Outdoor vs. indoor temperature (if weather integrated)
- Estimated AC cost

**Section 3: Lighting**
- Currently on lights count
- Most-used lights
- Lights left on overnight

**Section 4: Appliances**
- Cycle counts this month
- Most-used appliance
- Average cycles per week

**Section 5: System Health**
- Integration status (green/red indicators)
- Last update times
- Device connectivity (from Ubiquiti, if integrated)
- Unraid health (if integrated)

**Section 6: Network** (if Ubiquiti integrated)
- Devices currently connected
- Network uptime
- Bandwidth usage

---

### Phase 3: Advanced Features (Feasibility: TO VALIDATE)

#### A. Weekly Summary Automation
**Concept:** Send weekly summary notification

**Example Content:**
```
Weekly Home Summary:
- AC runtime: 42 hours (down 15% from last week)
- Estimated cost: €18.50
- Lights left on overnight: 2 times
- Dishwasher cycles: 5
- Most-used AC: Living Room (18 hours)
```

**Feasibility:** ✅ HIGH - Use template notification

---

#### B. Optimization Recommendations
**Concept:** Suggest improvements based on data

**Example Suggestions:**
- "Office AC ran 6 hours yesterday but you were only home 4 hours"
- "Living room lights left on 3 nights this week"
- "AC usage up 30% this week - check if windows left open"

**Feasibility:** MEDIUM - Requires defining "normal" patterns

---

## ⚠️ Open Questions

1. **Data Retention:**
   - How long to keep history? (10 days default, 30 days, 1 year?)
   - Comfortable with database size growth?

2. **Cost Tracking:**
   - What's your electricity rate (€/kWh)?
   - Interested in estimated costs or need precise measurement?

3. **Visualization Preferences:**
   - Prefer simple cards or detailed graphs?
   - Want real-time or daily summaries?
   - Mobile-friendly or desktop-focused?

4. **Priorities:**
   - Which metrics are most important?
   - What decisions would analytics inform?
   - What problems are you trying to solve?

---

## 🧪 Testing Plan

### Test 1: Sensor Creation
- [ ] Create history_stats sensors for AC runtime
- [ ] Create sensors for lighting usage
- [ ] Create sensors for appliance cycles
- [ ] Verify sensor accuracy

### Test 2: Cost Calculation
- [ ] Define power consumption estimates
- [ ] Create cost template sensors
- [ ] Test calculation accuracy
- [ ] Validate against actual bills (if possible)

### Test 3: Dashboard Creation
- [ ] Create "Insights" tab
- [ ] Add energy overview section
- [ ] Add climate section with graphs
- [ ] Test on mobile and desktop

### Test 4: Weekly Summary
- [ ] Create summary automation
- [ ] Test notification content
- [ ] Refine based on feedback

---

## 📝 Implementation Notes

*This section will be updated during implementation with findings, issues, and solutions.*

---

## ✅ Completion Criteria

- [ ] Core sensors created (AC runtime, lighting, appliances)
- [ ] Cost estimation working
- [ ] "Insights" dashboard tab created
- [ ] At least 3 sections populated with data
- [ ] Weekly summary automation working (optional)
- [ ] Documentation updated with sensor configurations

