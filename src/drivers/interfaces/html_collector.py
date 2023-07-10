"""Interface to implement HTML COLLECTOR methods

Raises:
    NotImplementedError: method "collect_info" not implemented
"""
from abc import ABC, abstractmethod
from typing import List, Dict

class HtmlCollectorInterface(ABC):
    """Interface that defines the HTML COLLECTOR methods

    Args:
        ABC (ABC): Abstract Class 

    Raises:
        NotImplementedError: method "collect_info" not implemented
    """
    @abstractmethod
    def collect_info(self, html:str) -> List[Dict[str, str]]:
        """Collects Data from destination

        Args:
            html (str): _description_

        Raises:
            NotImplementedError: method "collect_info" not implemented

        Returns:
            List[Dict[str, str]]: _description_
        """
        raise NotImplementedError("HtmlCollector.collect_info: not implemented")