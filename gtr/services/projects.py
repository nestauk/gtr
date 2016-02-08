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
gtr.Projects
~~~~~~~~~~~~~~~~

This module provides a Projects object to query Project data in the Gateway To Research GTR-2 API.

"""

from .base import _Service

class Projects(_Service):
    """Search GTR-2 for projects.
    """

    _FIELD_MAP = {
        'project_ref': 'pro.gr',
        'project_title': 'pro.t',
        'project_abs': 'pro.a'
    }

    def __init__(self):
        """Construct a Projects object."""
        super(Projects, self).__init__()
        self.session = self.get_session()

    def project(self, term, **kwargs):
        """Search for a project by id.

        Args:
          term (str): Term to search for.
          kwargs (dict): additional keywords passed into
            requests.session.get params keyword.
        """
        params = kwargs
        baseuri = self._BASE_URI + 'projects/' + term
        res = self.session.get(baseuri, params=params)
        self.handle_http_error(res)
        return res

    def projects(self, term, field=None, **kwargs):
        """Search for projects. Defaults to project_title. Other fields
        are:
            project_reference
            project_abstract

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
            params['f'] = 'pro.t'
        baseuri = self._BASE_URI + 'projects'
        res = self.session.get(baseuri, params=params)
        self.handle_http_error(res)
        return res

