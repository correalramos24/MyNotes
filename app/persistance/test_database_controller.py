from app.persistance.database_controller import ObjectDatabaseController
from app.domain.definitions import GenericObject
from pathlib import Path
from datetime import datetime as dt


def test_save_and_read_object():
    test_path = Path(Path.cwd(), "test_path")
    db_controller = ObjectDatabaseController(test_path, True)
    aux = GenericObject("Alfa", dt.now(), [])
    db_controller.save_object(aux, 'notes')
    aux2 = db_controller.read_object(hash(aux), 'notes')
    print(aux, aux2)
    assert (aux == aux2)


