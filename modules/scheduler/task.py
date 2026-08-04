"""
Scheduled Task
Project PEGASUS
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:

    id: int | None = None
    command: str = ""   
    execute_at: datetime | None = None