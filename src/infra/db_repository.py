from typing import Dict

from src.infra.db_connection import DBConnector
from src.infra.interfaces.db_repository import DBRepositoryInterface


class DBRepository(DBRepositoryInterface):
    @classmethod
    def insert_artist(cls, data:Dict)->None:
        query='''
            INSERT INTO artists (
                first_name,
                second_name,
                surname,
                artist_id,
                link,
                extraction_date
            ) VALUES (
                %s, %s, %s, %s, %s, %s
            )
        '''
        cursor = DBConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DBConnector.connection.commit()
        