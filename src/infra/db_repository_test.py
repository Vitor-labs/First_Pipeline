from typing import Dict

from .db_repository import DBRepository
from .db_connection import DBConnector
from src.stages.contracts.mocks import transform_mock


def test_insert_artist():
    DBConnector.connect()

    repo = DBRepository()
    data = transform_mock.content[1]

    repo.insert_artist(data)
