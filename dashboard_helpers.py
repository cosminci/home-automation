"""
Helper functions for creating dashboard cards using decluttering templates.
"""

def mushroom_switch(entity, icon, color="orange"):
    """Shorthand for mushroom switch template"""
    return {
        "type": "custom:decluttering-card",
        "template": "mushroom_switch",
        "variables": [{"entity": entity}, {"icon": icon}, {"color": color}]
    }

def mushroom_light(entity, name=" ", icon="mdi:led-strip-variant"):
    """Shorthand for mushroom light template"""
    return {
        "type": "custom:decluttering-card",
        "template": "mushroom_light",
        "variables": [{"entity": entity}, {"name": name}, {"icon": icon}]
    }

def mushroom_climate(entity, name=" ", icon="mdi:air-conditioner"):
    """Shorthand for mushroom climate template"""
    return {
        "type": "custom:decluttering-card",
        "template": "mushroom_climate",
        "variables": [{"entity": entity}, {"name": name}, {"icon": icon}]
    }


def network_button(entity, icon, color="red"):
    """Shorthand for network button template"""
    return {
        "type": "custom:decluttering-card",
        "template": "network_button",
        "variables": [{"entity": entity}, {"icon": icon}, {"color": color}]
    }


def mushroom_readonly(entity, icon, color="none"):
    """Read-only mushroom entity card (icon only)"""
    return {
        "type": "custom:mushroom-entity-card",
        "entity": entity,
        "icon": icon,
        "icon_color": color,
        "primary_info": "none",
        "secondary_info": "state",
        "tap_action": {"action": "more-info"}
    }


def network_status(entity, icon="mdi:access-point", on_states=("Connected", "connected")):
    """Network device status card with green/red icon based on state."""
    conditions = " or ".join("is_state('" + entity + "', '" + s + "')" for s in on_states)
    style = "ha-card { --card-mod-icon-color: {% if " + conditions + " %}green{% else %}red{% endif %}; }"
    return {
        "type": "custom:mushroom-entity-card",
        "entity": entity,
        "icon": icon,
        "icon_color": "none",
        "primary_info": "none",
        "secondary_info": "none",
        "card_mod": {"style": style}
    }


# Thermostat CSS template — CLIMATE_ENTITY and LQI_SENSOR are replaced at runtime
_THERMOSTAT_CSS = """
    mushroom-state-item { margin: 0 auto !important; }
    ha-card::before {
        content: '';
        position: absolute;
        top: 8px;
        right: 28px;
        width: 18px;
        height: 18px;
        {% set setpoint = state_attr('CLIMATE_ENTITY', 'temperature') | float(0) %}
        {% set current = state_attr('CLIMATE_ENTITY', 'current_temperature') | float(0) %}
        {% if setpoint > current %}
        {% set flame_color = '%23ff6600' %}
        {% else %}
        {% set flame_color = '%23888888' %}
        {% endif %}
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='{{ flame_color }}' d='M17.66 11.2C17.43 10.9 17.15 10.64 16.89 10.38C16.22 9.78 15.46 9.35 14.82 8.72C13.33 7.26 13 4.85 13.95 3C13 3.23 12.17 3.75 11.46 4.32C8.87 6.4 7.85 10.07 9.07 13.22C9.11 13.32 9.15 13.42 9.15 13.55C9.15 13.77 9 13.97 8.8 14.05C8.57 14.15 8.33 14.09 8.14 13.93C8.08 13.88 8.04 13.83 8 13.76C6.87 12.33 6.69 10.28 7.45 8.64C5.78 10 4.87 12.3 5 14.47C5.06 14.97 5.12 15.47 5.29 15.97C5.43 16.57 5.7 17.17 6 17.7C7.08 19.43 8.95 20.67 10.96 20.92C13.1 21.19 15.39 20.8 17.03 19.32C18.86 17.66 19.5 15 18.56 12.72L18.43 12.46C18.22 12 17.66 11.2 17.66 11.2M14.5 17.5C14.22 17.74 13.76 18 13.4 18.1C12.28 18.5 11.16 17.94 10.5 17.28C11.69 17 12.4 16.12 12.61 15.23C12.78 14.43 12.46 13.77 12.33 13C12.21 12.26 12.23 11.63 12.5 10.94C12.69 11.32 12.89 11.7 13.13 12C13.9 13 15.11 13.44 15.37 14.8C15.41 14.94 15.43 15.08 15.43 15.23C15.46 16.05 15.1 16.95 14.5 17.5H14.5Z'/%3E%3C/svg%3E");
        background-size: contain;
    }
    ha-card::after {
        content: '';
        position: absolute;
        top: 8px;
        right: 8px;
        width: 18px;
        height: 18px;
        {% set lqi = states('LQI_SENSOR') | int(0) %}
        {% if lqi >= 100 %}
        {% set color = '%2344bb44' %}
        {% set path = 'M12,3C7.79,3 3.7,4.41 0.38,7C4.41,12.06 7.89,16.37 12,21.5C16.08,16.42 20.24,11.24 23.65,7C20.32,4.41 16.22,3 12,3Z' %}
        {% elif lqi >= 50 %}
        {% set color = '%23ff9900' %}
        {% set path = 'M12,3C7.79,3 3.7,4.41 0.38,7C4.41,12.06 7.89,16.37 12,21.5C16.08,16.42 20.24,11.24 23.65,7C20.32,4.41 16.22,3 12,3M12,5C15.07,5 18.09,5.86 20.71,7.45L17.5,11.43C16.26,10.74 14.37,10 12,10C9.62,10 7.74,10.75 6.5,11.43L3.27,7.44C5.91,5.85 8.93,5 12,5Z' %}
        {% else %}
        {% set color = '%23dd3333' %}
        {% set path = 'M12,3C7.79,3 3.7,4.41 0.38,7C4.41,12.06 7.89,16.37 12,21.5C16.08,16.42 20.24,11.24 23.65,7C20.32,4.41 16.22,3 12,3M12,5C15.07,5 18.09,5.86 20.71,7.45L15.61,13.81C14.5,13.28 13.25,13 12,13C10.75,13 9.5,13.28 8.39,13.8L3.27,7.44C5.91,5.85 8.93,5 12,5Z' %}
        {% endif %}
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='{{ color }}' d='{{ path }}'/%3E%3C/svg%3E");
        background-size: contain;
    }
"""


def floor_heating_thermostat(climate_entity, lqi_sensor):
    """Floor heating thermostat card with flame and WiFi signal badges."""
    style = _THERMOSTAT_CSS.replace("CLIMATE_ENTITY", climate_entity).replace("LQI_SENSOR", lqi_sensor)
    return {
        "type": "custom:mushroom-climate-card",
        "entity": climate_entity,
        "name": " ",
        "icon": "mdi:heating-coil",
        "show_temperature_control": True,
        "collapsible_controls": True,
        "hvac_modes": [],
        "tap_action": {"action": "more-info"},
        "card_mod": {"style": style}
    }


def conditional_alert(entity, icon, color="red", wrap_grid=False):
    """Conditional card that only shows when entity is 'on'."""
    inner = mushroom_readonly(entity, icon, color)
    if wrap_grid:
        inner = {"type": "grid", "columns": 1, "square": False, "cards": [inner]}
    return {
        "type": "conditional",
        "conditions": [{"entity": entity, "state": "on"}],
        "card": inner
    }


