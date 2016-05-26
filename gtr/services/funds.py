"""
gtr.Funds
~~~~~~~~~~~~~~~~

This module provides a Funds object to query Fund data in the Gateway To Research GTR-2 API.

"""

from .base import _Service


class Funds(_Service):
    """Search GTR-2 for a fund or funds."""

    _field_map = {
        'title': 'fu.pro.t',
        'amount': 'fu.am',
        'org_name': 'fu.org.n',
        'type': 'fu.ty'
    }

    def __init__(self):
        """Construct a Funds object."""
        super(Funds, self).__init__()
        self.session = self.get_session()

    def fund(self, term, **kwargs):
        """Search for funds by id.

        Args:
          term (str): Fund id to search on
          kwargs (dict): additional keywords passed into
            requests.session.get params keyword.
        """
        params = kwargs
        baseuri = self._BASE_URI + 'funds/' + term
        res = self.session.get(baseuri, params=params)
        self.handle_http_error(res)
        return res

    def funds(self, term, field=None, **kwargs):
        """Search for funds matching a search term.

        Args:
          term (str): Fund id to search on
          field (str): The field to search on.
            Options are title, amount, org_name and type.
          kwargs (dict): additional keywords passed into
            requests.session.get params keyword.
        """
        params = kwargs
        params['q'] = term
        if field:
            params['f'] = field
        else:
            params['f'] = 'fu.org.n'
        baseuri = self._BASE_URI + 'funds'
        res = self.session.get(baseuri, params=params)
        self.handle_http_error(res)
        return res
