from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class PluginMetadata:
    """
    Immutable metadata describing a plugin.
    """

    name: str
    version: str
    author: str
    description: str

    category: str

    capabilities: List[str] = field(default_factory=list)

    supported_markets: List[str] = field(default_factory=list)
