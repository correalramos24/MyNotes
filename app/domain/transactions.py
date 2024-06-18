
from datetime import datetime as dt
from .objects import *
from utils.utils import *
from persistance.persistance_tx import *

def create_note(name: str, content: str, format: str,
                tag_list: list[str] = [],
                create_date : dt = dt.now()):
    
    
    # Create object:
    aux = Note(name, content, format, create_date, tag_list)
    log[0](f"Create note object with id {hash(aux)}\n{aux}\n")
    
    # Store into the DB:
    store_object(aux, 'notes')

    return


def list_notes() -> None:
    log[0](f"Listing all notes instances:\n")
    list_object('notes')


    