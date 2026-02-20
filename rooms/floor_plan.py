"""
Floor Plan View - Interactive floor plan with device overlays

CONFIGURATION GUIDE:
- Adjust 'left' and 'top' values (percentages) to position icons on your floor plan
- 'left': 0% = far left, 100% = far right
- 'top': 0% = top, 100% = bottom
- Start with rough estimates, then fine-tune by viewing the dashboard
"""

# ============================================================================
# DEVICE CONFIGURATION - Edit positions here (left%, top%)
# ============================================================================

DEVICES = {
    # Living Room
    "climate.ac_living": {"left": "23%", "top": "50%", "icon": "mdi:air-conditioner", "color_on": "blue"},
    "light.led_strip_window_2": {"left": "5%", "top": "85%", "icon": "mdi:led-strip-variant", "color_on": "orange"},
    "switch.dining_light": {"left": "17%", "top": "50%", "icon": "mdi:ceiling-light", "color_on": "orange"},
    "switch.ceiling_light_3": {"left": "17%", "top": "70%", "icon": "mdi:ceiling-fan-light", "color_on": "orange"},
    "light.ceiling_spots": {"left": "23%", "top": "70%", "icon": "mdi:spotlight", "color_on": "orange"},
    "media_player.hub_77_oled": {"left": "33%", "top": "73%", "icon": "mdi:television", "color_on": "green"},
    "media_player.soundbar_q990b": {"left": "33%", "top": "68%", "icon": "mdi:speaker", "color_on": "green"},
    "camera.camera_living_medium_resolution_channel": {"left": "28%", "top": "33%", "icon": "mdi:cctv", "color_on": "red"},
    "sensor.ap_living_state": {"left": "33%", "top": "55%", "icon": "mdi:access-point", "color_on": "green"},

    # Kitchen
    "light.led_strip_window_3": {"left": "5%", "top": "48%", "icon": "mdi:led-strip-variant", "color_on": "orange"},
    "switch.led_strip_countertop": {"left": "24%", "top": "29%", "icon": "mdi:led-strip", "color_on": "orange"},
    "switch.rail_spots_2": {"left": "18%", "top": "38%", "icon": "mdi:track-light", "color_on": "orange"},
    "switch.ceiling_spots": {"left": "23%", "top": "38%", "icon": "mdi:spotlight", "color_on": "orange"},
    "sensor.dishwasher_operation_state": {"left": "16%", "top": "29%", "icon": "mdi:dishwasher", "color_on": "blue"},
    "sensor.oven_operation_state": {"left": "11%", "top": "29%", "icon": "mdi:stove", "color_on": "orange"},
    "sensor.cooktop_operation_state": {"left": "11%", "top": "37%", "icon": "mdi:pot-steam", "color_on": "orange"},

    # Hallway
    "switch.ceiling_spots_4": {"left": "50%", "top": "35%", "icon": "mdi:spotlight", "color_on": "orange"},
    "camera.camera_hallway_medium_resolution_channel": {"left": "72%", "top": "37%", "icon": "mdi:cctv", "color_on": "red"},
    "sensor.cloud_gateway_max_state": {"left": "43%", "top": "23%", "icon": "mdi:router-wireless", "color_on": "green"},
    "sensor.switch_state": {"left": "43%", "top": "28%", "icon": "mdi:switch", "color_on": "green"},
    "binary_sensor.slzb_mr4u_ethernet": {"left": "47%", "top": "27%", "icon": "mdi:zigbee", "color_on": "green"},

    # Staircase
    "switch.staircase_lights": {"left": "88%", "top": "32%", "icon": "mdi:ceiling-light-multiple", "color_on": "orange"},

    # Terrace
    "switch.terrace_lights": {"left": "64%", "top": "70%", "icon": "mdi:outdoor-lamp", "color_on": "orange"},

    # Bedroom
    "climate.ac_bedroom": {"left": "23%", "top": "15%", "icon": "mdi:air-conditioner", "color_on": "blue"},
    "light.led_strip": {"left": "6%", "top": "6%", "icon": "mdi:led-strip-variant", "color_on": "orange"},
    "switch.rail_spots": {"left": "35%", "top": "15%", "icon": "mdi:track-light", "color_on": "orange"},
    "switch.ceiling_light": {"left": "17%", "top": "14%", "icon": "mdi:ceiling-light", "color_on": "orange"},
    "media_player.lg_webos_tv_oled48c22lb": {"left": "18%", "top": "22%", "icon": "mdi:television", "color_on": "green"},

    # Shower Bathroom
    "switch.led_strip_2": {"left": "50%", "top": "5%", "icon": "mdi:led-strip", "color_on": "orange"},
    "switch.ceiling_spots_3": {"left": "50%", "top": "11%", "icon": "mdi:spotlight", "color_on": "orange"},
    "switch.ventilator": {"left": "57%", "top": "5%", "icon": "mdi:fan", "color_on": "blue"},
    "climate.tze200_b6wax7g0_ts0601_thermostat": {"left": "57%", "top": "11%", "icon": "mdi:radiator", "color_on": "red"},

    # Kid's Room
    "climate.ac_iacopewee": {"left": "83%", "top": "51%", "icon": "mdi:air-conditioner", "color_on": "blue"},
    "light.led_strip_window_4": {"left": "80%", "top": "58%", "icon": "mdi:led-strip-variant", "color_on": "orange"},
    "light.led_strip_bed": {"left": "90%", "top": "43%", "icon": "mdi:led-strip-variant", "color_on": "orange"},
    "switch.rail_spots_3": {"left": "64%", "top": "50%", "icon": "mdi:track-light", "color_on": "orange"},
    "switch.ceiling_light_2": {"left": "77%", "top": "50%", "icon": "mdi:ceiling-light", "color_on": "orange"},
    "switch.wall_light": {"left": "80%", "top": "43%", "icon": "mdi:wall-sconce", "color_on": "orange"},
    "sensor.ap_iacopewee_state": {"left": "94%", "top": "50%", "icon": "mdi:access-point", "color_on": "green"},
    "camera.tapotroceni_hd_stream": {"left": "93%", "top": "59%", "icon": "mdi:cctv", "color_on": "red"},

    # Bathroom Tub
    "switch.led_strip": {"left": "56%", "top": "47%", "icon": "mdi:led-strip", "color_on": "orange"},
    "switch.ceiling_spots_2": {"left": "50%", "top": "47%", "icon": "mdi:spotlight", "color_on": "orange"},
    "switch.ventilator_2": {"left": "40%", "top": "48%", "icon": "mdi:fan", "color_on": "blue"},
    "climate.tze200_b6wax7g0_ts0601_thermostat_2": {"left": "40%", "top": "43%", "icon": "mdi:radiator", "color_on": "red"},

    # Office
    "climate.ac_office": {"left": "47%", "top": "60%", "icon": "mdi:air-conditioner", "color_on": "blue"},
    "light.led_strip_window": {"left": "51%", "top": "84%", "icon": "mdi:led-strip-variant", "color_on": "orange"},
    "switch.ceiling_light_4": {"left": "47%", "top": "70%", "icon": "mdi:ceiling-light", "color_on": "orange"},

    # Washer Room
    "sensor.washing_machine_operation_state": {"left": "53%", "top": "20%", "icon": "mdi:washing-machine", "color_on": "blue"},
    "sensor.dryer_operation_state": {"left": "58%", "top": "20%", "icon": "mdi:tumble-dryer", "color_on": "blue"},
}

# ============================================================================
# FLOOR PLAN GENERATION - Don't edit below unless changing functionality
# ============================================================================

def create_state_icon(entity_id, config):
    """Create a state-based icon element for the floor plan using card-mod for conditional styling"""
    entity_type = entity_id.split('.')[0]

    # Build the condition for "active" state based on entity type
    # These are Jinja2 templates processed by Home Assistant
    if entity_type == 'climate':
        if config.get('icon') == 'mdi:radiator':
            # TRV thermostats: active when setpoint > current temp (heating needed)
            condition = (
                f"state_attr('{entity_id}', 'temperature') | float(0) > "
                f"state_attr('{entity_id}', 'current_temperature') | float(100)"
            )
        else:
            # AC units: active when not off
            condition = f"states('{entity_id}') != 'off'"
    elif entity_type == 'camera':
        condition = f"states('{entity_id}') != 'unavailable'"
    elif entity_type == 'media_player':
        condition = f"states('{entity_id}') not in ['off', 'idle', 'standby', 'unavailable']"
    elif entity_type == 'binary_sensor':
        # Binary sensors: active when 'on'
        condition = f"states('{entity_id}') == 'on'"
    elif entity_type == 'sensor' and 'operation_state' in entity_id:
        # Appliance sensors: active when running (not ready, inactive, off, etc.)
        condition = f"states('{entity_id}') not in ['ready', 'inactive', 'off', 'unavailable', 'unknown']"
    elif entity_type == 'sensor' and '_state' in entity_id:
        # Network device sensors: active when connected
        condition = f"states('{entity_id}') in ['Connected', 'connected']"
    else:  # lights, switches
        condition = f"states('{entity_id}') == 'on'"

    # Build card-mod style with Jinja2 template for conditional coloring
    # Using --state-icon-color CSS variable (modern HA) with state_color: false
    color_on = config['color_on']
    card_mod_style = f"""
      :host {{
        --state-icon-color: {{% if {condition} %}}{color_on}{{% else %}}grey{{% endif %}};
      }}
    """

    return {
        "type": "state-icon",
        "entity": entity_id,
        "icon": config["icon"],
        "state_color": False,  # Disable default state coloring
        "tap_action": {"action": "more-info"},
        "style": {
            "left": config["left"],
            "top": config["top"],
            "transform": "translate(-50%, -50%)",
            "--mdc-icon-size": "24px"
        },
        "card_mod": {
            "style": card_mod_style
        }
    }


def get_view():
    """Generate the floor plan view"""

    # Create all device elements
    elements = [create_state_icon(entity_id, config) for entity_id, config in DEVICES.items()]

    return {
        "title": "Floor Plan",
        "path": "floor_plan",
        "icon": "mdi:floor-plan",
        "cards": [
            {
                "type": "picture-elements",
                "image": "/local/floor_plan_4k_inverted.jpg?v=3",
                "elements": elements
            }
        ]
    }

