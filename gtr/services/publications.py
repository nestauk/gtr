"""
gtr.Publications
~~~~~~~~~~~~~~~~

This module provides a Publications object to query publication data in the
Gateway To Research GTR-2 API.

"""

from .base import _Service


class Publications(_Service):
    """Search GTR-2 for a publication or publications."""

    # TODO - Implement user searchable fields using field codes
    _field_map = {
        'project_id': 'pub.p',
        'abstract': 'pub.pr.a',
        'title': 'pub.pr.t',
        'isbn': 'pub.isbn',
        'issn': 'pub.issn',
        'journal_title': 'pub.jt',
        'pubmed_title': 'pub.pmid',
        'doi': 'pub.doi',
        'date_published': 'pub.date'
    }

    def __init__(self):
        """Construct a Publications object."""
        super(Publications, self).__init__()
        self.session = self.get_session()

    def publication(self, term, **kwargs):
        """Search for publication by id.

        Args:
          term (str): Publication id to search on
          kwargs (dict): additional keywords passed into
            requests.session.get params keyword.
        """
        params = kwargs
        baseuri = self._BASE_URI + 'outcomes/publications/' + term
        res = self.session.get(baseuri, params=params)
        self.handle_http_error(res)
        return res

    def publications(self, term, field=None, **kwargs):
        """Search for publications matching a search term.

        Args:
          term (str): Publication id to search on
          field (str): The field to search on.
            Options are:
                project_id
                abstract
                title
                isbn
                issn
                journal_title
                pubmed_title
                doi
                date_published


          kwargs (dict): additional keywords passed into
            requests.session.get params keyword.
        """
        params = kwargs
        params['q'] = term
        if field:
            params['f'] = field
        baseuri = self._BASE_URI + 'outcomes/publications'
        res = self.session.get(baseuri, params=params)
        self.handle_http_error(res)
        return res
