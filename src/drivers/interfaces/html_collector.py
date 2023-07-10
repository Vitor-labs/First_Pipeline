from abc import ABC, abstractmethod
from typing import List, Dict

class HtmlCollectorInterface(ABC):
    @abstractmethod
    def collect_info(cls, html:str)->List[Dict[str,str]]:
        raise NotImplementedError("HtmlCollector.collect_info: not implemented")