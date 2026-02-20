"""
Shared WebSocket deployment logic for Home Assistant dashboards.
"""

import asyncio
import json
import os
import sys
import websockets

HA_URL = "ws://192.168.1.3:8123/api/websocket"
HA_TOKEN = os.environ.get("HA_TOKEN")


def check_token():
    """Validate that HA_TOKEN is set. Exits if not."""
    if not HA_TOKEN:
        print("Error: HA_TOKEN environment variable is not set.")
        print("Set it in ~/.zshrc or run: export HA_TOKEN='your_token'")
        sys.exit(1)


async def deploy_dashboard(url_path, config, create_if_missing=False, title=None, icon=None):
    """Deploy a dashboard config to Home Assistant via WebSocket.

    Args:
        url_path: Dashboard URL path (e.g. 'clean-home', 'home-insights')
        config: The full dashboard config dict
        create_if_missing: If True, create the dashboard first if save fails
        title: Dashboard title (required if create_if_missing is True)
        icon: Dashboard icon (required if create_if_missing is True)
    """
    check_token()
    print(f"\nDeploying dashboard '{url_path}'...")

    async with websockets.connect(HA_URL) as websocket:
        # Authenticate
        await websocket.recv()  # auth_required
        await websocket.send(json.dumps({
            "type": "auth",
            "access_token": HA_TOKEN
        }))
        auth_result = json.loads(await websocket.recv())
        if auth_result.get("type") != "auth_ok":
            print(f"Error: Authentication failed: {auth_result}")
            sys.exit(1)

        # Save dashboard config
        msg_id = 2
        await websocket.send(json.dumps({
            "id": msg_id,
            "type": "lovelace/config/save",
            "url_path": url_path,
            "config": config
        }))

        response = json.loads(await websocket.recv())

        # If save failed and create_if_missing, try creating the dashboard first
        if not response.get("success") and create_if_missing and title:
            msg_id += 1
            await websocket.send(json.dumps({
                "id": msg_id,
                "type": "lovelace/dashboards/create",
                "url_path": url_path,
                "title": title,
                "icon": icon or "mdi:view-dashboard",
                "mode": "storage"
            }))
            create_result = json.loads(await websocket.recv())

            if create_result.get("success"):
                msg_id += 1
                await websocket.send(json.dumps({
                    "id": msg_id,
                    "type": "lovelace/config/save",
                    "url_path": url_path,
                    "config": config
                }))
                response = json.loads(await websocket.recv())

        if response.get("success"):
            print("Dashboard deployed successfully!")
        else:
            print(f"Error: Deployment failed: {response}")
            sys.exit(1)
