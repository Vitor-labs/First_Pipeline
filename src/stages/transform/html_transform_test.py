from .html_transform import HtmlTransform
from ..contracts.mocks import extract_mock
from ..contracts import TransformContract
from ...errors import TransformError

def test_transform_success():
    transform_data = HtmlTransform()
    info = transform_data.transform(extract_mock)
    print(info)
    assert isinstance(info, TransformContract)
    assert 'first_name' in info.content[0]
    assert 'last_name' in info.content[0]
    assert 'surname' in info.content[0]
    assert 'artistid' in info.content[0]
    assert 'link' in info.content[0]
    assert 'extract_date' in info.content[0]
    

def test_transform_fail():
    transform_data = HtmlTransform()
    try:
        transform_data.transform('_')
    except Exception as exc:
        assert isinstance(exc, TransformError)