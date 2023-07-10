"""
Module Docstring
"""
from typing import Optional, Dict
import hvac


class HashiCorpVaultConnection:
    """Class to establish a connection with HashiCorp Vault."""

    def __init__(
        self,
        url: str,
        token: str,
        verify: Optional[bool] = True,
    ) -> None:
        """
        Initialize the HashiCorp Vault connection.

        Args:
            url (str): The URL of the Vault server.
            token (str): The authentication token for the Vault server.
            verify (bool, optional): Flag indicating whether to verify server's SSL certificate.
                Defaults to True.
        """
        self.url = url
        self.token = token
        self.verify = verify
        self.client = None

    def connect(self) -> None:
        """Establish a connection with HashiCorp Vault."""
        self.client = hvac.Client(url=self.url, token=self.token, verify=self.verify)
        if not self.client.is_authenticated():
            raise ValueError("Failed to authenticate with HashiCorp Vault")

    def read_secret(self, path: str) -> dict:
        """
        Read a secret from HashiCorp Vault.

        Args:
            path (str): The path to the secret in Vault.

        Returns:
            dict: The secret data.
        """
        if not self.client:
            raise ValueError("Vault connection has not been established")

        response = self.client.secrets.kv.v2.read_secret_version(path=path)

        if not response or not response.get("data"):
            raise ValueError("Failed to read secret from Vault")

        return response["data"]["data"]
    

    def create_secret(self, path: str, secret: Dict) -> dict:
        """
        Read a secret from HashiCorp Vault.

        Args:
            path (str): The path to the secret in Vault.

        Returns:
            dict: The secret data.
        """
        if not self.client:
            raise ValueError("Vault connection has not been established")

        response = self.client.secrets.kv.v2.create_or_update_secret(path=path, secret=secret)

        if not response:
            raise ValueError("Failed to create secret on Vault")

        return response
