from datetime import datetime as dt

from .definitions import *
from app.utils.my_logging import log
from app.persistance.database_controller import DatabaseController

persistence: DatabaseController


def init_domain():
    log[0](f"Init domain module\n")
    global persistence
    persistence = DatabaseController(Path("/home/vcorreal/MyNotes"))
    log[0](f"Init domain: DONE\n")


def create_note(name: str,
                content: str,
                tag_list=None,
                creation_date: dt = dt.now()):
    # Create object:
    if tag_list is None:
        tag_list = []
    aux = Note(name, creation_date, tag_list, content)
    log[0](f"Create note object with id {hash(aux)}\n{aux}\n")

    # Store into the DB:
    persistence.save_object(aux, persistence.BD_NOTES_FOLDER)

    return


def create_note_from_file(file_path: Path, name: str = None,
                          tag_list=None,
                          create_date: dt = dt.now()):
    # Check if the file exists, then store in the BD
    if tag_list is None:
        tag_list = []
    if not file_path.exists():
        print(f"ERROR: Unable to find file {file_path}")
        return

    # Name will be the name of the file is None:
    if name is None:
        name = file_path.name

    # Store task into DB && a copy of the file:
    internal_path = persistence.store_file(file_path)
    aux = FileNote(name, create_date, tag_list, internal_path)
    persistence.save_object(aux, 'notes')


def list_notes() -> None:
    log[0](f"Listing all notes instances:\n")
    instances = persistence.list_objects(persistence.BD_NOTES_FOLDER)

    for instance in instances:
        print(instance)


def list_tasks() -> None:
    log[0](f"Listing all tasks instances:\n")
    persistence.list_objects(persistence.BD_TASKS_FOLDER)
