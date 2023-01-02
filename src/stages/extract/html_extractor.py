from datetime import date

from src.drivers.interfaces.html_collector import HtmlCollectorInterface
from src.drivers.interfaces.http_request import HttpRequestInterface
from src.errors.extract_error import ExtractError
from src.stages.contracts.extract_contract import ExtractContract


class HtmlExtractor:
    def __init__(self, request:HttpRequestInterface, collector:HtmlCollectorInterface) -> None:
        self.__request = request
        self.__collector = collector

    def extract(self,):
        print("Running Extract stage")
        try:
            html = self.__request.request_from_url()
            info = self.__collector.collect_info(html['html'])

            return ExtractContract(
                raw_info=info,
                extract_date=date.today()
            )
        except Exception as exc:
            raise ExtractError(str(exc)) from exc
