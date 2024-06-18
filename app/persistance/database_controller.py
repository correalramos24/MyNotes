import pickle
import shutil
from pathlib import Path
import inspect

from app.domain.definitions import GenericObject
from app.utils.my_logging import log, setLogging


class DatabaseController:
    BD_NOTES_FOLDER = 'notes'
    BD_TASKS_FOLDER = 'tasks'
    BD_FILES_FOLDER = 'files'
    BD_TYPES = [BD_TASKS_FOLDER, BD_FILES_FOLDER, BD_NOTES_FOLDER]

    def __init__(self, bd_path, logging=False):
        setLogging(logging)
        log[0](f"Init persistence module at {bd_path}\n")
        # Check if folder exists create otherwise:
        if not bd_path.exists():
            log[0](f"BD not found, generating a new one\n")
            bd_path.mkdir()
            for bd_type in self.BD_TYPES:
                log[0](f"Init {bd_type}")
                Path(bd_path, bd_type).mkdir()

        # Save bd base path as an instance member:
        self.bd_base_path = bd_path
        log[0](f"Set runtime BD at {self.bd_base_path}\n")
        log[0](f"Init persistence: DONE\n")

    def store_file(self, source_path, overwrite=False) -> Path | None:
        file_name = source_path.name
        log[0](f"Storing file from {source_path} with name {file_name}\n")

        dst_path = Path(self.bd_base_path, self.BD_FILES_FOLDER, file_name)

        if not dst_path.exists() or overwrite:
            shutil.copy(source_path, dst_path)
            log[0](f"DONE => {dst_path}\n")
            return dst_path
        else:
            print("File already exists, aborting store the file")
            return None

    def save_object(self, obj: GenericObject, obj_type: str):
        try:
            self.__check_obj_type(obj_type)
            obj_path = Path(self.bd_base_path, obj_type, obj.get_file_name())
            log[0](f"Storing {obj_type} object with id {hash(obj)}\n")
            self.__store_object(obj_path, obj)
            log[0](f"Done {obj_path}\n")
        except Exception as e:
            log[1](str(e) + "\n")

    def read_object(self, obj_hash: int, obj_type: str):
        try:
            self.__check_obj_type(obj_type)
            obj_path = Path(self.bd_base_path, obj_type, str(obj_hash) + ".pkl")
            log[0](f"Loading {obj_type} object with id {obj_hash}\n")
            obj = self.__load_object(obj_path)
            log[0](f"Loaded!\n")
            return obj
        except Exception as e:
            log[1](str(e))
            return None

    def list_objects(self, obj_type) -> list[GenericObject]:
        self.__check_obj_type(obj_type)
        ret = []
        obj_bd_base_path = Path(self.bd_base_path, obj_type)
        for obj_file in obj_bd_base_path.glob("*.pkl"):
            ret.append(self.__load_object(obj_file))
        return ret

    @classmethod
    def __check_obj_type(cls, obj_type):
        bd_types = cls.BD_TYPES
        if obj_type not in bd_types:
            raise Exception(f"Incorrect {obj_type} type!")

    @staticmethod
    def __load_object(path):
        with open(path, 'rb') as obj_file:
            obj = pickle.load(obj_file)
            return obj

    @staticmethod
    def __store_object(obj_path, obj):
        with open(obj_path, 'wb') as obj_file:
            pickle.dump(obj, obj_file)
