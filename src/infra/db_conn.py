"""
Module Docstring
"""
from typing import Optional
from .vault_manager import HashiCorpVaultConnection

import psycopg2


class DBConnector:
    """
    Class to establish a connection with a PostgreSQL database
    using secrets from HashiCorp Vault.
    """

    @classmethod
    def from_vault(
        cls,
        vault_connection: HashiCorpVaultConnection,
        db_secret_path: str,
        db_name: Optional[str] = None,
    ) -> 'DBConnector':
        """
        Create a PostgreSQL Connection instance using secrets from HashiCorp Vault.

        Args:
            vault_connection (HashiCorpVaultConnection): An instance of HashiCorpVaultConnection
                used to retrieve database secrets.
            db_secret_path (str): The path to the database secrets in Vault.
            db_name (str, optional): The name of the database to connect to. Defaults to None.

        Returns:
            PostgreSQLConnection: The initialized PostgreSQLConnection instance.
        """
        if db_name is None:
            db_name = vault_connection.read_secret(db_secret_path).get("database")

        db_credentials = vault_connection.read_secret(db_secret_path)

        return cls(
            host=db_credentials.get("host"),
            port=db_credentials.get("port"),
            database=db_name,
            user=db_credentials.get("username"),
            password=db_credentials.get("password")
        )

    def __init__(
        self,
        host: str,
        port: int,
        database: str,
        user: str,
        password: str,
    ) -> None:
        """
        Initialize the PostgreSQL connection.

        Args:
            host (str): The hostname or IP address of the PostgreSQL server.
            port (int): The port number of the PostgreSQL server.
            database (str): The name of the database to connect to.
            user (str): The username for authentication.
            password (str): The password for authentication.
        """
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self) -> None:
        """Establish a connection with the PostgreSQL database."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
            )
        except psycopg2.Error as exc:
            raise ValueError(f"Failed to connect to PostgreSQL database: {exc}") from exc
