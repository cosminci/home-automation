from dashboard_helpers import (mushroom_switch, mushroom_light, mushroom_climate, network_button,
                               network_status, floor_heating_thermostat)


def get_view():
    return {
        "title": "Private Spaces",
        "path": "tab_private",
        "icon": "mdi:bed",
        "cards": [
            # Bedroom
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 3,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:bed",
                                "icon_color": "blue",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.rail_spots", "mdi:track-light"),
                            mushroom_switch("switch.ceiling_light", "mdi:ceiling-light")
                        ]
                    },
                    mushroom_light("light.led_strip"),
                    mushroom_climate("climate.ac_bedroom"),
                    {
                        "type": "custom:mushroom-media-player-card",
                        "entity": "media_player.lg_webos_tv_oled48c22lb",
                        "icon": "mdi:television",
                        "use_media_info": False,
                        "show_volume_level": False,
                        "volume_controls": ["volume_buttons"],
                        "collapsible_controls": True,
                        "primary_info": "none",
                        "secondary_info": "none"
                    }
                ]
            },
            # Shower Bathroom
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 4,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:shower-head",
                                "icon_color": "blue",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.led_strip_2", "mdi:led-strip"),
                            mushroom_switch("switch.ceiling_spots_3", "mdi:spotlight"),
                            mushroom_switch("switch.ventilator", "mdi:fan", "blue")
                        ]
                    },
                    floor_heating_thermostat(
                        "climate.tze200_b6wax7g0_ts0601_thermostat",
                        "sensor.tze200_b6wax7g0_ts0601_lqi"
                    )
                ]
            },
            # Kid's Room
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 4,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:teddy-bear",
                                "icon_color": "pink",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.rail_spots_3", "mdi:track-light"),
                            mushroom_switch("switch.ceiling_light_2", "mdi:ceiling-light"),
                            mushroom_switch("switch.wall_light", "mdi:wall-sconce")
                        ]
                    },
                    {
                        "type": "grid",
                        "columns": 2,
                        "square": False,
                        "cards": [
                            mushroom_light("light.led_strip_window_4", "🪟"),
                            mushroom_light("light.led_strip_bed", "🛏️")
                        ]
                    },
                    mushroom_climate("climate.ac_iacopewee"),
                    {
                        "type": "grid",
                        "columns": 4,
                        "square": False,
                        "cards": [
                            network_status("sensor.ap_iacopewee_state"),
                            {
                                "type": "custom:mushroom-entity-card",
                                "entity": "sensor.ap_iacopewee_uptime",
                                "icon": "mdi:clock-outline",
                                "primary_info": "none",
                                "secondary_info": "none"
                            },
                            network_button("button.ap_iacopewee_restart", "mdi:restart"),
                            network_button("button.switch_port_14_power_cycle", "mdi:power-plug-off")
                        ]
                    },
                    {
                        "type": "picture-entity",
                        "entity": "camera.tapotroceni_hd_stream",
                        "show_name": True,
                        "show_state": False,
                        "name": "📹 Kid's Room Camera"
                    }
                ]
            },
            # Bathroom Tub
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 4,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:bathtub",
                                "icon_color": "blue",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.led_strip", "mdi:led-strip"),
                            mushroom_switch("switch.ceiling_spots_2", "mdi:spotlight"),
                            mushroom_switch("switch.ventilator_2", "mdi:fan", "blue")
                        ]
                    },
                    floor_heating_thermostat(
                        "climate.tze200_b6wax7g0_ts0601_thermostat_2",
                        "sensor.tze200_b6wax7g0_ts0601_lqi_2"
                    )
                ]
            },
            # Office
            {
                "type": "custom:stack-in-card",
                "cards": [
                    {
                        "type": "grid",
                        "columns": 2,
                        "square": False,
                        "cards": [
                            {
                                "type": "custom:mushroom-template-card",
                                "icon": "mdi:desk",
                                "icon_color": "blue",
                                "primary": " ",
                                "secondary": " "
                            },
                            mushroom_switch("switch.ceiling_light_4", "mdi:ceiling-light")
                        ]
                    },
                    mushroom_light("light.led_strip_window"),
                    mushroom_climate("climate.ac_office")
                ]
            }
        ]
    }
