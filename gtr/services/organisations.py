"""gtr.Organisations
~~~~~~~~~~~~~~~~

This module provides a Funds object to query Fund data in the Gateway To Research GTR-2 API.

"""

from .base import _Service


class Organisations(_Service):
    """Search GTR-2 for an organisation, organisation
    or all organisations.
    """

    _FIELD_MAP = {
        'title': 'org.pro.t',
        'abstract': 'org.pro.a',
        'amount': 'fu.am',
        'org_name': 'org.n',
        'type': 'fu.ty'
    }

    def __init__(self):
        """Construct an Organisations object."""
        super(Organisations, self).__init__()
        self.session = self.get_session()

    def org(self, term, **kwargs):
        """Search for organisations by id.

        Args:
          term (str): Organisation id to search on
          kwargs (dict): additional keywords passed into
            requests.session.get params keyword.
        """
        params = kwargs
        baseuri = self._BASE_URI + 'organisations/' + term
        res = self.session.get(baseuri, params=params)
        self.handle_http_error(res)
        return res

    def orgs(self, term=None, field=None, **kwargs):
        """Search for organisations matching a search term.

        Args:
          term (str): Search term
          field (str): The field to search on.
            Options are title, amount, org_name and type.
          kwargs (dict): additional keywords passed into
            requests.session.get params keyword.
        """
        params = kwargs
        params['q'] = term
        if field:
            params['f'] = self._FIELD_MAP[field]
        else:
            params['f'] = 'org.n'
        baseuri = self._BASE_URI + 'organisations'
        res = self.session.get(baseuri, params=params)
        self.handle_http_error(res)
        return res
