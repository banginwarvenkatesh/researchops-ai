"""
Test the Plugin Framework.
"""

from framework.plugin_registry import PluginRegistry
from framework.capabilities import Capability
from framework.exceptions import PluginAlreadyRegisteredError
from plugins.stock.stock_plugin import StockPlugin


def main():

    print("=" * 60)
    print("ResearchOps AI Plugin Framework Test")
    print("=" * 60)

    registry = PluginRegistry()

    stock_plugin = StockPlugin()

    # Initialize Plugin
    stock_plugin.initialize()

    # Register Plugin
    registry.register(stock_plugin)

    print("\nRegistered Plugins:")
    print(registry.list_plugins())

    # Get Plugin
    plugin = registry.get_plugin("stock_plugin")

    print("\nPlugin Metadata:")
    print(plugin.metadata)

    # Execute Plugin
    result = plugin.execute(symbol="RELIANCE")

    print("\nExecution Result:")
    print(result)

    # Find Plugin By Capability
    plugins = registry.find_plugins_by_capability(
        Capability.STOCK_QUOTE
    )

    print("\nPlugins supporting STOCK_QUOTE:")
    print([p.metadata.name for p in plugins])

    # Duplicate Registration Test
    try:
        registry.register(stock_plugin)
    except PluginAlreadyRegisteredError as e:
        print("\nDuplicate Registration Test:")
        print(e)

    stock_plugin.shutdown()

    print("\nFramework Test Completed Successfully.")


if __name__ == "__main__":
    main()