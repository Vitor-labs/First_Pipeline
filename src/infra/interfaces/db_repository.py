from abc import ABC, abstractmethod
from typing import Dict


class DBRepositoryInterface:
    @abstractmethod
    def insert_artist(self, data:Dict)->None:
        raise NotImplementedError("DBRepository.insert_artist: not implemented")
