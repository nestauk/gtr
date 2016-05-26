import responses
import gtr


@responses.activate
def test_publication():
    "Searching for publications by id works"

    with open("tests/results.json") as results:
        body = results.read()

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/outcomes/publications/glaciers",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Publications().publication("glaciers")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]


@responses.activate
def test_publications():
    """Searching for publications works."""
    with open("tests/results.json") as results:
        body = results.read()

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/outcomes/publications?q=test&f=title",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Publications().publications("test", field="title")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]
