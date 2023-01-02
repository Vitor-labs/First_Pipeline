from typing import Dict

class HttpRequestSpy:
    def __init__(self)->None:
        self.page_count=0

    def request_from_url(self)->Dict[int,str]:
        self.page_count+=1
        return{
            'status_code':200,
            'html':'<h1>HelloWorld</h1>'
        }