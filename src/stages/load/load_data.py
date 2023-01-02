from src.infra.interfaces.db_repository import DBRepositoryInterface
from src.stages.contracts.transform_contract import TransformContract
from src.errors.load_error import LoadError

class LoadData:
    def __init__(self, repository:DBRepositoryInterface)->None:
        self.__repository=repository

    def load_data(self, transform_contract:TransformContract)->None:
        print("Running Load stage")
        try:
            content = transform_contract.content
            for data in content:
                self.__repository.insert_artist(data)
                
        except Exception as exc:
            raise LoadError(str(exc)) from exc

    