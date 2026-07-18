"""
Custom exceptions for the ResearchOps AI Framework.

All framework-specific exceptions should inherit from FrameworkError.
"""


class FrameworkError(Exception):
    """Base exception for the framework."""

    pass


class PluginError(FrameworkError):
    """Base exception for all plugin-related errors."""

    pass


class PluginAlreadyRegisteredError(PluginError):
    """Raised when attempting to register a plugin that already exists."""

    pass


class PluginNotFoundError(PluginError):
    """Raised when a requested plugin cannot be found."""

    pass


class PluginInitializationError(PluginError):
    """Raised when a plugin fails during initialization."""

    pass


class PluginExecutionError(PluginError):
    """Raised when a plugin fails during execution."""

    pass


class PluginHealthCheckError(PluginError):
    """Raised when a plugin fails its health check."""

    pass


class PluginDisabledError(PluginError):
    """Raised when attempting to execute a disabled plugin."""

    pass


class CapabilityNotSupportedError(FrameworkError):
    """Raised when no plugin supports the requested capability."""

    pass


class ConfigurationError(FrameworkError):
    """Raised when framework configuration is invalid."""

    pass