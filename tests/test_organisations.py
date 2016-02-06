import responses
import gtr

@responses.activate
def test_org():
    "Searching by org id works"

    with open("tests/results.json") as results:
        body = results.read()

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/organisations/test",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Organisations().org("test")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]

@responses.activate
def test_orgs():
    "Searching for organisations works"

    with open("tests/results.json") as results:
        body = results.read()

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/organisations?q=test&f=org.pro.t",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Organisations().orgs("test", field="title")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/organisations?q=test&f=org.n",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Organisations().orgs("test")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]