from dataclasses import dataclass
from typing import Dict

@dataclass
class Document:
    id: str
    title: str
    content: str
    source: str
    metadata: Dict