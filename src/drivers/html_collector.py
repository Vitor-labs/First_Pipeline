"""Class to define Extraction methods"""
from typing import List, Dict
from bs4 import BeautifulSoup 

from src.drivers.interfaces.html_collector import HtmlCollectorInterface


class HtmlCollector(HtmlCollectorInterface):
    """Class to define Extraction methods

    Args:
        HtmlCollectorInterface (ABC): Interface that defines the HTML COLLECTOR methods
    """
    @classmethod
    def collect_info(cls, html:str) -> List[Dict[str, str]]:
        """Collects Data from destination

        Args:
            html (str): url for crawlling

        Returns:
            List[Dict[str, str]]: _description_
        """
        soup = BeautifulSoup(html, 'html.parser')
        info = []

        artists_list = soup.find(class_='BodyText')
        artists_list_items = artists_list.find_all('a')

        for artist in artists_list_items:
            names = artist.contents[0]
            links = 'https://web.archive.org/'+artist.get('href')

            info.append({'name':names,'link':links})

        return info
