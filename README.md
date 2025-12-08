# 🏠 Home Assistant Dashboard

> AI agent documentation for maintaining Home Assistant setup on Unraid NAS (`tower.local`).

## Quick Reference

| Resource | URL |
|----------|-----|
| Home Assistant | http://tower.local:8123 |
| Main Dashboard | http://tower.local:8123/clean-home |
| Insights Dashboard | http://tower.local:8123/home-insights |

**Token:** `~/.zshrc` → `HA_TOKEN`

## API Usage

**REST API** (for querying states, services, etc.):
```bash
# Load token and query
source ~/.zshrc && curl -s -H "Authorization: Bearer $HA_TOKEN" \
  http://tower.local:8123/api/states | jq '.[] | select(.entity_id | startswith("light."))'

# Call a service
curl -X POST -H "Authorization: Bearer $HA_TOKEN" -H "Content-Type: application/json" \
  -d '{"entity_id": "light.living_room"}' \
  http://tower.local:8123/api/services/light/turn_on
```

**WebSocket API** (for dashboard updates):
```python
import asyncio, websockets, json, os

async def update_dashboard(config, url_path="clean-home"):
    async with websockets.connect("ws://tower.local:8123/api/websocket") as ws:
        await ws.recv()  # auth_required
        await ws.send(json.dumps({"type": "auth", "access_token": os.environ["HA_TOKEN"]}))
        await ws.recv()  # auth_ok
        await ws.send(json.dumps({
            "id": 1, "type": "lovelace/config/save",
            "url_path": url_path, "config": config
        }))
        return await ws.recv()
```

## Repository Structure

```
generate_dashboard.py          # Main dashboard generator
generate_insights_dashboard.py # Insights dashboard generator
dashboard_helpers.py           # Card creation helpers
templates/                     # Decluttering card templates (8 JSON)
rooms/                         # View modules (overview, open_space, private, utility, floor_plan)
configs/                       # HA config files (manual copy via vi required)
scripts/                       # Utility scripts (Hyundai token extractor, entity cleanup)
```

## Deploying Changes

**Dashboards** (auto-deploy via WebSocket API):
```bash
source ~/.zshrc && source /tmp/ha_venv/bin/activate && python3 generate_dashboard.py
source ~/.zshrc && source /tmp/ha_venv/bin/activate && python3 generate_insights_dashboard.py
```

**Config files** (`configs/`) - Manual copy required:
1. Docker → homeassistant → Console
2. `vi /config/automations.yaml` (or other config file)
3. Delete all (`gg` then `dG`), paste, save (`:wq`)
4. Scenes/Scripts: Developer Tools → YAML → Reload
5. Automations/Sensors: Restart HA container

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

- ✅ Deploy dashboards automatically (never ask user to run commands)
- ✅ Use WebSocket API for dashboards, REST API for queries only
- ❌ Config files cannot be deployed via API (manual vi copy required)
- ❌ Don't assume `light.*` entities are dimmable

## Utility Scripts

- `scripts/delete_entities.sh` - Remove entities from registry (creates backup)
- `scripts/HyundaiFetchApiTokensSelenium.py` - Extract Hyundai EU refresh token (requires OAuth2 credentials)

## Floor Plan

Edit device positions in `rooms/floor_plan.py` using percentage coordinates (`left`, `top`).

## Future Work

**Unraid Integration** (not working):
- Goal: Monitor array status, disk health, Docker containers, storage capacity
- Approach: HACS integration `domalab/ha-unraid` with Unraid 7.2+ built-in API
- Blocker: API key configuration not completed; use LAN IP (`192.168.1.3`) not hostname
