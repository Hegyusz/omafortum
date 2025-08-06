"""Platform for sensor integration."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .const import CONF_LOCALE, DOMAIN
from .sensors import MittFortumCostSensor, MittFortumEnergySensor

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up MittFortum sensors based on a config entry."""
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]
    device = data["device"]
    locale = entry.data[CONF_LOCALE]

    # Create sensor entities
    entities = [
        MittFortumEnergySensor(coordinator, device),
        MittFortumCostSensor(coordinator, device, locale),
    ]

    async_add_entities(entities, update_before_add=True)
