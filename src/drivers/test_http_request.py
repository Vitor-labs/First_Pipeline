from .http_request import HttpRequest

def test_request_from_url(requests_mock):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
    context = '<h1>HelloWorld</h1>'

    requests_mock.get(url, status_code=200, text=context)
    
    request = HttpRequest(url)
    response = request.request_from_url()

    assert 'status_code' in response 
    assert 'html' in response
    assert response['status_code'] == 200
    assert response['html'] == context