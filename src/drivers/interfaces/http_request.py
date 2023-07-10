"""
Module Docstring
"""
from abc import ABC, abstractmethod
from typing import Dict

class HttpRequestInterface(ABC):
    """
    his is an abstract base class for HTTP requests.

    Attributes:
        None

    Methods:
        request_from_url: Sends an HTTP request and returns the response.

    """
    @abstractmethod
    def request_from_url(self)->Dict[int,str]:
        """
        Sends an HTTP request to a specified URL and returns the response.

        Args:
            None

        Returns:
            dict: A dictionary containing the response data.
                The keys are integers representing status codes,
                and the values are strings representing the response content.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.s
        """
        raise NotImplementedError("HttpRequest.request_from_url: not implemented")
