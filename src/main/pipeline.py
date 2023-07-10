from src.drivers.html_collector import HtmlCollector
from src.drivers.http_request import HttpRequest
from src.infra.db_connection import DBConnector
from src.infra.db_repository import DBRepository
from src.stages.extract.html_extractor import HtmlExtractor
from src.stages.load.load_data import LoadData
from src.stages.transform.html_transform import HtmlTransform


class Pipeline:
    def __init__(self)->None:
        self.__url='https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
        self.__html_extractor=HtmlExtractor(HttpRequest(self.__url), HtmlCollector())
        self.__html_transform=HtmlTransform()
        self.__load_data=LoadData(DBRepository())

    def run(self)->None:
        DBConnector.connect()
        extract_contract = self.__html_extractor.extract()
        transform_contract = self.__html_transform.transform(extract_contract)
        self.__load_data.load_data(transform_contract)