# Unraid Integration - Implementation Tracker

**Status:** 🔍 Research Phase  
**Priority:** Medium (monitoring and maintenance)  
**Dependencies:** None

---

## 🎯 Goals

1. **System Monitoring** - Array status, disk health, temperature monitoring
2. **Docker Container Monitoring** - Container status, resource usage
3. **Storage Monitoring** - Disk usage, array capacity, cache usage
4. **Alert Integration** - Critical alerts for array issues, disk failures
5. **Dashboard Integration** - System health card, storage overview

---

## 🔧 Equipment Inventory

- **Unraid NAS** - Server name: `tower.local`
- **Unraid Version** - 7.2.2 ✅
- **Home Assistant Container** - Running on Unraid
- **Storage:** Array configuration TBD

**Action Items:**
- [x] Document Unraid version
- [ ] List all disks in array (parity, data, cache)
- [ ] Document Docker containers running
- [x] Verify network connectivity between HA and Unraid host

---

## 📋 Feasibility Research

### Integration Options

#### Option 1: Unraid API Integration (HACS) ✅ CHOSEN

**Integration:** `domalab/ha-unraid` (HACS custom integration)
**Repository:** https://github.com/domalab/ha-unraid

**Features:**
- Array status (started, stopped, expanding)
- Disk status (active, standby, disabled)
- Disk temperature monitoring
- Disk usage and capacity
- Docker container status
- VM status (if applicable)
- UPS status (if connected)
- Network statistics

**Setup Steps:**
1. **Enable Unraid API** (Built-in for Unraid 7.2+)
   - Go to Unraid WebGUI: `http://192.168.1.3`
   - Navigate to: **Settings → Management Access → API**
   - Enable GraphQL Sandbox (optional, for testing)
   - Create API key with name "Home Assistant"
   - Permissions needed:
     - Resources: Info, Servers, Array, Disk, Share
     - Actions: Read (All)
   - Copy the generated API key

2. **Install HACS Integration** (`chris-mc1/unraid_api`)
   - [x] HACS integration installed
   - [ ] Configure with Unraid credentials:
     - **URL:** `http://192.168.1.3` (use LAN IP, not hostname!)
     - **API Key:** (paste from step 1)
     - **Monitor Disks:** Yes/No
     - **Monitor Shares:** Yes/No
   - [ ] Verify sensors appear in HA

**Important:** Since HA runs as a Docker container on Unraid, use the LAN IP (`192.168.1.3`) not `tower.local` or gateway IPs. The Unraid WebUI only listens on the br0 (LAN) interface, not the Docker bridge.

**Requirements:**
- [x] Unraid API (built-in for 7.2+, no plugin needed!)
- [x] API key generated
- [x] Network access from HA container to Unraid host
- [x] Compatible Unraid version (7.2.2)

---

#### Option 2: SNMP Monitoring

**Integration:** Built-in SNMP integration  
**Documentation:** https://www.home-assistant.io/integrations/snmp/

**Claimed Features:**
- CPU usage
- Memory usage
- Disk I/O
- Network traffic
- Custom OID monitoring

**Requirements to Verify:**
- [ ] SNMP enabled on Unraid
- [ ] SNMP community string configured
- [ ] Network access on SNMP port (161)

**Questions/Concerns:**
- Limited to basic system metrics
- No array-specific status
- No Docker container monitoring

---

#### Option 3: REST API + Command Line Sensors

**Integration:** Custom REST sensors + SSH command line sensors  
**Documentation:** https://www.home-assistant.io/integrations/rest/

**Claimed Features:**
- Fully customizable
- Direct access to Unraid CLI
- Can monitor anything scriptable

**Requirements to Verify:**
- [ ] SSH access from HA to Unraid
- [ ] SSH key authentication configured
- [ ] Unraid CLI commands documented

**Questions/Concerns:**
- Most complex to set up
- Requires maintenance
- May break with Unraid updates

---

## 🏗️ Implementation Plan

### Phase 1: Research & Verification ✅ COMPLETE
- [x] Research available integration options
- [x] Verify Unraid version and compatibility (7.2.2)
- [x] Test network connectivity from HA to Unraid host
- [x] Decide on integration approach (HACS integration chosen)
- [ ] Document current array configuration

### Phase 2: Integration Setup (IN PROGRESS)
- [x] Install HACS integration
- [ ] Create API key in Unraid (Settings → Management Access → API)
- [ ] Configure HACS integration with credentials
- [ ] Test basic connectivity
- [ ] Verify sensors appear in HA
- [ ] Document available sensors

### Phase 3: Sensor Configuration
- [ ] Array status sensor
- [ ] Individual disk health sensors
- [ ] Disk temperature sensors
- [ ] Storage capacity sensors
- [ ] Docker container status sensors
- [ ] Network statistics sensors

### Phase 4: Dashboard Integration
- [ ] Add "System" tab or section to existing tab
- [ ] Create system health card
- [ ] Create storage overview card
- [ ] Create Docker container status card
- [ ] Add critical alerts to dashboard

### Phase 5: Automation Development
- [ ] Array stopped/degraded alert
- [ ] Disk failure alert
- [ ] High temperature alert (>50°C)
- [ ] Low storage space alert (<10% free)
- [ ] Docker container down alert (especially HA itself)

---

## 🚧 Blockers & Risks

**Potential Blockers:**
- HACS integration may require Unraid plugins not installed
- SNMP may not provide array-specific data
- SSH access may be security concern
- HA monitoring itself from same host may be circular dependency

**Mitigation Strategies:**
- Start with simplest integration (SNMP) to test feasibility
- Focus on most critical metrics first (array status, disk health)
- Consider external monitoring for HA container itself

---

## 📝 Notes & Decisions

**Date: 2025-11-25**
- User confirmed Unraid NAS at tower.local
- HA already running as Docker container on Unraid
- User interested in system monitoring integration
- Priority: Medium (nice to have, not critical)
- Unraid version: 7.2.2 (API built-in, no plugin needed)
- HACS integration installed, awaiting API key configuration
- Chosen approach: HACS integration (most comprehensive)

---

## 🔗 References

- [Unraid HACS Integration](https://github.com/domalab/ha-unraid)
- [HA SNMP Integration](https://www.home-assistant.io/integrations/snmp/)
- [HA REST Sensor](https://www.home-assistant.io/integrations/rest/)
- [HA Command Line Sensor](https://www.home-assistant.io/integrations/sensor.command_line/)

---

## ✅ Success Criteria

- [ ] Array status visible in HA dashboard
- [ ] Disk health monitoring for all array disks
- [ ] Storage capacity monitoring
- [ ] Critical alert automation for array issues
- [ ] Docker container status for key containers (HA, Plex, etc.)

