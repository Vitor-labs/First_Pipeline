from ..contracts.mocks import transform_mock
from .load_data import LoadData
from ...infra.tests import DBRepositorySpi
from ...errors import LoadError

def test_load_data_success():
    repo = DBRepositorySpi()
    load_data = LoadData(repo)

    load_data.load_data(transform_mock)

    assert repo.insert_artist_params == transform_mock.content


def test_load_data_fail():
    repo = DBRepositorySpi()
    load_data = LoadData(repo)

    try:
        load_data.load_data('_error')
    except Exception as exc:
        assert isinstance(exc, LoadError)