from .db_connection import DBConnector


def test_connect():
    assert DBConnector.connection is None

    DBConnector.connect()

    assert DBConnector.connection is not None
