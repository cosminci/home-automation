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


