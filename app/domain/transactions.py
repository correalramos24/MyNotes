
from datetime import datetime as dt
from pathlib import Path

from .objects import *
from utils.utils import log
from persistance.persistance_tx import *
from persistance.constants import *

def init_domain():
    log[0](f"Init domain module\n")
    init_persistance(Path("/home/vcorreal/MyNotes"))
    log[0](f"Init domain: DONE\n")

def create_note(name: str, 
                content: str, 
                tag_list: list[str] = [],
                create_date : dt = dt.now()):
    
    
    # Create object:
    aux = Note(name, content, create_date, tag_list)
    log[0](f"Create note object with id {hash(aux)}\n{aux}\n")
    
    # Store into the DB:
    store_object(aux, 'notes')

    return

def create_note_from_file(file_path: Path, name: str = None,
                    tag_list: list[str] = [],
                    create_date : dt = dt.now()):
    
    # Check if the file exists, then store in the BD
    if not file_path.exists():
        print(f"ERROR: Unable to find file {file_path}")
        return
        
    # Name will be the name of the file is None:
    if name is None:
        name = file_path.name

    # Store task into DB && a copy of the file:
    internal_path = store_file(file_path)
    aux = FileNote(name, create_date, tag_list, internal_path)
    store_object(aux, 'notes')


def list_notes() -> None:
    log[0](f"Listing all notes instances:\n")
    instances = list_objects(BD_NOTES_FOLDER)

    for instance in instances:
        print(instance)


def list_tasks() -> None:
    log[0](f"Listing all tasks instances:\n")
    list_objects(BD_TASKS_FOLDER)