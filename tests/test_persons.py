import responses
import gtr


@responses.activate
def test_persons():
    """Searching for persons works."""
    with open("tests/results.json") as results:
        body = results.read()

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/persons?q=test&f=per.sn",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Persons().persons("test", field="last_name")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/persons?q=test&f=per.fn",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Persons().persons("test")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]
