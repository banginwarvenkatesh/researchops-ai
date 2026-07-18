"""
Central registry for managing plugins.
"""

from typing import Dict, List

from framework.capabilities import Capability
from framework.exceptions import (
    PluginAlreadyRegisteredError,
    PluginNotFoundError,
)
from framework.plugin_base import PluginBase


class PluginRegistry:
    """
    Central registry for all loaded plugins.
    """

    def __init__(self):
        self._plugins: Dict[str, PluginBase] = {}

    def register(self, plugin: PluginBase) -> None:
        """
        Register a plugin.
        """
        name = plugin.metadata.name

        if name in self._plugins:
            raise PluginAlreadyRegisteredError(
                f"Plugin '{name}' is already registered."
            )

        self._plugins[name] = plugin

    def unregister(self, plugin_name: str) -> None:
        """
        Remove a plugin.
        """
        if plugin_name not in self._plugins:
            raise PluginNotFoundError(
                f"Plugin '{plugin_name}' not found."
            )

        del self._plugins[plugin_name]

    def get_plugin(self, plugin_name: str) -> PluginBase:
        """
        Retrieve a plugin by name.
        """
        if plugin_name not in self._plugins:
            raise PluginNotFoundError(
                f"Plugin '{plugin_name}' not found."
            )

        return self._plugins[plugin_name]

    def has_plugin(self, plugin_name: str) -> bool:
        """
        Check whether plugin exists.
        """
        return plugin_name in self._plugins

    def list_plugins(self) -> List[str]:
        """
        Return names of all registered plugins.
        """
        return sorted(self._plugins.keys())

    def list_enabled_plugins(self) -> List[str]:
        """
        Return enabled plugins.
        """
        return [
            plugin.metadata.name
            for plugin in self._plugins.values()
            if plugin.metadata.enabled
        ]

    def find_plugins_by_capability(
        self,
        capability: Capability,
    ) -> List[PluginBase]:
        """
        Find plugins supporting a capability.
        """
        return [
            plugin
            for plugin in self._plugins.values()
            if capability in plugin.metadata.capabilities
            and plugin.metadata.enabled
        ]