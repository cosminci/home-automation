# Ubiquiti Integration - Implementation Tracker

**Status:** 🔍 Research Phase  
**Priority:** High (enables presence detection for other automations)  
**Dependencies:** None

---

## 🎯 Goals

1. **UniFi Protect Integration** - Camera feeds, motion detection, security monitoring
2. **UniFi Network Integration** - Presence detection, device tracking, network monitoring
3. **Dashboard Integration** - Camera views, network status, presence indicators
4. **Automation Enablement** - Presence-based triggers for lights, AC, scenes

---

## 🔧 Equipment Inventory

- **Cloud Gateway Max** - Router/controller
- **UniFi Switches** - Network switches (model/count TBD)
- **UniFi Access Points** - WiFi APs (model/count TBD)
- **UniFi G Cameras** - Security cameras (model/count TBD)

**Action Items:**
- [ ] Document exact models and firmware versions
- [ ] Verify UniFi OS version on Cloud Gateway Max
- [ ] List all camera locations and purposes

---

## 📋 Feasibility Research

### UniFi Protect Integration (Cameras)

**Official Integration:** Yes (built-in to Home Assistant)  
**Documentation:** https://www.home-assistant.io/integrations/unifiprotect/

**Requirements to Verify:**
- [ ] UniFi Protect application running on Cloud Gateway Max
- [ ] Local user account with admin privileges (not cloud account)
- [ ] Network connectivity from HA to Cloud Gateway Max
- [ ] Camera firmware up to date

**Claimed Features:**
- Live camera feeds
- Motion/person/vehicle detection
- Doorbell press events
- Recording snapshots
- Camera on/off control
- Privacy mode toggle

**Questions/Concerns:**
- Does Cloud Gateway Max support UniFi Protect or only dedicated NVR devices?
- What's the performance impact of streaming multiple cameras to HA?
- Can we trigger automations from specific camera zones?

---

### UniFi Network Integration (Presence Detection)

**Official Integration:** Yes (built-in to Home Assistant)  
**Documentation:** https://www.home-assistant.io/integrations/unifi/

**Requirements to Verify:**
- [ ] UniFi Network application running on Cloud Gateway Max
- [ ] Local user account with admin privileges
- [ ] Network connectivity from HA to Cloud Gateway Max

**Claimed Features:**
- Device presence detection (device_tracker entities)
- Client connected/disconnected events
- Network traffic statistics
- Client blocking/unblocking
- DPI (Deep Packet Inspection) data
- Port forwarding control
- Guest network control

**Questions/Concerns:**
- How reliable is WiFi-based presence detection? (phone sleep mode issues?)
- Can we track specific family member devices?
- What's the detection latency (how fast does it know you're home)?

---

## 🏗️ Implementation Plan

### Phase 1: Research & Verification (Current)
- [ ] Verify Cloud Gateway Max supports UniFi Protect
- [ ] Check if cameras are already in UniFi Protect
- [ ] Create local admin user on UniFi controller
- [ ] Test network connectivity from HA to Cloud Gateway Max
- [ ] Document all camera locations and purposes

### Phase 2: UniFi Network Integration
- [ ] Add UniFi Network integration in HA
- [ ] Configure device trackers for family phones
- [ ] Test presence detection reliability
- [ ] Create person entities for family members
- [ ] Document detection latency and reliability

### Phase 3: UniFi Protect Integration (if supported)
- [ ] Add UniFi Protect integration in HA
- [ ] Configure camera entities
- [ ] Test live feeds in dashboard
- [ ] Configure motion detection zones
- [ ] Test snapshot capture

### Phase 4: Dashboard Integration
- [ ] Add "Security" tab with camera feeds
- [ ] Add presence indicators to relevant tabs
- [ ] Add network status card
- [ ] Test mobile dashboard performance with cameras

### Phase 5: Automation Development
- [ ] Presence-based "arriving home" automation
- [ ] Presence-based "leaving home" automation
- [ ] Camera motion alerts when away
- [ ] Network device alerts (unknown devices)

---

## 🚧 Blockers & Risks

**Potential Blockers:**
- Cloud Gateway Max may not support UniFi Protect (needs verification)
- Camera integration may require separate NVR device
- Presence detection may be unreliable with phone battery optimization

**Mitigation Strategies:**
- Research Cloud Gateway Max capabilities before proceeding
- Consider alternative presence detection methods if WiFi unreliable
- Test thoroughly before building automations on top

---

## 📝 Notes & Decisions

**Date: 2025-11-25**
- User confirmed equipment: Cloud Gateway Max, switches, APs, G cameras
- User interested in this integration as major overhaul
- Priority: High (enables other automations)

---

## 🔗 References

- [UniFi Network Integration Docs](https://www.home-assistant.io/integrations/unifi/)
- [UniFi Protect Integration Docs](https://www.home-assistant.io/integrations/unifiprotect/)
- [Cloud Gateway Max Specs](https://store.ui.com/us/en/pro/category/all-cloud-gateways/products/ucg-max)

---

## ✅ Success Criteria

- [ ] Reliable presence detection for at least 2 family members
- [ ] Camera feeds viewable in HA dashboard
- [ ] Motion detection triggers working
- [ ] At least 2 presence-based automations working reliably
- [ ] Network status monitoring functional

