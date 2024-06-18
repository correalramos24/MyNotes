
import pickle
import shutil
from pathlib import Path

from domain.objects import GenericObject
from utils.utils import *
from .constants import *

bd_base_path = None


def init_persistance(bd_abs_path: Path):
    global bd_base_path
    log[0](f"Init persistance module at {bd_abs_path}\n")

    # Check if folder exists && .notes file, create otherwise:
    if not bd_abs_path.exists():
        log[0](f"BD not found, generating a new one\n")
        bd_abs_path.mkdir()
        Path(bd_abs_path, BD_NOTES_FOLDER).mkdir()
        Path(bd_abs_path, BD_TASKS_FOLDER).mkdir()
        Path(bd_abs_path, BD_FILES_FOLDER).mkdir()

    bd_base_path = bd_abs_path
    log[0](f"Set runtime BD at {bd_base_path}\n")

    log[0](f"Init persistance: DONE\n")


def store_file(source_path: Path, overwrite=False):
    fname = source_path.name
    log[0](f"Storing file from {source_path} with name {fname}\n")

    dst_path = Path(bd_base_path, BD_FILES_FOLDER, fname)

    if dst_path.exists() and not overwrite:
        raise Exception("File already exists, aborting")
    
    shutil.copy(source_path, dst_path)
    log[0](f"DONE=> {dst_path}\n")
    return dst_path

def store_object(obj : GenericObject, obj_type: str):
    try:
        __check_obj_type__(obj_type)
        obj_path = Path(bd_base_path, obj_type, obj.get_file_name())
        log[0](f"Storing {obj_type} object with id {hash(obj)}\n")
        __store_object__(obj_path, obj)
        log[0](f"Done {obj_path}\n")
    except Exception as e:
        log[2](str(e)+"\n")
    

def load_object(obj_type: str, obj_hash: str) -> GenericObject:
    try:
        __check_obj_type__(obj_type)
        obj_path = Path(bd_base_path, obj_type, obj_hash + ".pkl")
        log[0](f"Loading {obj_type} object with id {obj_hash}\n")
        obj = __load_object__(obj_path)
        log[0](f"Loaded!\n")
        return obj
    except Exception as e:
        log[2](str(e))
        return None

def list_objects(obj_type) -> list[GenericObject]:
    __check_obj_type__(obj_type)
    ret = []
    obj_bd_base_path = Path(bd_base_path, obj_type)
    for obj_file in obj_bd_base_path.glob("*.pkl"):
        ret.append(__load_object__(obj_file))

    return ret
    

def __check_obj_type__(obj_type):
    if obj_type not in BD_TYPES:
        raise Exception(f"Incorrect {obj_type} type!")

def __load_object__(path):
    with open(path, 'rb') as obj_file:
        obj = pickle.load(obj_file)
        return obj

def __store_object__(obj_path, obj):
    with open(obj_path, 'wb') as obj_file:
        pickle.dump(obj, obj_file) 
