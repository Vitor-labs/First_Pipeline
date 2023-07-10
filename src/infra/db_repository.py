from typing import Dict

from src.infra.db_connection import DBConnector
from src.infra.interfaces.db_repository import DBRepositoryInterface


class DBRepository(DBRepositoryInterface):
    """
    Implementation of the DBRepositoryInterface for database
    operations.
    """

    @classmethod
    def insert_artist(cls, data:Dict)->None:
        """
        Insert an artist into the database.

        Args:
            data (Dict): A dictionary containing the artist data, with the following keys:
                - 'first_name': The first name of the artist.
                - 'second_name': The second name of the artist.
                - 'surname': The surname of the artist.
                - 'artist_id': The ID of the artist.
                - 'link': The link associated with the artist.
                - 'extraction_date': The date of extraction.

        Returns:
            None

        Raises:
            Any database-related exceptions that might occur during the insertion process.
        """
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
        