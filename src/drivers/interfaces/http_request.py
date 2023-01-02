from abc import ABC, abstractmethod
from typing import Dict

class HttpRequestInterface(ABC):
    @abstractmethod
    def request_from_url(self)->Dict[int,str]:
        raise NotImplementedError("HttpRequest.request_from_url: not implemented")
