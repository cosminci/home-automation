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

def mushroom_thermostat(entity, name=" ", icon="mdi:heating-coil"):
    """Shorthand for mushroom thermostat template (no off mode, tap opens more-info)"""
    return {
        "type": "custom:decluttering-card",
        "template": "mushroom_thermostat",
        "variables": [{"entity": entity}, {"name": name}, {"icon": icon}]
    }

def button_scene(entity, name, icon):
    """Shorthand for button scene template"""
    return {
        "type": "custom:decluttering-card",
        "template": "button_scene",
        "variables": [{"entity": entity}, {"name": name}, {"icon": icon}]
    }

def mushroom_entity(entity, name, icon, color="none"):
    """Shorthand for mushroom entity template (read-only sensors)"""
    return {
        "type": "custom:decluttering-card",
        "template": "mushroom_entity",
        "variables": [{"entity": entity}, {"name": name}, {"icon": icon}, {"color": color}]
    }

def network_button(entity, icon, color="red"):
    """Shorthand for network button template"""
    return {
        "type": "custom:decluttering-card",
        "template": "network_button",
        "variables": [{"entity": entity}, {"icon": icon}, {"color": color}]
    }

def network_device_status(entity, name, icon):
    """Shorthand for network device status template"""
    return {
        "type": "custom:decluttering-card",
        "template": "network_status",
        "variables": [{"entity": entity}, {"name": name}, {"icon": icon}]
    }

def mushroom_media_player(entity, icon="mdi:television", color="blue"):
    """Compact media player card (power + volume)"""
    return {
        "type": "custom:mushroom-entity-card",
        "entity": entity,
        "icon": icon,
        "icon_color": color,
        "primary_info": "none",
        "secondary_info": "none",
        "tap_action": {"action": "toggle"}
    }

def mushroom_select(entity, name, icon, color="blue"):
    """Compact select card"""
    return {
        "type": "custom:mushroom-select-card",
        "entity": entity,
        "name": name,
        "icon": icon,
        "icon_color": color,
        "secondary_info": "none"
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

def create_room_section(title, emoji, cards):
    """
    Create standardized room section with title and content.

    Args:
        title: Room name (e.g., "Living Room")
        emoji: Emoji icon for the room (e.g., "🛋️")
        cards: List of cards to display in the room section

    Returns:
        Dictionary containing the room section configuration
    """
    return {
        "type": "grid",
        "column_span": 4,
        "cards": [
            {
                "type": "custom:mushroom-title-card",
                "title": f"{emoji} {title}",
                "alignment": "center"
            },
            {
                "type": "custom:stack-in-card",
                "cards": cards
            }
        ]
    }

