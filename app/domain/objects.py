
from dataclasses import dataclass
from datetime import datetime
from typing import List
from pathlib import Path

@dataclass
class GenericObject:
    name: str
    create_date: datetime
    tags: List[str]
    # author: str Not required yet!

    def __hash__(self) -> int:
        return abs(hash(self.name))

    def get_file_name(self):
        return str(hash(self)) + ".pkl"

@dataclass
class Note(GenericObject):
    content: str
    def __hash__(self) -> int:
        return super().__hash__()

@dataclass
class FileNote(GenericObject):
    file_path : Path
    def __hash__(self) -> int:
        return super().__hash__()

@dataclass
class Task(GenericObject):
    curr_status: str
    deadline: datetime
    priority: int
    subtasks : List['Task']

    def __hash__(self) -> int:
        return super().__hash__()
