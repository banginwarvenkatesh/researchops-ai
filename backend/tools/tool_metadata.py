from dataclasses import dataclass
from typing import List


@dataclass
class ToolMetadata:
    name: str
    description: str
    category: str
    supported_markets: List[str]