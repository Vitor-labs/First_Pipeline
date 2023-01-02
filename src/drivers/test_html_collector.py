from .html_collector import HtmlCollector
from .mocks.http_request_mock import mock_request_from_page


def test_collect_info():
    response = mock_request_from_page()
    collector = HtmlCollector()
    info = collector.collect_info(response['html'])

    assert isinstance(info, list)
    assert isinstance(info[0], dict)
    assert 'name' in info[0]
    assert 'link' in info[0]