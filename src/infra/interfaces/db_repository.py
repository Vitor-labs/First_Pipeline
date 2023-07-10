"""
Module Docstring
"""
from abc import ABC, abstractmethod
from typing import Dict


class DBRepositoryInterface(ABC):
    """
    This class defines the interface for a database repository.

    Methods:
        insert_artist(data: Dict) -> None: Inserts an artist into the database.
            Parameters:
                data (Dict): A dictionary containing the data of the artist to be inserted.
            Raises:
                NotImplementedError: If the method is not implemented by the subclass.
    """
    @abstractmethod
    def insert_artist(self, data:Dict)->None:
        """
        Inserts an artist into the database repository.

        Args:
            data (Dict): A dictionary containing the artist information.

        Raises:
            NotImplementedError: This method is not implemented in the base class.
        """
        raise NotImplementedError("DBRepository.insert_artist: not implemented")
