import pytest
import requests
import responses

import gtr


def test_Service_session():
    """Get a session using an api"""
    session = gtr._Service().get_session()
    d = session.params
    assert not d    # Empty dicts eval to false


def test_product_token():
    """Get the product version"""
    assert gtr._Service().product_token == 'gtr/{0}'.format(gtr.__version__)


def test_user_agent():
    """Check User-agent correctly assigned"""
    session = gtr._Service().get_session()
    assert session.headers['User-Agent'].startswith('gtr')
    assert 'python-requests' in session.headers['User-Agent']


@responses.activate
def test_custom_messages():
    """Check status code error messaging"""
    fakeurl = 'https://example.com'
    responses.add(responses.GET, fakeurl, status=401)
    _service = gtr._Service()
    response = _service.get_session().get(fakeurl)

    assert _service.handle_http_error(response) is None

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        assert _service.handle_http_error(response,
                                          custom_messages={401: "error"})
        assert exc.value.message == 'error'

    with pytest.raises(requests.exceptions.HTTPError) as exc:
        assert _service.handle_http_error(response, raise_for_status=True)
        assert "401" in exc.value.message
