# -*- coding: utf-8 -*-

# Copyright (c) 2016 Nesta

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
