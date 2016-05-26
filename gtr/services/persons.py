"""
gtr.Persons
~~~~~~~~~~~~~~~~

This module provides a Persons object to query Person data in the Gateway To Research GTR-2 API.

"""

from .base import _Service

class Persons(_Service):
    """Search GTR-2 for persons.
    """

    _FIELD_MAP = {
        'first_name': 'per.fn',
        'last_name': 'per.sn',
        'first_last_name': 'per.fnsn',
        'other_name': 'per.org.n',
        'org_name': 'org.n',
        'proj_title': 'per.pro.t',
        'proj_abst': 'per.pro.abs'
    }

    def __init__(self):
        """Construct a Persons object."""
        super(Persons, self).__init__()
        self.session = self.get_session()

    def persons(self, term, field=None, **kwargs):
        """Search for persons by field. Defaults to first_name. Other fields
        are:
            last_name
            first_last_name
            other_name
            org_name
            proj_title
            proj_abstract

        Args:
          term (str): Term to search for.
          kwargs (dict): additional keywords passed into
            requests.session.get params keyword.
        """
        params = kwargs
        params['q'] = term
        if field:
            params['f'] = self._FIELD_MAP[field]
        else:
            params['f'] = 'per.fn'
        baseuri = self._BASE_URI + 'persons'
        res = self.session.get(baseuri, params=params)
        self.handle_http_error(res)
        return res
