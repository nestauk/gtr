import responses
import gtr


@responses.activate
def test_project():
    "Searching by project by id works"

    with open("tests/results.json") as results:
        body = results.read()

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/projects/test",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Projects().project("test")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]


@responses.activate
def test_projects():
    """Searching for projects works."""
    with open("tests/results.json") as results:
        body = results.read()

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/projects?q=test&f=pro.a",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Projects().projects("test", field="project_abs")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]

    responses.add(
        responses.GET,
        "http://gtr.rcuk.ac.uk/gtr/api/projects?q=test&f=pro.t",
        match_querystring=True,
        status=200,
        body=body,
        content_type="application/json")

    res = gtr.Projects().projects("test")

    assert res.status_code == 200
    assert sorted(res.json().keys()) == ["a",
                                         "b",
                                         "c",
                                         "d"]
