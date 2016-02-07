import responses
import gtr


@responses.activate
def test_fund():
    """Searching by fund id works."""
    with open("tests/results.json") as results:
        body = results.read()

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/funds/test",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Funds().fund("test")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]


@responses.activate
def test_funds():
    """Searching for funds works."""
    with open("tests/results.json") as results:
        body = results.read()

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/funds?q=test&f=test",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Funds().funds("test", field="test")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/funds?q=test&f=fu.org.n",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Funds().funds("test")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]
