from dataclasses import dataclass
from datetime import datetime
from typing import List
from pathlib import Path


@dataclass
class GenericObject:
    name: str
    create_date: datetime
    tags: List[str]

    def __hash__(self) -> int:
        return abs(hash(self.name))

    def get_file_name(self):
        return str(hash(self)) + ".pkl"

    def __str__(self):
        date_str = self.create_date.strftime("%d %B %Y")
        return f"{self.name} - {date_str} - {self.tags}"


@dataclass
class Note(GenericObject):
    content: str

    def __hash__(self) -> int:
        return super().__hash__()


@dataclass
class FileNote(GenericObject):
    file_path: Path

    def __hash__(self) -> int:
        return super().__hash__()


@dataclass
class Task(GenericObject):
    curr_status: str
    description: str
    deadline: datetime
    priority: int
    subtasks: List['Task']

    def __post_init__(self):
        # Check for empty fields:
        for attribute, value in self.__dict__.items():
            try:
                if attribute == '': 
                    attribute = None
            except:
                pass
        # Check for priority field
        if self.priority is not None and not isinstance(self.priority, int):
            try:
                self.priority = int(self.priority)
            except ValueError:
                print(f"Invalid value for priority: {self.priority}")


    def __hash__(self) -> int:
        return super().__hash__()

    @staticmethod
    def check_task_arguments(args) -> bool:
        pass

    def __str__(self):
        ret = f"[{self.curr_status}] {self.name}"
        if self.tags != []:
            ret += f" - {self.tags}"
        if self.subtasks != []:
            ret += f" with {len(self.subtasks)} subtasks"
        return ret
    
    def detailded_task_str(self) -> str:
        date_str = self.create_date.strftime("%d %B %Y")
        return f"[{self.curr_status}] {self.name} - {self.tags}"