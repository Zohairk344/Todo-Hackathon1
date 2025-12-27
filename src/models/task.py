from dataclasses import dataclass
from typing import Optional

# Implements: T-004
@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = None
    status: str = "Pending"
