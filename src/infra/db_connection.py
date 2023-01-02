import os
from pathlib import Path
import psycopg2
from dotenv import load_dotenv

path = Path('First_Pipeline/src/.env')
load_dotenv()

class DBConnector:
    connection = None

    @classmethod
    def connect(cls):
        print("Connecting to DataBase")
        conn = psycopg2.connect(database=os.getenv('DATABASE'),
                                host=os.getenv('HOST'),
                                user=os.getenv('USER'),
                                password=os.getenv('PASSWORD'),
                                port=os.getenv('PORT'))
        cls.connection = conn
