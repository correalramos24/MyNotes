
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from typing import List

status = Enum('stats', ['todo', 'done', 'noted'])

@dataclass
class GenericObject:
    name: str
    content: str
    format: str
    create_date: datetime
    # author: str Not required yet!

    def __hash__(self) -> int:
        return abs(hash(self.name))

@dataclass
class Note(GenericObject):
    tags: List[str]
    def __hash__(self) -> int:
        return super().__hash__()

@dataclass
class Task(GenericObject):
    curr_status: status
    deadline: datetime
    priority: int
    subtasks : List['Task']

    def __hash__(self) -> int:
        return super().__hash__()
