from .html_extractor import HtmlExtractor
from ...drivers.tests import HttpRequestSpy, HtmlCollectorSpy
from ...stages.contracts import ExtractContract
from ...errors import ExtractError


def test_extract_success():
    request = HttpRequestSpy()
    collector = HtmlCollectorSpy()
    extractor = HtmlExtractor(request, collector)

    response = extractor.extract()
    
    assert isinstance(response,ExtractContract)
    assert request.page_count == 1
    assert 'html' in collector.info_params


def test_extract_fail():
    extractor = HtmlExtractor('request', "collector")

    try:
        response = extractor.extract()
        assert isinstance(response,ExtractContract)
    except Exception as e:
        assert isinstance(e, ExtractError)
    
