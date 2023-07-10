"""
Module Docstring
"""
import os
import psycopg2

from dotenv import load_dotenv


load_dotenv()

class DBConnector:
    """
    Represents a connector for connecting to a PostgreSQL database.
    """
    connection = None

    @classmethod
    def connect(cls):
        """
        Establishes a connection to the PostgreSQL database.

        Returns:
            None

        Raises:
            psycopg2.OperationalError: If the connection fails.
        """
        print("Connecting to DataBase")
        conn = psycopg2.connect(database=os.getenv('DATABASE'),
                                host=os.getenv('HOST'),
                                user=os.getenv('USER'),
                                password=os.getenv('PASSWORD'),
                                port=os.getenv('PORT'))
        cls.connection = conn
