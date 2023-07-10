import requests
from typing import Dict

from src.drivers.interfaces.http_request import HttpRequestInterface


class HttpRequest(HttpRequestInterface):
    def __init__(self, url:str)->None:
        self.__url=url

    def request_from_url(self)->Dict[int,str]:
        response = requests.get(self.__url)
        return {"status_code":response.status_code, "html":response.text}
