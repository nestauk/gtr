# -*- coding: utf-8 -*-

# Copyright (c) 2016 Nesta

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests

from .. import __version__


class _Service(object):

    def __init__(self):
        self._BASE_URI = "http://gtr.rcuk.ac.uk/gtr/api/"

    def get_session(self, token=None, env=None):
        session = requests.Session()

        session.headers.update(
            {'User-Agent': ' '.join(
                [self.product_token, requests.utils.default_user_agent()]),
             'Accept': 'application/vnd.rcuk.gtr.json-v3'})     # Returns json only
        return session

    @property
    def product_token(self):
        """A product token for use in User-Agent headers."""
        return 'gtr/{0}'.format(__version__)

    def handle_http_error(self, response, custom_messages=None,
                          raise_for_status=False):
        if not custom_messages:
            custom_messages = {}
        if response.status_code in custom_messages.keys():
            raise requests.exceptions.HTTPError(
                custom_messages[response.status_code])
        if raise_for_status:
            response.raise_for_status()