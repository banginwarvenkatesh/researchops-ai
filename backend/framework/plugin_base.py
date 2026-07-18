"""
Abstract base class for all plugins.

Every plugin in ResearchOps AI must inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict

from framework.plugin_metadata import PluginMetadata


class PluginBase(ABC):
    """
    Base class for every plugin.
    """

    def __init__(self, metadata: PluginMetadata):
        self._metadata = metadata

    @property
    def metadata(self) -> PluginMetadata:
        """
        Returns plugin metadata.
        """
        return self._metadata

    @abstractmethod
    def initialize(self) -> None:
        """
        Called once when the plugin is loaded.
        Used for loading models, creating API clients,
        database connections, etc.
        """
        pass

    @abstractmethod
    def execute(self, **kwargs) -> Dict[str, Any]:
        """
        Executes the plugin's primary functionality.
        """
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """
        Returns True if plugin is healthy.
        """
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """
        Cleanly release resources.
        """
        pass