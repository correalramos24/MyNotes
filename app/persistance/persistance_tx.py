
import os
import pickle
from domain.objects import *
from utils.utils import *
import glob

bd_path = None

def init_persistance(bd_abs_path: str):
    global bd_path
    log[0](f"Init persistance module at {bd_abs_path}\n")

    # Check if folder exists && .notes file, create otherwise:
    if not os.path.exists(bd_abs_path):
        log[0](f"BD not found, generating a new one\n")
        os.makedirs(bd_abs_path)
        os.makedirs(os.path.join(bd_abs_path, 'notes'), exist_ok=True)
        os.makedirs(os.path.join(bd_abs_path, 'tasks'), exist_ok=True)
        with open(os.path.join(bd_abs_path,'.notes'), 'w') as notes_file:
            notes_file.write('')  # Crear el archivo vacío
        
    if not os.path.exists(os.path.join(bd_abs_path,'.notes')):
        log[2](f"UNABLE TO FIND METADATA FILE AT {bd_abs_path}\n")

    bd_path = bd_abs_path
    log[0](f"Set runtime BD at {bd_path}\n")

    log[0](f"Init persistance: DONE\n")


def store_object(obj, obj_type):
    aux_path = os.path.join(bd_path, obj_type, f"{hash(obj)}.pkl")
    log[0](f"Storing {obj_type} object with id {hash(obj)}\n")
    
    try:
        with open(aux_path, 'wb') as obj_file:
            pickle.dump(obj, obj_file)
        log[0](f"Done {aux_path}\n")
    except Exception as e:
        log[1](str(e))
    

def __load_object__(path):
    try:
        with open(path, 'rb') as obj_file:
            obj = pickle.load(obj_file)
            return obj
    except Exception as e:
        print(e)
        return None


def load_object(obj_type, obj_hash):

    aux_path = os.path.join(bd_path, obj_type, f"{obj_hash}.pkl")
    log[0](f"Loading {obj_type} object with id {obj_hash}\n")

    obj = __load_object__(aux_path)
    
    log[0](f"Loaded!\n")
    return obj


def list_object(obj_type):
    aux_path = os.path.join(bd_path, obj_type)
    for file in glob.glob(os.path.join(aux_path, "*.pkl")):
        obj : Note = __load_object__(file)
        print(file, obj.name, obj.create_date)
    
