# 🏠 Home Assistant Dashboard

> AI agent documentation for maintaining Home Assistant setup on Unraid NAS.

## Quick Reference

| Resource | URL |
|----------|-----|
| Home Assistant | `http://192.168.1.3:8123` (DNS: `tower.lan`) |
| Main Dashboard | `http://192.168.1.3:8123/clean-home` |
| Insights Dashboard | `http://192.168.1.3:8123/home-insights` |

**Token:** `~/.zshrc` → `HA_TOKEN` (long-lived access token, valid 10 years)

## API Usage

All API calls require `source ~/.zshrc` first (or the `HA_TOKEN` env var to be set).

**REST API** (querying states, calling services, managing configs):
```bash
# Query entity states
curl -s -H "Authorization: Bearer $HA_TOKEN" \
  http://192.168.1.3:8123/api/states | jq '.[] | select(.entity_id | startswith("light."))'

# Call a service
curl -X POST -H "Authorization: Bearer $HA_TOKEN" -H "Content-Type: application/json" \
  -d '{"entity_id": "light.living_room"}' \
  http://192.168.1.3:8123/api/services/light/turn_on

# Read automation config
curl -s -H "Authorization: Bearer $HA_TOKEN" \
  http://192.168.1.3:8123/api/config/automation/config/{automation_id}

# Write/update automation config
curl -X POST -H "Authorization: Bearer $HA_TOKEN" -H "Content-Type: application/json" \
  -d '{"alias":"...","triggers":[...],"actions":[...],"mode":"single"}' \
  http://192.168.1.3:8123/api/config/automation/config/{automation_id}

# Delete automation config
curl -X DELETE -H "Authorization: Bearer $HA_TOKEN" \
  http://192.168.1.3:8123/api/config/automation/config/{automation_id}

# Same pattern works for scenes and scripts:
#   /api/config/scene/config/{scene_id}
#   /api/config/script/config/{script_slug}
```

**WebSocket API** (dashboard deployment):
```python
import asyncio, websockets, json, os

async def update_dashboard(config, url_path="clean-home"):
    async with websockets.connect("ws://192.168.1.3:8123/api/websocket") as ws:
        await ws.recv()  # auth_required
        await ws.send(json.dumps({"type": "auth", "access_token": os.environ["HA_TOKEN"]}))
        await ws.recv()  # auth_ok
        await ws.send(json.dumps({
            "id": 1, "type": "lovelace/config/save",
            "url_path": url_path, "config": config
        }))
        return await ws.recv()
```

**Reload after config changes** (required for YAML-sourced configs like `sensors.yaml`, `templates.yaml`, `customize.yaml`):
```bash
# Reload specific domains (no restart needed)
curl -X POST -H "Authorization: Bearer $HA_TOKEN" \
  http://192.168.1.3:8123/api/services/automation/reload
curl -X POST -H "Authorization: Bearer $HA_TOKEN" \
  http://192.168.1.3:8123/api/services/scene/reload
curl -X POST -H "Authorization: Bearer $HA_TOKEN" \
  http://192.168.1.3:8123/api/services/script/reload
curl -X POST -H "Authorization: Bearer $HA_TOKEN" \
  http://192.168.1.3:8123/api/services/template/reload
curl -X POST -H "Authorization: Bearer $HA_TOKEN" \
  http://192.168.1.3:8123/api/services/history_stats/reload
```

## Repository Structure

```
generate_dashboard.py          # Main dashboard generator (deploys via WebSocket)
generate_insights_dashboard.py # Insights dashboard generator (deploys via WebSocket)
dashboard_helpers.py           # Card creation helpers
templates/                     # Decluttering card templates (8 JSON)
rooms/                         # View modules (overview, open_space, private, utility, floor_plan)
configs/                       # HA config files (automations/scenes/scripts: API-deployable; sensors/templates/customize: manual vi)
scripts/                       # Utility scripts (Hyundai token extractor, entity cleanup)
```

## Deploying Changes

**Dashboards** (auto-deploy via WebSocket API):
```bash
python3 generate_dashboard.py
python3 generate_insights_dashboard.py
```

**Automations, scenes, scripts** (auto-deploy via REST API):
- CRUD via `/api/config/{automation,scene,script}/config/{id}` (see API Usage above)
- Then call the appropriate reload service

**YAML-only config files** (`sensors.yaml`, `templates.yaml`, `customize.yaml`) - manual copy still required:
1. Docker → homeassistant → Console
2. `vi /config/sensors.yaml` (or other config file)
3. Delete all (`gg` then `dG`), paste, save (`:wq`)
4. Call the reload service for the relevant domain (see API Usage above)

## Integrations

| Type | Integrations |
|------|-------------|
| Built-in | UniFi Network, UniFi Protect, ZHA (SLZB-06M + Tuya TRVs), SmartThings |
| HACS | ConnectLife (ACs), Home Connect (Bosch), LG ThinQ (TVs), Hyundai/Kia Connect |
| Frontend | Mushroom, button-card, Stack In Card, Plotly Graph, Weather Radar |

**Known Limitations:**
- Bosch: Child lock not exposed for washer/dryer; cooktop power cannot be turned on remotely
- SmartThings: Soundbar source selection removed from API (Dec 2024)
- ZHA: Tuya TRV max_temp bug fixed via `customize.yaml`

## Critical Rules

- ✅ Deploy dashboards automatically via WebSocket API
- ✅ Deploy automations/scenes/scripts automatically via REST API config endpoints
- ✅ Use REST API for querying states and calling services
- ❌ `sensors.yaml`, `templates.yaml`, `customize.yaml` still require manual vi copy + reload
- ❌ Don't assume `light.*` entities are dimmable

## Utility Scripts

- `scripts/delete_entities.sh` - Remove entities from registry (creates backup)
- `scripts/HyundaiFetchApiTokensSelenium.py` - Extract Hyundai EU refresh token (requires OAuth2 credentials)

## Floor Plan

Edit device positions in `rooms/floor_plan.py` using percentage coordinates (`left`, `top`).

## Future Work

**Unraid Integration** (not working):
- Goal: Monitor array status, disk health, Docker containers, storage capacity
- Approach: HACS integration `chris-mc1/unraid_api` with Unraid 7.2+ GraphQL API
- Blocker: Integration requires Admin API key despite documentation claiming read-only scopes work ([issue #26](https://github.com/chris-mc1/unraid_api/issues/26)); `domalab/ha-unraid` alternative is abandoned
