"""
Implementations of HTTP requests abstractions
"""
import requests
from typing import Dict

from src.drivers.interfaces.http_request import HttpRequestInterface


class HttpRequest(HttpRequestInterface):
    """
    This class represents an HTTP request.

    Attributes:
        __url (str): The URL to send the request to.

    Methods:
        __init__(self, url: str) -> None:
            Initializes a new instance of the HttpRequest class.
        request_from_url(self) -> Dict[int, str]:
            Sends an HTTP GET request to the specified URL and returns the response.
    """
    def __init__(self, url:str)->None:
        """
        Initializes a new instance of the HttpRequest class.

        Args:
            url (str): The URL to send the request to.s
        """
        self.__url=url

    def request_from_url(self)->Dict[int,str]:
        """
        Sends an HTTP GET request to the specified URL and returns the response.

        Returns:
            dict: A dictionary containing the status code and HTML content of the response.
        """
        response = requests.get(self.__url)
        return {"status_code":response.status_code, "html":response.text}
