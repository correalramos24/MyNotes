from datetime import datetime as dt

from .definitions import *
from app.utils.my_logging import log
from app.persistance.database_controller import ObjectDatabaseController

persistence: ObjectDatabaseController


def init_domain():
    log[0](f"Init domain module\n")
    global persistence
    persistence = ObjectDatabaseController(Path("/home/vcorreal/MyNotes"))
    log[0](f"Init domain: DONE\n")


def create_tasks(name: str, description: str,
                 deadline: dt,
                 init_state: str = "TODO",
                 priority: int = 0,
                 tag_list=None,
                 creation_date: dt = dt.now()
                 ):
    # Create object:
    if tag_list is None:
        tag_list = []
    aux = Task(name, creation_date, tag_list, init_state, description, deadline, priority, [])
    log[0](f"Create task object with id {hash(aux)}\n{aux}\n")
    persistence.save_object(aux, persistence.BD_TASKS_FOLDER)


def create_subtask(super_task_hash: int,
                   name: str, description: str,
                   deadline: dt,
                   init_state: str = "TODO",
                   priority: int = 0,
                   tag_list=None,
                   creation_date: dt = dt.now()):

    super_task_obj = persistence.read_task(super_task_hash)
    if super_task_obj is None:
        print("Invalid task hash", super_task_hash, "(super-task)")

    aux_task = Task(name, creation_date, tag_list, init_state, description, deadline, priority, [])
    super_task_obj.subtasks.append(aux_task)
    persistence.save_object(super_task_obj, persistence.BD_TASKS_FOLDER)


def link_subtasks(super_task_hash: int, sub_task_hash: int):
    log[0](f"Linking {sub_task_hash} to {super_task_hash} \n")

    # Load OBJs:
    super_task_obj = persistence.read_task(super_task_hash)
    if super_task_obj is None:
        print("Invalid task hash", super_task_hash, "(super-task)")

    sub_task_obj = persistence.read_task(sub_task_hash)
    if sub_task_obj is None:
        print("Invalid task hash", sub_task_obj, "(subtask)")

    # Store the sub-task into the super-task
    super_task_obj.subtasks.append(sub_task_obj)

    persistence.save_object(super_task_obj, persistence.BD_TASKS_FOLDER)
    persistence.delete_object(sub_task_hash)


def create_note(name: str, content: str,
                tag_list=None, creation_date: dt = dt.now()):
    # Create object:
    if tag_list is None:
        tag_list = []
    aux = Note(name, creation_date, tag_list, content)
    log[0](f"Create note object with id {hash(aux)}\n{aux}\n")

    # Store into the DB:
    persistence.save_object(aux, persistence.BD_NOTES_FOLDER)


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


def list_notes() -> List[GenericObject]:
    log[0](f"Listing all notes instances:\n")
    instances = persistence.list_objects(persistence.BD_NOTES_FOLDER)

    for instance in instances:
        print(instance)

    return instances


def list_tasks() -> List[GenericObject]:
    log[0](f"Listing all tasks instances:\n")
    instances = persistence.list_objects(persistence.BD_TASKS_FOLDER)

    for instances in instances:
        print(instances)

    return instances


